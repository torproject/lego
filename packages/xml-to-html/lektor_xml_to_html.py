# -*- coding: utf-8 -*-
#pylint: disable=wrong-import-position
import sys

PY3 = sys.version_info > (3,)

from lektor.pluginsystem import Plugin

from xml.etree import ElementTree as etree
from urllib import request


class DisqusCommentsPlugin(Plugin):
    name = u'XML to HTML'
    description = u'Lektor plugin to add an XML feed as HTML.'


    def on_setup_env(self, **extra):

        def stream(identifier=None, url=None):
            webFile = request.urlopen("https://blog.torproject.org/events.xml")
            content = webFile.read()
            root = etree.fromstring(content)
            items = root.findall('channel/item')
            file_object  = open('../../../templates/stream.html', 'w')
            stream = ""
            for entry in items:
              title = entry.findtext('title')
              link = entry.findtext('link')
              stream += "<h3><a href=\"" + link +"\">" + title + "</a></h3>")

            return stream

        self.env.jinja_env.globals['render_strean'] = stream
