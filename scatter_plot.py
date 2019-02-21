import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [2, 3, 8, 4, 6, 7, 4, 1, 9]

# s stores the size of the dots on the graph
# marker stores the symbol that appears on the graph
# marker codes available online
plt.scatter(x, y, label='data', color='k', marker='*', s=100)
plt.legend()
plt.show()
