months = ['Jan', 'Feb', 'Mar']
sales = [100, 150, 130]

import matplotlib.pyplot as plt

plt.plot(months, sales)
plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Sales Data')
plt.show()