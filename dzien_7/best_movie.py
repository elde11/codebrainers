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
    Number_best_movies = titles.append(reader(row)['title'])
    
    if entry["score"] > best_title:
        best_score = entry["score"]
        entry+= 1
        # najlepszy_film = entry["title"]

print(f"Najlepszy tytuł filmu RdN to:" {"title"},{best_score})