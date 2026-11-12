liczba = int(input("Liczba wierszy: "))
if liczba == 0:
    pass
else:
    print("Python 0")

for liczba in range(liczba-1):
    print(f"Python {2**(liczba+1)}")
