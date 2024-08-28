oikea_käyttäjätunnus = "python"
oikea_salasana = "rules"
yritykset = 0
while yritykset < 5:
    käyttäjätunnus = input("käyttäjäntunnus:")
    salasana = input("salasana:")

    if käyttäjätunnus == oikea_käyttäjätunnus and salasana == oikea_salasana:
        print("Tervetuloa!")
        break
    else:
        yritykset += 1


    if yritykset == 5:
        print("Pääsy evätty!")
        break
