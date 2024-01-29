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
    # --------- contrainte 3 ----------------------
    satisfy(
        (hdd[1] == processor[0]) | (hdd[1] == processor[1])
    )
    x5 = Var(dom=range(5))
    satisfy(
        (processor[x5] == 1) &
        (imply((processor[j] == price[1]) & (processor[k] == price[3]), (x5 > j) & (x5 < k)) for j in range(5) for k in
         range(5))
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

