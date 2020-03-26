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
#    * Znajdź tytuły kilku najlepszych filmów
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