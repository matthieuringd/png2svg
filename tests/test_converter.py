from PIL import Image

from png2svg.converter import convert_file, image_to_svg


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


def test_convert_file_creates_svg(tmp_path):
    # Create a small temporary PNG image.
    input_path = tmp_path / "input.png"
    output_path = tmp_path / "output.svg"

    image = Image.new("RGB", (20, 20), color=(100, 150, 200))
    image.save(input_path)

    # Convert the PNG file into an SVG file.
    convert_file(
        input_path=input_path,
        output_path=output_path,
        radius=5,
    )

    # The output SVG file should have been created.
    assert output_path.exists()

    # Check that the generated file contains valid SVG content.
    content = output_path.read_text(encoding="utf-8")

    assert "<svg" in content
    assert "</svg>" in content
    assert "<polygon" in content
    assert 'fill="rgb(100,150,200)"' in content
