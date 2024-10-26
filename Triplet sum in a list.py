#You have been given a Python list [10,20, 30,9] and a value of 59. Write a python program to find the triplet in the list whose sum is equal to the given value.

list= [10,20, 30,9]
#The input list and value are initialized.
value=59
counter=0

#Using FOR  loop to iterate through different possibilities to find the triplet values that sum upto 59.
for x in list:
    if counter==1:
        break
    else:
        for y in list:
            if counter == 1:
                break
            else:
              for z in list:
                 if x+y+z==value:
                   print("The Triplets in the list with a sum value equal to 59 is: ",x,y,z)
                   counter=counter+1
                   break

