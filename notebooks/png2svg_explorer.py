# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "pillow",
# ]
# ///

import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


with app.setup:
    import io

    import marimo as mo
    from PIL import Image

    from png2svg.converter import image_to_svg


@app.cell(hide_code=True)
def _():
    mo.md(
        r"""
        # PNG2SVG Explorer

        Select an input image and choose the hexagon radius used for the conversion.
        """
    )
    return


@app.cell
def _():
    # File selector for the input image
    image_file = mo.ui.file(
        filetypes=[".png", ".jpg", ".jpeg"],
        multiple=False,
        label="Choose an image",
    )

    # Slider to control the hexagon radius
    radius = mo.ui.slider(
        start=2,
        stop=30,
        value=10,
        step=1,
        label="Hexagon radius",
    )

    mo.vstack([image_file, radius])
    return (image_file, radius)


@app.cell(hide_code=True)
def _(image_file, radius):
    mo.md(
        f"""
        ### Current settings

        **Radius:** {radius.value}

        **Image selected:** {"Yes" if image_file.value else "No"}
        """
    )
    return


@app.cell
def _(image_file, io, Image):
    image = None

    if not image_file.value:
        mo.md("No image selected yet.")
    else:
        # Marimo gives us the uploaded file in memory
        uploaded_file = image_file.value[0]

        # Open it with Pillow
        image = Image.open(io.BytesIO(uploaded_file.contents)).convert("RGB")

        # Display the input image
        image

    return (image,)


@app.cell
def _(image, radius, mo, image_to_svg):
    svg_text = None

    if image is None:
        svg_preview = mo.md("No SVG generated yet.")
    else:
        # Generate the SVG from the selected image and radius
        svg_text = image_to_svg(image, radius.value)
        svg_preview = mo.Html(svg_text)

    svg_preview
    return (svg_text,)


@app.cell
def _(svg_text, radius, mo):
    if svg_text is None:
        download_button = mo.md("Generate an SVG first.")
    else:
        download_button = mo.download(
            data=svg_text.encode("utf-8"),
            filename=f"output_radius_{radius.value}.svg",
            mimetype="image/svg+xml",
            label="Download SVG",
        )

    download_button
    return


if __name__ == "__main__":
    app.run()