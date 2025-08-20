#Code for the second video in the 3Blue1Brown series "Essence of Linear Algebra" in the LearningCV project
#This code is part of the LearningCV project, which aims to teach computer vision concepts using Python and NumPy.
# Code made by Chat GPT recreating code in my MatPlotBasics.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Initialize basis vectors
i = np.array([1, 0])  # Unit vector in the x-direction
j = np.array([0, 1])  # Unit vector in the y-direction

# --- Initial Plot Setup ---
fig, ax = plt.subplots(figsize=(6, 6))
plt.subplots_adjust(bottom=0.25)

# Initial quivers for i, j, and v
qi = ax.quiver(0, 0, i[0], i[1], angles='xy', scale_units='xy', scale=1, color='r', label='i')
qj = ax.quiver(0, 0, j[0], j[1], angles='xy', scale_units='xy', scale=1, color='b', label='j')
qv = ax.quiver(0, 0, 1, 1, angles='xy', scale_units='xy', scale=1, color='g', label='v = ai + bj')

# Set up plot limits, grid, labels
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.grid()
ax.axhline(0, color='black', linewidth=0.5, ls='--')
ax.axvline(0, color='black', linewidth=0.5, ls='--')
ax.set_title('Scaled Vectors and Resultant v')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.legend()

# --- Sliders ---
ax_slider_i = plt.axes([0.1, 0.05, 0.65, 0.03])
ax_slider_j = plt.axes([0.1, 0.01, 0.65, 0.03])

slider_i = Slider(ax_slider_i, 'Scale i', valmin=0, valmax=5, valinit=1)
slider_j = Slider(ax_slider_j, 'Scale j', valmin=0, valmax=5, valinit=1)

# --- Update Function ---
def update(val):
    scale_i = slider_i.val
    scale_j = slider_j.val

    # Update i and j
    qi.set_UVC(scale_i * i[0], scale_i * i[1])
    qj.set_UVC(scale_j * j[0], scale_j * j[1])

    # Update resultant v = ai + bj
    v = scale_i * i + scale_j * j
    qv.set_UVC(v[0], v[1])

    fig.canvas.draw_idle()

# Connect sliders
slider_i.on_changed(update)
slider_j.on_changed(update)

plt.show()
