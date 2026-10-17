from PIL import Image

from png2svg.sampling import sample_color


def test_sample_color_on_uniform_image():
    # Create a small 5x5 image where every pixel has the same RGB color.
    image = Image.new("RGB", (5, 5), color=(100, 150, 200))

    # Sampling around the center should return exactly the same color.
    color = sample_color(image, center_x=2, center_y=2, radius=1)

    assert color == (100, 150, 200)


def test_sample_color_computes_average():
    # Create a 3x3 image with a black background.
    image = Image.new("RGB", (3, 3), color=(0, 0, 0))

    # Change the center pixel to white.
    image.putpixel((1, 1), (255, 255, 255))

    # With radius 1, all 9 pixels are sampled.
    color = sample_color(image, center_x=1, center_y=1, radius=1)

    # Average: 255 / 9 = 28 using integer division.
    assert color == (28, 28, 28)
