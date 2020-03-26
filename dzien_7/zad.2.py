# wyjdz z petli nieskonczonosc dopiero 
# po 3 wscinieciach

ctrl_c = 0

while True:
    try:
        print (end=")")
    except KeyboardInterrupt:
        ctrl_c += 1
        if ctrl_c >= 2:
            print("Koniec psot")
        break