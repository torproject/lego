# Lektor markdown tag

Embed markdown in a lektor template

## Installation

If you're using this, you're probably working on a [Tor project lektor site](https://gitlab.torproject.org/tpo/web) that uses [lego](https://gitlab.torproject.org/tpo/web/lego/). In that case, you don't need to do anything special after running
```sh
git submodule update --init --recursive
```

If you're *not* working on a TPO site, you can clone the [lego repo](https://gitlab.torproject.org/tpo/web/lego/) and copy the `packages/lektor-md-tag` directory to your lektor site's `packages`. Here's a small script to do that for you:
```sh
# run this in your lektor site directory
git clone --depth 1 https://gitlab.torproject.org/tpo/web/lego
mkdir -p packages
mv lego/packages/lektor-md-tag packages
rm -rf lego
```

## Usage

From within your Lektor HTML template:
```jinja
{{ md('**This is bold!**') }}
```

This jinja function *will* wrap paragraphs in a set of `<p></p>` tags; don't add use this tag inside an HTML paragraph. The above snippet renders like this:
```html
<p><strong>This is bold!</strong></p>
```

## License

[0BSD](https://opensource.org/licenses/0BSD). I cannot realistically be bothered to deal with copyright and licensing, have fun!
