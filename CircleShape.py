import matplotlib.pyplot as plt
import Utils
import SOM
import numpy as np

radius = 2
centerX = 0
centerY = 0
neurons_size = 30


# type of network shape
type_of_shape = "square"

# Init neurons
if type_of_shape == "line":
    neurons = Utils.initNeuronsInLine(neurons_size, radius)
elif type_of_shape == "circle":
    neurons = Utils.initNeuronsInCircle(neurons_size, radius)
elif type_of_shape == "square":
    neurons = Utils.initNeuronsInSquare(25, 5, radius)

# create random points by radius
X = Utils.createRandomPointsInCircleArray(radius, centerX, centerY)

# algorithm
epochs = 10
SOM.fit(X, neurons, epochs)

# get the coordinates of neurons for presentation on the graph
x_values, y_values = Utils.getCoordinates(neurons, type_of_shape)

# paint points and neurons
fig, ax = plt.subplots()
plt.scatter(X[:, 0], X[:, 1], color='green', marker='x', label='points')
plt.scatter(neurons[:, 0], neurons[:, 1], color='red', marker='o', label='neurons')

if type_of_shape == "square":
    x_values = np.array_split(x_values, 10)
    y_values = np.array_split(y_values, 10)
    plt.plot(x_values[0], y_values[0], color='red', linewidth=1.0)
    plt.plot(x_values[1], y_values[1], color='red', linewidth=1.0)
    plt.plot(x_values[2], y_values[2], color='red', linewidth=1.0)
    plt.plot(x_values[3], y_values[3], color='red', linewidth=1.0)
    plt.plot(x_values[4], y_values[4], color='red', linewidth=1.0)
    plt.plot(x_values[5], y_values[5], color='red', linewidth=1.0)
    plt.plot(x_values[6], y_values[6], color='red', linewidth=1.0)
    plt.plot(x_values[7], y_values[7], color='red', linewidth=1.0)
    plt.plot(x_values[8], y_values[8], color='red', linewidth=1.0)
    plt.plot(x_values[9], y_values[9], color='red', linewidth=1.0)
else:
    plt.plot(x_values, y_values, color='red', linewidth=1.0)

c1 = plt.Circle((centerX, centerY), 2, color='blue', fill=False)
ax.add_artist(c1)
plt.show()
