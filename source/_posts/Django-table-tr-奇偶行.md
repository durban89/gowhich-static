---
title: Django table tr 奇偶行
tags:
  - Django
categories:
  - 技术
date: 2025-06-20 14:13:14
---

Method 1: The Cross-Browser CSS Way

The easiest way to do this is to make use of the built-in Django `{% raw %}{% cycle %}{% endraw %}` tag. Here’s how to use it for a table containing blog entries:

```html
<table>
<tbody>
{% for blog in blogs %}
  {% for entry in blog.entries %}
    <tr class="{% cycle 'odd' 'even' %}">
      {{entry.date}}
      {{entry.title}}
      {{entry.comments}}
    </tr>
  {% endfor %}
{% endfor %}
</tbody>
</table>
```

Method 2: The Pure CSS Way

```css
tbody tr:nth-child(even) td {background: #bbeebb;}
tbody tr:nth-child(odd) td {background: #e5f9e5;}
```

