wiek = int(input("podaj mi swój wiek:"))
plec = input ("podj swoją płeć [K/M]: ")
plec = plec[0].upper() #obcinamy słowo wprowadzone do pierwszej litery Mężczyzna czyli będziemy analizować M 

if plec == 'K':
    wiek_emerytalny = 60
else:
    wiek_emerytalny = 65

if 18 <= wiek < wiek_emerytalny:
    print ("Musisz pracować")
    print ("taki mamy klimat")

elif wiek < 18:
    print("ucz się, młokosie")

elif wiek >= wiek_emerytalny:
     print("Gratulujemy emerytury, -ZUS")

else:
    print ("Dziwna sytuacja, nie przewidziałem tego...")

#print ("Po ifie")

# (Nie) jawna konwersja do typu logicznego
# lista = []
# if lista:
#     pass

# print(bool(lista))

print(bool(""))
print(bool("Damian"))

#operatory logiczne
# not
# and
# or 
