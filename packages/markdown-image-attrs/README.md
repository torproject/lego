# Lektor Markdown Extension for Image and Link attributes

[![PyPI version](https://img.shields.io/pypi/v/lektor-markdown-image-attrs.svg)](https://pypi.org/project/lektor-markdown-image-attrs/)
[![PyPI Supported Python Versions](https://img.shields.io/pypi/pyversions/lektor-markdown-image-attrs.svg)](https://pypi.python.org/pypi/lektor-markdown-image-attrs/)
[![GitHub license](https://img.shields.io/github/license/dairiki/lektor-markdown-image-attrs)](https://github.com/dairiki/lektor-markdown-image-attrs/blob/master/LICENSE)
[![GitHub Actions (Tests)](https://github.com/dairiki/lektor-markdown-image-attrs/workflows/Tests/badge.svg)](https://github.com/dairiki/lektor-markdown-image-attrs/actions)

This plugin hacks up Lektor’s Markdown renderer to add syntax which allows
arbitrary HTML attributes to be set on image and link tags.

## Motivation

Markdown, as implemented in Lektor, provides nice shorthand syntax for
marking up images.  It does not provide any syntax for controlling
image styling, e.g., sizing and alignment.  This plugin molests
Markdowns syntax for image (and link) titles to allow setting
arbitrary HTML attributes on image and link tags.

### On using raw HTML

It is true that one can simply include raw HTML `<img>` tags within
Markdown text.  However, since this bypasses Markdown processing
altogether, it also bypasses Lektor’s resolution of image/link
URLs. This can be undesirable.

## Setting attributes on link and image tags in Markdown text

These hacks allow one to set attributes on image and link tags, by overloading
Markdown’s syntax for setting title attributes.

If the title of a Markdown image or link looks like a set of
(non-empty) HTML attributes, they are interpreted as such, and stuck
onto the produced `<a>` or `<img>` tag.

```markdown
![My cat, Fluffy](fluffy.jpg "class=img-responsive")
```

will produce
```html
<img src="fluffy.jpg" class=img-responsive>
```

If you do want to set a title as well, you may surround the extra attributes
with angle brackets and append them at the end of the title.   Both of these
are equivalent:

```markdown
![My cat, Fluffy](fluffy.jpg "Fluffy at rest <class=img-responsive>")
```

```markdown
![My cat, Fluffy](fluffy.jpg "title='Fluffy at rest' class=img-responsive")
```

If you’d like to set a title, when the title text looks like a set of HTML attributes, simply append an empty set of angle brackets to the title:

```markdown
![My cat, Fluffy](fluffy.jpg "Fluffy=resting <>")
```

This works with reference-style links and images as well:

```markdown
Here’s a photo of [my cat][]:  ![fluffy][]

[fluffy]: fluffy.jpg   (style='width: 80px;')
[my cat]: <http://fluffy.example.org>   'Fluffy’s website <class="external link">'
```

## Testing

We now use [hatch](https://hatch.pypa.io/latest/) for packaging and development.

To run all tests, including under a full matrix of python and lektor
versions, as well as combined coverage tests:

```sh
hatch run full
```

The `dev` environment specifies additional dependencies useful for
development.  E.g. I start emacs via:

```sh
hatch run dev:emacs lektor_markdown_image_attrs.py &
```

## Acknowledgments

Ideas were gleaned from this [blog post](https://www.xaprb.com/blog/how-to-style-images-with-markdown/) by Baron Schwartz.

## Author

Jeff Dairiki <dairiki@dairiki.org>



