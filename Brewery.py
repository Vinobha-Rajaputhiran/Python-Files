""""
Using the URL https://restcountries.com/v3.1/all wirte a python program which will do the following.
    1. List the names of all breweries present in the states of Alaska, Maine and New York.
    2. What is the count of breweries in each of the states mentioned above?
    3. Count the number of types of breweries present in the states mentioned above?
    4. Count and list how many breweries have websites in the states of Alaska, Maine and New York.
"""

import requests
# requests module is imported to work with api data

#Method to create appropriate link using the user input state name
def create_url(state_name):
    state_name = state_name.lower().replace(" ","_")
    url= "https://api.openbrewerydb.org/v1/breweries?by_state="+state_name
    return url

class Breweries:
    #Constructor for Breweries class
    def __init__(self, url):
        self.url = url
        self.brewery_list = []
        self.brewery_type = []
        self.brewery_websites=[]

    #Method to get API CODE
    def api_status_code(self):
        response = requests.get(self.url)
        return response.status_code

    #Method to get the data from the URL link
    def fetch_api_data(self):
        if self.api_status_code() == 200:
            return requests.get(self.url).json()
        else:
            return "ERROR-404"

    #Method to get the list of names of the breweries in the state
    def fetch_brewery_names(self):
        if self.api_status_code() == 200:
            brewery_data = self.fetch_api_data()
            for brewery in brewery_data:
                    self.brewery_list.append(brewery['name'])
            return self.brewery_list
        else:
            return "ERROR-404"

    #Method to get the count of the breweries in the state
    def count_of_brewery(self):
        if self.api_status_code() == 200:
            brewery_list=self.fetch_brewery_names()
            return len(brewery_list)

    #Method to get the list and count of brewery websites in the state
    def count_brewery_websites(self):
        if self.api_status_code() == 200:
            brewery_data=self.fetch_api_data()
            for brewery in brewery_data:
                if brewery['website_url'] != None:
                    self.brewery_websites.append(brewery['website_url'])
            return self.brewery_websites

    #Method to get the count of the types of breweries in the state
    def types_of_brewery(self):
        if self.api_status_code() == 200:
            brewery_data=self.fetch_api_data()
            for brewery in brewery_data:
                if brewery['brewery_type'] not in self.brewery_type:
                    self.brewery_type.append(brewery['brewery_type'])
            return len(self.brewery_type)
        else:
            return "ERROR-404"



if __name__ == '__main__':
    state_name = str(input("Enter the state name: "))
    #The State Names: Alaska, Maine, New York
    brew=Breweries(create_url(state_name))

    print(f"The List of Breweries in {state_name} is: \n")
    for names in brew.fetch_brewery_names():
        print(names)

    print(f"The Count of Breweries in {state_name} is: {brew.count_of_brewery()}\n")

    print(f"The Count of Types of Breweries in {state_name} is: {brew.types_of_brewery()}\n")

    print(f"The List of Breweries websites in {state_name} is: \n")
    for websites in brew.count_brewery_websites():
        print(websites)

    print(f"The Count of Breweries with websites in {state_name} is: {len(brew.count_brewery_websites())}\n")
