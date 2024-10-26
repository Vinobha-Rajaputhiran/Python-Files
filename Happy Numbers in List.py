#You have been given a python list [10, 501, 22, 37, 100, 999, 87, 351]. Create a new list with the ahappy numbers.

input= [10, 501, 22, 37, 100, 999, 87, 351]
#Input list

HappyNumList=[]
#Empty list to append values.

#Function to filter out the happy numbers
def CheckHappyNumber(n):
    digit = sum = 0
    while (n > 0):
        digit = n % 10
        sum = sum + (digit * digit)
        n = n // 10
    return sum
#FOR loop to loop the values of the list to filter the happy numbers.
for x in input:
  result = x

  while (result != 1 and result != 4):
   result = CheckHappyNumber(result)

  if (result == 1):
    HappyNumList.append(x)

print("Happy Numbers List: ", HappyNumList)



