# zadanie na wtorek 
# gra w zgadywanie liczb


#import random

#wylosowana_liczba = random.randint (1,100)

#tutaj daj zmienne dot. wygranej i liczby prób

#1.brak wygranej  
#2. nieprzekroczona liczba prób
#while (dwa_warunki)  

#pobranie danych od użytkownika
#musimy spr czy użytkownik zgadł
# a jeśli nie to napisać czy trafił za nisko czy za wysoko if - spr 3 sytuacje 
# pamiętaj o zwiększaniu liczby prób (+=)

#pass

# komunikat o przegranej lub wygranej 

import random

a = random.randint(1,30)
#guess = int(input("Zgadnij liczbę w zakresie od 1 do 30"))

while True:
    guess = int(input("Zgadnij liczbę w zakresie od 1 do 30"))
    if a == guess:
        print("Brawo, to ta liczba!")
        break
    else:
        print("Niestety, próbuj dalej")
        if guess > a:
            print("Twoja liczba jest większa")
        else:
            print("Twoja liczba jest mniejsza")
            continue




