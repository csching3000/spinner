import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Checks if user input is a digit
def getNumber():
    while True:
        number = input("Enter # of sections: ")
        if number.isdigit():
            return int(number)
        else:
            print("Invalid Input. Please enter a #")

# Getting the size and label of each slice of the wheel/pie chart
def getLabelsAndSliceSizes(n):
    s = []
    l = []
    for i in range(n):
        s.append(int(100 / n))
        l.append(input("Enter a label for the slice " + str(i + 1) + ": "))
    return s, l

# requesting user input and getting # of slices for wheel/pie chart
slices = getNumber()
sizes, labels = getLabelsAndSliceSizes(slices)

# Create a figure and axes
fig, ax = plt.subplots()

# Function to update the pie chart for each frame
def update(frame):
    ax.clear()
    ax.pie(sizes, labels=labels, startangle=frame)
    ax.set_title('Spinning Pie Chart')

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 10), interval=10)

# Save the animation (optional)
# ani.save('spinning_pie_chart.gif', writer='pillow')

# Show the animation
plt.show()

