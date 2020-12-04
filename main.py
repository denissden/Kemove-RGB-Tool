import json
from frame import Frame
from image import KeyboardImage
from color_layer import Layer
from functions import *



FRAME_INDEX = "frame_selection_range"
KEYS_AMOUNT = 61


with open("test_color.Advanced", "r") as f:
    ALL_JSON = json.load(f)

print(ALL_JSON["pagedata"]["matrix_ColorMode"][0])

colors = KeyboardImage("gradient.jpg").pack()

ALL_JSON["pagedata"]["matrix_ColorMode"] = colors

frames = []

f = Frame()
f.key_selection = [True] * KEYS_AMOUNT
frames.append(f.pack())

ALL_JSON["pagedata"]["matrix_frames"] = frames
ALL_JSON["pagedata"]["currentFramesIndex"] = 60
ALL_JSON["pagedata"]["projectCode"] = ""


print(ALL_JSON)
input()
with open("test_result.Advanced", "w+") as f:
    json.dump(ALL_JSON, f)
