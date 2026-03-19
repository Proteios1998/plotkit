import numpy as np
import matplotlib.colors as mcolors

def generate_palette(n=5, hue_range=(0, 1), saturation=0.65, lightness=0.55):
    """
    Generate evenly spaced colors in HSL space.
    """
    hues = np.linspace(hue_range[0], hue_range[1], n, endpoint=False)
    colors = [mcolors.hsv_to_rgb((h, saturation, lightness)) for h in hues]
    return [mcolors.to_hex(c) for c in colors]


def qualitative_palette(n=8):
    return generate_palette(n, saturation=0.7, lightness=0.6)


def sequential_palette(n=6, base_color="#1f77b4"):
    base = np.array(mcolors.to_rgb(base_color))
    colors = [base * (0.3 + 0.7 * i / (n - 1)) for i in range(n)]
    return [mcolors.to_hex(c) for c in colors]


def diverging_palette(n=7, low="#d73027", high="#4575b4"):
    low_rgb = np.array(mcolors.to_rgb(low))
    high_rgb = np.array(mcolors.to_rgb(high))

    mid = np.array([1, 1, 1])
    half = n // 2

    colors = []
    for i in range(half):
        t = i / (half - 1)
        colors.append(mcolors.to_hex(low_rgb * (1 - t) + mid * t))

    if n % 2 == 1:
        colors.append("#ffffff")

    for i in range(half):
        t = i / (half - 1)
        colors.append(mcolors.to_hex(mid * (1 - t) + high_rgb * t))

    return colors
