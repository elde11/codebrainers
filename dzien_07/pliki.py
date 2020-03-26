# 1. otwarcie pliku

open("przykladowy.csv,"r", encoding="utf-8")
# "r" read - odczyt pliku
# "w" write - zapisz do pliku od poczatku/ tworzenie pliku
# "a" append - zapis na koncu pliku/ 
#tworzenie 
# 2. dzialenie na pliku 
lines = f.readlines()
print(lines[0])
# 3. zamkniecie pliku
f.close()


with open("przykladowy.csv","r") as f:
    lines = f.readlines()
    print(lines[0])



    import csv
    with open("przykladowy.csv","r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(
                {
                    "year":int(row["Year"]),
                    "score": int(row["Score"]),
                    "title": row["Title"],
                }
            )

    print (data[0])


# srednia ocen filmow 
# mediana
#najgorszy film 
# szukamy najgorszego  filmu ,
# znajdz srednia
znajdz rok w ktorym robert 
#  jesli wiecej ich jest to mamy
# najlepszy film

najgorsza_ ocena = 1000
for entry in data:
    if entry["score"] < najgorsza_ocena:
        najgorsza_ocena = entry ["score"]
print (f"Najgorsza ocena filmu to: {najgorsza_ocena}")