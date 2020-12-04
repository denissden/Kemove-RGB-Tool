import json


class Map:
    def __init__(self, path, size):
        with open(path, "r") as f:
            self.map = json.load(f)
        self.sizex, self.sizey = size

    def __getitem__(self, key):
        x1, y1, x2, y2 = self.map[key]
        return x1 * self.sizex, y1 * self.sizey, x2 * self.sizex, y2 * self.sizey

    def __setitem__(self, key, value):
        self.map[key] = value

    def __len__(self):
        return len(self.map)