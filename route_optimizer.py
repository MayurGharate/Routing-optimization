
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="📡 Real-Time Location Tracker", layout="wide")
st.title("📡 Real-Time Browser Location Tracker (JS-based)")

st.markdown("### Step 1: Allow location access when prompted")

# JavaScript to fetch location and send it back via postMessage
components.html(
    """
    <script>
    const sendLocation = () => {
        navigator.geolocation.watchPosition(
            (position) => {
                const lat = position.coords.latitude;
                const lon = position.coords.longitude;
                const data = { type: 'FROM_JS', lat: lat, lon: lon };
                window.parent.postMessage(data, '*');
            },
            (error) => {
                console.error("Error getting location: ", error);
            },
            {
                enableHighAccuracy: true,
                maximumAge: 1000,
                timeout: 5000
            }
        );
    };
    sendLocation();
    </script>
    """,
    height=0
)

# Capture streamed data from browser using query parameters (limited native support)
# This is placeholder - full real-time postMessage handling needs a custom Streamlit component to fully capture messages.

st.info("🛑 This script sends live location from your browser, but Streamlit alone cannot yet capture it directly in real-time without extra JS bridges.")

st.markdown("👉 To go further, use `streamlit-js-events` or build a [Streamlit Custom Component](https://docs.streamlit.io/1.25.0/library/components) to receive `postMessage` events properly.")
