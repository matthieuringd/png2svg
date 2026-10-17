"""SVG generation utilities for PNG to SVG conversion."""


def svg_polygon(
    vertices: list[tuple[float, float]],
    color: tuple[int, int, int],
) -> str:
    """Return an SVG polygon element from vertices and an RGB color."""

    # SVG expects coordinates in the form: x1,y1 x2,y2 x3,y3 ...
    points = " ".join(f"{x},{y}" for x, y in vertices)

    red, green, blue = color

    # Create one SVG polygon filled with the sampled RGB color.
    return f'<polygon points="{points}" fill="rgb({red},{green},{blue})" />'


def svg_document(
    width: int,
    height: int,
    polygons: list[str],
) -> str:
    """Return a complete SVG document containing the given polygons."""

    # Join all polygon elements together, one per line.
    polygon_content = "\n".join(polygons)

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}">\n'
        f"{polygon_content}\n"
        "</svg>"
    )
