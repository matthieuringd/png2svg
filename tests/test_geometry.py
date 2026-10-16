from png2svg.geometry import hexagon_vertices
import math

def test_hexagon_has_six_vertices():
    # A regular hexagon must always contain exactly six corner points.
    vertices = hexagon_vertices(center_x=0.0, center_y=0.0, radius=1.0)

    # We only check the number of generated vertices for this first test.
    assert len(vertices) == 6

def test_hexagon_first_vertex_is_correct():
    # With a center at (0, 0) and radius 1,
    # the first vertex at angle 0° should be located at (1, 0).
    vertices = hexagon_vertices(center_x=0.0, center_y=0.0, radius=1.0)

    x, y = vertices[0]

    assert math.isclose(x, 1.0)
    assert math.isclose(y, 0.0, abs_tol=1e-9)