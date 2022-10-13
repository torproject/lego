# lektor-npm-support

[![Build Status](https://travis-ci.org/sterin/lektor-npm-support.svg)](https://travis-ci.org/sterin/lektor-npm-support)
[![Build status](https://ci.appveyor.com/api/projects/status/6op1csefpi9l8hbg?svg=true)](https://ci.appveyor.com/project/sterin/lektor-npm-support)
[![Code Coverage](https://codecov.io/gh/sterin/lektor-npm-support/branch/master/graph/badge.svg)](https://codecov.io/gh/sterin/lektor-npm-support)

`lektor-npm-support` makes it easy to use [Parcel](https://parcel.js.org), [webpack](https://webpack.js.org), [browserify](http://browserify.org/), or any other tool to build assets for [Lektor](https://github.com/lektor/lektor) projects. 

## Enabling the Plugin

To enable the plugin, run this command while inside your Lektor project directory:

```bash
lektor plugins add lektor-npm-support
```

## Example: Creating a [Parcel](https://parceljs.org/) Project

Create a `parcel/` folder and inside that folder create the following files:

### `configs/npm-support.ini`

This file instructs the plugin how to generate the assets:

```ini
[parcel]
npm = yarn
watch_script = watch
build_script = build
install_args = --force
```

* The section name `[parcel]` is the name of the folder where the Parcel project is located.
* `npm` is the package manager command used to build the project. This example will use [Yarn](https://yarnpkg.com).
* `watch_script` is the npm script used in `lektor server -f npm`,
* `build_script` is the npm script used in `lektor build -f npm`,

This plugin supports more than one such entry.

#### install_args

```
[parcel]
npm = yarn
install_args = --force
watch_script = watch
build_script = build
```

The `install_args` line is the argument string passed to `npm install`. This is optional, and only recommended if your project *needs* to use an install flag.

### `parcel/package.json`

This is a standard `package.json` file. It should contain two entries in the `scripts` section. The `build` script is used during `lektor build -f npm`, and the `watch` script is used during `lektor server -f npm`.

```json
{
  "name": "my-parcel-project",
  "version": "1.0.0",
  "scripts": {
    "watch": "NODE_ENV=development parcel --out-dir=../assets/static/gen --out-file=main.js --public-url=./assets/ main.js",
    "build": "NODE_ENV=production parcel build --out-dir=../assets/static/gen --out-file=main.js --public-url=./assets/ main.js"
  },
  "private": true
}
```

Now we can use `yarn add` to add Parcel, [Babel](https://babeljs.io/) and [Sass](https://sass-lang.com/):

```
$ cd </path/to/your/lektor/project>/parcel
$ yarn add parcel-bundler babel-preset-env node-sass
```

### `parcel/babelr.rc`

Next up is a simple Babel config file, using the recommended `env` preset.

```json
{
  "presets": ["env"]
}
```

### `parcel/main.scss`

A simple SCSS file.

```scss
body {
  border: 10px solid red;
}
```

### `parcel/main.js`

A simple Javascript file that imports the SCSS file so that Parcel will know to include it as well.

```javascript
import './main.scss';
```

## Running the Server

Now you're ready to go.  When you run `lektor server` nothing wil happen, 
instead you need to now run it as `lektor server -f npm` which
will enable the Parcel build.  Parcel will automatically build your files
into `assets/static/gen` and this is where Lektor will then pick up the
files.  This is done so that you can ship the generated assets
to others that might not have these tools, which simplifies using a
Lektor website that use this plugin.

## Manual Builds

To manually trigger a build that also invokes webpack you can use `lektor build -f npm`.

## Including The Files

Now you need to include the files in your template.  This will do it:

```html
<link rel="stylesheet" href="{{ '/static/gen/main.css'| asseturl }}">
<script type=text/javascript src="{{ '/static/gen/main.js'| asseturl }}" charset="utf-8"></script>
```

## Complete Working Example

The `examples` folder of this repository contains working projects.


## Credits

This plugin is based on the official [lektor-webpack-support](https://github.com/lektor/lektor-webpack-support) Lektor plugin by [Armin Ronacher](http://lucumr.pocoo.org/about/).
