import pandas as pd
import matplotlib.pyplot as plt


oly_data =  pd.read_csv("olympics.csv")
print(oly_data)

plt.style.use('_mpl-gallery')

age = oly_data['Age']
height =oly_data['Height']
# Create a scatter plot
fig, ax = plt.subplots(figsize=(10, 6))
scatter = ax.scatter(age, height, 
                     cmap='coolwarm', alpha=0.7, s=50)

# Add labels and title
ax.set_title('Age and Height of Athletes', fontsize=14)
ax.set_xlabel('Age', fontsize=12)
ax.set_ylabel('Height (cm)', fontsize=12)

# Add a color bar
# cbar = fig.colorbar(scatter, ax=ax)
# cbar.set_label('Temperature (°C)', fontsize=12)

# Add a grid
ax.grid(True, linestyle='--', alpha=0.7)


plt.show()