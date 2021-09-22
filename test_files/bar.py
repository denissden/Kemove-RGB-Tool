from keyboard_image import KeyboardImage
from PIL import Image, ImageDraw, ImagePalette


image = KeyboardImage("../monitor2.png").colors

image = Image.open("../color.png")
out = image.convert('P', palette=Image.ADAPTIVE, colors=12)
out = out.convert("RGB")
l = out.getcolors()
print(l)
out.show()



i = KeyboardImage("../monitor2.png")

i.draw_map()
print(i.reduced_map)
