# plotkit/plots.py
import numpy as np
import matplotlib.pyplot as plt
from .auto import apply_auto_theme
from scipy import stats

def manhattan_plot(
    chrom,
    pos,
    pval,
    ax=None,
    genomewide_line=5e-8,
    suggestive_line=1e-5,
    title="Manhattan Plot"
):
    """
    Generate a Manhattan plot.

    Parameters
    ----------
    chrom : array-like
        Chromosome numbers (1..22, X optional)
    pos : array-like
        Base-pair positions
    pval : array-like
        P-values
    """

    chrom = np.asarray(chrom)
    pos = np.asarray(pos)
    pval = np.asarray(pval)

    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 5))

    palette = apply_auto_theme("gwas")

    # Sort by chromosome and position
    order = np.lexsort((pos, chrom))
    chrom, pos, pval = chrom[order], pos[order], pval[order]

    # Compute cumulative positions
    unique_chroms = np.unique(chrom)
    offsets = {}
    current_offset = 0
    xticks = []
    xtick_labels = []

    x = np.zeros_like(pos, dtype=float)

    for i, c in enumerate(unique_chroms):
        mask = chrom == c
        positions = pos[mask]

        offsets[c] = current_offset
        x[mask] = positions + current_offset

        center = positions.mean() + current_offset
        xticks.append(center)
        xtick_labels.append(str(c))

        current_offset += positions.max()

    # Plot
    for i, c in enumerate(unique_chroms):
        mask = chrom == c
        color = palette[i % len(palette)]
        ax.scatter(
            x[mask],
            -np.log10(pval[mask]),
            s=6,
            color=color,
            rasterized=True
        )

    # Significance lines
    if genomewide_line:
        ax.axhline(-np.log10(genomewide_line), linestyle="--")
    if suggestive_line:
        ax.axhline(-np.log10(suggestive_line), linestyle=":")

    ax.set_xticks(xticks)
    ax.set_xticklabels(xtick_labels)
    ax.set_xlabel("Chromosome")
    ax.set_ylabel("-log10(p)")
    ax.set_title(title)

    return ax


def qq_plot(pval, ax=None, title="QQ Plot", show_lambda=True):
    """
    Generate a QQ plot for GWAS p-values.
    """

    pval = np.asarray(pval)
    pval = pval[~np.isnan(pval)]
    pval = np.sort(pval)

    n = len(pval)

    if ax is None:
        fig, ax = plt.subplots(figsize=(5, 5))

    # Expected
    expected = -np.log10(np.linspace(1/(n+1), 1, n))
    observed = -np.log10(pval)

    ax.scatter(expected, observed, s=8)

    # Diagonal
    max_val = max(expected.max(), observed.max())
    ax.plot([0, max_val], [0, max_val], linestyle="--")

    # Lambda GC
    if show_lambda:
        chisq = stats.chi2.isf(pval, 1)
        lambda_gc = np.median(chisq) / stats.chi2.ppf(0.5, 1)
        ax.text(0.1, max_val * 0.9, f"$\\lambda$ = {lambda_gc:.3f}")

    ax.set_xlabel("Expected -log10(p)")
    ax.set_ylabel("Observed -log10(p)")
    ax.set_title(title)

    return ax
