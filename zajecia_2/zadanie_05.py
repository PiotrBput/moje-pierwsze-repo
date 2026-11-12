punkty = int(input("Liczba punktów: "))

if punkty >= 10:
    print("Zaliczone")
else:
    print("Niezaliczone")
    print("Brakuje punktów: ", 10-punkty)