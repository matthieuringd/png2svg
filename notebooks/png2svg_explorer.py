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
    import marimo as mo
    import io
    from PIL import Image
    from png2svg.converter import image_to_svg


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    # PNG2SVG Explorer

    Select an input image and choose the hexagon radius used for the
    conversion.
    """)
    return


@app.cell
def _():
    # File selector for the input image.
    image_file = mo.ui.file(
        filetypes=[".png", ".jpg", ".jpeg"],
        multiple=False,
        label="Choose an image",
    )

    # Radius controls the size of the generated hexagons.
    radius = mo.ui.slider(
        start=2,
        stop=30,
        value=10,
        step=1,
        label="Hexagon radius",
    )

    mo.vstack(
        [
            image_file,
            radius,
        ]
    )


    return image_file, radius


@app.cell(hide_code=True)
def _(image_file, radius):
    mo.md(f"""
    ### Current settings

    **Radius:** `{radius.value}`

    **Image selected:** `{"Yes" if image_file.value else "No"}`
    """)
    return

@app.cell
def _(image_file):
    image = None

    if not image_file.value:
        preview = mo.md("No image selected yet.")
    else:
        # Get the uploaded file from Marimo.
        uploaded_file = image_file.value[0]

        # Create the Pillow image that will later be used for conversion.
        image = Image.open(
            io.BytesIO(uploaded_file.contents)
        ).convert("RGB")

        # Explicitly create a visual preview in the notebook.
        preview = mo.image(uploaded_file.contents)

    preview


@app.cell
def _(image, radius):
    if image is None:
        result = mo.md("No SVG generated yet.")
        svg_content = None
    else:
        svg_content = image_to_svg(image, radius.value)
        result = mo.Html(svg_content)

    result
    return svg_content

# We make sure our conversion cell returns the SVG text
@app.cell
def _(image, radius):
    if image is None:
        svg_text = None
    else:
        svg_text = image_to_svg(image, radius.value)

    svg_text

# We display the SVG in another cell
@app.cell
def _(mo, svg_text):
    if svg_text is None:
        svg_preview = mo.md("No SVG generated yet.")
    else:
        svg_preview = mo.Html(svg_text)

    svg_preview

# Cell to add the download button
@app.cell
def _(mo, svg_text, radius):
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

if __name__ == "__main__":
    app.run()
