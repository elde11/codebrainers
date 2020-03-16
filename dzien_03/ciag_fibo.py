x = int(input("podaj liczbę dla której obliczymy kod fibonacciego:  "))
x0=0
x1=1
if x == 0:
    print(0)
elif x == 1:
    print(1)
else:
    for element in range(1,x):
        x2=x1+x0
        x0=x1
        x1=x2
    print(x2)
    