"""Extend Markdown syntax to allow setting arbitrary HTML attributes
on images and links.

"""
from __future__ import annotations

import inspect
import re

import mistune
import lektor.pluginsystem


# Regex construction
_bits = {
    # attribute name
    'name': r'[_:a-z][-.0-9_:a-z]*',  # NB: more restrictive than HTML spec
    # unquoted attribute value
    'uvalue': r'[-.0-9_:a-z]+',       # NB: more restrictive than HTML sepc
    # quoted attribute value
    'qvalue1': r" ' [^'>]* ' ",
    'qvalue2': r' " [^">]* " ',
    }
_bits['value'] = r'(?: {uvalue} | {qvalue1} | {qvalue2})'.format(**_bits)
# non-empty attribute
_bits['nonempty_attribute'] = r'{name} \s* = \s* {value}'.format(**_bits)
# possibly-empty attribute
_bits['attribute'] = r'{name} (?: \s* = \s* {value})?'.format(**_bits)


# Trailing, possibly empty, list of attributes, surround by <>
trailing_attrs_re = re.compile(
    r'''
    \s* < \s* (?P<attrs>
        (?: {attribute} (?: \s+ {attribute} )* )?
    ) \s* > \s* \Z
    '''.format(**_bits), re.X | re.I)

# Nothing but a non-empty list of non-empty attribute (without angle brackets)
implicit_attrs_re = re.compile(
    r'''
    \A \s* (?P<attrs>
        {nonempty_attribute} (?: \s+ {nonempty_attribute} )*
    ) \s* \Z
    '''.format(**_bits), re.X | re.I)


def extract_attrs_from_title(bound: inspect.BoundArguments) -> str | None:
    """Extract explict HTML attributes from title parameter.

    If such attributes are found, the bound arguments in ``bound``
    are modified in-place, and the extracted attributes are returned.
    """
    arguments = bound.arguments
    attrs = None
    title = arguments.get("title")
    if title:
        m = (trailing_attrs_re.search(title)
             or implicit_attrs_re.match(title))
        if m is not None:
            attrs = m.group('attrs')
            arguments["title"] = title[:m.start()] if m.start() > 0 else None
    return attrs


try:
    _renderer = mistune.HTMLRenderer()
except AttributeError:
    _renderer = mistune.Renderer()
LINK_ARGS = inspect.signature(_renderer.link)
IMAGE_ARGS = inspect.signature(_renderer.image)
del _renderer


class MarkdownRendererMixin:
    """This allows one to set attributes on image and link tags by
    including them in the markdown title for the image or link.

    Examples::

        ![my cat](cat.jpg "Fluffy, my cat <class='img-responsive'>")


        (Not to be confused with this one: ![my other cat][fluffy].)

        [fluffy]: other-cat.jpg (Not Fluffy <style="width: 25px;">)

    """
    def link(self, *args, **kwargs):
        bound = LINK_ARGS.bind(*args, **kwargs)
        attrs = extract_attrs_from_title(bound)
        markup = super().link(*bound.args, *bound.kwargs)
        if attrs:
            # FIXME: hackish
            markup = markup.replace(' href=', ' %s href=' % attrs)
        return markup

    def image(self, *args, **kwargs):
        bound = IMAGE_ARGS.bind(*args, **kwargs)
        attrs = extract_attrs_from_title(bound)
        markup = super().image(*bound.args, *bound.kwargs)
        if attrs:
            # FIXME: hackish
            markup = markup.replace(' src=', ' %s src=' % attrs)
        return markup


class LektorPlugin(lektor.pluginsystem.Plugin):
    name = 'Lektor Markdown Image and Link Attributes'
    description = (
        'Extend Lektor’s Markdown syntax to allow setting '
        'arbitrary HTML attributes on images and links.')

    def on_markdown_config(self, config, **extra):
        # XXX: This is fragile, but I'm not sure how better to do this.
        # Here we attempt to put our mixin the top of the MRO so that it
        # will be called above any calls to other mixins which affect
        # the rendering of images and/or links.
        config.renderer_mixins.insert(0, MarkdownRendererMixin)
