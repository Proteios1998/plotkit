import matplotlib.pyplot as plt

def show_palette(palette):
    fig, ax = plt.subplots(figsize=(len(palette), 1))
    for i, color in enumerate(palette):
        ax.add_patch(plt.Rectangle((i, 0), 1, 1, color=color))

    ax.set_xlim(0, len(palette))
    ax.set_ylim(0, 1)
    ax.axis("off")
    plt.show()
