# -*- coding: utf-8 -*-

#Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted.
#
#THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from lektor.markdown import markdown_to_html
from lektor.pluginsystem import Plugin

import markupsafe


class MarkdownTagPlugin(Plugin):
    name = 'lektor markdown tag'
    description = 'Embed markdown in a lektor template'

    def on_setup_env(self, **extra):
        def md(markdown_str: str):
            return markupsafe.Markup(markdown_to_html(markdown_str)[0])
        self.env.jinja_env.globals.update(md=md)
