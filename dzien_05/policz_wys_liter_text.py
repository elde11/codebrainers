# uzyj dict
#policz wystapienie liter w tekscie


tekst = "ala ma kota, kot ma ale, a to jest kanapa pana kota"

counter = dict()

for a in tekst:
    if a in counter:
        counter[a] += 1
    else:
        counter[a] = 1
print (counter)


# opcja 2 : defaultdict
#import collections
from collections import defaultdict

counter2 =  defaultdict(int)
for a in tekst:
    counter2[a] += 1
print (counter2)


#3 opcja 

from collections import Counter

counter3 = Counter(tekst)
print(counter3)