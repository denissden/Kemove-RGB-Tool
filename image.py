from PIL import Image, ImageDraw, ImagePalette
from color_layer import Layer
from map import Map
from CONSTANTS import *


class KeyboardImage:
    def __init__(self, path):
        self.image = Image.open(path)
        self.image = self.image.convert("RGB")
        self.w, self.h = self.image.size
        self.map = Map("map61key.json", (self.w, self.h))

        self.colors = Image.new(mode="RGB", size=(len(self.map), 1))
        self.pairs = []
        self.keys = []
        self.reduced_map = []
        self.get_keys()
        self.colors = self.colors
        red = self.colors.convert('P', palette=Image.ADAPTIVE, colors=MAX_COLORS)
        red = red.convert("RGB")
        self.reduced_colors = red
        self.get_out_map()

    def get_from_map(self, index):
        new_im = self.image.crop(self.map[index])
        return new_im

    def draw_map(self):
        image = ImageDraw.Draw(self.image)
        for i in range(len(self.map)):
            key = self.map[i]
            color = self.reduced_colors.getpixel((i, 0))
            image.rectangle(key, fill=color, outline="red")
        self.image.show()

    def get_keys(self):
        for i in range(len(self.map)):
            key = self.get_from_map(i)
            key = KeyImage(key)
            self.keys.append(key)
            self.colors.putpixel((i, 0), key.average_color)

    def get_out_map(self):
        all_colors = set()
        for i in range(self.reduced_colors.size[0]):
            c = self.reduced_colors.getpixel((i, 0))
            all_colors.add(c)

        layers = []
        for color in all_colors:
            l = Layer()
            l.r, l.g, l.b = color
            for i in range(self.reduced_colors.size[0]):
                c = self.reduced_colors.getpixel((i, 0))
                if color == c:
                    l[i] = True
            layers.append(l)

        self.reduced_map = layers

    def pack(self):
        ret = []
        for l in self.reduced_map:
            ret.append(l.pack())
        return ret




class KeyImage:
    def __init__(self, image):
        self.image = image
        self.w, self.h = self.image.size
        self.average_color = self.get_average()

    def get_average(self, img=-1):
        if img != -1:
            w, h = img.size
            loaded = img.load()
        else:
            w, h = self.w, self.h
            loaded = self.image.load()
        r, g, b = 0, 0, 0
        for y in range(h):
            for x in range(w):
                pixr, pixg, pixb = loaded[x, y][:3]
                r += pixr
                g += pixg
                b += pixb
        count = w * h
        return int(r / count), int(g / count), int(b / count)
