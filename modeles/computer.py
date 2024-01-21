from pycsp3 import *

andrew = Var(dom=range(5))
processor = VarArray(size = 5, dom=range(5))
hdd = VarArray(size = 5, dom=range(5))
price = VarArray(size = 5, dom=range(5))


#contraintes globales
satisfy (
    AllDifferent(processor)
)
satisfy (
    AllDifferent(hdd)
)
satisfy (
    AllDifferent(price)
)
x0 = Var(dom=(0,3))
x1 = Var(dom=(1,4))
x2 = Var(dom=(3,4))
x3 = Var(dom=(1,3))
#--------- contrainte 1 --------------------
satisfy (
    (ift(x0 == 0,x1==1, x1==4)) & (ift(x2 == 3, x3==1, x3==3)) & (andrew == price[x0]) & (price[x1] == processor[x2]) & (processor[x3] == 3) 
)
x4 = Var(dom=range(5))
#--------- contrainte 2 ----------------------
satisfy (
    imply (hdd[i] == processor[3], x4 < i) for i in range(5)
)

satisfy (
    imply(hdd[i] == andrew, i < x4) for i in range(5)
)

satisfy (
    (andrew != 4) & (hdd[x4] != 1)
)

x = VarArray(size=5, dom= range(5))
satisfy (
    (AllDifferent(x)) & (x[0] == andrew) & (x[1] == processor[0]) & (x[2] == hdd[0]) & (x[3] == price[2]) & (x[4] == hdd[x4])
)

# --------- contrainte 3 ----------------------
satisfy (
    (hdd[1] == processor[0]) | (hdd[1] == processor[1])
)
x5 = Var(dom=range(5))
satisfy (
    (processor[x5] == 1) & 
    (imply ((processor[j] == price[1]) & (processor[k] == price[3]), (x5>j) & (x5<k)) for j in range(5) for k in range(5))
)

# ----------- contrainte 4 ------------------
satisfy (
    hdd[1] != 4
)
satisfy (
    price[0] != hdd[1]
)
x6 = VarArray(size= 2,dom=range(5))
satisfy (
    (processor[x6[0]] == hdd[2]) & (x6[1] == hdd[2])
)
satisfy (
    (imply(processor[i] == price[0], i < x6[0])) for i in range(5)
)
satisfy (
    (imply(i == price[0], i < x6[1])) for i in range(5)
)

if solve(sols=ALL) :
    print("Number of solutions: ", n_solutions())

if solve(sols=ALL) is SAT:
    for i in range(n_solutions()):       
        print(f" Processor : {values(processor)}")
        print(f" HDD : {values(hdd)}")
        print(f" Price : {values(price)}")
        print(f"Andrew : {value(andrew)}")
