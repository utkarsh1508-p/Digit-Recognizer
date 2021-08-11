import numpy as np


def initialise(a, b):
    epsilon = 0.15
    c = np.random.rand(a, b + 1) * (
                2 * epsilon) - epsilon  # Randomly initialises values of thetas between [-epsilon, +epsilon]
    return c
