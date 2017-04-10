import scipy.io as sp
import numpy as np
from collections import OrderedDict
import scipy.stats as ss
from Normalizar import normalizar
from VecinosCercanos import vecinosCercanos
from VentanaParzen import ventanaParzen

punto = input('Ingrese el punto que quiere realizar: ')

if punto == "5":

    #  ... PUNTO 5 ...

    mat = sp.loadmat('DatosClasificacion.mat')
    # print(mat)
    mat = OrderedDict(mat)

    Xclass = mat.get('Xclas')
    Xclass = Xclass[:, 0:3]

    Yclass = mat.get('Yclas')

    N = len(Xclass)
    porcentaje = N * 0.7

    np.random.seed(0)
    ind = np.random.permutation(range(N))

    Xtrain = Xclass[ind[0:int(porcentaje)],:]
    Xtest = Xclass[ind[int(porcentaje):Xclass[:,1].size], :]
    Ytrain = Yclass[ind[0:int(porcentaje)], :]
    Ytest = Yclass[ind[int(porcentaje):Yclass.size], :]

    mu = Xtrain.mean(0)
    sigma = Xtrain.std(0, ddof = 1)
    Xtrain = ss.zscore(Xtrain)

    Xtest = normalizar(Xtest,mu,sigma)

    k=6
    Yesti = vecinosCercanos(Xtest, Xtrain, Ytrain, k)

    cont = 0
    i = 0
    print(Ytest.size)

    while (i < Ytest.size):
        if (Ytest[i] == Yesti[i]):
            cont = cont + 1
        i = i + 1

    Eficiencia = cont / Ytest.size
    Error = 1 - Eficiencia

    print("La eficiencia en prueba es: ", Eficiencia)
    print("El error de clasificación en prueba es: ", Error)


elif punto == "6":

    #  ... PUNTO 6 ...
    mat = sp.loadmat('DatosClasificacion.mat')
    mat = OrderedDict(mat)

    Xclass = mat.get('Xclas')
    Xclass = Xclass[:, 0:3]

    Yclass = mat.get('Yclas')

    N = len(Xclass)
    porcentaje = N * 0.7

    np.random.seed(0)
    ind = np.random.permutation(range(N))

    Xtrain = Xclass[ind[0:int(porcentaje)], :]
    Xtest = Xclass[ind[int(porcentaje):Xclass[:, 1].size], :]
    Ytrain = Yclass[ind[0:int(porcentaje)], :]
    Ytest = Yclass[ind[int(porcentaje):Yclass.size], :]

    mu = Xtrain.mean(0)
    sigma = Xtrain.std(0, ddof=1)
    Xtrain = ss.zscore(Xtrain)

    Xtest = normalizar(Xtest, mu, sigma)

    M = Ytrain.size

    Xtrain1 = []

    for j in range(M):
        if(Ytrain[j] == 1):
            Xtrain1.append(Xtrain[j, :])

    Xtrain2 = []

    for j in range(M):
        if (Ytrain[j] == 2):
            Xtrain2.append(Xtrain[j, :])

    Xtrain3 = []

    for j in range(M):
        if (Ytrain[j] == 3):
            Xtrain3.append(Xtrain[j, :])


    h = 0.05
    funcion1 = ventanaParzen(Xtest, Xtrain1, h)
    funcion2 = ventanaParzen(Xtest, Xtrain2, h)
    funcion3 = ventanaParzen(Xtest, Xtrain3, h)

    funcion = np.column_stack((funcion1, funcion2, funcion3))
    funcion = [list(row) for row in funcion]

    Yesti = []

    for j in range(funcion.__len__()):
        Yesti.append(funcion[j].index(max(funcion[j])))

    i=0
    cont = 0

    while (i < Ytest.size):
        if (Ytest[i] == Yesti[i]):
            cont = cont + 1
        i = i + 1

    Eficiencia = 1 - cont / Ytest.size
    Error = 1 - Eficiencia

    print("La eficiencia en prueba es: ", Eficiencia)
    print("El error de clasificación en prueba es: ", Error)







