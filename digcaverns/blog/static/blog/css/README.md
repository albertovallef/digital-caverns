## Generate Pygments code styling

Defaults code annotations:

```bash
pygmentize -S default -f html -a .codehilite > article_detail.css
```

## Customize other article html tags

Overwrite current html elements:

```css
.article-post h1 {
    background-color: lightblue
}
```
