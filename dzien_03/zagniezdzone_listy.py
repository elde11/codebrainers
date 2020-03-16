nested = [
    [
        "Piotr",
    ],
    [ 
        "Max", "Karolina",
    ],
    [
        "Asia", "Kamila",
    ],
    [
        "Sabina", "Michal", "Grzesiek",
    ],
    [
        "Michal",
    ],
]
print(nested)
print(nested[-1])
print (nested[-2][1]) 
print (len(nested)) # liczba ławek
print(len(nested[-2]))

#nested.append ("Rafał") # dodawanie stringa do listy poprzez .append
nested[-1].append ("Rafał") # Rafał będzie siedział z ostatnim w tabeli czyli z Michałem
print (nested)
