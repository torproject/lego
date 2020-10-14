import os
from setuptools import setup

tests_require = [
    'lektor',
    'pytest',
    'pytest-cov',
    'pytest-mock'
]


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='lektor-npm-support',
    author=u'Baruch Sterin',
    author_email='lektor-npm-support@bsterin.com',
    version='0.1.4',
    url='http://github.com/sterin/lektor-npm-support',
    license='BSD',
    description="Adds support for using npm/yarn to build assets in Lektor",
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    py_modules=['lektor_npm_support'],
    setup_requires=['pytest-runner'],
    tests_require=tests_require,
    entry_points={
        'lektor.plugins': [
            'npm-support = lektor_npm_support:NPMSupportPlugin',
        ]
    }
)
