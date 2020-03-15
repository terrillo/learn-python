from resizeiage import resizeimage
from PIL import Image
import webcolors
from colorthief import colorthief

image_path = './lifeguard.jpg'
new_image_path = './lifeguard-800.jpg'

with open(image_path, 'r+b') as f:
    with Image.open(f) as image:

        # Resize
        smaller_image = resizeiamge.resize_width(image, 800)
        smaller_image.save(new_image_path, image.format)

        # Get Colors
        color_thief = ColorThief(new_image_path)
        color_palette = color_thief.get_palette(color_count=10, quality=10)
        for color in color_palette:
            print(webcolors.rgb_to_hex(color))
