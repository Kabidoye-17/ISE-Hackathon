import requests
from bs4 import BeautifulSoup

def convert_price(price_string):
    price_string = price_string.replace(',', '')
    
    if 'per week' in price_string:
        weekly_price = int(price_string[1:price_string.index(' ')])
        monthly_price = weekly_price * 4
        return monthly_price
    elif 'per month' in price_string:
        monthly_price = int(price_string[1:price_string.index(' ')])
        return monthly_price
    else:
        return None
    

def remove_monthly(price_string):
    return price_string.replace('monthly', '').strip()


def scrape_real_estate_listings_daft(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url, headers=headers)


    if response.status_code == 200:

        soup = BeautifulSoup(response.content, 'html.parser')

        listings = soup.find_all('div', class_='Cardstyled__TitleBlockWrapper-nngi4q-5 bsQod')

        for listing in listings:
        
            price = listing.find('h3', class_='TitleBlock__StyledCustomHeading-sc-1avkvav-5 blbeVq').text.strip()

            location = listing.find('h2', class_='TitleBlock__Address-sc-1avkvav-8 dzihyY').text.strip()

            bedrooms = listing.find('p', class_='TitleBlock__CardInfoItem-sc-1avkvav-9 iLMdur').text.strip()

            property_type = listing.find('p', class_='TitleBlock__CardInfoItem-sc-1avkvav-9 cKZZql').text.strip()

            print(f"Price: {convert_price(price)}")
            print(f"Location: {location}")
            print(f"Bedrooms: {bedrooms}")
            print(f"property type: {property_type}" )
            print("--------------------------")
    else:
        print("Failed to retrieve webpage.")


def scrape_real_estate_listings_property(url):
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:

        soup = BeautifulSoup(response.content, 'html.parser')

        listings = soup.find_all('div', class_='search_result')

        for listing in listings:
        

            price = listing.find('div', class_='sresult_description').h3.text.strip()

            location = listing.find('div', class_='sresult_address').h2.a.text.strip()

            bedrooms = listing.find('div', class_='sresult_description').h4.text.strip()

        
            print(f"Price: {remove_monthly(price)}")
            print(f"Location: {location}")
            print(f"Bedrooms: {bedrooms}")
            print("--------------------------")
    else:
        print("Failed to retrieve webpage.")



daft_url = 'https://www.daft.ie/property-for-rent/limerick/houses'
propertyie_url = 'https://www.property.ie/property-to-let/limerick/'



scrape_real_estate_listings_daft(daft_url)
scrape_real_estate_listings_property(propertyie_url)



