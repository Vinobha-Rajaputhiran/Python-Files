#Task: Write a python function to read from a text file. The function will take the name of a text file and display its contents into the console.
def readfile(filename): 
    #Define function to read from text file
    f= open(filename,'r')
    print(f.read())
    f.close()

filename = input("Enter file name: ") 
#Enter the filename to be opened with .txt extension
readfile(filename) 
#Call function with the input file name
