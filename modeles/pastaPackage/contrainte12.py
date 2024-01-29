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

    count = 0
    for i in range(5):
        for j in range(i + 1, 6):
            for matrixRow in range(len(datas[count])):
                for matrixColumn in range(len(datas[count][matrixRow])):
                    if datas[count][matrixRow][matrixColumn] == -1:
                        satisfy(
                            matrice[i][matrixRow] != matrice[j][matrixColumn]
                        )
                    if datas[count][matrixRow][matrixColumn] == 1:
                        satisfy(
                            matrice[i][matrixRow] == matrice[j][matrixColumn]
                        )
            count += 1

    if solve() is SAT:
        return True
    else:
        return False



