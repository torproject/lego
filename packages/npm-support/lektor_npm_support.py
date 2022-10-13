import os
import threading
import collections
from builtins import object


from lektor.pluginsystem import Plugin
from lektor.reporter import reporter
from lektor.utils import locate_executable, portable_popen


popen_args_type = collections.namedtuple('popen_args_type', ['args', 'cwd'])


class ProcessSequence(object):

    def __init__(self, procs):
        self.mutex = threading.Lock()
        self.procs = list(reversed(procs))
        self.current = None
        self._start_next_process()

    def _start_next_process(self):
        self.current = None
        if self.procs:
            p = self.procs.pop()
            self.current = portable_popen(p.args, cwd=p.cwd)

    def kill(self):
        with self.mutex:
            if self.current:
                self.current.kill()
                self.procs = []

    def wait(self):
        while True:
            if self.current is None:
                return
            self.current.wait()
            if self.current.returncode != 0:
                return
            with self.mutex:
                self._start_next_process()


class ProcessManager(object):

    def __init__(self):
        self.cv = threading.Condition()
        self.procs = set()

    def _thread(self, p):
        try:
            p.wait()
        except:
            pass
        finally:
            with self.cv:
                if p in self.procs:
                    self.procs.remove(p)
                self.cv.notifyAll()

    def start(self, *procs):
        p = ProcessSequence(procs)
        self.procs.add(p)
        threading.Thread(target=self._thread, args=(p,)).start()

    def kill(self):
        with self.cv:
            for p in self.procs:
                p.kill()
            self.procs = []

    def wait(self):
        with self.cv:
            while self.procs:
                self.cv.wait()

    def __bool__(self):
        with self.cv:
            return bool(self.procs)


class NPMRunner(object):

    def __init__(self, folder, npm, build_script, watch_script, install_args):
        self.folder = folder
        self.npm = npm
        self.build_script = build_script
        self.watch_script = watch_script
        self.install_args = install_args

    def npm_args(self, *args):
        return popen_args_type([self.npm] + list(args), self.folder)

    def build(self, proc):
        proc.start(
            self.npm_args('install', self.install_args),
            self.npm_args('run', self.build_script)
        )

    def watch(self, proc):
        proc.start(self.npm_args('install'), self.npm_args('run', self.watch_script))


class NPMSupportPlugin(Plugin):
    name = 'npm Support Plugin'
    description = "Adds support for using npm/yarn to build assets in Lektor"

    def __init__(self, *args, **kwargs):
        Plugin.__init__(self, *args, **kwargs)
        self.proc_manager = ProcessManager()

    def is_enabled(self, extra_flags):
        return 'npm' in extra_flags

    def runners(self):
        config = self.get_config()
        for section in config.itersections():
            props = config.section_as_dict(section)
            yield NPMRunner(
                folder=os.path.join(self.env.root_path, section),
                npm=props.get('npm', 'npm'),
                build_script=props.get('build_script', 'build'),
                watch_script=props.get('watch_script', 'watch'),
                install_args=props.get('install_args', '')
            )

    def on_server_spawn(self, extra_flags, **extra):
        if self.is_enabled(extra_flags):
            reporter.report_generic('Starting npm watchers')
            for r in self.runners():
                r.watch(self.proc_manager)

    def on_server_stop(self, **extra):
        if self.proc_manager:
            reporter.report_generic('Stopping npm watchers')
            self.proc_manager.kill()
            reporter.report_generic('Stopped npm watchers')

    def on_before_build_all(self, builder, **extra):
        if self.proc_manager or not self.is_enabled(builder.extra_flags):
            return
        reporter.report_generic('Starting npm build')
        for r in self.runners():
            r.build(self.proc_manager)
        self.proc_manager.wait()
        reporter.report_generic('Finished npm build')
