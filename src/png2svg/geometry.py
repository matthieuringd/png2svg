"""Geometry utilities for the PNG to SVG conversion."""

import math


def hexagon_vertices(
    center_x: float,
    center_y: float,
    radius: float,
) -> list[tuple[float, float]]:
    """Return the six vertices of a regular hexagon.

    The hexagon is defined by its center coordinates and its radius.
    The radius is the distance from the center to each vertex.
    """

    vertices = []

    # A regular hexagon has 6 corners, separated by 60 degrees.
    for i in range(6):
        angle = math.radians(60 * i)

        # Convert polar coordinates into normal x/y coordinates.
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)

        vertices.append((x, y))

    return vertices


def hexagon_centers(
    width: int,
    height: int,
    radius: float,
) -> list[tuple[float, float]]:
    """Return the centers of a hexagonal grid covering an image."""

    centers = []

    horizontal_spacing = 1.5 * radius
    vertical_spacing = math.sqrt(3) * radius

    column = 0
    x = radius

    while x < width:
        # Start half a hexagon height from the top border.
        vertical_offset = vertical_spacing / 2 if column % 2 == 1 else 0

        y = vertical_spacing / 2 + vertical_offset

        while y < height:
            centers.append((x, y))
            y += vertical_spacing

        x += horizontal_spacing
        column += 1

    return centers
