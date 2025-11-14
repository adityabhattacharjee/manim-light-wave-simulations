# Light Interference and Diffraction with Manim

This project demonstrates light interference and diffraction using Manim, a mathematical animation engine.

## Features

1. **Light Interference (Double-Slit)**
   - **Presenter Information**: Displayed on all slides
   - **Introduction**: "What is Interference?" with definition and key concepts
   - Visualizes wave interference from two point sources (S1 and S2)
   - Shows waves expanding and overlapping
   - **Detailed wave superposition demonstration**:
     - Shows individual sine waves with marked crests and troughs
     - Demonstrates **constructive interference** (Crest + Crest = Bright)
     - Demonstrates **destructive interference** (Crest + Trough = Dark/Cancelled)
     - Visual proof of how waves add and cancel
   - Returns to full setup showing wave interference in real-time
   - Displays the complete interference pattern with bright and dark fringes

2. **Light Diffraction (Single-Slit)**
   - **Presenter Information**: Displayed on all slides
   - **Introduction**: "What is Diffraction?" explaining:
     - Definition of diffraction
     - How light bends around obstacles
     - Why light doesn't travel in straight lines through small openings
     - That it proves light behaves as a wave
   - Demonstrates single-slit diffraction phenomenon
   - Shows Huygens' Principle (each point in slit acts as wave source)
   - Visualizes wavelet propagation and interference
   - Shows wave field between slit and screen
   - Displays final diffraction pattern on screen
   - Includes the intensity distribution formula

## Requirements

- Python 3.7+
- Manim
- NumPy

## Installation

1. Clone this repository
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the interference demo:
```bash
manim -pql main.py LightInterference
```

To run the diffraction demo:
```bash
manim -pql main.py LightDiffraction
```

To run the interactive menu (currently in development):
```bash
manim -pql main.py LightDemo
```

## Controls

- Press `q` to quit the animation
- Press `p` to pause/resume the animation
- Use the left/right arrow keys to move frame by frame when paused

## Customization

You can modify the following parameters in the code:
- Wavelength of light
- Distance between sources
- Refractive indices
- Animation speeds
- Colors and styles

## License

This project is open source and available under the MIT License.
