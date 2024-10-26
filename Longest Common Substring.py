#Write a program that takes two strings and returns the longest common substring between them.

input1 = input('Enter the first string: ') 
#Get string1 from user
input2 = input('Enter the second string: ') 
#Get string2 from user
answer = ""  
#Assigned an empty string variable to append the common substring characters
len1, len2 = len(input1), len(input2)
for i in range(len1): 
    #FOR loop to iterate the characters in string1
    for j in range(len2): 
        #FOR loop to iterate the characters in string2
        temp=0
        match = ''
        while ((i+temp < len1) and (j+temp<len2) and   input1[i+temp] == input2[j+temp]): 
            #Condition to check if the iterate string characters are equal
            match = match+ input2[j+temp]
            temp = temp+1
        if (len(match) > len(answer)): 
            answer = match

print("The longest common substring is: ", answer) 
#Print the longest common substring
