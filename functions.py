def rgb_to_hex(rgb):
    s = '%02x%02x%02x' % rgb
    return s.upper()


def hex_to_rgb(value):
    value = value.lower()
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))