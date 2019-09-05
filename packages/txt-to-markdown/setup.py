from setuptools import setup

setup(
    name='lektor-txt-to-markdown',
    version='0.1',
    author=u'Hiro',
    author_email='hiro@torproject.org',
    url='https://github.com/torproject/lego/packages/txt-to-markdown',
    license='GPL',
    py_modules=['lektor_txt_to_markdown'],
    entry_points={
        'lektor.plugins': [
            'xml-to-html = lektor_txt_to_markdown:TxtToMarkdownPlugin',
        ]
    }
)
