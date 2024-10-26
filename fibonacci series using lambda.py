#Task: Using the Python Lambda function create a Fibonacci series from 1 to 50

n= int(input("Enter the range: "))

fib= lambda x: x if x<=1 else fib(x-1)+fib(x-2) 
#lambda function created
#example fib(2)--> fib(1)+fib(0) = 1+0 = 1

print("The Fibonacci series is: ")
#call the lambda function using the for loop to get the sequence required
for x in range(n):
    print(fib(x))
