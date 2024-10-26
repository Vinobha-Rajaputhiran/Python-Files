#Write a program that takes a string and returns True if its a Palindrome and False, otherwise.

val1= input("Enter the string: ") 
#Get input from user        
val2= val1[::-1] 
#Reverse the string 
print("Is the string palindrome?")
if val1 == val2: 
    #IF statement to check if the reversed string is identical to the user input string.
    print("True") 
    #If the condition is satisfied, the user string is a Palindrome
else:
    print("False") 
    #If the condition is not satisfied, the user string is not a Palindrome
