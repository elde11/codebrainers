#slowo = input("Wpisz slowo: ")
#czy_palindrom = True  # lub False
#for i in range(len(slowo)):
 #   if slowo[i] ...  slowo[-i - 1]:
  #      pass




slowo = input("Wprowadź słowo: ")
czy_palindrom = True
for i in range(len(slowo)):
    if slowo[i] != slowo[-i-1]:
        czy_palindrom = False 
        break

print(f"Palidrom: {czy_palindrom}")
if czy_palindrom:
    print("tak to jest palidrom")
else:
    print ("To nie jest palidrom")
        
        