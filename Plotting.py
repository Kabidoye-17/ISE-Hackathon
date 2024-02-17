import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

def plot_coordinates(longitudes, latitudes):
    plt.figure(figsize=(10, 6))

    # Create a map using Basemap
    m = Basemap(projection='merc', llcrnrlat=min(latitudes)-1, urcrnrlat=max(latitudes)+1,
                llcrnrlon=min(longitudes)-1, urcrnrlon=max(longitudes)+1, resolution='i')

    # Draw coastlines, countries, and states
    m.drawcoastlines()
    m.drawcountries()
    m.drawstates()

    # Convert latitude and longitude to map coordinates
    x, y = m(longitudes, latitudes)

    # Plot the points on the map
    m.scatter(x, y, marker='o', color='red', zorder=5)

    plt.title('Plotting Coordinates on Map')
    plt.show()

# Example coordinates (replace with your own list)
longitudes = [-6.2597, -6.2566, -6.2609]
latitudes = [53.3478, 53.3489, 53.3505]

# Plot the coordinates on a map
plot_coordinates(longitudes, latitudes)
