#Create a pyramid of numbers from 1 to 20 using FOR loop.
#Using FOR loop with the given range of values 20
for x in range(20): 
    for y in range(x+1): 
        # Nested FOR loop to iterate the pyramid shape for each line using the 'end' method.
        print(y + 1, end=" ")
    print()
