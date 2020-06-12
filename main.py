import matplotlib.pyplot as plt
import Utils
import SOM
import numpy as np

radius = 2
centerX = 0
centerY = 0
neurons_size = 30

# Init neurons
# neurons = Utils.initNeuronsInLine(neurons_size, radius)
# neurons = Utils.initNeuronsInCircle(neurons_size, radius)
neurons = Utils.initNeuronsInSquare(25, 5, radius)

# create random points by radius
X = Utils.createRandomPointsArray(radius, centerX, centerY)

# algorithm
epochs = 10
SOM.fit(X, neurons, epochs)

# get the coordinates of neurons for presentation on the graph
x_values, y_values = Utils.getCoordinates(neurons, "circle")

# y = []
# y.append(neurons[:5, 0])
# y.append(neurons[5:10, 0])
# print(y)

# paint points and neurons
fig, ax = plt.subplots()
plt.scatter(X[:, 0], X[:, 1], color='green', marker='x', label='points')
plt.scatter(neurons[:, 0], neurons[:, 1], color='red', marker='o', label='neurons')
plt.plot(x_values, y_values, color='red', linewidth=1.0)
c1 = plt.Circle((centerX, centerY), radius, color='blue', fill=False)
ax.add_artist(c1)
plt.show()
