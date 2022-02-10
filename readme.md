# Reveal's Altair theme

A Reveal theme for [altair](https://altair-viz.github.io/).

With much gratitude to the [Los Angeles Times](https://github.com/datadesk/altair-latimes).


## Instructions

After setting up a Python virtualenv, install from PyPI:

```sh
% pip install altair-reveal
```

Import theme with Altair, then register and enable theme.

```python
import altair as alt
import altair_reveal as reveal

alt.themes.register('reveal', reveal.theme)
alt.themes.enable('reveal')
```

View and use a (limited) color palette.

```python
altair_reveal.palette
```

## Examples

Check out [the `examples` notebook](examples.ipynb) for examples of charts, including customizations.

## Fonts

System-wide 'Tenon' font installation required.

