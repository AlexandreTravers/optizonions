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

#pareils pour ceux sortis après 8h

#contrainte : Un homme et une femme sont aller voir une séance avant 8h mais ce n'était pas en milieu de semaine
#TODO: c'est quoi milieu de semaine????

#contrainte : Mark a choisi Scarcrow, et son visionnage était 1h5 parès celui de scarface
#TODO: Est-ce une bonne façon de faire?
satisfy (
    (2 == film[2]) & (2 == time[4]) & (film[3] == time[1])
)

#contrainte: Jessica et Mary n'ont eu leurs présentation un jour paire

#contrainte: 88 minutes a été montré 40 minutes après l'heure et 40 minutes après la séance de jeudi
#Affichage du résultat


if solve() is SAT:
    print(f" Heure : {values(time)}")
    print(f" Jour : {values(day)}")
    print(f" Film : {values(film)}")
