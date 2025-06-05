import streamlit as st
from st_bridge import bridge, html
import openrouteservice
import folium
from streamlit_folium import folium_static

st.set_page_config(page_title="📡 GPS Tracker (Async Fix)", layout="wide")
st.title("📡 Real-Time GPS Tracker with Async JS & Fallback")

client = openrouteservice.Client(key='YOUR_API_KEY')  # Replace with actual API key

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

st.subheader("Step 1: Browser GPS Capture")

data = bridge("location-bridge", default="no data yet")

html("""
<script>
(async function() {
  try {
    const pos = await new Promise((resolve, reject) => {
      navigator.geolocation.getCurrentPosition(resolve, reject, {
        enableHighAccuracy: true,
        timeout: 10000,
        maximumAge: 0
      });
    });

    const coords = pos.coords.latitude + "," + pos.coords.longitude;
    alert("📍 GPS Detected: " + coords);  // Show popup for confirmation

    if (window.top?.stBridges) {
      console.log("✅ Sending GPS via window.top");
      window.top.stBridges.send("location-bridge", coords);
    } else if (window.parent?.stBridges) {
      console.log("✅ Sending GPS via window.parent");
      window.parent.stBridges.send("location-bridge", coords);
    } else {
      alert("❌ Could not find stBridges to send data.");
    }
  } catch (err) {
    alert("❌ GPS error: " + err.message);
    console.error("GPS error:", err);
  }
})();
</script>
""", iframe=False)

st.markdown("📡 Raw location data from browser:")
st.code(data)

if data != "no data yet" and "," in data:
    lat, lon = map(float, data.split(","))
    current_coords = [lon, lat]
    st.success(f"✅ Location: Latitude {lat:.5f}, Longitude {lon:.5f}")

    selected_keys = st.multiselect("Step 2: Select Destinations", list(locations_dict.keys()))

    if st.button("Step 3: Optimize Route") and selected_keys:
        coordinates = [current_coords] + [locations_dict[k] for k in selected_keys]
        with st.spinner("Routing..."):
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
                folium.Marker(location=loc, popup=label, tooltip=label,
                              icon=folium.Icon(color="green" if idx == 0 else "blue")).add_to(m)

            folium_static(m)
else:
    st.info("📡 Waiting for real-time GPS data...")