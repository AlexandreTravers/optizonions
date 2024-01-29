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

    #contrainte: 88 minutes a été montré 40 minutes après l'heure et 40 minutes après la séance de jeudi
    satisfy (
        film[0] == time[2]
    )
    satisfy (
        day[3] == time[1]
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


