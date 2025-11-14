# Manim Light Wave Simulations

Manim animations demonstrating light wave phenomena: double-slit interference and single-slit diffraction.

## Features

- **LightInterference**: Double-slit setup, wave superposition, constructive/destructive interference, fringe pattern.
- **LightDiffraction**: Single-slit diffraction using Huygens' principle, wavelets, intensity distribution, final pattern.
- **LightDemo**: Combined/demo scene.

## Quick Start

```bash
# macOS: system deps for cairo (required by manim/manimpango)
brew install cairo pkg-config

# create & activate venv
python3 -m venv venv
source venv/bin/activate

# install python deps
pip install -r requirements.txt
```

## Run

```bash
# Interference (1080p, quick preview)
manim -pql main.py LightInterference

# Diffraction (1080p, quick preview)
manim -pql main.py LightDiffraction

# Demo scene
manim -pql main.py LightDemo
```

- Outputs are written to `media/videos/main/` (e.g., `1080p60/LightInterference.mp4`).
- Use `-pqh` for higher quality or `-pqm`/`-pql` for medium/low.

## Controls

- `q` quit
- `p` pause/resume
- Arrow keys frame step when paused

## Customize

Adjust parameters in `main.py`:
- Wavelength, source spacing, slit width
- Animation speeds, colors/styles

## Requirements

- Python 3.9+
- Manim, NumPy (see `requirements.txt`)

## Project Structure

- `main.py` — scenes: `LightInterference`, `LightDiffraction`, `LightDemo`
- `requirements.txt` — Python dependencies
- `media/` — render outputs (gitignored)

## License

This project is released under the MIT License. See `LICENSE`.

## Repository

https://github.com/adityabhattacharjee/manim-light-wave-simulations
