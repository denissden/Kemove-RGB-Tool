from CONSTANTS import *
from functions import *


class Layer:
    r, g, b = 255, 255, 255

    def __init__(self, index=0, color_mode=0, code_name=1337):
        self.color = rgb_to_hex((self.r, self.g, self.b))
        self.border = False
        self.color_mode = color_mode
        self.mode_name = COLOR_MODES[self.color_mode]
        self.speed1 = 1
        self.speed2 = 1
        self.key_selection = [False] * KEYS_AMOUNT
        self.codename = code_name
        self.adjustable = ADJUSTABLES[self.color_mode]

    def unpack(self, dictionary):
        self.color = dictionary["color"]
        self.r, self.g, self.b = hex_to_rgb(self.color)
        self.border = dictionary["border"]
        self.color_mode = dictionary["colorMode"]
        self.mode_name = dictionary["modeName"]
        self.speed1 = dictionary["speed"]
        self.speed2 = dictionary["speed2"]
        self.key_selection = dictionary["frame_selection_range"]
        self.codename = 1337
        self.adjustable = dictionary["adjustable"]

    def pack(self):
        dictionary = dict()
        dictionary["color"] = rgb_to_hex((self.r, self.g, self.b))
        dictionary["border"] = self.border
        dictionary["colorMode"] = self.color_mode
        dictionary["modeName"] = self.mode_name
        dictionary["speed"] = self.speed1
        dictionary["speed2"] = self.speed2
        dictionary["frame_selection_range"] = self.key_selection
        dictionary["codeName"] = self.codename
        dictionary["adjustable"] = self.adjustable
        return dictionary

    def __getitem__(self, key):
        return self.key_selection[key]

    def __setitem__(self, key, value):
        self.key_selection[key] = False if not value or value <= 0 else True

    def clear(self):
        self.key_selection = [False] * KEYS_AMOUNT

    def set_color(self, rgb):
        self.r, self.g, self.b = rgb
