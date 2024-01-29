from pycsp3 import *


def check (contraintes): 
    var = []
    for i in range(3):
        var.append(VarArray(size=3, dom=range(3)))
    
    satisfy (
        AllDifferent(var[0])
    )
    satisfy (
        AllDifferent(var[1])
    )
    satisfy (
        AllDifferent(var[2])
    )

    for i in contraintes :
        if i[2] == "!=" :
            satisfy (
                var[i[0]][i[1]] != var[i[3]][i[4]]
            )
        elif i[2] == "==" :
            satisfy (
                var[i[0]][i[1]] == var[i[3]][i[4]]
            )
    
    if solve(sols=ALL) is SAT:
        return n_solutions()
    else :
        return 0
