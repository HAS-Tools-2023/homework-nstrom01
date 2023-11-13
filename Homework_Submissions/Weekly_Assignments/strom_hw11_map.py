#%%
import matplotlib.pyplot as plt
import matplotlib as mpl 
import pandas as pd 
import numpy as np
import geopandas as gpd
import fiona
from shapely.geometry import Point
import contextily as ctx
import os 
#%% Creating variables for the data of plotting interest

huc8 = gpd.read_file(os.path.join('../Week 11/arizona_huc8_shapefile', 'WBDHU8.shp'))
AZ_state = gpd.read_file(os.path.join('../Week 11/arizona_shapefile', 'tl_2016_04_cousub.shp'))

land_sub_az = gpd.read_file(os.path.join('../Week 11/Land_Subsidence', 'Land_Subsidence.shp'))
land_sub_az = land_sub_az.to_crs(AZ_state.crs) 
    # changing the coordinate system of land_sub_AZ to same as other shapes

recharge_sites_AZ = gpd.read_file(os.path.join('../Week 11/Recharge AZ', 'Recharge.shp'))
recharge_sites_AZ = recharge_sites_AZ.to_crs(AZ_state.crs) 
    # changing the coordinate system of land_sub_AZ to same as other shapes

file_H = os.path.join('../Week 11/WBD_15_HU2_GDB', 'WBD_15_HU2_GDB.gdb')
#fiona.listlayers(file_H)

WBDLine = gpd.read_file(file_H, layer = "WBDLine")
HU8 = gpd.read_file(file_H, layer = "WBDHU8")
super_fund = os.path.join('../Week 11', 'SuprFundSite_Boundaries.gdb')
#fiona.listlayers(super_fund)

polygon_sf_bounds = gpd.read_file(super_fund, layer = "OU_BOUNDARIES_SF")
sf_site_points = gpd.read_file(super_fund, layer = "SITE_FEATURE_POINTS_SF")
#%%

#%%
populDense_cities_AZ = np.array([[-112.0740, 33.4484], 
                                 [-110.9742,32.2540],
                                 [-111.8315, 33.4152],
                                 [-111.8413, 33.3062],
                                 [-111.7890, 33.3528]])
pop_AZ_cities = gpd.GeoDataFrame([Point(xy) for xy in populDense_cities_AZ], 
                            columns=['geometry'],
                            crs=AZ_state.crs)
#%%
def plotlayer(layer_name, color_of_interest = 'green'): 
    """ Used to quickly view the viual attributes of a .shp file
        Input: a dataset layer that has been read in and defined
                enter the name of the defined layer of interest and 
                desired color of the plot
    
        Returns: a single layer visual plot of your layer"""
    fig, ax = plt.subplots(figsize=(10, 10))
    layer_name.plot(ax=ax, color = color_of_interest)
    ax.set_title('plot')
    plt.show()
#%%
def plot_GDB_layer(file_name, layer_name):
    """ Used to quickly view the viual attributes of a .gdb file
        Input: a GDB dataset layer that has been read in and defined
                enter the name of the defined embedded GDB layer of interest and 
                desired color of the plot
    
        Returns: a single layer visual plot of your layer"""
    x = gpd.read_file(file_name, layer = layer_name)
    fig, ax = plt.subplots(figsize=(10, 10))
    x.plot(ax=ax)
    ax.set_title(layer_name)
    plt.show()
#%%
#plotlayer(huc8)
#plotlayer(AZ_state)
#plot_GDB_layer(file_H,'WBDLine')
#%%

fig, ax = plt.subplots(figsize = (10,10))

land_sub_az.plot(ax=ax, color='purple', hatch = '/////', edgecolor='yellow', label='land sub',zorder = 3, alpha = 0.6)
AZ_state.plot(ax=ax, color='red', edgecolor='black', label='AZ state', alpha =.2)
HU8.plot(ax=ax, color = 'blue', alpha = .2)
recharge_sites_AZ.plot(ax=ax, color = 'blue', zorder = 4, alpha =.8)
pop_AZ_cities.plot(ax=ax, color = 'red', zorder = 5, markersize =15, edgecolor = 'black')



ax.set_title('Locations of Signifcant Land Subsidence in AZ and Groundwater Recharge Areas')


ctx.add_basemap(ax,crs=AZ_state.crs.to_string())

plt.legend(['Top 5 most populated AZ Cities'])
plt.show()


#%%
# recharge data: https://uair.library.arizona.edu/item/292543/browse-data/Water?page=1
# land subsidence data: https://gisdata2016-11-18t150447874z-azwater.opendata.arcgis.com/datasets/azwater::land-subsidence/explore?location=33.335434%2C-111.650169%2C7.99

