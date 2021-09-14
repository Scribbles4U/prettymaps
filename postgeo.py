#!/usr/bin/python3

import sys
sys.path.append('../')

import vsketch
from prettymaps import *
import matplotlib.font_manager as fm
from matplotlib import pyplot as plt

location = input('What location to map (City, Country): ')
filename = input('Name of file (ex. city.png): ')


def postprocessing(layers):
    layers['perimeter'] = layers['perimeter'].buffer(10)
    return layers

fig, ax = plt.subplots(figsize = (15, 12), constrained_layout = True)

layers = plot(
    f'{location}',

    ax = ax,

    postprocessing = postprocessing,

    layers = {
            'perimeter': {},
            'streets': {
                'width': {
                    #'motorway': 8,
                    'trunk': 6,
                    'primary': 6,
                    'secondary': 5,
                    'tertiary': 4,
                    'residential': 3,
                    #'living_street': 3,
                    'pedestrian': 1.5,
                    'footway': 1.5,
                    #'track': 1,
                    #'bridleway': 1
                }
            },
            'building': {'tags': {'building': True}, 'union': False},
            'water': {'tags': {'natural': ['water', 'bay']}},
            'green': {'tags': {'landuse': 'grass', 'natural': ['island', 'wood'], 'leisure': 'park'}},
        },
        drawing_kwargs = {
            'background': {'fc': '#F7F3F5', 'ec': '#EFE7EB', 'hatch': 'ooo...', 'zorder': -1},
            'perimeter': {'fc': '#F7F3F5', 'ec': '#2F3737', 'lw': 3, 'hatch': 'ooo...', 'hatch_c': '#EFE7EB',  'zorder': 0},
            'green': {'fc': '#AABD8C', 'ec': '#2F3737', 'hatch_c': '#b3cfa5', 'hatch': 'ooo...', 'lw': 0, 'zorder': 1},
            'water': {'fc': '#a1e3ff', 'hatch': 'ooo...', 'hatch_c': '#80bed9', 'lw': 0, 'zorder': 2},
            'streets': {'fc': '#3b4545', 'lw': 0, 'zorder': 3},
            'building': {'palette': ['#433633', '#FF5E5B'], 'ec': '#2F3737', 'hatch': 'ooo...', 'hatch_c': '#b3504f', 'lw': 0, 'zorder': 4},
        },

        osm_credit = {'color': '#3b4545'}
)

plt.savefig(f'{filename}')
