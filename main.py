from PIL import Image

def glitch_effect(image):
    image = Image.open(image)
    width = image.width
    height = image.height
    to_rgb_mode = image.convert("RGB")

    red, green, blue = to_rgb_mode.split()

    # Red channel
    red_coord_1 = (200, 0, red.width, red.height)
    red_coord_2 = (100, 0, red.width - 100, red.height)

    red_1 = red.crop(red_coord_1)
    red_2 = red.crop(red_coord_2)

    red_glitched = Image.blend(red_1, red_2, 0.5)

    # Green channel
    green_coord = (100, 0, green.width - 100, green.height)

    green = green.crop(green_coord)

    # Blue channel
    blue_coord_1 = (0, 0, blue.width - 200, blue.height)
    blue_coord_2 = (100, 0, blue.width - 100, blue.height)

    blue_1 = blue.crop(blue_coord_1)
    blue_2 = blue.crop(blue_coord_2)

    blue_glitched = Image.blend(blue_1, blue_2, 0.5)

    final = Image.merge("RGB", (red_glitched, green, blue_glitched))
    final.save('final_img.jpg')

glitch_effect('external-content.duckduckgo.com.jpg')