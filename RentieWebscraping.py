import requests
from bs4 import BeautifulSoup
import re
import csv

def write_to_csv(propertyInformation):
    file_path = 'csvFiles/rentIEInformation.csv'
    propertyInformationString = ", ".join(propertyInformation)
    print(propertyInformationString)
    
    try:
        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([propertyInformationString])
            print("String has been written to", file_path)
    except IOError as e:
        print("There was an error writing to the file:", e)

def scrape_rent_ie(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if request was successful
    if response.status_code == 200:
        
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all the listings on the page
        Searchresults = soup.find_all('div', class_='search_result')
        
        # Iterate through each listing and extract relevant information
        for houses in Searchresults:
            # Will store the information
            propertyInformation = []
            # full addresss
            addresses = houses.find('div', class_='sresult_address').h2.a.text.strip()
            propertyInformation.append(str(addresses))
            print(addresses)

            # price per month
            price = houses.find('h4').text.strip()
            pricePattern = r"€([0-9,]+)"
            pricePerMonthMatches = re.findall(pricePattern, price)
            pricePerMonth = int((pricePerMonthMatches[0]).replace(",",""))
            propertyInformation.append(str(pricePerMonth))
            print(pricePerMonth)
            
            # Gets Lines of Bedrooms and Bathrooms
            bedroomsAndBathrooms = houses.find('h3').text.strip()
            
            # Gets Bedrooms
            
            bedroomPattern = r"(\d+)\s*bedroom"
            bedmatch= re.search(bedroomPattern, bedroomsAndBathrooms)
            
            # Checks if there is bedrooms (May be a studio)
            numOfBedrooms = None
            if bedmatch:
                numOfBedrooms = bedmatch.group(1)
            else:
                numOfBedrooms = -1
            propertyInformation.append(str(numOfBedrooms))
            print(numOfBedrooms)
                
            # Gets Bathrooms
            bathroomPattern = r"(\d+)\s*bathroom"
            bathmatch= re.search(bathroomPattern, bedroomsAndBathrooms)
            
            # checks if there is bathrooms (may be a studio)
            numOfBathrooms = None
            if bathmatch:
                numOfBathrooms = bathmatch.group(1)
            else:
                numOfBathrooms = -1
            propertyInformation.append(str(numOfBathrooms))
            print(numOfBathrooms)
            
            write_to_csv(propertyInformation)
            
    else:
        print("Failed to retrieve webpage.")

    
        
# URL of the real estate listings page
url = 'https://www.rent.ie/houses-to-let/renting_dublin/'

# Call the function to scrape real estate listings
scrape_rent_ie(url)