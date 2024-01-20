from pycsp3 import *

andrew = Var(dom=range(5))
monitor = VarArray(size = 5, dom=range(5))
processor = VarArray(size = 5, dom=range(5))
hdd = VarArray(size = 5, dom=range(5))
price = VarArray(size = 5, dom=range(5))

#contraintes globales
satisfy (
    AllDifferent(monitor)
)
satisfy (
    AllDifferent(processor)
)
satisfy (
    AllDifferent(hdd)
)
satisfy (
    AllDifferent(price)
)
#--------- contrainte 1 --------------------


#--------- contrainte 2 ----------------------
satisfy (
    andrew != monitor[3]
)

# --------- contrainte 3 ----------------------


# ----------- contrainte 4 ------------------
if solve() is SAT:
    
    print(f" Monitor : {values(monitor)}")
    print(f" Processor : {values(processor)}")
    print(f" HDD : {values(hdd)}")
    print(f" Price : {values(price)}")
    print(f"Andrew : {value(andrew)}")
