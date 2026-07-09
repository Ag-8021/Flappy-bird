# FlappyBird-Pygame

A classic 2D arcade clone of the popular game "Flappy Bird" built using Python and the Pygame library. This project implements custom physics, random obstacle generation, collision processing, and a game-over UI state machine.

## Features
* **Physics Simulation:** Realistic bird movement handling gravity acceleration and instant velocity changes via jumping.
* **Procedural Obstacles:** Endless pipe generation with randomized heights and static gap constraints.
* **Collision Engine:** Pixel-and-bounding-box logic monitoring boundaries (ceiling/floor) and obstacle overlap to trigger accurate game-over sequences.
* **State Management:** Seamless transitions from a splash "Ready" screen to the active gameplay loop, ending in a static "Game Over" scoreboard.

## Controls
* **Spacebar:** Jump upwards / Flap wings
* **Close window (X):** Exit game

## Getting Started

### Option 1: Direct Play (Windows Users)
No Python setup required!
1. Navigate to the latest release or project folder.
2. Download and double-click `flappy_bird.exe` to start playing instantly.

### Option 2: Run the Source Code
If you want to run or modify the Python code directly:

#### Prerequisites
Make sure you have Python 3.x and Pygame installed:
```bash
pip install pygame
