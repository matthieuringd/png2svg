# PNG2SVG

Description

PNG2SVG is a Python application that converts raster images into scalable SVG
illustrations made of colored hexagons.

The input image is sampled using a regular hexagonal grid. For each hexagon,
the application computes an average RGB color from the corresponding area of
the original image and creates an SVG polygon using that color.

The project was developed using Test-Driven Development and includes a reusable
Python library, a command-line interface, an interactive Marimo interface,
automated tests, static analysis, and continuous integration with GitHub Actions.

## Features

- Read PNG, JPG, and JPEG images with Pillow
- Generate a regular hexagonal grid over the image
- Sample and average RGB colors from the source image
- Generate SVG polygons from the sampled colors
- Export the complete result as a scalable `.svg` file
- Configure the hexagon radius
- Convert files directly from the command line
- Upload and convert images interactively with Marimo
- Preview the original and generated images
- Download the generated SVG from the Marimo interface
- Automated testing and code quality checks with GitHub Actions
## Installation
Clone the repository:

```bash
git clone https://github.com/matthieuringd/png2svg.git
cd png2svg

Install the project and its dependencies with uv:
uv sync --all-groups


## Usage

The application provides a command-line interface for converting an image
directly into SVG.
Basic usage:
uv run png2svg input.png output.svg

You can customize the size of the generated hexagons with the --radius
parameter:
uv run png2svg input.png output.svg --radius 10

A smaller radius produces more hexagons and therefore preserves more details:
uv run png2svg input.png output.svg --radius 5

A larger radius produces fewer, larger hexagons and a more stylized result.

### Python

The conversion logic can also be used directly from Python:

from pathlib import Path

from png2svg.converter import convert_file

convert_file(
    input_path=Path("input.png"),
    output_path=Path("output.svg"),
    radius=10,
)

The lower-level conversion function can operate directly on a Pillow image:

from PIL import Image

from png2svg.converter import image_to_svg

image = Image.open("input.png").convert("RGB")

svg_content = image_to_svg(
    image=image,
    radius=10,
)

### Marimo interface

The project includes an interactive Marimo notebook:
notebooks/png2svg_explorer.py

Launch it with:
uv run marimo edit notebooks/png2svg_explorer.py

The interface allows the user to:
- upload an image;
- choose the hexagon radius with a slider;
- preview the original image;
- generate the SVG interactively;
- preview the generated hexagonal image;
- download the generated .svg file.
The notebook reuses the functions from the png2svg package and does not
reimplement the conversion algorithm.

## How it works

The conversion pipeline is:
Input image
    ↓
Load image with Pillow
    ↓
Generate hexagonal grid positions
    ↓
Generate the six vertices of each hexagon
    ↓
Sample pixels around each hexagon center
    ↓
Compute the average RGB color
    ↓
Generate an SVG polygon
    ↓
Combine all polygons
    ↓
Write the complete SVG file

A regular flat-top hexagon is defined from its center and radius.
The centers are arranged using:
horizontal spacing = 1.5 × radius
vertical spacing   = √3 × radius

Alternating columns are vertically shifted to create the hexagonal grid.
## Project structure

png2svg/
├── src/
│   └── png2svg/
│       ├── __init__.py
│       ├── cli.py
│       ├── converter.py
│       ├── geometry.py
│       ├── sampling.py
│       └── svg.py
│
├── tests/
│   ├── test_cli.py
│   ├── test_converter.py
│   ├── test_geometry.py
│   ├── test_sampling.py
│   └── test_svg.py
│
├── notebooks/
│   └── png2svg_explorer.py
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── .gitignore
├── .python-version
├── pyproject.toml
├── uv.lock
└── README.md
## Development

Each feature is developed using:
GitHub Issue
    ↓
Feature branch
    ↓
Failing test
    ↓
Implementation
    ↓
Passing tests
    ↓
Pull Request
    ↓
Continuous Integration
    ↓
Merge into main

The project uses Test-Driven Development whenever possible:
1. Red — write a failing test;
2. Green — implement the smallest solution that passes;
3. Refactor — improve the implementation without changing its behavior.

## Testing and quality checks
Run the complete test suite with:
uv run pytest -v

Run the tests with coverage:
uv run pytest --cov=src --cov-report=term-missing

The project requires at least 90% source-code coverage.

## Example