# Lego

This repository contains templates, models, assets, databags, and lektor plugins used by many of the lektor sites. It's intended to be added as a submodule, to keep the style and assets up-to-date between sites.

You won't use this repo directly. You'll usually clone it as a submodule:
```
git clone https://gitlab.torproject.org/tpo/web/tpo
cd tpo
git submodule update --init

# or
git clone --recurse-submodules https://gitlab.torproject.org/tpo/web/tpo
```

You might also want to add it to a new lektor project:
```
# from the project root
git submodule add https://gitlab.torproject.org/tpo/web/lego.git

# now symlink files/directories from lego to the proper location...
```

## Package may contain

Here's what's inside lego:

* `assets/`
  * `assets/javascript/`: Contains the javascript used by bootstrap
  * `assets/scss/`: Contains the SCSS for lego. This is Bootstrap v4, with our own styles layered on top
  * `assets/static/`: Contains fonts, images, and minified bootstrap js, as well as the compiled SCSS output
* `databags/`: All the databags used by the lego templates
* `models/`: Contains a model for redirect pages
* `packages/`: A number of mirrored and patched python packages. See each package's README for details
* `templates/`: Useful templates used by several of the sites
