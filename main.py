#1,2
# def przedstaw(imie,nazwisko):
#     print(imie[0].capitalize()+'.'+nazwisko.capitalize())
# print("Podaj imie: ")
# imie = input()
# print("Podaj nazwisko: ")
# nazwisko = input()
# przedstaw(imie,nazwisko)

#3
#nieskonczone
# def ile_lat(a,b,wiek):
#     if(wiek>b):
#         a = a-1
#         b = (b+100) - wiek
#         rok_ur = str(a + b)
#     else:
#         b = b-wiek
#         rok_ur = str(a + b)
#     return rok_ur
#
# a = input("dwie pierwsze cyfry roku: ")
# b = input("dwie nastepne cyfry roku: ")
# wiek = input("Podaj wiek: ")
# print(ile_lat(a,b,wiek))
#


# 6
# suma = 0
# while (suma<100):
#     a = int(input())
#     suma = suma + a
#     print("aktualna suma:",suma)



#7
# a=input("podaj ilosc elementow listy")
# def kr(lista):
#     kr = tuple(lista)
#     return kr
# lista = []
# while len(lista) < a:
#     a = input()
#     lista.append(a)
#

# 9
# def dzien_tygodnia(a):
#     kr = ('Niedziela','Poniedzialek','Wtorek','Sroda','Czwartek','Piatek','Sobota')
#     return kr[a]
# a = int(input('Podaj nr dnia tygodnia:'))
# print(dzien_tygodnia(a))