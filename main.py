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
        listings = soup.find_all('div', class_='listing')

        # Iterate through each listing and extract relevant information
        for listing in listings:
            # Extract property title
            title = listing.find('h2', class_='title').text.strip()

            # Extract property price
            price = listing.find('span', class_='price').text.strip()

            # Extract property location
            location = listing.find('p', class_='location').text.strip()

            # Print the extracted information
            print(f"Title: {title}")
            print(f"Price: {price}")
            print(f"Location: {location}")
            print("--------------------------")
    else:
        print("Failed to retrieve webpage.")

# URL of the real estate listings page
url = 'https://www.zillow.com/homes/'

# Call the function to scrape real estate listings
scrape_real_estate_listings(url)
