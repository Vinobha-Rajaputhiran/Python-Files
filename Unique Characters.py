#Write a program that tales a string and returns the number of unique characters in it.

input= str(input("Enter a string: ")) 
#Get input value from user
input2 = input.replace(' ', '') 
#removing space in the input string using the replace function
x= set(input2) 
#converting the string to set data type as set does not accept duplicate values
print('The number of unique character: ', len(x)) 
#Printing the length of the set x which contains the unique characters of the input string.
