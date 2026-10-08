"""Generates a faint house outline to trace — the 'same house' benchmark."""
from PIL import Image, ImageDraw


def house_template(width: int = 700, height: int = 400) -> Image.Image:
    img = Image.new("RGB", (width, height), "#fafafa")
    d = ImageDraw.Draw(img)
    ink = "#d0d0d0"
    # body
    d.rectangle([220, 200, 480, 340], outline=ink, width=3)
    # roof
    d.polygon([(200, 200), (350, 110), (500, 200)], outline=ink, width=3)
    # door + window
    d.rectangle([320, 270, 380, 340], outline=ink, width=3)
    d.rectangle([240, 230, 290, 270], outline=ink, width=3)
    # sun
    d.ellipse([520, 40, 580, 100], outline=ink, width=3)
    return img
