from pycsp3 import *

def pastaCon(datas):
    shirt = VarArray(size = 5, dom = range(5))
    name = VarArray(size = 5, dom = range(5))
    surname = VarArray(size = 5, dom = range(5))
    pasta = VarArray(size = 5, dom = range(5))
    wine = VarArray(size = 5, dom = range(5))
    age = VarArray(size = 5, dom = range(5))
    matrice = [shirt, name, surname, pasta, wine, age]

    satisfy (
        AllDifferent(shirt),
        AllDifferent(name),
        AllDifferent(surname),
        AllDifferent(pasta),
        AllDifferent(wine),
        AllDifferent(age),
    )

    # Mme Lopes est à la 5ème position
    satisfy(
        surname[2] == 4
    )

    for i in range(len(datas)):
        for j in range(len(datas[i])):
            for k in range(len(datas[i][j])):
                if datas[i][j][k] == -1:
                    satisfy (matrice[j][k] != i)
                elif datas[i][j][k] == 1:
                    satisfy(matrice[j][k] == i  ) 

    if solve() is SAT:
        return True
    else:
        return False



