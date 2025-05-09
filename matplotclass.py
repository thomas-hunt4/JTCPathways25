import matplotlib.pyplot as plt
import numpy as np


cleaned_data = {
'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
'temperature': [32.5, 31.8, 33.4, 89.6, 31.2], # All in °F (converted 32°C to 89.6°F)
'humidity': [65, 70, 68, 67, 66], # All as percentages
'precipitation': [0.0, 5.1, 12.7, 0.0, 2.5] # All in mm (converted inches to mm)
}

# taco_data = {
#     'day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# }

#creat a bar chart
# fig, ax = plt.subplots(figsize=(12, 6))

# ax.set_title()
# ax.set_xlabel()
# ax.set_ylabel
# ax.set_ylim()



# plt.savefig('check_out_my_graph.png')
# plt.close()

# months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# rainfall = [30,25, 50,40,60,70,90,85,70,60,50, 35]
fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(cleaned_data['date'],cleaned_data['temperature'], color='skyblue', edgecolor='navy')
# print(ax.__dict__ )
# print(dir(ax)) #shows methods and attributes of the ax object
# print(fig.__dict__)
# print(dir(fig))
ax.set_title('Monthly Rainfall', fontsize=14, fontweight='bold')
ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Temperature (C)')
ax.set_ylim(0, 100)
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height +1, f'{height} mm', ha='center', va='bottom')
plt.savefig('rainfall_bar_chart.png')
plt.close()
print("Plot saved as 'rainfall_bar_chart.png'")


# plt.style.use('_mpl-gallery')

# # Make data
# x = cleaned_data['temperature']
# y = cleaned_data['humidity']
# z = cleaned_data['precipitation']
# dx = np.ones_like(x)*0.5
# dy = np.ones_like(x)*0.5
# dz = cleaned_data['date']

# # Plot
# fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
# ax.bar3d(x, y, z, dx, dy, dz)

# ax.set(xticklabels=[],
#        yticklabels=[],
#        zticklabels=[])

# # plt.show()
plt.style.use('_mpl-gallery')

# make the data
# np.random.seed(3)
x = cleaned_data['temperature']
y = cleaned_data['humidity']
# size and color:
sizes = np.random.uniform(15, 80, len(x))
colors = np.random.uniform(15, 80, len(x))

# plot
fig, ax = plt.subplots(figsize=(10,6))

scatter = ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)

ax.set_title('Temperature v Humidity', fontsize=14)
ax.set_xlabel('Temperature (C)', fontsize=12)
ax.set_ylabel('Humidity (%)', fontsize=12)

cbar = fig.colorbar(scatter, ax=ax)
cbar.set_label('Temperature (C)', fontsize=12)

plt.show()
ax.grid(True, linestyle='--', alpha=0.7)

# plt.savefig('new_chart.png')
# plt.close()






'''
##stack plot set up<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
plt.style.use('_mpl-gallery')

# make data
x = np.arange(0, 10, 2)
ay = [1, 1.25, 2, 2.75, 3]
by = [1, 1, 1, 1, 1]
cy = [2, 1, 2, 1, 2]
y = np.vstack([ay, by, cy])

# plot
fig, ax = plt.subplots()

ax.stackplot(x, y)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()
'''
