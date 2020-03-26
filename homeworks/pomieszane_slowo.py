import random

lista = ["jeden","dwa","trzy"]

# Komputer losuje słowo z dostępnego zakresu (posiada listę słów). Wysosowane słowo jest nadal listą.
losuj = [random.choice(lista)]

# Zamieniam wylosowane słowo na stringa.
losuj_str = ''.join(losuj)

# Następnie litery są mieszane.
# Wymieszane litery pokazywane są graczowi.
print(''.join(random.sample(losuj_str,len(losuj_str))))

# Gracz musi zgadnąć co to za słowo. 
gracz = input("Podaj słowo: ")

# Gracz zgaduje do skutku. Dopiero zgadnięcie przerywa grę.
# Rozszerzenie: gracz może wybrać na klawiaturze „q” lub „Q”, aby zakończyć grę przed czasem.
while losuj_str != gracz:
    if gracz == "Q" or gracz == "q":
        print("Exit!")
        break
    else:
        print("Źle, jeszcze raz: ")
        gracz = input("Podaj słowo: ")
        
print("Dobrze!")