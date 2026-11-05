imie = input("Imie: ")
cz1 = int(input("Punkty z pierwszej części: "))
cz2 = int(input("Punkty z drugiej części: "))

if (cz1>=5) and (cz2>=5) and (cz1 + cz2 >= 15):
    print("Student: ", imie)
    print("Suma: ", cz1 + cz2)
    print("Status: Zaliczone")
else:
    print("Student: ", imie)
    print("Suma: ", cz1 + cz2)
    print("Status: Niezaliczone")