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

# Creating the labels for the sections in the wheel
def getLabels(n):
    l = []
    for i in range(sections):
        l.append(input("Enter a label for section " + str(i + 1) + ": "))
    return l

# Creating the sections in the wheel
def createSections(n):
    s = []
    for i in range(n):
        s.append(int(100 / n))
    return s

# requesting user input and constructing the wheel
sections = getNumber()
labels = getLabels(sections)
sizes = createSections(sections)

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

