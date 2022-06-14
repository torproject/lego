 SCSS compiler for lektor
=============================
[![PyPI version](https://badge.fury.io/py/lektor-scss.svg)](https://badge.fury.io/py/lektor-scss)
 [![Downloads](https://pepy.tech/badge/lektor-scss)](https://pepy.tech/project/lektor-scss)
 ![Upload Python Package](https://github.com/chaos-bodensee/lektor-scss/workflows/Upload%20Python%20Package/badge.svg)
 ![Linting Python package](https://github.com/chaos-bodensee/lektor-scss/workflows/Linting%20Python%20package/badge.svg)

SCSS compiler for [Lektor](https://getlektor.com) that compiles css from sass.

 How does it actually work?
----------------------------
 + It uses [libsass](https://github.com/sass/libsass-python)
 + It looks for ``.scss`` and ``.sass`` files *(ignores part files that begin with a underscore e.g. '_testfile.scss') and compiles them as part of the build process.*
 + It only rebuilds the css when it's needed (file changed, a file it imports changed or the config changed).
 + When starting the the development server it watches the files for changes in the background and rebuilds them when needed.

 Installation
-------------
You can install the plugin with Lektor's installer:
```bash
lektor plugins add lektor-scss
```

Or by hand, adding the plugin to the packages section in your lektorproject file:
```ini
[packages]
lektor-scss = 1.4.1
```
 Usage
------
To enable the plugin, pass the ``scss`` flag when starting the development
server or when running a build:
```bash
# build and compile css from scss
lektor build -f scss

# edit site with new generated css
lektor server -f scss
```

 Python3
----------
It is highly recommended to use this plugin with a python3 version of lektor.

Since lektor can be used as a python module it is possible to enforce this *(after lektor is installed eg. with ``pip3 install --user --upgrade lektor``)* with the following command:
```bash
# run a python3 lektor server with new generated css
python3 -m lektor server -f scss
```

 Configuration
-------------
The Plugin has the following settings you can adjust to your needs:

|parameter      |default value      |description                                                                                       |
|---------------|-------------------|--------------------------------------------------------------------------------------------------|
|source_dir     |assets/scss/       | the directory in which the plugin searchs for sass files (subdirectories are included)           |
|output_dir     |assets/css/        | the directory the compiled css files get place at                                                |
|output_style   |compressed         | coding style of the compiled result. choose one of: 'nested', 'expanded', 'compact', 'compressed'|
|source_comments|False              | whether to add comments about source lines                                                       |
|precision      |5                  | precision for numbers                                                                            |
|include_paths  |                   |If you want to include SASS libraries from a different directory, libsass's compile function has a parameter called `include_paths` to add those directories to the search path. |


An example file with the default config can be found at ``configs/scss.ini``. For every parameter that is not specified in the config file the default value is used by the plugin.

 Development
-------------
To test and/or develop on this plugin in your running lektor installation, simply place it in the ``packages/`` Folder and have a look at the [Lektor Doku](https://www.getlektor.com/docs/plugins/dev/)

<!-- How to add to pypi: https://packaging.python.org/tutorials/packaging-projects/ -->
<!-- Python RELEASEING moved to github action -->
<!-- You have to edit the version number in README and setup.py manually -->
