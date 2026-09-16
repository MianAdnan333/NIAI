import matplotlib.pyplot as plt

x_axis = [1, 2, 3, 4, 5]
y_axis = [10, 20, 15, 30, 25]

plt.plot(x_axis, y_axis, marker='o', color='green', linestyle='--')

plt.title("Updated Data Visualization")
plt.xlabel("Time Step")
plt.ylabel("Measured Value")
plt.grid(True)

plt.show()