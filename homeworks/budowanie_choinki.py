cnt = int(input('Podaj rozmiar choinki: '))

for i in range(0, cnt):
    for j in range(0, i + 2):
        for k in range(0, j + 1):
            print('#', end='')
        print()