import matplotlib.pyplot as plt

# If some data point has multiple attributes, a stack plot is useful to show the individual variations

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

sleeping = [6, 6, 7, 8, 6, 9, 9]
studying = [3, 4, 4, 3, 4, 5, 6]
coding = [2, 3, 2, 3, 2, 5, 6]
others = [13, 11, 11, 10, 12, 5, 3]

plt.stackplot(days, studying, coding, others, sleeping, colors=['c', 'r', 'green', 'k'])

# we cannot add labels to the stack plot directly
# We do it using a fake plot to get the legend that tells the colors corresponding to the data

# linewidth measures the size of the line in the legend as well as the plot
plt.plot([], [], color='k', label='sleeping', linewidth=10)
plt.plot([], [], color='green', label='others', linewidth=10)
plt.plot([], [], color='r', label='coding', linewidth=10)
plt.plot([], [], color='c', label='studying', linewidth=10)


plt.xlabel('days')
plt.ylabel('time spent')
plt.title('Time spent during the week')
plt.legend()
plt.show()
