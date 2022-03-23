import random
#zadanie 4
# def czy_trpr(a,b,c):
#     if (a ** 2 + b ** 2 == c ** 2 or
#         a ** 2 + c ** 2 == b ** 2 or
#         b ** 2 + c ** 2 == a ** 2):
#         print("podany trojkat jest prostokatny")
#     else:
#         print("trojkat nie jest prostokatny")
#
# print("Podaj podstawy trojkata:")
# a=int(input())
# b=int(input())
# c=int(input())
# czy_trpr(a,b,c)
#zadanie2
# lista = []
# a=0
# for x in range(10):
#    lista.append(random.randint(0,100))
# print(lista)
# listaparz = [x for x in lista if x%2 == 0]
# print(listaparz)

#zadanie 1
# a = []
# for x in range(0,10):
#     a.append(x)
# print(a)
#
# b=[]
# for y in range(8):
#     b.append(4**y)
# print(b)
#
# c=[]
# for z in b:
#     if z%2 == 0:
#         c.append(z)
# print(c)

#zadanie 3
# a = {'mleko':'ml','mąka':'kg','ogorek':'sztuki','pomidory':'sztuki'}
# b = {key:value for key,value in a.items()if value=='sztuki'}
# print(b)


# #zadanie 7
# def il_el_ciagu (* liczby):
#     if len(liczby) == 0:
#         return 0
#     else:
#         iloczyn = 1
#         for x in liczby:
#             iloczyn *= x
#         return iloczyn
# print(il_el_ciagu(1,2,3,4))

# #zadanie 5
# def pole_trapezu(a=5,b=8,h=4):
#     return ((a+b)*h)/2
#
# print(pole_trapezu())

#zadanie 6
# def iloczyn_ciagu(a=1,b=4,ile=10):
#     suma=0
#     i=0
#     while(i<ile):
#         suma=suma+a
#         a=a*4
#         i=i+1
#     return suma
#
# print(iloczyn_ciagu())
