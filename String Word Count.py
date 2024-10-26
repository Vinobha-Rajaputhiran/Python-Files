#Write a program that takes a string and returns the number of words in it.

input= input("Enter the string: ") 
#Get input from user
words = input.split() 
#Using the split function break the string into a list of words at the presence of a space.
print("The number of words in the string: ", len(words)) 
#Print the length of the list to get the number of words in the string.
