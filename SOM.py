import math


# calculate distance between two points
def euclideanDistance(point, neuron):
    return math.sqrt(math.pow(point[0] - neuron[0], 2) + math.pow(point[1] - neuron[1], 2))


# choose nearest neuron to current point
def chooseNeuronToMove(point, neurons):
    min_distance = math.inf
    min_distance_index = -1
    for index in range(len(neurons) - 1):
        distance = euclideanDistance(point, neurons[index])
        if distance < min_distance:
            min_distance = distance
            min_distance_index = index

    return min_distance_index


# topological neighborhood
def neighborFunction(winner_neuron, neuron, sigma):
    distance = euclideanDistance(winner_neuron, neuron)
    return math.exp(- (math.pow(distance, 2) / (2 * math.pow(sigma, 2))))


# update neuron place
def updateNeuronPlacement(point, neuron, alpha, h):
    return neuron + alpha * h * (point - neuron)


# update sigma by iteration number
def updateSigma(sigma, iteration, lambda_start):
    # return sigma / (1 + (current_iteration / iteration_size))
    return sigma * math.exp(-iteration / lambda_start)


# update alpha value
def updateAlpha(alpha, iteration, lambda_start):
    return alpha * math.exp(-iteration / lambda_start)


# start algorithm
def fit(points, neurons, epochs, radius):
    alpha_start = 0.01

    sigma_start = radius / 2 + 0.0001

    lambda_start = epochs / math.log(epochs)

    # train each point by epochs amount
    for iteration in range(epochs):

        # update learning variables
        alpha = updateAlpha(alpha_start, iteration, epochs)
        sigma = updateSigma(sigma_start, iteration, lambda_start)

        for point in points:

            # find winner
            winner_neuron_index = chooseNeuronToMove(point, neurons)

            # for each neuron
            for neighbor_index in range(len(neurons)):

                distance = euclideanDistance(neurons[winner_neuron_index], neurons[neighbor_index])

                if distance < sigma:
                    h = neighborFunction(neurons[winner_neuron_index], neurons[neighbor_index], sigma)
                    neurons[neighbor_index] = updateNeuronPlacement(point, neurons[neighbor_index], alpha, h)


