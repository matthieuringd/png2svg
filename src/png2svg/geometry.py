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