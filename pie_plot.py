import matplotlib.pyplot as plt

time_spent = [8, 3, 6, 7]
activities = ['Sleeping ', 'Studying', 'Coding', 'Chill']

# round() is an float method that rounds to the required number of places
percentages = [round((float(element) * 100 / 24), 2) for element in time_spent]
act_final = [activities[i] + ' ' + str(percentages[i]) + '%' for i in range(len(time_spent))]

# startangle specifies the starting angle of the pie chart(0 by default)
# shadow adds shadow to the plot(duh)
# explode removes a slice of the graph. Extent for individual elements can be varied

plt.pie(time_spent, labels=act_final, colors=['k', 'c', 'r', 'g'], startangle=30, shadow=True, explode=[0, 0, 0.2, 0])
plt.title('Time spent on sunday')
plt.show()
