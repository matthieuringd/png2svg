from PIL import Image

from png2svg.converter import image_to_svg


INPUT_FILE = "input.png"
OUTPUT_FILE = "output.svg"


image = Image.open(INPUT_FILE).convert("RGB")

svg_content = image_to_svg(
    image=image,
    radius=10,
)

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    file.write(svg_content)

print(f"SVG generated successfully: {OUTPUT_FILE}")