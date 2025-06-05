#!/usr/bin/env python
# coding: utf-8

# In[2]:


import openrouteservice
from openrouteservice import convert
import folium


# In[3]:


client = openrouteservice.Client(key='5b3ce3597851110001cf6248fd384fc7d57149b19033e37efb7e90ec')


# In[11]:


locations_dict = {
    "Nashik - Plant 1":        [73.7795, 19.9425],
    "Nashik - Plant 2":        [73.7795, 19.9425],
    "Nashik - Tooling Centre": [73.7795, 19.9425],
    "Nashik - Die Shop":       [73.7649, 19.9315],

    "Pune - Chakan Plant":     [73.7085, 18.7557],
    "Pune - Vasuli Plant":     [73.7200, 18.7568],
    "Pune - Die Shop":         [73.7050, 18.7600],

    "Dewas Plant":             [76.1152, 22.9672]  # Dewas - routable road point
}


# In[12]:


print("Select locations to visit (comma-separated numbers):\n")
for key in locations_dict:
    print(key)


# In[6]:


input_str = input("\nEnter numbers (e.g., 1,3,5,7): ")
selected_indices = [int(i.strip()) for i in input_str.split(",")]


# In[7]:


selected_keys = [list(locations_dict.keys())[i - 1] for i in selected_indices]
coordinates = [locations_dict[key] for key in selected_keys]


# In[8]:


optimized = client.directions(
    coordinates=coordinates,
    profile='driving-car',
    optimize_waypoints=True,
    format='geojson'
)


# In[9]:


map_center = coordinates[0][::-1]
m = folium.Map(location=map_center, zoom_start=6)
folium.GeoJson(optimized).add_to(m)

for key in selected_keys:
    loc = locations_dict[key][::-1]
    folium.Marker(location=loc, popup=key).add_to(m)

m.save("user_selected_optimized_route.html")
print("\n✅ Route map saved as 'user_selected_optimized_route.html'")


# In[ ]:




