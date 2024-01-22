from pycsp3 import *

time = VarArray(size = 5, dom=range(5))
day = VarArray(size = 5, dom=range(5))
film = VarArray(size = 5, dom=range(5))

#contraintes globales
satisfy (
    AllDifferent(time)
)
satisfy (
    AllDifferent(day)
)
satisfy (
    AllDifferent(film)
)
satisfy (
    film[0] != 3
)
#contrainte : de tout les films sortie au 21ème siècle, aucuns n'a été choisi par jessica. Un a ouvert la semaine, un autre a fermé la semaine
satisfy (
    (0 != film[0]) & (0 != film[4])
)

satisfy (
    ((film[0] == day[0]) & (film[4] == day[4])) | ((film[0] == day[4]) & (film[4] == day[0]))
)

#Affichage du résultat

if solve(sols=ALL) :
    print("Number of solutions: ", n_solutions())


