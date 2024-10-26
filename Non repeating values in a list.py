#Write a python program to find the non-repeating elements in a given list of integers.

list= list(input("Enter the list of values: "). split())
#Receive input list from user

list2=[]
#empty list

for x in list:
    count=0
    #counter set at zero. If the counter exceed zero, then the interger is a repeating.
    for y in list:
        if x==y:
            count=count+1
        if count>1:
            break

    if count==1:
        list2.append(x)
        #Append the non-repeating elements to empty output list

print("The list of non repeating values: ",list2)
