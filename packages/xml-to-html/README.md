# Lektor XML atom feed to html

This plugin enables a way to import an atom xml feed into [Lektor](http://getlektor.com) static website directly in the template.

## Configuration

In the template where you would like to import the feed add the following:

```
{{ render_stream("https://blog.example.org/rss.xml")|safe }}

```

The plugin will add the following to your built html:

```
<div class="row">
  <h3>
    <a href="https://www.example.org/posts/this-is-a-post-link">
      This is a post title
    </a>
  </h3>
</div>
```

For each entry in your feed.
