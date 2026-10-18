# PNG2SVG

PNG2SVG is a Python application that converts raster images into scalable SVG illustrations made of colored hexagons.

The input image is covered with a regular hexagonal grid. For each hexagon, the application samples pixels from the corresponding area of the original image, computes an average RGB color, and generates an SVG polygon using that color.

The project was developed using Test-Driven Development (TDD) and includes a reusable Python package, a command-line interface, an interactive Marimo application, automated tests, static analysis, continuous integration, and automatic deployment with GitHub Actions.

## Live demo

The interactive Marimo application is available online through GitHub Pages:

**https://matthieuringd.github.io/png2svg/**

The application runs directly in the browser using WebAssembly. Users can upload an image, select the hexagon radius, preview the generated result, and download the SVG file.

## Features

- Read PNG, JPG, and JPEG images with Pillow
- Generate a regular hexagonal grid over an image
- Sample and average RGB colors from the source image
- Generate SVG polygons from the sampled colors
- Export the result as a scalable `.svg` file
- Configure the hexagon radius
- Convert images directly from the command line
- Use the conversion functions as a Python package
- Upload and convert images interactively with Marimo
- Preview the generated SVG in the browser
- Download the generated SVG from the Marimo interface
- Run automated tests and code-quality checks with GitHub Actions
- Deploy the interactive application automatically to GitHub Pages

## Installation

Clone the repository:

```bash
git clone https://github.com/matthieuringd/png2svg.git
cd png2svg
```

Install the project and all development dependencies with `uv`:

```bash
uv sync --all-groups
```

## Usage

### Command-line interface

The application provides a command-line interface for converting an image directly into SVG.

Basic usage:

```bash
uv run png2svg input.png output.svg
```

You can customize the size of the generated hexagons with the `--radius` parameter:

```bash
uv run png2svg input.png output.svg --radius 10
```

A smaller radius generates more hexagons and preserves more details:

```bash
uv run png2svg input.png output.svg --radius 5
```

A larger radius generates fewer, larger hexagons and produces a more stylized result.

### Python

The conversion can also be used directly from Python:

```python
from pathlib import Path

from png2svg.converter import convert_file

convert_file(
    input_path=Path("input.png"),
    output_path=Path("output.svg"),
    radius=10,
)
```

The lower-level conversion function can operate directly on a Pillow image:

```python
from PIL import Image

from png2svg.converter import image_to_svg

image = Image.open("input.png").convert("RGB")

svg_content = image_to_svg(
    image=image,
    radius=10,
)
```

### Marimo interface

The project includes an interactive Marimo notebook:

```text
notebooks/png2svg_explorer.py
```

Launch it locally with:

```bash
uv run marimo edit notebooks/png2svg_explorer.py
```

The interface allows the user to:

- upload an image;
- choose the hexagon radius with a slider;
- preview the selected image;
- generate the SVG interactively;
- preview the generated hexagonal image;
- download the generated `.svg` file.

The notebook reuses the functions from the `png2svg` package and does not reimplement the conversion algorithm.

The same interface is also deployed publicly with WebAssembly:

**https://matthieuringd.github.io/png2svg/**

## How it works

The conversion pipeline is:

```text
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
Generate the complete SVG document
```

A regular flat-top hexagon is defined from its center and radius.

The grid uses the following spacing:

```text
horizontal spacing = 1.5 × radius
vertical spacing   = √3 × radius
```

Alternating columns are vertically shifted to create the hexagonal grid.

## Project structure

```text
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
│       ├── tests.yml
│       └── deploy-pages.yml
│
├── .gitignore
├── .python-version
├── pyproject.toml
├── uv.lock
└── README.md
```

## Development workflow

Each feature is developed using the following workflow:

```text
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
```

The project uses Test-Driven Development whenever possible:

1. **Red** — write a failing test.
2. **Green** — implement the smallest solution that makes the test pass.
3. **Refactor** — improve the implementation without changing its behavior.

## Testing and quality checks

Run the complete test suite with:

```bash
uv run pytest -v
```

Run the tests with coverage:

```bash
uv run pytest --cov=src --cov-report=term-missing
```

The project requires at least 90% source-code coverage.

Check formatting:

```bash
uv run ruff format --check src tests
```

Run the Ruff linter:

```bash
uv run ruff check src tests
```

Run static type checking:

```bash
uv run mypy src
```

Check Marimo WebAssembly compatibility:

```bash
uv run marimo check notebooks/png2svg_explorer.py --select MW
```

## Continuous Integration

GitHub Actions automatically checks the project on pushes and pull requests.

The CI workflow runs:

- Ruff formatting checks
- Ruff linting
- mypy static type checking
- pytest unit tests
- coverage checks
- Marimo WebAssembly compatibility checks

The interactive Marimo application is also automatically exported and deployed to GitHub Pages after successful validation.

## Technologies

The project uses:

- Python
- Pillow
- SVG
- uv
- pytest
- pytest-cov
- Ruff
- mypy
- Marimo
- WebAssembly / Pyodide
- Git
- GitHub
- GitHub Actions
- GitHub Pages

## Example

Convert an image with a hexagon radius of 10:

```bash
uv run png2svg input.png output.svg --radius 10
```

The generated `output.svg` reproduces the main colors and structures of the original image using a scalable hexagonal mosaic.

The radius controls the level of detail:

```text
smaller radius → more hexagons → more detail
larger radius  → fewer hexagons → more stylized result
```

## Author

Matthieu Ringard  
Master 1 Data Science — Centrale Lille