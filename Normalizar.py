import numpy as np

def normalizar(Datos,MU,SIG):
    N = MU.size

    Z = np.zeros_like(Datos)

    for i in range(N):
        vector = (Datos[:, i]-MU[i])/ SIG[i]
        Z[:,i] = vector.T

    return Z
