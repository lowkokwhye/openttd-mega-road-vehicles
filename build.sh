#!/bin/sh
set -eu
cd "$(dirname "$0")"
python tools/generate_sprites.py
nmlc --grf mega_road_vehicles_v0.1.0.grf --lang src/lang src/mega_road_vehicles.nml
