#for element in range(2,17):
   # print(element, "kwadrat to", element**2)

#for element in range(1,101):
    #if element % 15 == 0:
        #print(element, "FizzBuzz")
    #elif element % 3 == 0:
        #print(element, "Fizz")
    #elif element % 5 == 0:
        #print(element, "Buzz")
    #else:
       # print(element)


for element in range(1,101):
    if element % 3 == 0 and element % 5 !=0:
        print(element, "Fizz")
    elif element % 5 == 0 and element % 3 !=0:
        print(element, "Buzz")
    elif element % 15 == 0:
        print(element, "FizzBuzz")
    else:
        print(element)
