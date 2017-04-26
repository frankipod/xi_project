
# coding: utf-8

# In[4]:

import googlemaps


# In[5]:

gmaps = googlemaps.Client(key = 'AIzaSyAXSxOd6vkVEYzmt_EAoR_H6XnqioeY9Ok')


# In[6]:

my_distance = gmaps.distance_matrix('Chicago','New York City')


# In[7]:

print(my_distance)


# In[101]:

home_addr = [ '1313 pagewynne drive, plano tx',
             'ut dallas',
            '2400 Preston Rd #200, Plano, TX 75093',
             '6121 W Park Blvd, Plano, TX 75093',
             '2300 Coit Rd, Plano, TX 75075',
             '3800 N Central Expy, Plano, TX 75074',
             '4757 W Park Blvd #108, Plano, TX 75093',
             '2109 W Parker Rd #210, Plano, TX 75023',
             '5901 Coit Rd, Plano, TX 75093',
             '710 W Renner Rd #220, Richardson, TX 75080']
 #            '2800 W 15th St, Plano, TX 75075',
#             '2925 Custer Rd, Plano, TX 75075',
#             'Market Plaza, 320 Coit Rd, Plano, TX 75075',
 #            '1101 Coit Rd, Plano, TX 75075',
#             '4608 W Plano Pkwy, Plano, TX 75093']

#             '7887 McCallum Blvd, Dallas, TX 75252',
 #            '2230 N Coit Rd, Richardson, TX 75080',
 #            '4899 Gramercy Oaks Dr, Dallas, TX 75287',
 #            ' 1600 Rio Grande Dr, Plano, TX 75075',
  #           '725 Synergy Park Blvd, Richardson, TX 75080'
             
            


# In[102]:

work_addr = ['2001 Rankin Rd, Houston, TX 77073','ut dallas']

len(home_addr)


# In[103]:

my_distance = gmaps.distance_matrix(home_addr,home_addr)


# In[104]:

print(my_distance)


# In[119]:


my_distance['rows'][3]['elements'][2]['distance']['value']


# In[134]:

nn = len(home_addr)
import numpy as np
distance_matrix = np.empty([nn,nn])
duration_matrix = np.empty([nn,nn])


# In[135]:

for ii in np.arange(nn):
    for jj in np.arange(nn):
        distance_matrix[ii,jj] = my_distance['rows'][ii]['elements'][jj]['distance']['value']
        duration_matrix[ii,jj] = my_distance['rows'][ii]['elements'][jj]['duration']['value']


# In[139]:

import pandas as pd


# In[140]:

df_distance = pd.DataFrame(distance_matrix,index = home_addr,columns = home_addr)


# In[142]:

df_duration = pd.DataFrame(duration_matrix,index = home_addr,columns = home_addr)


# In[143]:

df_duration


# In[146]:

df_distance.to_csv('distance.csv')
df_duration.to_csv('duration.csv')


# In[ ]:



