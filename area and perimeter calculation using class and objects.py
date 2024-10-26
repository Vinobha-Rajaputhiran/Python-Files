#Task: Using Python's OOP scheme complete the below tasks
#(a) Create a python class called Circle with Constructor which will take a list as an argument. The list is [10, 501, 22, 37, 100, 999, 87, 351]
#(b) Create proper member variable inside the task if re  quired and use them when necessary. For example for this task create a private class variable names pi=3.141.
#(c) From the given list create two class Methods Area and Perimeter. Use the methods to calculate the area and perimeter for the given list.
class Circle:

    def __init__(self): #Constructor with input list
        self.list = [10, 501, 22, 37, 100, 999, 87, 351]

    def area(self):
        __pi = 3.141 #Private variable assigned as pi
        area_list = []
        for radis in self.list: #iterate the list values and calulate area
            area_circle = radis * radis * __pi
            area_list.append(area_circle) #append the area values to new list
        return area_list

    def perimeter(self):
        __pi = 3.141
        perimeter_list = []
        for radis in self.list: #iterate the list values and calulate perimeter
            perimeter_circle = 2 * __pi * radis
            perimeter_list.append(perimeter_circle) #append the perimeter values to new list
        return perimeter_list


list_radius = Circle() #Object is defined
print("Returning Area of Values: ")
print(list_radius.area()) #The area method is called

print("Returning Perimeter of Values: ")
print(list_radius.perimeter()) #The perimeter method is called

