#Tuple ( z polskiego "Krostki")
T1 = ("Damian", "Lipniak")
print (T1)

T2 = ("Damian")

T3 = (
    "Michał",
    "Max",
    "Karolina"
    "Kamila"
)
print (T3)
print (T3[-1])
print(len(T3))

# "Rozbijanie" elementów

T1 = ("Damian", "Lipniak")
#imie = T1[0]
#nazwisko = T1[1]

imie, nazwisko = T1
print (imie, nazwisko)


#Słownik- typ mapujący, typ haszujący

D1 = {
    'klucz': 'wartosc',
    123: 'Student',
    (0, 0, 7): 'Bond. James Bond.',
    }
print (D1)
print (D1['klucz'])
print (D1[123])
print (D1[ (0, 0, 7) ])

print (list(D1. keys())[1])
print (list(D1. values())[2])
print ("*" * 20)
print (list (D1.items()))

#zbiór (set) 
Z1 = {1, 9, 3, 4, 1, 2, 3, 46, 1, 2, 3, 4}
print (Z1)