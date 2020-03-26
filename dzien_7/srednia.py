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
    suma += entry["score"]
    liczba_elementów += 1

print(f"Średnia Arytmetyczna ocen filmów RdN to:",suma/liczba_elementów)
