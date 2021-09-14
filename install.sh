#!/bin/bash
pip install git+https://github.com/abey79/vsketch#egg=vsketch
pip install git+https://github.com/marceloprates/prettymaps.git

mkdir ../prints
mkdir ../assets
mkdir ../assets/Permanent_Marker/
wget -O ../assets/Permanent_Marker/PermanentMarker-Regular.ttf https://github.com/marceloprates/prettymaps/raw/main/assets/Permanent_Marker/PermanentMarker-Regular.ttf
