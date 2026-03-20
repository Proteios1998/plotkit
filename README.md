# PlotKit

**PlotKit** is a lightweight Python toolkit for **publication-quality plotting**, including automatic theme selection, color palettes, font control, and built-in support for multi-panel figures and genomic plots (Manhattan & QQ plots).  

It is designed for **scientific workflows** such as GWAS, LD heatmaps, and general data visualization, making your figures consistent, reproducible, and visually appealing.

---

## Features

- 🎨 **Automatic theme selection** based on plot type (`scatter`, `line`, `bar`, `heatmap`, `gwas`, `manhattan`, `qq`, etc.)
- 🌈 **Curated color palettes** (grgstyle, customized pink/purple/blue/orange, Tableau, Colorblind-safe, Diverging, Sequential)
- 🔤 **Font control** (Nimbus Sans / fallback fonts) with automatic PDF-friendly embedding
- 🧩 **Multi-panel figure support** with panel labels (A, B, C…)
- 🧬 **Built-in Manhattan and QQ plots** for genomic analyses
- 📐 **Automatic font scaling** based on figure size and plot density
- 🖼 **Publication-ready defaults** (tight layouts, consistent typography, vector export)

---

## Installation

```bash
pip install plotkit
```
Or install locally:
```bash
git clone <repo-url>
cd plotkit
pip install -e .
```

## Quick Start
### Check the color palettes
```
from plotkit.palettes import PALETTES
from plotkit.preview import palette_showcase_figure

palette = PALETTES["grgstyle"]
palette_showcase_figure(palette)
```
