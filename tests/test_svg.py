from png2svg.svg import svg_polygon, svg_document


def test_svg_polygon_contains_vertices_and_color():
    # Simple hexagon-like coordinates used to test the SVG formatting.
    vertices = [
        (10.0, 10.0),
        (20.0, 10.0),
        (25.0, 20.0),
        (20.0, 30.0),
        (10.0, 30.0),
        (5.0, 20.0),
    ]

    color = (100, 150, 200)

    polygon = svg_polygon(vertices, color)

    # The result should be an SVG polygon using the given points and RGB color.
    assert "<polygon" in polygon
    assert 'fill="rgb(100,150,200)"' in polygon
    assert "10.0,10.0" in polygon

def test_svg_document_wraps_polygons():
    polygon = svg_polygon(
        vertices=[
            (10.0, 10.0),
            (20.0, 10.0),
            (25.0, 20.0),
            (20.0, 30.0),
            (10.0, 30.0),
            (5.0, 20.0),
        ],
        color=(100, 150, 200),
    )

    document = svg_document(
        width=100,
        height=80,
        polygons=[polygon],
    )

    # A complete SVG document should contain an opening SVG tag,
    # the polygon content, and a closing SVG tag.
    assert '<svg' in document
    assert 'width="100"' in document
    assert 'height="80"' in document
    assert polygon in document
    assert "</svg>" in document