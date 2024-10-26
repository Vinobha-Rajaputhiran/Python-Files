#Write a Python program to find the minimum element in a rated and sorted list.

list= list(input("Enter the list of elements: ").split())
#Receive list input from user.

newlist= sorted(list)
#Utilizing the sorted method to sort the user list in ascending order.

print("The minimum element in the given list is: ", newlist[0])
#The index value of 0 contains the minimum element in the list.
