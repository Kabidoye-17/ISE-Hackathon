import requests
from bs4 import BeautifulSoup

def scrape_real_estate_listings(url):
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

            address = houses.find('div', class_='sresult_address').h2.a.text.strip()
        
            price = houses.find('h4').text.strip()
            
            bedrooms = houses.find('h3').text.strip()
            
            print(f"address: {address}")
            print(f"Price: {price}")
            print(f"bedrooms: {bedrooms}")
            print("--------------------------")
    else:
        print("Failed to retrieve webpage.")

# URL of the real estate listings page
url = 'https://www.rent.ie/houses-to-let/renting_dublin/south-dublin-city/'

# Call the function to scrape real estate listings
scrape_real_estate_listings(url)