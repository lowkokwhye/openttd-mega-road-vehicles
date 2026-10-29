# Mega Road Vehicles (OpenTTD NewGRF)

Separate OpenTTD road vehicle NewGRF, starting with **MegaBus**. This project is independent of Maglev High Capacity Wagons.

## MegaBus v0.1.0

- Passengers: 5,000
- Speed: 512 km/h
- Power: 2,585 hp
- Vehicle weight: 35 tonnes
- Lifetime: 255 years
- Purchase cost factor: 0; running cost base: none, running cost factor: 0
- Target reliability: 99% (not guaranteed by the NewGRF reliability settings)
- Target maximum tractive effort: 34.2 kN (requires OpenTTD physics validation)
- Fast loading: 255

OpenTTD economy settings affect the displayed purchase price; check whether $0 is achieved in-game. Engine reliability is not directly fixed at 99% by `reliability_decay: 0`.

## Graphics

Original eight-view OpenGFX second-generation passenger bus sprites, from `sprites/png/roadvehicles/vehiclesroad01.png`, mapped using original `base-3092-road-vehicles.pnml` geometry. OpenGFX contributors' art is GPL-2.0; retain attribution when distributing. Sprites are generated as indexed 8bpp to preserve the original palette.

## Build

```sh
python -m pip install nml Pillow
sh build.sh
```

GitHub Actions builds `mega_road_vehicles_v0.1.0.grf` automatically on push and publishes an artifact.

## Future expansion

The project is designed to add further buses and cargo-specific road vehicles without changing the GRF name or repository identity.
