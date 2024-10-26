#Write a program that takes a string and returns True if it is an anagram of another string, False otherwise.

input1= str(input("Enter first string: ")) 
#Get string1 from user
input2= str(input("Enter second string: ")) 
#Get string2 from user

print("Are the two given strings Anagrams? ", end="")

if (sorted(input1) == sorted(input2)): 
        #counter() function can also be used here
        print("True")  
        #If the sorted instance of string 1 is equal to that of string 2 then strings are a palindrome of each other.
else:
        print("False")  
        #If the sorted instance of string 1 is not equal to that of string 2 then strings are not a palindrome of each other.

