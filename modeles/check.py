from pycsp3 import *

def check(contraintes):
    var = []
    for i in range(3):
        var.append(VarArray(size=3, dom=range(3)))

    satisfy(
        AllDifferent(var[0])
    )
    satisfy(
        AllDifferent(var[1])
    )
    satisfy(
        AllDifferent(var[2])
    )

    for i in contraintes:
        if i[2] == "!=":
            satisfy(
                var[i[0]][i[1]] != var[i[3]][i[4]]
            )
        elif i[2] == "==":
            satisfy(
                var[i[0]][i[1]] == var[i[3]][i[4]]
            )

    if solve(sols=ALL) is SAT:
        return n_solutions()
    else:
        return 0


def check2(datas, contraintes):
    var = []
    var1 = VarArray(size=3, dom=range(3))
    var2 = VarArray(size=3, dom=range(3))
    var3 = VarArray(size=3, dom=range(3))
    var.append(var1)
    var.append(var2)
    var.append(var3)

    matrice = var
    satisfy(
        AllDifferent(var[0])
    )
    satisfy(
        AllDifferent(var[1])
    )
    satisfy(
        AllDifferent(var[2])
    )
    for contrainte in contraintes.contraintes:
        if contrainte[2] == "!=":
            satisfy(
                var[contrainte[0]][contrainte[1]] != var[contrainte[3]][contrainte[4]]
            )
        elif contrainte[2] == "==":
            satisfy(
                var[contrainte[0]][contrainte[1]] == var[contrainte[3]][contrainte[4]]
            )

    count = 0
    for i in range(2):
        for j in range(i + 1, 3):
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


def check_test(datas, contraintes):
    result = []
    for c in contraintes:
        clear()
        result.append(check2(datas, c))
        clear()
    return result