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

# ZADANIA:
# Znajdź tytuł najgorszego filmu Roberta de Niro
#    * Znajdź tytuły kilku najgorszych filmów
# Znajdź tytuł najlepszego filmu RdN
#    * Znajdź tytuły kilku najlepszego filmów
# Znajdź średnią ocen filmów RdN
# * Znajdź medianę ocen filmów RdN
# * Znajdź rok, w którym RdN wydał najwięcej filmów

worst_score = 1000
worst_score = data[0]["score"]
for entry in data:
    if entry["score"] < worst_score:
        worst_score = entry["score"]
        # najgorszy_film = entry["title"]

print(f"Najgorsza ocena filmu RdN to: {worst_score}")


# Najgorszy tytuł filmu 


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

# ZADANIA:
# Znajdź tytuł najgorszego filmu Roberta de Niro
#    * Znajdź tytuły kilku najgorszych filmów
# Znajdź tytuł najlepszego filmu RdN
#    * Znajdź tytuły kilku najlepszego filmów
# Znajdź średnią ocen filmów RdN
# * Znajdź medianę ocen filmów RdN
# * Znajdź rok, w którym RdN wydał najwięcej filmów

worst_title = 1000
worst_title = data[0]["title"]
for entry in data:
    if entry["title"] < worst_title:
        worst_title = entry["title"]
        # najgorszy_film = entry["title"]

print(f"Najgorszy tytuł filmu RdN to: {worst_title}")




# tytuł najlepszego filmu 

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
for entry in data:
    if entry["title"] > best_title:
        best_title = entry["title"]
        # najlepszy_film = entry["title"]

print(f"Najlepszy tytuł filmu RdN to: {best_title}")


# Lista kilku najlepszych filmów RdN 

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

best_title = 90
best_title = data[0]["title"]  
best_score = data[0]["score"]      
Number_best_movies = []
liczba_filmow = 3

while len(Number_best_movies) < 3:
    Number_best_movies = data.append(["score"])
    if entry["score"] > best_title:
        best_title = entry["title"]
        Number_best_movies.append
        # najlepszy_film = entry["title"]

print(f"Najlepszy tytuł filmu RdN to: {best_title}")




# średnia arytmetyczna ocen

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

for entry in data:
    suma +=  entry["score"]
    liczba_elementów += 1

print(f"Średnia Arytmetyczna ocen filmów RdN to:", suma/liczba_elementów)
