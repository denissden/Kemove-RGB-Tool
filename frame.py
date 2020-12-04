from CONSTANTS import *


class Frame:
    def __init__(self, index=0):
        self.name = f"frame{index}"
        self.frame_time = 0.1
        self.key_selection = [False] * KEYS_AMOUNT

    def unpack(self, dictionary):
        self.name = dictionary["name"]
        self.frame_time = dictionary["frame_time"] / 10
        self.key_selection = dictionary["frame_selection_range"]

    def pack(self):
        dictionary = dict()
        dictionary["name"] = self.name
        dictionary["frame_time"] = int(self.frame_time * 10)
        dictionary["frame_selection_range"] = self.key_selection
        return dictionary

    def __getitem__(self, key):
        return self.key_selection[key]

    def __setitem__(self, key, value):
        self.key_selection[key] = False if not value or value <= 0 else True

    def clear(self):
        self.key_selection = [False] * KEYS_AMOUNT

