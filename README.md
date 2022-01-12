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

You might also want to add it to a new lektor project. This is a three-step process:

1. Clone the submodule from the project root: `git submodule add https://gitlab.torproject.org/tpo/web/lego.git`
2. Edit the submodule URL. See <#relative-submodule-urls>.
3. Symlink everything you need. See <#symlinking-lego>.

## Relative submodule URLs

Gitlab CI requires that submodules hosted on the same server as the main repo use relative URLs. If your project isn't hosted on <https://gitlab.torproject.org> or isn't using Gitlab CI, you can skip this!

Relative submodule URLs means that if lego is located at <https://gitlab.torproject.org/tpo/web/lego> and your project is `https://gitlab.torproject.org/tpo/web/some_website`, then your submodule URL should be `../lego.git` **The .git suffix is required**. If your project is hosted in your own namespace (like a fork), your repo URL should look like `https://gitlab.torproject.org/user/repo` your submodule URL should be `../../tpo/web/lego.git`. This means that forking requires you to change your submodule URL to use CI. This is a known bug with upstream gitlab <https://gitlab.com/gitlab-org/gitlab-runner/-/issues/3374> and TPA is looking into solutions in the meantime.

## Symlinking lego

Adding lego as a submodule doesn't actually do anything on its own. You'll need to symlink the parts of lego that you want. For instance, lektor installs all the python packages in `/packages`. Symlinking `/lego/packages` to `/packages` means lektor will install all the packages lego comes with. You can even pick and choose what packages get symlinked: `mkdir -p packages && ln -s ../lego/lektor-md-tag ../lego/npm-support packages`

A list of things contained in lego and descriptions of them is <#package-may-contain>. Usually, you'll want to symlink `/lego/assets/*` to `/assets`, `/lego/templates/*` to `/templates`, `/lego/databags/*` to `/databags*`, and the entire `/lego/packages` directory to `/packages`

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

## License

**TBD**

Lego (and all of TPO's web projects unless otherwise specified) do not yet have a license.
