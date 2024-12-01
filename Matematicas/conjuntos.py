A = {2,4,5,7}
B = {1,3,3,1,3}
C = {"Juan", "Luis", "Braulio"}


print(f"El conjunto A tiene estos valores {A}")
print(f"El conjunto B tiene estos valores {B}")
print(C)



#Conjuntos vacios

D = set()
print("D es", D)
D.add(7)
print("Ahora D es:", D)

D.update([2, 4, 10, 12])

print("Ahora es", D)


D.discard(10)
print("D:", D)

D.clear()
print("Se eliminó todo")



E = {2,3,4,8,10,12,15,18}
F = {8,10,15,5,4,1}

c1 = len(E)
c2 = len(F)
print(f"La longuitud de E es:", c1)




#EJERCICIO EN CLASE

G = {1,2,3,4,5}
H = {4,5,6,7}
U = {1,2,3,4,5,6,7,8,9}

c3 = len(G)
c4 = len(H)
c5 = len(U)

print(f"La cantidad de elementos del conjunto G es {c3}")
print(f"La cantidad de elementos del conjunto H es {c4}")
print(f"La cantidad de elementos del conjunto U es {c5}")

#OPERACIONES CON CONJUNTOS

#UNIÓN
print("Realizaremos la union de dos conjuntos")
GUF = G|H
print(f"E unión F es igual a :{GUF}")


#INTERSECCIÓN
print("Realizaremos la interseccion de dos conjuntos")
GIH = G&F
print(GIH)

#Diferencia
print("Realizaremos la diferencia de dos conjuntos")
GDH = G-F
print(GDH)


#EJERCICIOS
#H-G
#Diferencia
print("Realizaremos la diferencia de dos conjuntos")
HDG = H-G
print(HDG)


#Dif, Simétrica
print("Esta es la diferencia de dos conjuntos")
GXH = G|H
print("Esta es la diferencia simétrica")
#Complemento de G
print("Este es el complemento de dos conjuntos")
Gc = U-G
print(Gc)
#Complemento de H
Hc = U-H
print(Hc)