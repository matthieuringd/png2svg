from PIL import Image

from png2svg.converter import image_to_svg


def test_image_to_svg_returns_complete_svg():
    # Create a small image with one uniform color.
    image = Image.new("RGB", (20, 20), color=(100, 150, 200))

    svg = image_to_svg(image, radius=5)

    # The result should be a complete SVG document.
    assert "<svg" in svg
    assert "</svg>" in svg

    # Since the whole image has the same color,
    # the generated polygons should use this RGB value.
    assert 'fill="rgb(100,150,200)"' in svg

    # The output should contain at least one hexagonal polygon.
    assert "<polygon" in svg