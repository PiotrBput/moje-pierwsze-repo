n = 0
liczba = int(input("Liczba wierszy: "))

if liczba == 0:
    pass
else:
    print("Python 0")

while n < liczba-1:
    print(f"Python {2**(n+1)}")
    n = n +1