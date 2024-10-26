#Write a Python program to calculate the total number of vowels and the count of each individual vowel a,e,i,o,u in the string "Guvi Geeks Network Private Limited"

input="Guvi Geeks Network Private Limited" 
#Given string input

val1=val2=val3=val4=val5=0 
#Each counter variable for the vowels is initialized at zero
#FOR loop to iterate through the string
for x in input:  
    if x=='a':   
        #If the condition is satisfied the vowels counters will be incremented.
        val1=val1+1
    elif x=='e':
        val2=val2+1
    elif x == 'i':
        val3=val3+1
    elif x=='o':
        val4=val4+1
    elif x=='u':
        val5=val5+1
# The counter variables holding the vowel count are printed
print ("The vowel values in the given statement are as below:") 
print('a=', val1)
print('e=', val2)
print('i=', val3)
print('o=',val4)
print('u=', val5)
