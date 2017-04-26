
# coding: utf-8

# In[1]:

import googlemaps
import pandas as pd
import numpy as np


# In[2]:

gmaps = googlemaps.Client(key = 'AIzaSyAXSxOd6vkVEYzmt_EAoR_H6XnqioeY9Ok')
gcode = googlemaps.Client(key = 'AIzaSyD2nDCH07GkK-aM1zTowtMaYhuLvOcJOFo')


# In[3]:

addrs = [ '1313 pagewynne drive, plano tx',
             'ut dallas',
            '2400 Preston Rd #200, Plano, TX 75093',
             '6121 W Park Blvd, Plano, TX 75093',
             '2300 Coit Rd, Plano, TX 75075',
             '3800 N Central Expy, Plano, TX 75074',
             '4757 W Park Blvd #108, Plano, TX 75093',
             '2109 W Parker Rd #210, Plano, TX 75023',
             '5901 Coit Rd, Plano, TX 75093',
             '710 W Renner Rd #220, Richardson, TX 75080']     
nn = len(addrs)


# In[4]:

location = np.empty([nn,2])
for ii in np.arange(nn):
    geocode_dict = gcode.geocode(addrs[ii])
    location[ii,0],location[ii,1] = geocode_dict[0]['geometry']['location']['lat'],geocode_dict[0]['geometry']['location']['lng']


# In[5]:

print(location)


# In[6]:

my_distance = gmaps.distance_matrix(addrs,addrs)


# In[7]:

distance_matrix = np.empty([nn,nn])
duration_matrix = np.empty([nn,nn])


# In[8]:

for ii in np.arange(nn):
    for jj in np.arange(nn):
        distance_matrix[ii,jj] = my_distance['rows'][ii]['elements'][jj]['distance']['value']
        duration_matrix[ii,jj] = my_distance['rows'][ii]['elements'][jj]['duration']['value']


# In[9]:

df_distance = pd.DataFrame(distance_matrix,index = addrs,columns = addrs)


# In[10]:

df_duration = pd.DataFrame(duration_matrix,index = addrs,columns = addrs)


# In[11]:

df_location = pd.DataFrame(location,index = addrs,columns = ['latitude', 'longitude'])


# In[12]:

df_location


# In[13]:

df_distance.to_csv('distance.csv')
df_duration.to_csv('duration.csv')
df_location.to_csv('location.csv')

