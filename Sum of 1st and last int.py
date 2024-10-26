#Write a python program to find the sum of the first and last digit of an integer.

input= int(input("Enter the integer: "))
#Receive input from usesr

str_input = str(input)
#Convert the integer to string to fix index numbers.

sum = int(str_input[0]) + int(str_input[-1])
#Add the integer values of the first and last indexes of the string to get the solution.

print("The sum of the first and last digit of the integer are: ", sum)
