import seaborn as sns
import matplotlib.pyplot as plt

x_axis = [1, 2, 3, 4, 5, 6]
y_axis = [10, 5, 15, 7, 25, 12]

# Set the visual style (aesthetically pleasing default)
sns.set_theme(style="whitegrid")

# Create the plot
# Seaborn's lineplot function automatically makes it look polished
plt.figure(figsize=(8, 5))
sns.lineplot(x=x_axis, y=y_axis, marker='o', color='green', linestyle='--')

# Add titles and labels
plt.title("Seaborn Version of the Plot")
plt.xlabel("Time Step")
plt.ylabel("Measured Value")

plt.show()