import matplotlib.pyplot as plt

# plotting the line y = mx + c
m1 = 3
m2 = -1 / m1
c = 0
x = [0, 1, 2, 3]
y1 = []

for element in x:
    res = element * m1 + c
    y1.append(res)

y2 = []
for element in x:
    res1 = element * m2 + c
    y2.append(res1)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Perpendicular Lines')
plt.plot(x, y1, label='Line A', color='green')
plt.plot(x, y2, label='Line B', color='red')
plt.legend()
# print(y)
print(y1)
print(y2)
plt.show()
