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


suma = 0
liczba_elementów = 0

for i in data:
    suma += i
    liczba_elementów += 1

print(f"Średnia Arytmetyczna ocen filmów RdN to:", suma/liczba_elementów)






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


