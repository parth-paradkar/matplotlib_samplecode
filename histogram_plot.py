import matplotlib.pyplot as plt

ages = [1, 23, 4, 4, 111, 23, 45, 67, 76, 51, 89, 34, 11, 1, 90, 44, 35, 37, 87, 67, 65, 43, 23, 32, 24, 25]
y = [str(element) + '01232' for element in ages]
# bins contains the intervals in which the data is placed
bins = [0, 10, 20, 30, 40, 50, 50, 60, 70, 80, 90, 100, 110]

# rwidth stores the width of the bars
plt.hist(ages, bins, histtype='bar', rwidth=0.8, color='c')
plt.xlabel('Ages')
plt.ylabel('No. of People')
plt.show()
