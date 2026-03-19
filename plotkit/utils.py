import json

def save_palette(palette, name, path="palettes.json"):
    try:
        with open(path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    data[name] = palette

    with open(path, "w") as f:
        json.dump(data, f, indent=4)


def load_palette(name, path="palettes.json"):
    with open(path, "r") as f:
        data = json.load(f)
    return data.get(name)
