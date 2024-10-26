#Write a program that takes a string and returns a new string with all the vowels removed.
#Enter the user input statement
input = input('Enter the statement: ')
for x in input: 
    #FOR loop to iterate the input string 
    if x!='a' and x!='e' and x!='i' and x!='o' and x!='u' and x!='A' and x!='E' and x!='I' and x!='O' and x!='U': 
        #IF condition to print non-vowel strings
        print(x, end='')
