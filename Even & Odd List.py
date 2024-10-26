#You have been given a python list [10, 501, 22, 37, 100, 999, 87, 351]. Your task is to create two separate lists containing even and odd numbers.

list= [10, 501, 22, 37, 100, 999, 87, 351]
#utilizing list comprehension to break the lists into two

evenlist= [x for x in list if x%2==0]
oddlist = [x for x in list if x%2!=0]

print("Even List: ", evenlist)
print("Odd List: ", oddlist)
