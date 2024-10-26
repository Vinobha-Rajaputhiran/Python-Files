#Task: Write a python program using function to create a text file with the current timestamp

f=open('task7.txt','x') 
#Create a text file using python
f.close()

def currenttimestamp(): 
    #function to get the current system time stamp
    import datetime 
    #Get time stamp using datetime module. Time module can also be used.
    ts= datetime.datetime.now()
    return ts.strftime("%I:%M:%S %p")  
    # Return the timestamp value

f= open('task7.txt', 'w')
f.write(currenttimestamp())
f.close()

