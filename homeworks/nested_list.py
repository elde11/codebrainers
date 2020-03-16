nested = [
    ["Piotr", ],
    ["Max", "Karolina", ],
    ["Asia", "Kamila", ],
    ["Sabina", "Michał", "Grzesiek", ],
    ["Michał", ],
    # <--
]

print(nested)
# print(nested[-1])
print(nested[-2][0])
print(len(nested))  # liczba ławek
print(len(nested[-2]))

nested[-1].append( "Rafał" )
print(nested)

# lista_wizytowka = [nazwisko, tytul]
# print(lista_wizytowka)
# nazwisko = "Piotr Banaszkiewicz"
# lista_wizytowka[0] = nazwisko

# print(lista_wizytowka)