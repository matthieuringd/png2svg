"""Color sampling utilities for PNG to SVG conversion."""

from PIL import Image


def sample_color(
    image: Image.Image,
    center_x: int,
    center_y: int,
    radius: int,
) -> tuple[int, int, int]:
    """Return the average RGB color around a given center point."""

    red_total = 0
    green_total = 0
    blue_total = 0
    pixel_count = 0

    # Sample pixels in a square area around the center.
    for x in range(center_x - radius, center_x + radius + 1):
        for y in range(center_y - radius, center_y + radius + 1):
            # Ignore coordinates outside the image boundaries.
            if 0 <= x < image.width and 0 <= y < image.height:
                red, green, blue = image.getpixel((x, y))

                red_total += red
                green_total += green
                blue_total += blue
                pixel_count += 1

    # Compute the average value of each RGB channel.
    return (
        red_total // pixel_count,
        green_total // pixel_count,
        blue_total // pixel_count,
    )