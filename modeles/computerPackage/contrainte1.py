from pycsp3 import *

def computerCon(datas):
    andrew = Var(dom=range(5))
    monitor = VarArray(size = 5, dom=range(5))
    processor = VarArray(size = 5, dom=range(5))
    hdd = VarArray(size = 5, dom=range(5))
    price = VarArray(size = 5, dom=range(5))
    matrice = [monitor, price, hdd, processor]
    
    
    #contraintes globales
    satisfy (
        AllDifferent(monitor)
    )
    satisfy (
        AllDifferent(processor)
    )
    satisfy (
        AllDifferent(hdd)
    )
    satisfy (
        AllDifferent(price)
    )
    x0 = Var(dom=(0,3))
    x1 = Var(dom=(1,4))
    x2 = Var(dom=(3,4))
    x3 = Var(dom=(1,3))
    #--------- contrainte 1 --------------------
    satisfy (
        (ift(x0 == 0,x1==1, x1==4)) & (ift(x2 == 3, x3==1, x3==3)) & (andrew == price[x0]) & (price[x1] == processor[x2]) & (processor[x3] == 3)
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

