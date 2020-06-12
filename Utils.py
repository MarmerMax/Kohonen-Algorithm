import numpy as np
import math
from random import random


def randomPointCircle(radius, centerX, centerY):
    r = radius * math.sqrt(random())
    theta = random() * 2 * math.pi
    x = centerX + r * math.cos(theta)
    y = centerY + r * math.sin(theta)
    return np.array([x, y])


def createRandomPointsArray(radius, centerX, centerY):
    # Init points (just for now)
    size = 50
    X = np.zeros((size, 2))
    for i in range(size):
        X[i] = randomPointCircle(radius, centerX, centerY)

    return X


def initNeuronsInLine(neurons_size, radius):
    neurons = np.zeros((neurons_size, 2))
    step = (radius * 2) / len(neurons)
    start_point = -radius
    for i in range(neurons_size):
        start_point += step
        neurons[i] = np.array([start_point, 0])

    return neurons


def initNeuronsInCircle(neurons_size, radius):
    neurons = np.zeros((neurons_size, 2))
    pi = math.pi
    for i in range(len(neurons)):
        neurons[i][0] = math.cos(2 * pi / len(neurons) * i) * radius
        neurons[i][1] = math.sin(2 * pi / len(neurons) * i) * radius

    # return [(math.cos(2 * pi / n * x) * r, math.sin(2 * pi / n * x) * r) for x in range(0, n + 1)]
    return neurons


def initNeuronsInSquare(neurons_size, neurons_per_line, radius):
    neurons = np.zeros((neurons_size, 2))
    step = (radius * 2) / (neurons_per_line - 1)
    point_x = -radius
    point_y = -radius
    rows = int(neurons_size / neurons_per_line)
    for i in range(rows):
        for j in range(neurons_per_line):
            neurons[i * neurons_per_line + j] = np.array([point_x, point_y])
            point_x += step
        point_x = -radius
        point_y += step
    return neurons


def getCoordinates(array, type):
    if type == "circle" or type == "line":
        x = array[:, 0]
        y = array[:, 1]
        return x, y

    if type == "square":
        x = np.array([])
        y = np.array([])
        i = 0
        while i < len(array):
            x = np.append(x, np.array(array[i:i + 5, 0]), 0)
            y = np.append(y, np.array(array[i:i + 5, 1]), 0)
            i += 5

        i = 0
        while i < 5:
            j = 0
            column_x = np.array([])
            column_y = np.array([])
            line_length = int(len(array) / 5)

            while j < line_length:
                column_x = np.append(column_x, np.array([array[j * line_length + i, 0]]), 0)
                column_y = np.append(column_y, np.array([array[j * line_length + i, 1]]), 0)

                j += 1

            x = np.append(x, column_x, 0)
            y = np.append(y, column_y, 0)

            i += 1

        return x, y
