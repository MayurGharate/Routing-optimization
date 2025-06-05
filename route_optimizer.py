#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import openrouteservice
import folium
from streamlit_folium import folium_static
from streamlit_js_eval import streamlit_js_eval

st.set_page_config(page_title="Route Optimizer with Live Location", layout="wide")
st.title("📍 Route Optimizer with Browser Geolocation")

client = openrouteservice.Client(key='5b3ce3597851110001cf6248fd384fc7d57149b19033e37efb7e90ec')

locations_dict = {
    "Nashik - Plant 1":        [73.7795, 19.9425],
    "Nashik - Plant 2":        [73.7795, 19.9425],
    "Nashik - Tooling Centre": [73.7795, 19.9425],
    "Nashik - Die Shop":       [73.7649, 19.9315],
    "Pune - Chakan Plant":     [73.7085, 18.7557],
    "Pune - Vasuli Plant":     [73.7200, 18.7568],
    "Pune - Die Shop":         [73.7050, 18.7600],
    "Dewas Plant":             [76.1152, 22.9672]
}

if "route_map" not in st.session_state:
    st.session_state["route_map"] = None

st.subheader("Step 1: Allow Access to Your Current Location")
location = streamlit_js_eval(js_expressions="navigator.geolocation.getCurrentPosition((pos) => pos.coords)", key="get_location")

if location is None:
    st.info("🔒 Waiting for location permission... Please allow location access in your browser.")
    st.stop()

current_coords = [location['longitude'], location['latitude']]

selected_keys = st.multiselect("Step 2: Select Locations to Visit", list(locations_dict.keys()))

if st.button("Step 3: Optimize Route") and len(selected_keys) >= 1:
    coordinates = [current_coords] + [locations_dict[key] for key in selected_keys]

    with st.spinner("Optimizing route using OpenRouteService..."):
        optimized = client.directions(
            coordinates=coordinates,
            profile='driving-car',
            optimize_waypoints=True,
            format='geojson'
        )

        map_center = current_coords[::-1]
        m = folium.Map(location=map_center, zoom_start=6)
        folium.GeoJson(optimized).add_to(m)

        ordered_indices = optimized["properties"]["way_points"]
        ordered_keys = ["Current Location"] + selected_keys
        for i, idx in enumerate(ordered_indices):
            loc = coordinates[idx][::-1]
            label = f"{i+1}. {ordered_keys[idx]}"
            icon_color = "green" if idx == 0 else "blue"
            folium.Marker(location=loc, popup=label, tooltip=label,
                          icon=folium.Icon(color=icon_color)).add_to(m)

        st.session_state["route_map"] = m
        st.success("✅ Route optimized and displayed on the map.")
elif st.button("Step 3: Optimize Route"):
    st.warning("Please select at least one destination.")

if st.session_state["route_map"]:
    folium_static(st.session_state["route_map"])


# In[ ]:




