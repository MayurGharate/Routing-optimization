
import streamlit as st
from st_bridge import bridge, html
import openrouteservice
import folium
from streamlit_folium import folium_static

st.set_page_config(page_title="📡 Debug GPS Tracker", layout="wide")
st.title("📡 Real-Time GPS Debug with streamlit-bridge")

# Setup OpenRouteService client
client = openrouteservice.Client(key='5b3ce3597851110001cf6248fd384fc7d57149b19033e37efb7e90ec')  # Replace with actual API key

locations_dict = {
    "Nashik - Plant 1": [73.7795, 19.9425],
    "Nashik - Plant 2": [73.7795, 19.9425],
    "Nashik - Tooling Centre": [73.7795, 19.9425],
    "Nashik - Die Shop": [73.7649, 19.9315],
    "Pune - Chakan Plant": [73.7085, 18.7557],
    "Pune - Vasuli Plant": [73.7200, 18.7568],
    "Pune - Die Shop": [73.7050, 18.7600],
    "Dewas Plant": [76.1152, 22.9672]
}

# Get location from browser via bridge
st.subheader("Step 1: Allow browser GPS and confirm popup appears")

data = bridge("location-bridge", default="no data yet")

# Inject JS with alert to confirm it's firing
html("""
<script>
navigator.geolocation.getCurrentPosition(function(position) {
    const coords = position.coords.latitude + "," + position.coords.longitude;
    alert("📍 GPS Location Detected: " + coords);  // DEBUG: Popup
    window.top.stBridges.send("location-bridge", coords);
});
</script>
""", iframe=False)

# Show raw data for debug
st.code(f"📡 Raw location data: {data}", language="text")

if data != "no data yet" and "," in data:
    lat, lon = map(float, data.split(","))
    current_coords = [lon, lat]
    st.success(f"✅ Parsed Location: {lat:.5f}, {lon:.5f}")

    selected_keys = st.multiselect("Step 2: Select Destinations", list(locations_dict.keys()))

    if st.button("Step 3: Optimize Route") and selected_keys:
        coordinates = [current_coords] + [locations_dict[k] for k in selected_keys]
        with st.spinner("Optimizing route..."):
            optimized = client.directions(
                coordinates=coordinates,
                profile='driving-car',
                optimize_waypoints=True,
                format='geojson'
            )

            m = folium.Map(location=current_coords[::-1], zoom_start=6)
            folium.GeoJson(optimized).add_to(m)

            ordered_keys = ["Current Location"] + selected_keys
            waypoints = optimized["properties"]["way_points"]
            for i, idx in enumerate(waypoints):
                loc = coordinates[idx][::-1]
                label = f"{i + 1}. {ordered_keys[idx]}"
                color = "green" if idx == 0 else "blue"
                folium.Marker(location=loc, popup=label, tooltip=label,
                              icon=folium.Icon(color=color)).add_to(m)

            folium_static(m)
else:
    st.info("📡 Waiting for GPS signal or user permission...")
