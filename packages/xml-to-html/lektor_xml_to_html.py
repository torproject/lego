# -*- coding: utf-8 -*-
#pylint: disable=wrong-import-position
import sys

PY3 = sys.version_info > (3,)

from lektor.pluginsystem import Plugin

from xml.etree import ElementTree as etree
from urllib import request

webFile = request.urlopen("https://blog.torproject.org/events.xml")
content = webFile.read()
root = etree.fromstring(content)
items = root.findall('channel/item')
file_object  = open('../../../templates/stream.html', 'w')
for entry in items:
  title = entry.findtext('title')
  link = entry.findtext('link')
  file_object.write("<h3><a href=\"" + link +"\">" + title + "</a></h3>")
  file.close()
