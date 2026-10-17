import math

from png2svg.geometry import hexagon_centers, hexagon_vertices


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


def test_hexagon_grid_contains_centers():
    # Even for a small image, the grid should generate at least one hexagon center.
    centers = hexagon_centers(width=100, height=100, radius=10)

    assert len(centers) > 0


def test_hexagon_grid_starts_at_expected_position():
    # The first hexagon is placed with its center one radius away from the borders.
    centers = hexagon_centers(width=100, height=100, radius=10)

    x, y = centers[0]

    assert math.isclose(x, 10.0)
    assert math.isclose(y, math.sqrt(3) * 5)


def test_second_column_is_vertically_shifted():
    centers = hexagon_centers(width=100, height=100, radius=10)

    # Horizontal spacing between flat-top hexagons is 1.5 * radius.
    second_column_x = 10.0 + 1.5 * 10

    second_column = [(x, y) for x, y in centers if x == second_column_x]

    # Alternate columns should be shifted vertically.
    assert second_column[0][1] > 10.0
