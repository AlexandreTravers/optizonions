from pycsp3 import *


def computerCon(datas):
    monitor = VarArray(size=5, dom=range(5))
    processor = VarArray(size=5, dom=range(5))
    hdd = VarArray(size=5, dom=range(5))
    price = VarArray(size=5, dom=range(5))
    matrice = [monitor, price, hdd, processor]

    # contraintes globales
    satisfy(
        AllDifferent(monitor)
    )
    satisfy(
        AllDifferent(processor)
    )
    satisfy(
        AllDifferent(hdd)
    )
    satisfy(
        AllDifferent(price)
    )
    # ----------- contrainte 4 ------------------
    satisfy(
        hdd[1] != 4
    )
    satisfy(
        price[0] != hdd[1]
    )
    x6 = VarArray(size=2, dom=range(5))
    satisfy(
        (processor[x6[0]] == hdd[2]) & (x6[1] == hdd[2])
    )
    satisfy(
        (imply(processor[i] == price[0], i < x6[0])) for i in range(5)
    )
    satisfy(
        (imply(i == price[0], i < x6[1])) for i in range(5)
    )

    count = 0
    for i in range(3):
        for j in range(i + 1, 4):
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

