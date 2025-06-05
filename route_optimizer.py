#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import openrouteservice
import folium
from streamlit_folium import st_folium


# In[4]:


client = openrouteservice.Client(key="5b3ce3597851110001cf6248fd384fc7d57149b19033e37efb7e90ec")


# In[5]:


locations_dict = {
    "Chennai":        [80.2707, 13.0827],
    "Bengaluru":      [77.5946, 12.9716],
    "Hyderabad":      [78.4867, 17.3850],
    "Coimbatore":     [76.9558, 11.0168],
    "Mumbai":         [72.8777, 19.0760],
    "Pune":           [73.8567, 18.5204],
    "Ahmedabad":      [72.5714, 23.0225],
    "Nagpur":         [79.0882, 21.1458],
    "Kolkata":        [88.3639, 22.5726],
    "Visakhapatnam":  [83.2185, 17.6868],
}

st.title("🧭 Route Optimization Tool")
st.subheader("Select Locations to Visit:")


# In[8]:


selected_locations = st.multiselect(
    "Choose locations in the order you'd like to visit (min 2):",
    list(locations_dict.keys())
)


# In[9]:


if len(selected_locations) >= 2:
    coordinates = [locations_dict[loc] for loc in selected_locations]


# In[16]:


try:
    optimized = client.directions(
        coordinates=coordinates,
        profile='driving-car',
        optimize_waypoints=True,
        format='geojson'
    )

    # Create map
    m = folium.Map(location=coordinates[0][::-1], zoom_start=6)
    folium.GeoJson(optimized).add_to(m)

    for loc in selected_locations:
        folium.Marker(locations_dict[loc][::-1], popup=loc).add_to(m)

    st.success("✅ Optimized route generated below:")
    st_folium(m, width=725)

except Exception as e:
    st.error(f"Error during optimization: {e}")
else:
 st.warning("Please select at least two locations to proceed.")


# In[ ]:


get_ipython().system('streamlit run route_optimizer.py')


# In[ ]:




