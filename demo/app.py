import streamlit as st
import folium
from streamlit_folium import st_folium
import openrouteservice

st.set_page_config(page_title="Carbon-Aware Route Optimizer", layout="wide")
st.title("🚚 Carbon-Aware Route Optimizer (OpenRouteService Demo)")

API_KEY = "eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6IjQ3MWRmZjgxOWYzODQzODZhZDRmNDM5MzIyMDY3ZmY3IiwiaCI6Im11cm11cjY0In0="
client = openrouteservice.Client(key=API_KEY)

# Coordinates: Seattle
start = (-122.335167, 47.608013)           # (lon, lat)
waypoints = [(-122.330, 47.610), (-122.325, 47.615)]
end = (-122.320, 47.620)

# Persistent state for route data
if "route_geometry" not in st.session_state:
    st.session_state.route_geometry = None

st.write("Click below to fetch and display a baseline driving route.")

# Container to hold the map so it doesn't re-mount each time
map_container = st.empty()

if st.button("Show Baseline Route"):
    try:
        coords = [start] + waypoints + [end]
        route = client.directions(
            coordinates=coords,
            profile="driving-car",
            format="geojson"
        )
        st.session_state.route_geometry = route["features"][0]["geometry"]["coordinates"]
        st.success("Route loaded!")

    except Exception as e:
        st.error(f"❗ Route request failed: {e}")
        st.session_state.route_geometry = None

# Draw map only if we have geometry
if st.session_state.route_geometry:
    m = folium.Map(location=[start[1], start[0]], zoom_start=13)

    folium.PolyLine([(lat, lon) for lon, lat in st.session_state.route_geometry],
                    color="blue", weight=4, opacity=0.8).add_to(m)

    folium.Marker([start[1], start[0]], popup="Start",
                  icon=folium.Icon(color="green")).add_to(m)
    folium.Marker([end[1], end[0]], popup="End",
                  icon=folium.Icon(color="red")).add_to(m)

    # Render map in fixed container
    map_container.folium_static = st_folium(m, width=800, height=600)
else:
    st.info("No route loaded yet.")
