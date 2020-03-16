#pętla
# while

index = 0

while index < 10:
    print(f"Hello World x{index}")
    index += 1
    # index = index + 1

#for
kolekcja = {
    'Linux': "Michał", 
    "Web": "Piotr",
    "OOP": "Artur",
}
for klucz, wartosc in kolekcja.items():
    print(klucz, wartosc)


lista = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for liczba in lista:
    print(liczba, liczba**2, liczba**(1/2))


lista = ["Jakub", "Piotr", "Piotr", "Artur"]
for klucz, wartosc in enumerate(lista):
    print(klucz + 2, wartosc)


    

