import math
# lista = []
# 1a
# lista = []
# for i in range(1,11):
#     lista.append(i)
# print(lista)

# 1b
# lista = []
# for i in range(0,21):
#     if(i%2==0):
#         lista.append(i)
# print

# 1c
# lista = []
# for i in range(1,11):
#     lista.append(math.pow(i,2))
# print(lista)

# 1d
# lista = []
# for i in range(1,11):
#     lista.append(i*0)
# print

# 1e
# lista = []
# for i in range(1,11):
#     if(i%2==0):
#         lista.append(1)
#     else:
#         lista.append(0)
# print

# 1f
# lista = []
# for i in range (1,11):
#     if(i<6):
#        lista.append(i-1)
#     elif(i>6):
#     lista.append(i-6)
#     else:
#         lista.append(0)
#     print(lista)

#2a
# lista = []
# i = 1
# while i<11:
#     lista.append(i)
#     i += 1
# print(lista)

# 2b
# lista = []
# i = 1
# while i<21:
#     if(i%2==0):
#         lista.append(i)
#     i += 1
# print(lista)

# 2c
# i=1
# while i<11:
#     lista.append(math.pow(i,2))
#     i += 1
# print(lista)

# 2d
# i=1
# while i<11:
#     lista.append(0)
#     i += 1
# print(lista)

# 2e
# i=1
# while i<11:
#     if(i%2==0):
#         lista.append(1)
#     else:
#         lista.append(0)
#     i+=1
# print(lista)
#

# 2f

# i=1
# while i<11:
#     if(i<6):
#         lista.append(i-1)
#     elif(i>6):
#         lista.append(i-6)
#     else:
#         lista.append(0)
#     i += 1
# print(lista)

# 3a
# lista = [-4, 7, -3, 8]
# def ile_ujemnych(lista):
#     suma_ujemnych = 0
#     for i in lista:
#         if i<0:
#             suma_ujemnych += 1
#     return suma_ujemnych
#
# def iloczyn(lista):
#     liczba = 1
#     for i in lista:
#         liczba = liczba * i
#     return liczba
#
# def minmax(lista):
#     min=10
#     max=0
#     for i in lista:
#         if(i<min):
#             min = i
#         elif(i>max):
#             max = i
#     lista2=[]
#     lista2.append(min)
#     lista2.append(max)
#     return lista2
#
# def suma_przemienna(lista):
#     suma=0
#     pom=1
#     for i in lista:
#         if(pom%2==1):
#             suma=suma+i
#         else:
#             suma=suma-i
#         pom+=1
#     return suma
#
#
#
#
#
# def main():
#     lista = [-4, 7, -3, 8]
#     print(ile_ujemnych(lista))
# print(minmax(lista))
# print(suma_przemienna(lista))
# 7
# lista=[]
# def tw_listy(lista):
#     for i in lista:
#         a = input()
#         if not(a == lista[1:10]):
#             lista.append(a)
#         if len(lista) == 10:
#             break
# tw_listy(lista)
# print(lista)

lista = []
while len(lista) < 10:
    a=input()
    if not(a==lista[1:10]):
        lista.append(a)
print(lista)
