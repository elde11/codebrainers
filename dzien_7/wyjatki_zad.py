class MojWlasnyWyjatek(exception):

    # wywolali i obsluzyli nastepujace wyjatki
    # KeyError
    #ValueError 
    #AttributError

try:
    dictionary = dict()
    print (dictionary["prowadzący"])
except KeyError:
    print ("Błąd klucza")

try:
    int(input("Wprowadź liczbę:"))
except ValueError:
    print (" Nie wprowadziłeś poprawnej liczby")


try:
    "Piotr".capitalize
except AttributeError:
    print(" ten atrybut nie istnieje")