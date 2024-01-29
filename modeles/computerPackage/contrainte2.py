from pycsp3 import *


def computerCon(datas):
    andrew = Var(dom=range(5))
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
    x4 = Var(dom=range(5))
    # --------- contrainte 2 ----------------------
    satisfy(
        imply(hdd[i] == processor[3], x4 < i) for i in range(5)
    )

    satisfy(
        imply(hdd[i] == andrew, i < x4) for i in range(5)
    )

    satisfy(
        (andrew != 4) & (hdd[x4] != 1)
    )

    x = VarArray(size=5, dom=range(5))
    satisfy(
        (AllDifferent(x)) & (x[0] == andrew) & (x[1] == processor[0]) & (x[2] == hdd[0]) & (x[3] == price[2]) & (
                    x[4] == hdd[x4])
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

