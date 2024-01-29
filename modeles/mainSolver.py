from al_pacinoPackage import contrainte1,contrainte2,contrainte3,contrainte4,contrainte5,contrainte6,contrainte7
from computerPackage import contrainte1 as comc1, contrainte2 as comc2,contrainte3 as comc3, contrainte4 as comc4
from pycsp3 import *


"""
matrix = [[[-1, 1, -1, -1, -1],
          [-1, -1, -1, 1, -1],
          [-1, -1, 1, -1, -1],
          [-1, -1, -1, -1, 1],
          [1, -1, -1, -1, -1]],

          [[-1, -1, 1, -1, -1],
          [-1, -1, -1, 1, -1],
          [-1, 1, -1, -1, -1],
          [-1, -1, -1, -1, 1],
          [1, -1, -1, -1, -1]],

          [[-1, -1, -1, 1, -1],
          [-1, 1, -1, -1, -1],
          [-1, -1, -1, -1, 1],
          [1, -1, -1, -1, -1],
          [-1, -1, 1, -1, -1]],

          [[-1, -1, -1, -1, 1],
          [-1, -1, -1, 1, -1],
          [1, -1, -1, -1, -1],
          [-1, 1, -1, -1, -1],
          [-1, -1, 1, -1, -1]],

          [[-1, -1, -1, -1, 1],
          [-1, -1, -1, 1, -1],
          [1, -1, -1, -1, -1],
          [-1, -1, 1, -1, -1],
          [-1, 1, -1, -1, -1]],

          [[1, -1, -1, -1, -1],
          [-1, -1, 1, -1, -1],
          [-1, 1, -1, -1, -1],
          [-1, -1, -1, 1, -1],
          [-1, -1, -1, -1, 1]]]
"""
def transposée (matrix) :
    resultat = list(zip(*matrix))
    return resultat

def main(matrix, pb) :
    datas = [matrix[0], matrix[1], matrix[2],transposée(matrix[5]), transposée(matrix[3]),transposée(matrix[4])]
    resultats= []
    if pb == 1:
        resultats.append(contrainte1.al_pacinoCon(datas))
        clear()
        resultats.append(contrainte2.al_pacinoCon(datas))
        clear()
        resultats.append(contrainte3.al_pacinoCon(datas))
        clear()
        resultats.append(contrainte4.al_pacinoCon(datas))
        clear()
        resultats.append(contrainte5.al_pacinoCon(datas))
        clear()
        resultats.append(contrainte6.al_pacinoCon(datas))
        clear()
        resultats.append(contrainte7.al_pacinoCon(datas))
    elif pb == 2:
        resultats.append(comc1(datas))
        clear()
        resultats.append(comc2(datas))
        clear()
        resultats.append(comc3(datas))
        clear()
        resultats.append(comc4(datas))
        clear()
    print(resultats)
    return resultats

