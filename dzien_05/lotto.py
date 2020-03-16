import random 

random.randint(1,49)
liczba_kulek = 6 
wylosowane_liczby =[]

while len(wylosowane_liczby) < 6:
    wylosowana = random.randint(1,49)
    if wylosowana not in wylosowane_liczby:
        wylosowane_liczby.append(wylosowana) # append dodaje wylosowane kulki do listy

print(wylosowane_liczby)