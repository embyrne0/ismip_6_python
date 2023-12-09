import matplotlib.pyplot as plt
import cartopy
import cartopy.crs as ccrs
from cartopy import config
import cartopy.feature as cfeature
import netCDF4 as nc
from netCDF4 import Dataset



def Base_temp_VUW_PISM(ax, lon_UP, lat_UP, base_UP, label):
        UP_pcm = ax.pcolormesh(lon_UP, lat_UP, base_UP[0, :, :], transform=ccrs.PlateCarree(), cmap='viridis',
                         vmin=0, vmax=274)
        # Add colorbar with padding
        UP_bar = plt.colorbar(UP_pcm, ax=ax, label=label, pad=0.05)
        
def cartopy_basemap(lon=None, lat=None, base=None, label='Colorbar'):

    # Set the center coordinates for Greenland
    center_lon, center_lat = -40, 70

    # Create an Orthographic projection centered on Greenland
    projection = ccrs.Orthographic(central_longitude=center_lon,      central_latitude=center_lat)

    # Create a figure and axis with the Orthographic projection
    fig, ax = plt.subplots(subplot_kw={'projection': projection}, figsize=(10, 10))

    # Set the extent, Can use this as a *zoom method*
    ax.set_extent([-59, -25, 58, 84], crs=ccrs.PlateCarree())

    # Add coastlines, land features, and Gridlines
    ax.coastlines(zorder=1)
    ax.add_feature(cfeature.LAND, facecolor='tan', edgecolor='none')
    ax.gridlines(draw_labels=True, dms=True, x_inline=False, y_inline=False)

    # Set the extent, Can use this as a *zoom method*
    ax.set_extent([-59, -25, 58, 84], crs=ccrs.PlateCarree())

    # Adding labels so it doesn't cross into the map 
    ax.set_title('Basemap of Greenland', fontsize=14)
    ax.text(-0.07, 0.55, 'latitude', va='bottom', ha='center',
            rotation='vertical', rotation_mode='anchor',
            transform=ax.transAxes)
    ax.text(0.5, -.06, 'longitude', va='bottom', ha='center',
            rotation='horizontal', rotation_mode='anchor',
            transform=ax.transAxes)
    
    if lon is None or lat is None or base is None:
        plt.show()
    else: 
        Base_temp_VUW_PISM(ax, lon, lat, base, label)
        plt.show()
    