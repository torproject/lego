from setuptools import setup

setup(
    name='lektor-xml-to-html',
    version='0.1',
    author=u'Hiro',
    author_email='hiro@torproject.org',
    url='https://github.com/torproject/lego/packages/xml-to-html',
    license='GPL',
    py_modules=['lektor_xml_to_html'],
    entry_points={
        'lektor.plugins': [
            'xml-to-html = lektor_xml_to_html:XmlToHtmlPlugin',
        ]
    }
)
