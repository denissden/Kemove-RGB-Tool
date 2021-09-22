import json
from frame import Frame
from kemove_project_presets import *
from random import randint


def export_advanced(file, image):
    filename = file.split("/")[-1]
    file += ".Advanced"

    preset = parse_preset(ADVANCED, filename)

    frames = []
    f = Frame()
    f.key_selection = [True] * KEYS_AMOUNT
    frames.append(f.pack())

    preset["pagedata"]["matrix_frames"] = frames

    colors = image.pack()
    preset["pagedata"]["matrix_ColorMode"] = colors
    with open(file, "w+") as f:
        json.dump(preset, f)


def parse_preset(preset, filename):
    for key, value in preset.items():
        if type(value) == str:
            value.replace("%filename%", filename)
            value.replace("%random%", randint(1000000, 10000000))
            preset[key] = value
    return preset
