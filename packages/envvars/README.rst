lektor-envvars
##############

.. image:: https://circleci.com/gh/elbaschid/lektor-envvars.svg?style=svg
    :target: https://circleci.com/gh/elbaschid/lektor-envvars


Why this project?
-----------------

**TL;DR** You can use environment variables in your Lektor templates.

I've been working with `Lektor <https://www.getlektor.com/docs/plugins/>`_ as as
static site generator in quite a few projects and really enjoy it. Most recently
I work on a project that used an environment variable to create slightly
different version of the site for ``development``, ``staging`` and ``production``.

Lektor doesn't have a way to add *environment variables* into the templates, so
I started building my own little plugin.


How to install it in Lektor
---------------------------

You can easily install this plugin following the `Lektor docs
<https://www.getlektor.com/docs/plugins/>`_. All you need to do is run::

    $ lektor plugin add lektor-envvars

This will automatically install the plugin and add it to your project
configuration.


Using environment variables
---------------------------

You are able to access environment variables using the ``envvars`` function
inside your Jinja2 template. This function is added whenever lektor is running
a new build. 

All environment variables are prefixed with ``LEKTOR_`` by default. Let's look
at a simple example with an environment varialbe ``LEKTOR_DEBUG=true``::

    $ export LEKTOR_DEBUG=true

You can access this variable inside any Jinja2 template::

    {{ envvars('DEBUG') }}

which will display ``true`` instead.


Converting values
-----------------

That's a great start but what if you want this to be a boolean value instead of
the string ``true``? You simply convert the value::

    {{ envvars('DEBUG', bool) }}

or you can now even do::

    {% if envvars('DEBUG', bool) %}
        ...
    {% endif %}


Custom prefixes (or no prefix)
------------------------------

If you don't like the ``LEKTOR_`` prefix, you can either use your own prefix by
setting the prefix in the ``configs/lektor-envvars.ini`` file::

    [envvars]
    prefix = MY_OWN_

You can now use ``MY_OWN_DEBUG`` instead of ``LEKTOR_DEBUG``. This means that
all environment variables need to be prefixed with ``MY_OWN_`` now instead.

You can also ignore the prefix all together::

    {{ envvars('DEBUG', no_prefix=True) }}

which will give you access to the environment variable ``DEBUG``.


License
-------

This code is licensed under the `MIT License`_.

.. _`MIT License`: https://github.com/elbaschid/lektor-envvars/blob/master/LICENSE
