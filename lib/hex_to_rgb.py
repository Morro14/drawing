def convert(hex: str):
    rgb = []
    for i in (0, 2, 4):
        rgb.append(int(hex[i:i + 2], base=16))
    return tuple(rgb)


def list(hex_list: list):

    rgb_list = []
    for i in range(len(hex_list)):
        rgb_list.append(convert(hex_list[i]))
    return rgb_list
