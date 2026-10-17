"""Main PNG to SVG conversion logic."""

from pathlib import Path

from PIL import Image

from png2svg.geometry import hexagon_centers, hexagon_vertices
from png2svg.sampling import sample_color
from png2svg.svg import svg_document, svg_polygon


def image_to_svg(
    image: Image.Image,
    radius: int,
) -> str:
    """Convert a Pillow image into an SVG made of colored hexagons."""

    polygons = []

    # Generate all hexagon center positions needed for the image.
    centers = hexagon_centers(
        width=image.width,
        height=image.height,
        radius=radius,
    )

    for center_x, center_y in centers:
        # Compute the six vertices of this hexagon.
        vertices = hexagon_vertices(
            center_x=center_x,
            center_y=center_y,
            radius=radius,
        )

        # Sample the average color around the hexagon center.
        color = sample_color(
            image=image,
            center_x=round(center_x),
            center_y=round(center_y),
            radius=radius,
        )

        # Convert the geometry and color into an SVG polygon.
        polygon = svg_polygon(vertices, color)
        polygons.append(polygon)

    # Wrap every polygon inside a complete SVG document.
    return svg_document(
        width=image.width,
        height=image.height,
        polygons=polygons,
    )


def convert_file(
    input_path: Path,
    output_path: Path,
    radius: int,
) -> None:
    """Convert an input image file into an SVG file."""

    # Open the image and make sure its pixels are represented as RGB values.
    image = Image.open(input_path).convert("RGB")

    # Reuse the main conversion logic.
    svg_content = image_to_svg(image, radius)

    # Write the generated SVG to disk.
    output_path.write_text(svg_content, encoding="utf-8")
