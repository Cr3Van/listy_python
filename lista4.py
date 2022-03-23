import random
import sys
# # zadanie 1
# lista = []
# for x in range(4):
#     lista.append(random.randint(0,30))
# print(lista)
# plik = open('wyniki.txt','w+')
# for x in lista:
#     x=x*2
#     plik.write(str(x))
#     plik.write(' ')
# plik.close()

#  zadanie 2
# with open('wyniki.txt','r')
# for linia in plik:
#     print(linia,end="")
# plik.close()

# zadanie 3
# zadanie 4
# class NaZakupy:
#     def __init__(self,nazwa_produktu,ilosc,jednostka_miary,cena):
#         self.nazwa_produktu = nazwa_produktu
#         self.ilosc = ilosc
#         self.jednostka_miary = jednostka_miary
#         self.cena = cena
#
#     def wyswietl_produkt(self):
#        return "Produkt: {} ilość: {} jednostka: {} cena: {} zł".format(self.nazwa_produktu,self.ilosc,self.jednostka_miary,self.cena)
#
#     def ile_produktu(self):
#         return "Ilosc twojego produktu to {} {} ".format(self.ilosc,self.jednostka_miary)
#     def ile_kosztuje(self):
#         return "Twoje zakupy kosztują {} zł".format(self.ilosc * self.cena)
#
# Ziemniak = NaZakupy('Ziemniaki' , 3 , 'kg' , 3)
# print(Ziemniak.wyswietl_produkt())
# print(Ziemniak.ile_produktu())
# print(Ziemniak.ile_kosztuje())

#zadanie 5
class ciagi_aryt:
    def __init__(self,a1,q,ilosc):
        self.a1 = a1
        self.q = q
        self.ilosc = ilosc

    def wyswietl_dane(self):
        return "Element pierwszy {} o ile zwiekszamy {} i ile ma elementow{}".format(self.a1,self.q,self.ilosc)

    def pobierz_parametry:
        print("Podaj pierwszy element")
        self.a1 = int(input())



    def policz_sume:
        suma = a1
        for i in ilosc
            a1=a1 + q
            suma = suma + a1
        return suma



class Robaczek:
    def __init__(self,x,y,krok):
        self.x = x
        self.y = y
        self.krok = krok

    def idz_w_gore(self,kroki=1):
        self.y += self.krok * kroki

    def idz_w_dol(self,kroki=1):
        self.y -= self.krok * kroki

    def idz_w_lewo(self,kroki=1):
        self.x -= self.krok * kroki

    def idz_w_prawo(self,kroki=1):
        self.x += self.krok * kroki

    def gdzie_jestes(self):
        return self.x,self.y

robak = Robaczek(0,0,1)
robak.idz_w_dol(2)
robak.idz_w_gore(4)
robak.idz_w_lewo(2)
robak.idz_w_prawo(3)
print(robak.gdzie_jestes())




