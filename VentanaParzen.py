import math
import numpy as np
from GaussianKernel import gaussianKernel

def ventanaParzen(Xval,Xent,h):

    M = Xval[:, 1].size
    Xent = [list(row) for row in Xent]
    N = Xent.__len__()

    Yesti = range(M)
    Yesti = [i * 0 for i in Yesti]

    for j in range(M):

        sum = 0

        for k in range(N):

            dist = 0

            for l in range(3):
                dist = dist + np.power((Xval[j, l] - Xent[k][l]), 2)

            dist = math.sqrt(dist)
            dist = dist / h
            numerador = gaussianKernel(dist)
            sum = sum + numerador

        Yesti[j] = sum/N

    return Yesti