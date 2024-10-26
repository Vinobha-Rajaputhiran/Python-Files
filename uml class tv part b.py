#Task: Part - B
#Inherit a TV class add additional properties like screen thickness, energy usage, Lifespan, Refresh rate, functionalities like viewingAngle, Backlight, DisplayDetails, which displays the detailed features of the TV
#Multiple Inheritance is used here

# Parent Class
class TV:
    def __init__(self, brand, OnOFF_status, channel, volume):
        self.price = 1500
        self.inches = 23
        self.channel=channel
        self.volume=volume
        self.brand = brand
        self.OnOFF_status= OnOFF_status

    def volume_change(self, value):
        if value<=100:
            self.volume=value
        elif value>self.volume:
            pass
        print("The current volume is", self.volume)

    def channel_change(self,value):
        if value<=50:
            self.channel=value
        elif value>self.channel:
            pass
        print("The current channel is", self.channel)

    def reset_settings(self):
        self.channel=1
        self.volume=50

    def status(self):
        print(self.brand, "at channel", self.channel, "and at volume",  self.volume)
#Objects defined with default parameters
set1=TV("Panasonic","On", 1,50)
set2=TV("Samsung","On", 1,50)

#Child Class One
class plasma(TV):
    def __init__(self, channel, volume, brand):
        self.screen='Wide'
        self.thickness= 24
        self.energy_usage='High'
        self.Lifespan= 'Low'
        self.Refresh_rate= 'Slow'
        self.channel = channel
        self.volume = volume
        self.brand = brand

    def viewingAngle(self):
        print("Viewing Angle is 180 degrees")
        
    def Backlight(self):
        print("Backlight is OFF")

    def DisplayDetails1(self):
        print("Volume:", self.volume, "Channel: ",self.channel, "Screen: ", self.screen, "Thickness: ", self.thickness, "Energy: ", self.energy_usage, "Lifespan: ", self.Lifespan, "Refresh_rate: ", self.Refresh_rate)

#Child Class Two
class LED(TV):
    def __init__(self, channel, volume, brand):
        self.screen='Flat'
        self.thickness= 32
        self.energy_usage='Low'
        self.Lifespan= 'High'
        self.Refresh_rate= 'Fast'
        self.channel = channel
        self.volume = volume
        self.brand = brand

    def viewingAngle(self):
        print("Viewing Angle is 90 degrees")
        
    def Backlight(self):
        print("Backlight is ON")

    def DisplayDetails2(self):
        print("Volume:", self.volume, "Channel: ",self.channel, "Screen: ", self.screen, "Thickness: ", self.thickness, "Energy: ", self.energy_usage, "Lifespan: ", self.Lifespan, "Refresh_rate: ", self.Refresh_rate)
#The Methods from parent class is called as below:
plasma1= plasma(23,5,'LG')
plasma1.channel_change(12)
plasma1.volume_change(150)
plasma1.status()
plasma1.DisplayDetails1()
print()
#Line Break for viewing purposes
LED1=LED(65, 77,'OnePlus')
LED1.volume_change(12)
LED1.channel_change(43)
LED1.status()
LED1.DisplayDetails2()
