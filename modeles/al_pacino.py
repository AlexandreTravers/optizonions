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
#contrainte : de tout les films sortie au 21ème siècle, aucuns n'a été choisi par jessica. Un a ouvert la semaine, un autre a fermé la semaine
satisfy (
    (0 != film[0]) & (0 != film[4])
)
satisfy (
    ((film[0] == day[0]) & (film[4] == day[4])) | ((film[0] == day[4]) & (film[4] == day[0]))
)
#contrainte : Donnie brasco est sortie a 20h30
satisfy (
    film[1] == time[3]
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
#contrainte : Un homme et une femme sont aller voir une séance avant 8h mais ce n'était pas en milieu de semaine
#Je prend en compte que milieu de semaine c’est mercredi
h = Var(dom=(1,2))
f = Var(dom=(0,3,4))
satisfy (
    ((time[0]==h) & (time[1] == f)) | ((time[0]==f) & (time[1] == h))
)
satisfy (
    (time[0] != day[2]) & (time[1] != day[2])
)
#contrainte : Mark a choisi Scarcrow, et son visionnage était 1h5 parès celui de scarface
satisfy (
    (2 == film[2]) & (2 == time[4]) & (film[3] == time[1])
)

#contrainte: Jessica et Mary n'ont eu leurs présentation un jour paire
#Je pars du principe que Mardi et Jeudi sont les jours paires
satisfy (
    (day[1] != 0) & (day[1] != 3) & (day[3] != 0) & (day[3] != 3)
)

#contrainte: 88 minutes a été montré 40 minutes après l'heure et 40 minutes après la séance de jeudi
satisfy (
    film[0] == time[2]
)
satisfy (
    day[3] == time[1]
)
#Affichage du résultat

if solve(sols=ALL) :
    print("Number of solutions: ", n_solutions())

if solve(sols=ALL) is SAT:
    print(f" Heure : {values(time)}")
    print(f" Jour : {values(day)}")
    print(f" Film : {values(film)}")

