"""
Reveal theme for the data visualization library Altair.
"""

# Color schemes and defaults
palette = dict(
    black='#222222',
    white='#ffffff',
    background='#f9f9f9',
    light_grey='#dddddd',
    dark_grey='#666666',
    orange='#e54600',
    dark_blue='#004488',
    blue='#0077bb',
    magenta='#c51b8a'
)

def theme():
    """
    Altair theme for Reveal
    """
    return dict(
        config=dict(
            view=dict(
                width=320,
                height=500,
                strokeOpacity=0
            ),
            background=palette['background'],
            padding={'left': 20, 'top': 20, 'right': 20, 'bottom': 80},
            arc=dict(fill=palette['blue']),
            area=dict(fill=palette['blue']),
            line=dict(stroke=palette['blue'], strokeWidth=3),
            path=dict(stroke=palette['blue']),
            rect=dict(fill=palette['blue']),
            shape=dict(stroke=palette['blue']),
            bar=dict(fill=palette['blue']),
            point=dict(stroke=palette['blue']),
            symbol=dict(fill=palette['blue'], size=30),
            title=dict(
                font='Tenon', 
                fontSize=28, 
                color=palette['black'], 
                fontWeight=500,
                align='left', 
                anchor='start',
                subtitleFont='Tenon',
                subtitleColor=palette['black'],
                subtitleFontSize=20,
                subtitleFontWeight=300,
                subtitlePadding=10,
                subtitleLineHeight=24
            ),
            axis=dict(
                gridColor=palette['light_grey'],
                title=None,
                titleColor=palette['dark_grey'],
                titleFontWeight=300,
                labelColor=palette['dark_grey'],
                labelFont='Tenon',
                labelFontSize=13,
                labelFontWeight=400,
                labelFlush=False,
                labelPadding=5,
                tickSize=6,
            ),
            axisX=dict(
                domainColor=palette['dark_grey'],
                tickColor=palette['dark_grey'],
            ),
            axisY=dict(
                domainColor=palette['background'],
                tickColor=palette['background'],
            ),
            legend=dict(
                title=None,
                orient='top',
                direction='horizontal',
                offset=40,
                columnPadding=20,
                titleFont='Tenon',
                titleFontSize=16,
                titleFontWeight=400,
                labelAlign='left',
                labelFont='Tenon',
                labelFontSize=16,
                labelFontWeight=300,
                labelColor=palette['black'],
                labelBaseline='middle',
                rowPadding=10,
                symbolType='square',
            )
        )
    )