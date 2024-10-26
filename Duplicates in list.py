#Write a python program to find the duplicate values in three user lists.

#Receive three input lists from the user.
list1= list(input("Enter the values of list 1: ").split())
list2= list(input("Enter the values of list 2: ").split())
list3= list(input("Enter the values of list 3: ").split())

#Using list comprehension to find the common values  between list1 and list 2 to create consolidated_list1
consolidated_list1= [x for x in list1 if x in list2]
#Using list comprehension to find the common values  between create consolidated_list1 and list 3 to create consolidated_list2 which contains the duplicate values.
consolidated_list2=[x for x in consolidated_list1 if x in list3]

print("The Duplicate Values in the lists are: ", consolidated_list2)
