from pycsp3 import * 


shirt = VarArray(size = 5, dom = range(5))
name = VarArray(size = 5, dom = range(5))
surname = VarArray(size = 5, dom = range(5))
pasta = VarArray(size = 5, dom = range(5))
wine = VarArray(size = 5, dom = range(5))
age = VarArray(size = 5, dom = range(5))

satisfy (
    AllDifferent(shirt),
    AllDifferent(name),
    AllDifferent(surname),
    AllDifferent(pasta),
    AllDifferent(wine),
    AllDifferent(age),
)

#La femme qui porte un t-shirt blanc est à côté de la femme qui aime le vin Italien
satisfy (
    imply(shirt[3] == i, (wine[4] == i+1) | (wine[4] == i-1)) for i in range(5)
)

#Mme Miller se situe entre Mme Davis et Mme Brown
satisfy (
    (surname[1] < surname[3]) & (surname[0] > surname[3])
)

#La plus jeune est en 3ème position
satisfy (
    age[0] == 2
)

#La femme qui aime le vin Chilien aime aussi les farfalle
satisfy (
    wine[2] == pasta[0]
)

#La personne qui aime le vin Argentin est en première position
satisfy (
    wine[1] == 0
)

#Andrea est juste a droite de la femme qui a 35 ans
satisfy (
    name[0] == age[1] +1
)

#La femme au t-shirt bleue est entre Mme Davis et Holly
satisfy (
    (shirt[0] > surname[1]) & (shirt[0] < name[1])
)

#Holly est à la droite de la femme avec un t-shirt rouge
satisfy (
    name[1] > shirt[2]
)

#La femme avec un t-shirt rouge est juste à gauche de la femme qui a 35 ans
satisfy (
    shirt[4] == age[1]-1
)
#Mme Brown est à la gauche de Julie
satisfy (
   surname[0] == name[2]-1
)

#Victoria est à côté de Leslie
satisfy (
    (name[4] - name[3] == 1) | (name[3] - name[4] == 1)
)

#Mme Lopes est à la 5ème position
satisfy (
    surname[2] == 4
)

#Mme Wilson porte le t-shirt blanc
satisfy (
    shirt[3] == surname[4]
)

#La femme qui aime les lasagnes est entre celle qui aime les vins Italien et celle qui aime les spaguetti
satisfy (
    (pasta[1] > wine[4]) & (pasta[1] < pasta[3]) 
)

#Leslie est exactement à la gauche de le femme qui a 30 ans
satisfy (
    name[3] == age[0]-1
)

#La femme la plus jeune aime les Penne
satisfy (
    age[0] == pasta[2]
)
#La femme qui a 40 ans aime les lasagnes
satisfy (
    age[2] == pasta[1]
)

#La femme qui a 45 ans est à la droite de la femme avec un tshirt rouge
satisfy (
    age[3] > shirt[2]
)

#La femme avec un tshirt rouge est à gauche de la femme qui aime les vins australien
satisfy (
    shirt[2] < wine[0]
)
#Mme Wilson est à côté de la femme qui a 30 ans
satisfy (
    (surname[4] == age[0]-1) | (surname[4] == age[0]+1)
)

#La femme avec un t-shirt bleu est en deuxième position
satisfy (
    shirt[0] == 1
)

#La femme qui aime les vins australien est entre victoria et la femme qui aime les vins français
satisfy (
    (wine[0] > name[4]) & (wine[0] < wine[3])
)
#Affichage du résultat

if solve(sols=ALL) is SAT:
    print("Number of solutions: ", n_solutions())

if solve() is SAT:    
    print(f" shirt : {values(shirt)}")
    print(f" name : {values(name)}")
    print(f" surname : {values(surname)}")
    print(f" pasta : {values(pasta)}")
    print(f" wine : {values(wine)}")
    print(f" age : {values(age)}")



