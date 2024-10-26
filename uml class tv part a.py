#Task: Part - A
#Create a TV class with properties like brand, channel, price, inches, OnOFF status, and volume. Specify the brand in a constructor parameter. The channel should be 1 by default. Volume should be 50 by default.
#Add methods to increase and decrease volume. Volume can't never be below 0 or above 100.
#Add a method to set the channel. Let's say the TV has only 50 channels so if you try to set channel 60 the TV will stay at the current channel.
#Add a method to reset TV so it goes back to channel 1 and volume 50. (Hint: consider using it from the constructor).
#It's useful to write a status that returns info about the TV status like: "Panasonic at channel 8, volume 75".
class TV:
    def __init__(self, brand, OnOFF_status, channel, volume):
        #Constructor with initialized variables
        self.price = 1500
        self.inches = 23
        self.channel=channel
        self.volume=volume
        self.brand = brand
        self.OnOFF_status= OnOFF_status
    #Methods added to change volume& channel, reset settings and display the status of the changes made
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

set1.volume_change(23)
set1.channel_change(35)
set1.status()

set2.volume_change(125)
set2.channel_change(52)
set2.status()

