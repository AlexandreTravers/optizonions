from pycsp3 import *

def al_pacinoCon(datas):
    name = VarArray(size=5, dom=range(5))
    time = VarArray(size = 5, dom=range(5))
    day = VarArray(size = 5, dom=range(5))
    film = VarArray(size = 5, dom=range(5))
    matrice = [name, time, day, film]

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

    #contrainte : de tout les films sortie au 21ème siècle, aucuns n'a été choisi par jessica. Un a ouvert la semaine, un autre a fermé la semaine
    satisfy (
        (name[0] != film[0]) & (name[0] != film[4])
    )

    satisfy (
        ((film[0] == day[0]) & (film[4] == day[4])) | ((film[0] == day[4]) & (film[4] == day[0]))
    )

    for dataRow in range(len(datas)):
        for dataColumn in range(len(datas[dataRow])):
            for matrixRow in range(len(datas[dataRow][dataColumn])):
                for matrixColumn in range(len(datas[dataRow][dataColumn][matrixRow])):
                    if(datas[dataRow][dataColumn][matrixRow][matrixColumn] == -1):
                        satisfy(
                            matrice[dataRow][matrixRow] != matrice[dataColumn][matrixColumn]
                        )
                    elif(datas[dataRow][dataColumn][matrixRow][matrixColumn] == 1):
                        satisfy(
                            matrice[dataRow][matrixRow] == matrice[dataColumn][matrixColumn]
                        )

    if solve() is SAT:
        return True
    else:
        return False


