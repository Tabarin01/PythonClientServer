s1 = "afragola"
print(s1)
print(len(s1))
print(s1[1])

print(s1[1::1])
print(s1[2:4:])
print(s1[::-1])

# liste in python
L = [1,6,9,5,4,7]
print(len(L))
print(L[2])
print(L[::-1])
print(L[3:1:-1])

print([1,2] + [4,2])
L += [568]
L.append(568)
L.append([568])
print(L)

# raddoppia il valore di una lista
L1 = ["1", 5, 8, "12.5", 5.7]
L2 = []
for x in L1:
    if type(x) == type(1):
        L2.append(int(x) * 2)
    else:
        L2.append(float(x) * 2)
    #L2 += [x * 2]

print(L2)

print(ord("A"))
print(chr(68))

for i in range(26):
    a_ascii = ord("a")
    lettera = chr(a_ascii + i)
    print(f"{i} => {lettera}")


import random
n = random.randint(10,100)
print(n)

random.random()

print( random.choice("parola") )
print( random.choice([31,37,43,47,"numero primo", "primo", "numero"]) )

# Estrarre i gironi del mondiale da una lista di squadre
squadre = ["germania", "francia", "spagna", "argentina", "marocco", "brasile", "svizzera", "giappone"]
estratte = []
def estrai():
    global squadre, estratte
    while True:
        s = random.choice(squadre)
        if s not in estratte:
            estratte.append(s)
            return s

for i in range(len(squadre)//2):
    s1 = estrai()
    s2 = estrai()
    girone = chr(i+ord("A"))
    print(f"{girone} : {s1} - {s2}")



for i in range(len(squadre)//2):
    s1 = random.choice(squadre)
    squadre.remove(s1)

    s2 = random.choice(squadre)
    squadre.remove(s2)

    girone = chr(i+ord("A"))
    print(f"{girone} : {s1} - {s2}")


# tuple
[1,2,3]
tupla = (1,2,3,"ciao")
domanda = (1.5 ,)
non_tupla = (1.5)

#tupla[0] = 2
# print(tupla.append(5))
L3 = []
for x in tupla:
    L3.append(x)
L3[0] = 10
print(L3)