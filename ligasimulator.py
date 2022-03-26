# LIGASIMULATOR
# Spiller hjemme- og bortekamp mellom alle lagene i ligaen
import random
from itertools import permutations
import numpy as np


# [LAGNAVN, xG for hjemme, xG mot hjemme, xG for borte, xG imot borte]
lag_liste = [
    ["Arsenal", 1.4, 0.9, 1, 0.9],
    ["Brentford", 1.2, 1, 1, 1],
    ["Chelsea", 2, 0.5, 1.3, 0.7],
    ["Liverpool", 2.2, 0.6, 1.6, 0.7]
    ]

def spill_sesong(lag):

    def spill_kamp(h, b):

        hjemmemaal = (h[1] + b[4]) / 2              # forventet antall hjemmemål FOR + bortemål IMOT dividert på 2
        bortemaal = (b[3] + h[2]) / 2               # forventet antall bortemål FOR + hjemmemål IMOT dividert på 2

        #hjemmemaal = ((h[1] + b[2]) / 2)           # slik vil det se ut dersom det spilles på nøytral bane (EM/VM etc)
        #hjemmemaal = ((b[1] + h[2]) / 2)

        hm = np.random.poisson(hjemmemaal)
        bm = np.random.poisson(bortemaal)

        return (h[0], b[0], hm, bm)


    perm = permutations(lag, 2)                     # fikser permutasjoner for oss
                                                    # PS: dersom det kun skal spilles én kamp bruker vi combinations(lag, 2) i steden

    resultater = []

    for i in list(perm):
        resultater.append(list(spill_kamp(list(i)[0], list(i)[1])))


    return resultater

print(spill_sesong(lag_liste))