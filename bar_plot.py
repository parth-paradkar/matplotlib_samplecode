import matplotlib.pyplot as plt
x1 = [1, 3, 5, 7, 9]
y1 = [3, 5, 1, 2, 7]

x2 = [2, 4, 6, 8, 10]
y2 = [5, 6, 3, 4, 8]

plt.bar(x1, y1, label='Data1', color='red')
plt.bar(x2, y2, label='Data2', color='blue')
plt.legend()
plt.show()
