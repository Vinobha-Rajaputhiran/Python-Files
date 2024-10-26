#Write a program that takes a string and returns the most frequent character in it.

input= str(input("Enter your string: ")) 
#Get input string from user
input1=list(input.replace(" ","")) 
#Utilized replace function to remove any spaces in the user input

print("The most common character in the string is: ", end="")

from collections import Counter 
#counter function is used to find the frequency of each character
ordered= Counter(input1)
print(ordered.most_common(1)[0][0]) 
#The first aka highest value is taken
