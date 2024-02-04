from modeles.al_pacinoPackage import contrainte1 as pacc1,contrainte2 as pacc2,contrainte3 as pacc3,contrainte4 as pacc4,contrainte5 as pacc5,contrainte6 as pacc6,contrainte7 as pacc7
from modeles.computerPackage import contrainte1 as comc1, contrainte2 as comc2,contrainte3 as comc3, contrainte4 as comc4
from modeles.pastaPackage import contrainte1, contrainte2, contrainte3, contrainte4, contrainte5, contrainte6, contrainte7, contrainte8, contrainte9, contrainte10, contrainte11, contrainte12, contrainte13, contrainte14, contrainte15, contrainte16, contrainte17, contrainte18, contrainte19, contrainte20, contrainte21, contrainte22
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
class ObjetMatrice:
    def __init__(self, matrice, pb):
        self.matrice = matrice
        self.pb = pb
        self.result = self.main()

    def transposée (self,matrix) :
        resultat = list(zip(*matrix))
        return resultat
    
    def setMatrix(self, matrice) :
        self.matrice = matrice

    def setPb(self, pb): 
        self.pb = pb
    
    def getMatrix(self):
        return self.matrice

    def getPb(self):
        return self.pb
    
    def getResult(self) :
        return self.result
    
    def main(self) :
        clear()
        if(self.pb == 3):
            datas = []
            for i in self.matrice:
                datas.append(i)
        else:
            datas = [self.matrice[0], self.matrice[1], self.matrice[2], self.transposée(self.matrice[5]), self.transposée(self.matrice[3]), self.transposée(self.matrice[4])]
        resultats= []
        if self.pb == 2:
            resultats.append(pacc1.al_pacinoCon(datas))
            clear()
            resultats.append(pacc2.al_pacinoCon(datas))
            clear()
            resultats.append(pacc3.al_pacinoCon(datas))
            clear()
            resultats.append(pacc4.al_pacinoCon(datas))
            clear()
            resultats.append(pacc5.al_pacinoCon(datas))
            clear()
            resultats.append(pacc6.al_pacinoCon(datas))
            clear()
            resultats.append(pacc7.al_pacinoCon(datas))
        elif self.pb == 1:
            resultats.append(comc1.computerCon(datas))
            clear()
            resultats.append(comc2.computerCon(datas))
            clear()
            resultats.append(comc3.computerCon(datas))
            clear()
            resultats.append(comc4.computerCon(datas))
            clear()
        elif self.pb == 3:
            resultats.append(contrainte1.pastaCon(datas))
            clear()
            resultats.append(contrainte2.pastaCon(datas))
            clear()
            resultats.append(contrainte3.pastaCon(datas))
            clear()
            resultats.append(contrainte4.pastaCon(datas))
            clear()
            resultats.append(contrainte5.pastaCon(datas))
            clear()
            resultats.append(contrainte6.pastaCon(datas))
            clear()
            resultats.append(contrainte7.pastaCon(datas))
            clear()
            resultats.append(contrainte8.pastaCon(datas))
            clear()
            resultats.append(contrainte9.pastaCon(datas))
            clear()
            resultats.append(contrainte10.pastaCon(datas))
            clear()
            resultats.append(contrainte11.pastaCon(datas))
            clear()
            resultats.append(contrainte12.pastaCon(datas))
            clear()
            resultats.append(contrainte13.pastaCon(datas))
            clear()
            resultats.append(contrainte14.pastaCon(datas))
            clear()
            resultats.append(contrainte15.pastaCon(datas))
            clear()
            resultats.append(contrainte16.pastaCon(datas))
            clear()
            resultats.append(contrainte17.pastaCon(datas))
            clear()
            resultats.append(contrainte18.pastaCon(datas))
            clear()
            resultats.append(contrainte19.pastaCon(datas))
            clear()
            resultats.append(contrainte20.pastaCon(datas))
            clear()
            resultats.append(contrainte21.pastaCon(datas))
            clear()
            resultats.append(contrainte22.pastaCon(datas))
            clear()
        return resultats

"""
matrice_exemple = [[[-1, 1, -1, -1, -1],
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


pb_exemple = 2
objet = ObjetMatrice(matrice_exemple,pb_exemple)
objet.setMatrix(matrice_exemple)
objet.setPb(pb_exemple)
objet.main()
print(objet.getResult)
"""