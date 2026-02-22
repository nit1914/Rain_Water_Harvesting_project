import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(6, 9.7, 'AquaEase: Inclusive Rainwater Harvesting System Prototype', ha='center',
        fontsize=14, weight='bold')

# Catchment Area (Roof)
roof = patches.Polygon([[3, 9], [6, 9.5], [9, 9], [6, 8.8]], closed=True, color='skyblue')
ax.add_patch(roof)
ax.text(6, 9.6, 'Catchment Area (Roof)', ha='center', fontsize=10)

# Gutter Pipe
ax.arrow(6, 8.8, 0, -1, head_width=0.2, head_length=0.2, fc='gray', ec='black')
ax.text(6.3, 8.3, 'Gutter Pipe', fontsize=9)

# First Flush Diverter
ffd = patches.Rectangle((5.5, 7.5), 1, 0.5, linewidth=1, edgecolor='black', facecolor='lightcoral')
ax.add_patch(ffd)
ax.text(6, 7.3, 'First Flush\nDiverter', ha='center', fontsize=9)

# Filtration Unit
filter_unit = patches.Rectangle((5, 6.2), 2, 1, linewidth=1, edgecolor='black', facecolor='lightgreen')
ax.add_patch(filter_unit)
ax.text(6, 6.6, 'Filtration Unit\n(Sand, Charcoal, Mesh)', ha='center', fontsize=9)

# Arrow from filtration to tank
ax.arrow(6, 6.2, 0, -1, head_width=0.2, head_length=0.2, fc='gray', ec='black')

# Storage Tank
tank = patches.Rectangle((4.5, 2.5), 3, 3, linewidth=1.5, edgecolor='black', facecolor='lightblue')
ax.add_patch(tank)
ax.text(6, 4.8, 'Storage Tank\n(100L, Insulated)', ha='center', fontsize=9)

# Water level indicators
ax.add_patch(patches.Circle((7.7, 4.5), 0.15, color='blue'))
ax.text(8.1, 4.5, 'Full Indicator', fontsize=8)
ax.add_patch(patches.Circle((7.7, 3.3), 0.15, color='red'))
ax.text(8.1, 3.3, 'Low Indicator', fontsize=8)

# Tap outlet
tap = patches.Rectangle((5.7, 2), 0.6, 0.3, linewidth=1, edgecolor='black', facecolor='orange')
ax.add_patch(tap)
ax.text(6, 1.7, 'Child-safe Low Tap\n(Easy Grip Handle)', ha='center', fontsize=9)

# Optional Solar Pump Panel
panel = patches.Rectangle((1, 7.5), 1.5, 1, linewidth=1, edgecolor='black', facecolor='gold')
ax.add_patch(panel)
ax.text(1.75, 7.3, 'Solar Panel\n(Optional)', ha='center', fontsize=8)

# Accessibility Labels
ax.text(9.5, 7.5, 'Accessibility Features:', fontsize=10, weight='bold')
ax.text(9.5, 7.1, '- Low-height tap for elderly/children', fontsize=9)
ax.text(9.5, 6.8, '- Color-coded level indicators', fontsize=9)
ax.text(9.5, 6.5, '- Easy-clean filter unit', fontsize=9)
ax.text(9.5, 6.2, '- Visual and video instructions (QR code)', fontsize=9)

plt.tight_layout()
plt.show()