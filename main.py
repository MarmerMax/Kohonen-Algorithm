import matplotlib.pyplot as plt
import Utils
import SOM
import numpy as np

radius = 2
centerX = 0
centerY = 0
neurons_size = 30

# type of train shape -> ["circle", "ring"]
type_of_shape = "ring"

# create random points by chosen type of shape
if type_of_shape == "circle":
    X = Utils.createRandomPointsInCircleArray(radius, 100, centerX, centerY)
elif type_of_shape == "ring":
    X = Utils.createRandomPointsInRingArray(radius * 2, radius, 50, centerX, centerY)

# type of neurons network shape -> ["line", "circle", "square"]
type_of_network = "square"

# create neurons points by chosen type of network
if type_of_network == "line":
    neurons = Utils.initNeuronsInLine(neurons_size, radius)
elif type_of_network == "circle":
    neurons = Utils.initNeuronsInCircle(neurons_size, radius)
elif type_of_network == "square":
    neurons = Utils.initNeuronsInSquare(25, 5, radius)

# algorithm
epochs = 50
errors = SOM.fit(X, neurons, epochs, radius)
# print(neurons)

# get the coordinates of neurons for presentation on the graph
x_values, y_values = Utils.getCoordinates(neurons, type_of_network)

# paint points and neurons
fig, ax = plt.subplots()
plt.scatter(X[:, 0], X[:, 1], color='green', marker='x', label='points')
plt.scatter(neurons[:, 0], neurons[:, 1], color='red', marker='o', label='neurons')

if type_of_network == "square":
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

if type_of_shape == "circle":
    c1 = plt.Circle((centerX, centerY), radius, color='blue', fill=False)
    ax.add_artist(c1)
elif type_of_shape == "ring":
    c1 = plt.Circle((centerX, centerY), radius, color='blue', fill=False)
    c2 = plt.Circle((centerX, centerY), radius * 2, color='blue', fill=False)
    ax.add_artist(c1)
    ax.add_artist(c2)

# plt.plot(range(1, len(errors) + 1), errors, color='red')
# plt.xlabel('Epochs')
# plt.ylabel('Sum-squared-error')
# plt.show()

plt.show()
