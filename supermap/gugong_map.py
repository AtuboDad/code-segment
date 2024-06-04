# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from prettymaps import *
import matplotlib.font_manager as fm

fig, axl = plt.subplots(figsize=(12, 12), constrained_layout=True)
dilate = 100
layers = plot(
    (39.91645697864148, 116.39077532493388),
    radius=600,
    ax=axl,
    layers={
        'perimeter': {'circle': False, 'dilate': dilate},
        'streets': {
            'custom_filter': '["highway"~"motorway|trunk|primary|secondary|tertiary|residential|service|unclassified|pedestrian|footway"]',
            'width': {
                'motorway': 5,
                'trunk': 5,
                'primary': 4.5,
                'tertiary': 3.5,
                'residential': 3,
                'service': 2,
                'unclassified': 2,
                'pedestrian': 2,
                'footway': 1,
            },
            'circle': False,
            'dilate': dilate
        },
        'building': {'tags': {'building': True, 'landuse': 'construction'}, 'union': False, 'circle': False, 'dilate': dilate},
        'water': {'tags': {'natural': ['water', 'bay']}, 'union': False, 'circle': False, 'dilate': dilate},
        'green': {'tags': {'landuse': 'grass', 'natural': ['island', 'wood'], 'leisure': 'park'}, 'union': False, 'circle': False, 'dilate': dilate},
        'forest': {'tags': {'landuse': 'forest'}, 'union': False, 'circle': False, 'dilate': dilate},
        'parking': {'tags': {'amenity': 'parking', 'highway': 'pedestrian', 'man_made': 'pier'}, 'union': False, 'circle': False, 'dilate': dilate}
    },
    drawing_kwargs={
        'background': {'fc': '#F2F4CB', 'ec': '#dadbc1', 'hatch': 'ooo...', 'zorder': -1},
        'perimeter': {'fc': '#F2F4CB', 'ec': '#dadbc1', 'lw': 0, 'hatch': 'ooo...', 'zorder': 0},
        'green': {'fc': '#D0F1BF', 'ec': '#2F3737', 'lw': 1, 'zorder': 1},
        'forest': {'fc': '#64B96A', 'ec': '#2F3737', 'lw': 1, 'zorder': 1},
        'water': {'fc': '#a1e3ff', 'ec': '#2F3737', 'hatch': 'ooo...', 'hatch_c': '#85c9e6', 'lw': 1, 'zorder': 2},
        'parking': {'fc': '#F2F4CB', 'ec': '#2F3737', 'lw': 1, 'zorder': 3},
        'streets': {'fc': '#2F3737', 'ec': '#475657', 'alpha': 1, 'lw': 0, 'zorder': 3},
        'building': {'palette': ['#FFC857', '#E9724C', '#C5283D'], 'ec': '#2F3737', 'lw': 1, 'zorder': 1},
    },
    osm_credit={'color': '#2F3737'}
)

axl.text(
    0.5, 0.5,
    '故宫，故宫',
    zorder=6,
    ha='center',
    va='center',
    fontsize=60,
    fontproperties=fm.FontProperties(fname=r'D:\workspaces\pythonspaces\QT_downloader\Commons\FZKaTong-M19S.ttf'),
    transform=axl.transAxes
)

plt.show()