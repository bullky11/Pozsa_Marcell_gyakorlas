import  random
import math
"""random_szam = random.randint(1,10)
print(random_szam)
asd=math.sqrt(9)
print(asd)
print(9**0.5)"""
sorozat=[-3,5,11,-2,4]
def kiir():
    i = 0
    while i<(len(sorozat)):
        if i < (len(sorozat) -1):
            print(sorozat[i],end="#")
        else:
            print(sorozat[i],end="")
        i +=1
def veletlen(i):
    sorozat[i]=sorozat[i]+random.randint(5,12)
    print(sorozat)

def utolso_csere():
    paratlan_szam = int(input("Adj meg egy 3 al osztható kétjegyű páratlan számot"))
    while paratlan_szam %3!=0 or paratlan_szam<=10  or paratlan_szam%2==0:
        paratlan_szam = int(input("Adj meg egy 3 al osztható kétjegyű páratlan számot"))
    sorozat.append(paratlan_szam)

print(sorozat)









