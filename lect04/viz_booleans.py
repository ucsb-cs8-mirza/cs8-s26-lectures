"""
Lecture 4 — Boolean Visualizations
Run this file to generate two projector-ready figures:
  1. Truth table grid (and / or / not)
  2. if-elif-else flowchart
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np

TRUE_COLOR  = "#2f9e44"   # green
FALSE_COLOR = "#e03131"   # red
COND_COLOR  = "#f08c00"   # amber  (diamond / condition nodes)
CODE_COLOR  = "#1971c2"   # blue   (code-body nodes)
TERM_COLOR  = "#5f3dc4"   # purple (start / end nodes)
TEXT_COLOR  = "white"


# ── 1. Truth Table Grid ────────────────────────────────────────────────────────

def _cell(ax, x, y, w, h, facecolor, text, fontsize=13):
    rect = FancyBboxPatch((x, y), w, h,
                          boxstyle="round,pad=0.05",
                          facecolor=facecolor,
                          edgecolor="white", linewidth=2)
    ax.add_patch(rect)
    ax.text(x + w / 2, y + h / 2, text,
            ha="center", va="center",
            fontsize=fontsize, fontweight="bold", color=TEXT_COLOR)


def _table(ax, headers, rows, col_w, row_h):
    """Draw a truth table. Headers sit directly on top of data rows."""
    n_rows = len(rows)
    n_cols = len(headers)

    # ylim: data rows span 0 → n_rows*row_h, header sits on top → +row_h
    ax.set_xlim(-0.05, n_cols * col_w + 0.05)
    ax.set_ylim(-0.1, (n_rows + 1) * row_h + 0.1)
    ax.axis("off")

    # Header row — directly above the data
    header_y = n_rows * row_h
    header_colors = ["#343a40"] * n_cols
    for i, (label, hc) in enumerate(zip(headers, header_colors)):
        _cell(ax, i * col_w, header_y, col_w, row_h, hc, label, fontsize=14)

    # Data rows — row 0 at top, last row at bottom
    for r, row in enumerate(rows):
        y = (n_rows - 1 - r) * row_h
        for c, val in enumerate(row):
            color = TRUE_COLOR if val else FALSE_COLOR
            _cell(ax, c * col_w, y, col_w, row_h, color, str(val), fontsize=13)


def plot_truth_tables():
    fig, axes = plt.subplots(1, 3, figsize=(16, 6))
    fig.patch.set_facecolor("#f8f9fa")

    col_w, row_h = 1.7, 1.0

    # ── AND ──
    axes[0].set_facecolor("#f8f9fa")
    axes[0].set_title("A  and  B", fontsize=17, fontweight="bold", pad=14)
    _table(axes[0],
           headers=["A", "B", "A and B"],
           rows=[
               (False, False, False),
               (False, True,  False),
               (True,  False, False),
               (True,  True,  True),
           ],
           col_w=col_w, row_h=row_h)

    # ── OR ──
    axes[1].set_facecolor("#f8f9fa")
    axes[1].set_title("A  or  B", fontsize=17, fontweight="bold", pad=14)
    _table(axes[1],
           headers=["A", "B", "A or B"],
           rows=[
               (False, False, False),
               (False, True,  True),
               (True,  False, True),
               (True,  True,  True),
           ],
           col_w=col_w, row_h=row_h)

    # ── NOT ──
    axes[2].set_facecolor("#f8f9fa")
    axes[2].set_title("not  A", fontsize=17, fontweight="bold", pad=14)
    _table(axes[2],
           headers=["A", "not A"],
           rows=[
               (False, True),
               (True,  False),
           ],
           col_w=col_w, row_h=row_h)

    # Shared legend
    t_patch = mpatches.Patch(color=TRUE_COLOR,  label="True")
    f_patch = mpatches.Patch(color=FALSE_COLOR, label="False")
    fig.legend(handles=[t_patch, f_patch], loc="lower center",
               ncol=2, fontsize=13, framealpha=0.9)

    fig.suptitle("Boolean Operators — Truth Tables",
                 fontsize=20, fontweight="bold", y=1.02)
    plt.tight_layout(rect=[0, 0.06, 1, 1])
    out = "truth_tables.png"
    plt.savefig(out, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
    print(f"Saved {out}")
    plt.show()


# ── 2. if / elif / else Flowchart ─────────────────────────────────────────────

def _box(ax, cx, cy, w, h, color, text, fontsize=14):
    box = FancyBboxPatch((cx - w / 2, cy - h / 2), w, h,
                         boxstyle="round,pad=0.12",
                         facecolor=color, edgecolor="#333", linewidth=2,
                         zorder=3)
    ax.add_patch(box)
    ax.text(cx, cy, text, ha="center", va="center",
            fontsize=fontsize, fontweight="bold", color=TEXT_COLOR, zorder=4)


def _diamond(ax, cx, cy, w, h, color, text, fontsize=13):
    pts = [[cx, cy + h/2], [cx + w/2, cy], [cx, cy - h/2], [cx - w/2, cy]]
    diamond = plt.Polygon(pts, facecolor=color, edgecolor="#333", linewidth=2, zorder=3)
    ax.add_patch(diamond)
    ax.text(cx, cy, text, ha="center", va="center",
            fontsize=fontsize, fontweight="bold", color=TEXT_COLOR, zorder=4)


def _arrow(ax, x1, y1, x2, y2, label="", label_dx=0.0, label_dy=0.0, color="#333"):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="->", color=color, lw=2.5), zorder=2)
    if label:
        mx = (x1 + x2) / 2 + label_dx
        my = (y1 + y2) / 2 + label_dy
        ax.text(mx, my, label, ha="center", va="center",
                fontsize=15, color="#c92a2a", fontweight="bold", zorder=6,
                bbox=dict(facecolor="white", edgecolor="none", pad=3))


def plot_flowchart():
    fig, ax = plt.subplots(figsize=(11, 14))
    fig.patch.set_facecolor("#f8f9fa")
    ax.set_facecolor("#f8f9fa")
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 15)
    ax.axis("off")
    ax.set_title("if / elif / else — Control Flow",
                 fontsize=17, fontweight="bold", pad=14)

    # ── nodes ──
    # Start
    _box(ax, 5, 14, 3, 0.8, TERM_COLOR, "START", fontsize=15)
    _arrow(ax, 5, 13.6, 5, 13.0)

    # if condition
    _diamond(ax, 5, 12.1, 4.6, 1.6, COND_COLOR, "if  condition 1?", fontsize=13)

    # True → if body  (horizontal arrow: lift label above the line)
    _arrow(ax, 7.3, 12.1, 9.5, 12.1, "True", label_dy=0.3)
    _box(ax, 9.5, 11.0, 2.2, 0.9, CODE_COLOR, "if-body\n(runs)", fontsize=13)
    _arrow(ax, 9.5, 10.55, 9.5, 9.0)

    # False → elif condition  (vertical arrow: push label to the right)
    _arrow(ax, 5, 11.3, 5, 10.3, "False", label_dx=0.75)
    _diamond(ax, 5, 9.4, 4.6, 1.6, COND_COLOR, "elif  condition 2?", fontsize=13)

    # elif True → elif body  (horizontal arrow: lift label above the line)
    _arrow(ax, 7.3, 9.4, 9.5, 9.4, "True", label_dy=0.3)
    _box(ax, 9.5, 8.3, 2.2, 0.9, CODE_COLOR, "elif-body\n(runs)", fontsize=13)
    _arrow(ax, 9.5, 7.85, 9.5, 6.8)

    # elif False → else body  (vertical arrow: push label to the right)
    _arrow(ax, 5, 8.6, 5, 7.5, "False", label_dx=0.75)
    _box(ax, 5, 7.0, 2.2, 0.9, "#c92a2a", "else-body\n(runs)", fontsize=13)
    _arrow(ax, 5, 6.55, 5, 5.8)

    # ── merge lines to END ──
    merge_y = 5.5
    # from if-body
    ax.plot([9.5, 9.5, 5], [9.0, merge_y, merge_y],
            color="#333", lw=2, zorder=2)
    # from elif-body (already continues down to merge_y via arrow to 6.8)
    ax.plot([9.5, 9.5], [6.8, merge_y], color="#333", lw=2, zorder=2)
    # from else-body (arrow already ends at 5.8, draw down)
    ax.plot([5, 5], [5.8, merge_y], color="#333", lw=2, zorder=2)
    ax.annotate("", xy=(5, 5.0), xytext=(5, merge_y),
                arrowprops=dict(arrowstyle="->", color="#333", lw=2), zorder=2)

    # End
    _box(ax, 5, 4.5, 3, 0.8, TERM_COLOR, "END\n(rest of program)", fontsize=14)

    # ── annotation: only ONE branch runs ──
    ax.text(0.2, 9.4,
            "Exactly ONE\nbranch runs",
            ha="center", va="center", fontsize=12,
            color="#2f9e44", fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#d3f9d8",
                      edgecolor="#2f9e44", linewidth=2))
    ax.annotate("", xy=(2.7, 9.4), xytext=(1.4, 9.4),
                arrowprops=dict(arrowstyle="->", color="#2f9e44", lw=1.5))

    plt.tight_layout()
    out = "ifelse_flowchart.png"
    plt.savefig(out, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
    print(f"Saved {out}")
    plt.show()


if __name__ == "__main__":
    plot_truth_tables()
    plot_flowchart()
