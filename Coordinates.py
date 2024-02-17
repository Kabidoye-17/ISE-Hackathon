from geopy.geocoders import GoogleV3

def get_coordinates(address, api_key):
    geolocator = GoogleV3(api_key=api_key)
    location = geolocator.geocode(address)
    print(dir(location))

    if location:
        return location.latitude, location.longitude
    else:
        return None, None

# Provide your API key here
api_key = "AIzaSyAoQChLOeVRGbFAkCQ6trSiETUTBeWPYAQ"

addresses = [
    "Apartment A, 2a Jamestown Road, Dublin 8, Inchicore, Dublin 8",
    "11 Dunville Avenue, Ranelagh, Ranelagh, Dublin 6",
    "128 Lansdowne Park, Ballsbridge, Ballsbridge, Dublin 4"
]

for address in addresses:
    latitude, longitude = get_coordinates(address, api_key)
