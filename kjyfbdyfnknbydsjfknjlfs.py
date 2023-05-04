#1.

cislo = int(input("Zadej cele cislo: "))

if cislo > 0:
    print("Cislo je kladne.")
elif cislo < 0:
    print("Cislo je zaporne.")
else:
    print("Cislo je nula.")

#2.
a = float(input("Zadejte první číslo: "))
b = float(input("Zadejte druhé číslo: "))
c = float(input("Zadejte třetí číslo: "))

if a > b and a > c:
    print("Největší číslo je", a)
elif b > a and b > c:
    print("Největší číslo je", b)
else:
    print("Největší číslo je", c) 
    #3.

vek = int(input("Zadej svůj věk: "))

if vek < 0:
    print("Věk nemůže být záporný.")
elif vek < 15:
    print("Jsi ještě moc mladý chlapec.")
elif vek >= 18 and vek <= 65:
    print("Už můžeš volit v prezidentských volbách.")
else:
    print("Jako jsi celkem děda a boomer.")

print()

#4.

import random

výhra = random.randint(1, 100)
pokusy = 5

print("Máš 5 pokusů na to, aby jsi uhádl/a číslo od 1 do 100.")

while pokusy > 0:
    hadane_cislo = int(input("Hádej číslo: "))
    if hadane_cislo == výhra:
        print("Gratuluji, uhádl/a jsi číslo na první pokus!")
        break
    elif hadane_cislo < výhra:
        print("Tvé hádané číslo je menší než výherní číslo.")
    else:
        print("Tvé hádané číslo")