from al_pacinoPackage import contrainte1,contrainte2,contrainte3,contrainte4,contrainte5,contrainte6,contrainte7
from pycsp3 import *

"""
matrix = [[[-1, 1, 0],
          [1, 0, -1],
          [0, 0, -1]],
          [[1, -1, -1],
          [-1, 0, 0],
          [-1, 0, 0]],
          [[1, -1, -1],
          [-1, 0, 0],
          [-1, 0, 0]],
          [[1, -1, -1],
          [-1, 0, 0],
          [-1, 0, 0]],
          [[1, -1, -1],
          [-1, 0, 0],
          [-1, 0, 0]],
          [[1, -1, -1],
          [-1, 0, 0],
          [-1, 0, 0]]]
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

def transposée (matrix) :
    resultat = list(zip(*matrix))
    return resultat

datas = [matrix[0], matrix[1], matrix[2],transposée(matrix[5]), transposée(matrix[3]),transposée(matrix[4])]
resultats= []
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
print(resultats)

#print(al_pacinoCon(matrix))