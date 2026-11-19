n = int(input("Liczba studentów: "))
suma = 0
wynik = int()
for i in range(1, n+1):
    wynik = int(input("Podaj wynik: "))
    
    while wynik > 100 or wynik < 0:
        print("Niepoprawny wynik")
        wynik = int(input("Podaj wynik:"))
    suma = suma + wynik
print("Suma:", suma)