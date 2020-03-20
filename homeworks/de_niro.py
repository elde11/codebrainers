# srednia arytmetyczna ocen



import csv


data = []

# otwarcie pliku
with open("przykladowy.csv", "r") as f:
    # DictReader pozwoli odczytywać dane z pliku CSV
    # i będzie je zwracał jako słowniki
    reader = csv.DictReader(f)

    # iterujemy po readerze
    for row in reader:
        # dokonujemy konwersji danych i dokładamy je na
        # koniec naszej listy
        data.append(
            {
                "year": int(row["Year"]),
                "score": int(row["Score"]),
                "title": row["Title"],
            }
        )

lista = [86,17,73,40,98,88,97,41,99,47,67,93,97,75,90,89,60,98,65,10,80,78,96,64,47,88,29,96,76,69,65,71,87,67,75,78,96,39,80,86,74,38,80,85,87,72,68,38,69,43,43,84,41,73,33,48,27,4,35,38,4,46,13,54,21
,76,19,51,46,72,10,50,25,7,70,92,51,29,46,7,29,11,9,60,26,61,11]
suma = 0
liczba_elementów = 0

for i in data:
    suma += i
    liczba_elementów += 1

print(f"Średnia Arytmetyczna ocen filmów RdN to:",suma/liczba_elementów)






# liczba najgorszych filmow de niro 


import csv

data = []
# otwarcie pliku
with open("przykladowy.csv", "r") as f:
    # DictReader pozwoli odczytywać dane z pliku CSV
    # i będzie je zwracał jako słowniki
    reader = csv.DictReader(f)

    # iterujemy po readerze
    for row in reader:
        # dokonujemy konwersji danych i dokładamy je na
        # koniec naszej listy
        data.append(
            {
                "year": int(row["Year"]),
                "score": int(row["Score"]),
                "title": row["Title"],
            }
        )

best_title = 100
best_title = data[0]["title"]        
Number_best_movie = 3
entry "score" in range (93,100): 

while len(Number_best_movie) < 3:
    Number_best_movie = data.append["score"]
    if entry["title"] > best_title:
        best_title = entry["title"]
        # najlepszy_film = entry["title"]

print(f"Najlepszy tytuł filmu RdN to: {best_title}")


