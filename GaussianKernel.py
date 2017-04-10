import math

def gaussianKernel(u):

    k = 0.5 * math.exp(-0.5 * (math.pow(u, 2)))
    return k
