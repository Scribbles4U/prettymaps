#!/usr/bin/python3

import sys
sys.path.append('../')

import vsketch
from prettymaps import *
import matplotlib.font_manager as fm
from matplotlib import pyplot as plt

location = input('What location to map (City, Country): ')
filename = input('Name of file (ex. city.png): ')

palette = ['#FFC857', '#E9724C', '#C5283D']

fig, ax = plt.subplots(figsize = (12, 12), constrained_layout = True)

backup = plot(
    f'{location}', radius = 1500,

    ax = ax,

    layers = {
            'perimeter': {},
            'streets': {
                'width': {
                    'motorway': 5,
                    'trunk': 5,
                    'primary': 4.5,
                    'secondary': 4,
                    'tertiary': 3.5,
                    'residential': 3,
                    'living_street': 2,
                    'pedestrian': 1,
                    'footway': 1,
                    'track': 1,
                    'bridleway': 1
                }
            },
            'building': {'tags': {'building': True, 'landuse': 'construction'}, 'union': False},
            'water': {'tags': {'natural': ['water', 'bay']}},
            'green': {'tags': {'landuse': 'grass', 'natural': ['island', 'wood'], 'leisure': 'park'}},
            'scrub': {'tags': {'natural': 'scrub'}},
            'walls': {'tags': {'manmade': 'embankment'}},
        },
        drawing_kwargs = {
            'background': {'fc': '#F2F4CB', 'ec': '#dadbc1', 'hatch': 'ooo...', 'zorder': -1},
            'perimeter': {'fc': '#F2F4CB', 'ec': '#dadbc1', 'lw': 0, 'hatch': 'ooo...',  'zorder': 0},
            'green': {'fc': '#D0F1BF', 'ec': '#2F3737', 'hatch_c': '#b3cfa5', 'hatch': 'ooo...', 'lw': 1, 'zorder': 1},
            'scrub': {'fc': '#89d689', 'ec': '#2F3737', 'hatch_c': '#75bd75', 'hatch': 'ooo...', 'lw': 1, 'zorder': 1},
            'water': {'fc': '#a1e3ff', 'ec': '#2F3737', 'lw': 1, 'zorder': 2},
            'streets': {'fc': '#2F3737', 'ec': '#475657', 'alpha': 1, 'lw': 0, 'zorder': 3},
            'walls': {'fc': '#2F3737', 'ec': '#475657', 'alpha': 1, 'lw': 0, 'zorder': 3},
            'building': {'palette': palette, 'ec': '#2F3737', 'lw': .5, 'zorder': 4},
        },

        osm_credit = {'color': '#2F3737'}
)

plt.savefig(f'{filename}')
