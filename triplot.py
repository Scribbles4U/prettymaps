#!/usr/bin/python3

import sys
sys.path.append('../')

import vsketch
from prettymaps import *
import matplotlib.font_manager as fm
from matplotlib import pyplot as plt

location = input('1. What location to map (City, Country): ')
location2 = input('2. What location to map (City, Country): ')
location3 = input('3. What location to map (City, Country): ')
filename = input('Name of file (ex. city.png): ')

fig, ax = plt.subplots(figsize = (12, 12), constrained_layout = True)

places = {
    f'{location}': ['#EEE4E1', '#E7D8C9', '#E6BEAE'],
    f'{location2}': ['#49392C', '#77625C', '#B2B1CF', '#E1F2FE', '#98D2EB'],
    f'{location3}': ['#BA2D0B', '#D5F2E3', '#73BA9B', '#F79D5C'],
}

for i, (place, palette) in enumerate(places.items()):
    plot(
        place,

        ax = ax,

        layers = {
            'perimeter': {},
            'streets': {
                'width': {
                    'trunk': 6,
                    'primary': 6,
                    'secondary': 5,
                    'tertiary': 4,
                    'residential': 3.5,
                    'pedestrian': 3,
                    'footway': 3,
                    'path': 3,
                }
            },
            'building': {'tags': {'building': True, 'leisure': ['track', 'pitch']}, 'union': False},
            'water': {'tags': {'natural': ['water', 'bay']}},
            'park': {'tags': {'leisure': 'park'}},
            'forest': {'tags': {'landuse': 'forest'}},
            'garden': {'tags': {'leisure': 'garden'}},
        },
        drawing_kwargs = {
            'perimeter': {'fill': False, 'lw': 0, 'zorder': 0},
            'park': {'fc': '#AABD8C', 'ec': '#87996b', 'lw': 1, 'zorder': 1},
            'forest': {'fc': '#78A58D', 'ec': '#658a76', 'lw': 1, 'zorder': 1},
            'garden': {'fc': '#a9d1a9', 'ec': '#8ab58a', 'lw': 1, 'zorder': 1},
            'water': {'fc': '#92D5F2', 'ec': '#6da8c2', 'lw': 1, 'zorder': 2},
            'streets': {'fc': '#F1E6D0', 'ec': '#2F3737', 'lw': 1.5, 'zorder': 3},
            'building': {'palette': palette, 'ec': '#2F3737', 'lw': 1, 'zorder': 4},
        },

        osm_credit = {'x': -.57, 'y': -.55, 'color': '#2F3737'} if i == 0 else None
    )

ax.autoscale()

plt.savefig(f'{filename}')
