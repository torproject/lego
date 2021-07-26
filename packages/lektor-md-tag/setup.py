import ast
import io
import re

from setuptools import setup, find_packages

with io.open('README.md', 'rt', encoding="utf8") as f:
    readme = f.read()

_description_re = re.compile(r'description\s+=\s+(?P<description>.*)')

with open('lektor_markdown_tag.py', 'rb') as f:
    description = str(ast.literal_eval(_description_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    author='',
    author_email='',
    description=description,
    keywords='Lektor plugin',
    license='0BSD',
    long_description=readme,
    long_description_content_type='text/markdown',
    name='lektor-markdown-tag',
    packages=find_packages(),
    py_modules=['lektor_markdown_tag'],
    # url='[link to your repository]',
    version='0.1',
    classifiers=[
        'Framework :: Lektor',
        'Environment :: Plugins',
    ],
    entry_points={
        'lektor.plugins': [
            'markdown-tag = lektor_markdown_tag:MarkdownTagPlugin',
        ]
    }
)
