luvut = []

while True:
    luku = input("Syötä luku:")



    if luku == "":
        break
    try:
        luku = int(luku)
        luvut.append(luku)
    except ValueError:
        print("Anna kelvollinen luku")

if luvut:
    print("Pienin luku on", min(luvut))
    print("Suurin luku on", max(luvut))
else:
    print("Et syöttänyt lukua")




