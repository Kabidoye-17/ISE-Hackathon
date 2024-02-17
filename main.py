import requests
from bs4 import BeautifulSoup

def scrape_real_estate_listings(url):
    # Send a GET request to the URL
    #response = requests.get(url)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url, headers=headers)

   

    # Check if request was successful
    if response.status_code == 200:

        soup = BeautifulSoup(response.content, 'html.parser')

        listings = soup.find_all('div', class_='Cardstyled__TitleBlockWrapper-nngi4q-5 bsQod')

        for listing in listings:
        
            # Extract property price
            price = listing.find('h3', class_='TitleBlock__StyledCustomHeading-sc-1avkvav-5 blbeVq').text.strip()

            # Extract property location
            location = listing.find('h2', class_='TitleBlock__Address-sc-1avkvav-8 dzihyY').text.strip()

            #print(f"Title: {title}")
            print(f"Price: {price}")
            print(f"Location: {location}")
            print("--------------------------")
    else:
        print("Failed to retrieve webpage.")
# URL of the real estate listings page
url = 'https://www.daft.ie/property-for-rent/limerick/houses'

# Call the function to scrape real estate listings
scrape_real_estate_listings(url)
