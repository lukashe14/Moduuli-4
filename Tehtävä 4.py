import random
oikea_luku = random.randint(1,10)
while True:
    luku = int(input("Syötä arvaus:"))

    if luku == oikea_luku:
        print("Oikein!")
        break
    if luku > oikea_luku:
        print("Liian suuri arvaus:")
    if luku < oikea_luku:
        print("Liian pieni arvaus:")



