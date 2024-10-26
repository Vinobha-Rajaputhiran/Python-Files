#Task: Write a Python code using the Lambda function to check every element of a list is an integer or string

input_list =[1,3,'guvi', 56, 'python', 67, 'selenium', 9.0] 
#Mixed input list with int and str

#lamda function to execute the given condition
result= lambda x: f"{x} is an integer" if type(x) is int\
    else f"{x} is a string" if type(x) is str \
    else f"{x} is not a defined data type"

for x in input_list: 
    #lamda function is called
    print(result(x))

