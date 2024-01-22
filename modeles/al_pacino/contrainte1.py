from pycsp3 import *

name = VarArray(size = 5, dom=range(5))
time = VarArray(size = 5, dom=range(5))
day = VarArray(size = 5, dom=range(5))
film = VarArray(size = 5, dom=range(5))

#contraintes globales
satisfy (
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

if solve() is SAT:
    print("C'est SAT")
else :
    print("c'est pas SAT")



