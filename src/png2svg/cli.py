"""Command-line interface for png2svg."""

import argparse
from pathlib import Path

from png2svg.converter import convert_file


def build_parser() -> argparse.ArgumentParser:
    """Create and return the command-line argument parser."""

    parser = argparse.ArgumentParser(
        prog="png2svg",
        description="Convert an image into an SVG made of colored hexagons.",
    )

    parser.add_argument(
        "input",
        help="Path to the input image.",
    )

    parser.add_argument(
        "output",
        help="Path to the output SVG file.",
    )

    parser.add_argument(
        "--radius",
        type=int,
        default=10,
        help="Hexagon radius used for the conversion (default: 10).",
    )

    return parser


def main() -> None:
    """Run the PNG to SVG conversion from the command line."""

    parser = build_parser()
    args = parser.parse_args()

    convert_file(
        input_path=Path(args.input),
        output_path=Path(args.output),
        radius=args.radius,
    )


if __name__ == "__main__":
    main()
