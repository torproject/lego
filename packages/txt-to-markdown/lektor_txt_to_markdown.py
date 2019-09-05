# -*- coding: utf-8 -*-
#pylint: disable=wrong-import-position
import sys

PY3 = sys.version_info > (3,)

from lektor.pluginsystem import Plugin

from urllib import request


class TxtToMarkdownPlugin(Plugin):
    name = u'TXT to Markdown'
    description = u'Lektor plugin to add a remote TXT doc into Markdown.'


    def on_setup_env(self, **extra):

        def stream(url=None):
            webFile = request.urlopen(url)
            content = webFile.read()
            text ="<pre>" + content + "</pre>"

            return text

        self.env.jinja_env.globals['render_text'] = text
