from PIL import Image, ImageDraw, ImagePalette, ImageEnhance

from color_layer import Layer
from map import Map
from CONSTANTS import *
import colorsys


class KeyboardImage:
    contrast = 1

    def __init__(self, path):
        self.image = Image.open(path)
        self.image = self.image.convert("RGB")
        self.w, self.h = self.image.size
        self.map = Map(KEY_MAP, (self.w, self.h))

        self.colors = Image.new(mode="RGB", size=(len(self.map), 1))
        self.pairs = []
        self.keys = []
        self.reduced_map = []
        self.get_keys()
        self.colors = self.colors
        self.reduce_colors(self.colors)
        #self.get_out_map()

        self.enhancer = ImageEnhance.Contrast(self.colors)
        self.last_hue = 0

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
        self.get_out_map()
        ret = []
        for l in self.reduced_map:
            ret.append(l.pack())
        return ret

    def reduce_colors(self, colors):
        red = colors.convert('P', palette=Image.ADAPTIVE, colors=MAX_COLORS)
        red = red.convert("RGB")
        self.reduced_colors = red
        self.reduced_colors_original = red.copy()

    def set_contrast(self, number):
        if self.contrast != number:
            out = self.enhancer.enhance(number)
            self.reduce_colors(out)

    def set_hue(self, hue=0, sat=0, vib=0):
        d = (float(hue) - self.last_hue) / 360
        for i in range(self.reduced_colors.size[0]):
            c = self.reduced_colors_original.getpixel((i, 0))
            h, s, v = colorsys.rgb_to_hsv(*c)
            print(d, h)
            r, g, b = colorsys.hsv_to_rgb((d + h) % 1, s, v + vib)
            c = int(r), int(g), int(b)
            self.reduced_colors.putpixel((i, 0), c)
        print(self.reduced_colors.getpixel((i, 0)))


    def __getitem__(self, key):
        return self.reduced_colors.getpixel((key, 0))

    def __setitem__(self, key, value):
        self.reduced_colors.putpixel((key, 0), value)

    def __len__(self):
        return self.reduced_colors.size[0]



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
