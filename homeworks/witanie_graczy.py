list = str(input('Podaj liste imion: '))

for i in list.split():
    for j in i.split(','):
        print('hi ' + j)