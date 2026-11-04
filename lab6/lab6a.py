import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10,100)
y = 2*x + (np.sin(x))**2 + 3
plt.plot(x, y)
plt.title('helo,po!')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

plt.savefig('po.pdf')
print("The plot has been saved as 'po.pdf'.")
plt.show()