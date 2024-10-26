#You have been given a python list [10, 501, 22, 37, 100, 999, 87, 351]. The task is to create a new list containing all the prime numbers.


list= [10, 501, 22, 37, 100, 999, 87, 351]

primelist= []
#Emty list is created to append all the prime numbers.

#FOR loop will return all the prime values.
for x in list:

    if x==0 or x<=1:
        continue

    for y in range (2, x):
            if x%y==0:
                break
    else:
        primelist.append(x)
        #Prime numbers appended to empty list

print("Prime Numbers List: ", primelist)
