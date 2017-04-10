import math
import numpy as np
import scipy.stats as ss

def vecinosCercanos(Xval,Xent,Yent,k):

    N = Xent[:,1].size
    M = Xval[:,1].size

    Yesti = range(M)
    Yesti = [i*0 for i in Yesti]
    dis = range(N)
    dis = [i * 0 for i in dis]
    ind = range(k)
    ind = [i * 0 for i in ind]
    Yaux = range(k)
    Yaux = [i * 0 for i in Yaux]

    for j in range(M):

        for h in range(N):
            sum = 0

            for l in range(3):
                sum = sum + np.power((Xval[j, l] - Xent[h, l]), 2)

            dis[h] = math.sqrt(sum)

        dis2 = np.sort(dis)
        dis2 = dis2.T
        l=0
        while(l < k):

            aux = np.where(dis == dis2[l])
            aux = [list(row) for row in aux]

            len = aux.__len__()

            z = 0
            while(z < len):
                if(l >= k):
                    z = len + 3
                else:
                    ind[l]= aux[z]
                    l = l + 1
                z = z + 1


        for w in range(k):

            Yaux[w] = Yent[ind[w]].item(0)

        Yesti[j] = ss.mode(Yaux) # moda
        Yesti[j] = (Yesti[j])[0][0]



    return Yesti