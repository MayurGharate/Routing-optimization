
import streamlit as st
import openrouteservice
import folium
from streamlit_folium import folium_static
from streamlit_geolocation import geolocation

st.set_page_config(page_title="Live Location Route Optimizer", layout="wide")
st.title("📍 Live Route Optimizer Using Your Browser Location")

# Initialize OpenRouteService client
client = openrouteservice.Client(key='5b3ce3597851110001cf6248fd384fc7d57149b19033e37efb7e90ec')

# Plant and shop locations
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

# Session state to store map
if "route_map" not in st.session_state:
    st.session_state["route_map"] = None

st.subheader("Step 1: Allow Browser Location Access")
location = geolocation()

if not location:
    st.info("🔒 Waiting for location permission. Please allow it in your browser.")
    st.stop()

current_coords = [location['lng'], location['lat']]  # [longitude, latitude]

st.success(f"📍 Your current location: {current_coords[1]}, {current_coords[0]}")

# Location selection
selected_keys = st.multiselect("Step 2: Select Destinations", list(locations_dict.keys()))

# Optimize button
if st.button("Step 3: Optimize Route") and len(selected_keys) >= 1:
    coordinates = [current_coords] + [locations_dict[key] for key in selected_keys]

    with st.spinner("Optimizing route..."):
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

# Show map if available
if st.session_state["route_map"]:
    folium_static(st.session_state["route_map"])
