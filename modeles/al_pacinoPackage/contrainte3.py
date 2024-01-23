from pycsp3 import *

def al_pacinoCon(datas):
    name = VarArray(size=5, dom=range(5))
    time = VarArray(size = 5, dom=range(5))
    day = VarArray(size = 5, dom=range(5))
    film = VarArray(size = 5, dom=range(5))
    matrice = [name, film, day, time]

    #contraintes globales
    satisfy(
        AllDifferent(name)
    )
    satisfy (
        AllDifferent(time)
    )
    satisfy (
        AllDifferent(day)
    )
    satisfy (
        AllDifferent(film)
    )

    #contrainte: les films montrés avant 8h l'ont été a des jours consécutifs
    x0 = Var(dom=range(5))
    satisfy (
        imply((time[0] == day[i]) , (time[1] == day[x0]) & (abs(x0-i)==1)) for i in range (5)
    )

    #pareils pour ceux sortis après 8h
    x1 = Var(dom=range(5))
    x2 = Var(dom=range(5))
    satisfy (
        imply((time[2] == day[i]) , (time[3] == day[x1]) & (time[4] == day[x2]) & (abs(x1-i) - abs(x2-i) < 4)) for i in range (5)
    )

    count = 0
    for i in range (3):
        for j in range (i+1,4):           
            for matrixRow in range(len(datas[count])):
                for matrixColumn in range(len(datas[count][matrixRow])):                    
                    if datas[count][matrixRow][matrixColumn] == -1 :
                        satisfy (
                            matrice[i][matrixRow] != matrice[j][matrixColumn]
                        )
                    if datas[count][matrixRow][matrixColumn] == 1 :
                        satisfy (
                            matrice[i][matrixRow] == matrice[j][matrixColumn]
                        )
            count += 1

    if solve() is SAT:
        return True
    else:
        return False


