#funnel("leave", "eave") => true
#funnel("reset", "rest") => true
#funnel("dragoon", "dragon") => true
#funnel("eave", "leave") => false
#funnel("sleet", "lets") => false
#funnel("skiff", "ski") => false




def funnel(slowo1, slowo2):
    for i in range(len(slowo1)):
        wyraz = slowo1[0:i]+slowo1[i+1:]
        if wyraz == slowo2:
            return True
    else: False
print()