tydzien = 7
dni = int(input("Ile dni ma tydzień? "))

if dni == tydzien:
    print("Poprawna odpowiedź")
else:
    dni = int(input("Druga próba: "))
    if dni == tydzien:
        print("Poprawna odpowiedź")
    else:
        print("Błędna odpowiedź")
    