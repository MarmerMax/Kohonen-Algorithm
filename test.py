import math
from random import random
import matplotlib.pyplot as plt
import numpy as np

radius = 2
centerX = 0
centerY = 0
neurons_size = 30


def randomPointCircle(radius,centerX,centerY):
    r = radius * math.sqrt(random())
    theta = random() * 2 * math.pi
    x = centerX + r * math.cos(theta)
    y = centerY + r * math.sin(theta)
    return np.array([x,y])


def initNeuronsLine(neurons_size, radius, leftPoint):
    neurons = np.zeros((neurons_size, 2))
    step = (radius * 2) / len(neurons)
    for i in range(neurons_size):
        leftPoint += step
        neurons[i] = np.array([leftPoint, 0])

    return neurons


# Init neurons
neurons = initNeuronsLine(neurons_size, radius, -2)


# Init points (just for now)
size = 50
X = np.zeros((size, 2))
for i in range(size):
    X[i] = randomPointCircle(radius, centerX, centerY)


# paint points and neurons
fig, ax = plt.subplots()
plt.scatter(X[:, 0], X[:, 1], color='green', marker='x', label='points')
plt.scatter(neurons[:, 0], neurons[:, 1], color='red', marker='o', label='neurons')

c1 = plt.Circle((centerX, centerY), radius, color='blue', fill=False)
ax.add_artist(c1)
plt.show()
