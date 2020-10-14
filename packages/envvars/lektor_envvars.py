from environs import Env
from lektor.pluginsystem import Plugin

__version__ = "18.6.12.4"

DEFAULT_PREFIX = "LEKTOR_"


class LektorEnv:
    def __init__(self, config=None):
        self.env = Env()

        if not config:
            self.prefix = DEFAULT_PREFIX
        else:
            self.prefix = config.get("envvar.prefix", DEFAULT_PREFIX)

    def envvars(self, name, var_type=None, no_prefix=False):
        prefix = "" if no_prefix else self.prefix

        with self.env.prefixed(prefix):
            if var_type:
                return getattr(self.env, var_type)(name)
            else:
                return self.env(name)


class EnvvarsPlugin(Plugin):
    name = "Environment Variables"
    description = "A plugin making environment variables available in templates."

    def on_setup_env(self, **extra):
        config = self.get_config()
        self.env.jinja_env.globals.update({"envvars": LektorEnv(config).envvars})
