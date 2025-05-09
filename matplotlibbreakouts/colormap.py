import matplotlib.pyplot as plt
import numpy as np

cleaned_data = {
'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
'temperature': [32.5, 31.8, 33.4, 89.6, 31.2], # All in °F
'humidity': [65, 70, 68, 67, 66], # All as percentages
'precipitation': [0.0, 5.1, 12.7, 0.0, 2.5] # All in mm
}


plt.style.use('_mpl-gallery')


# Generate 2D temperature data (e.g., a temperature map)
xgrid, ygrid = np.meshgrid(np.linspace(-5, 5, 100), np.linspace(-5, 5, 100))
distance = np.sqrt(xgrid**2 + ygrid**2)
temperature = np.sin(distance) * 20 + 15  # Temperature between -5°C and 35°C

# Create a figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Plot with 'coolwarm' colormap (good for temperature)
im1 = ax1.imshow(temperature, cmap='coolwarm', origin='lower', 
                extent=[-5, 5, -5, 5], vmin=0, vmax=30)
ax1.set_title('Temperature Map (coolwarm)')
ax1.set_xlabel('X-coordinate')
ax1.set_ylabel('Y-coordinate')
fig.colorbar(im1, ax=ax1, label='Temperature (°C)')

# Plot with 'viridis' colormap (good for general data)
im2 = ax2.imshow(temperature, cmap='viridis', origin='lower', 
                extent=[-5, 5, -5, 5], vmin=0, vmax=30)
ax2.set_title('Temperature Map (viridis)')
ax2.set_xlabel('X-coordinate')
ax2.set_ylabel('Y-coordinate')
fig.colorbar(im2, ax=ax2, label='Temperature (°C)')

plt.tight_layout()

# plt.savefig('colorMap.png', dpi=300, bbox_inches='tight')
# plt.close()

print("Plot saved as 'colorMap.png'")

plt.show()