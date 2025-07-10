import pandas as pd
import numpy as np
import streamlit as st
import pydeck as pdk

locations = pd.read_csv('locations.csv')
aq = np.load('pred_aq.npy')

st.title("AlohaAir Locations Map")

selected_location = st.empty()

timepoint = st.slider(
    "Show timepoint:",
    min_value=0,
    max_value=aq.shape[0] - 1,
    value=0,
    step=1,
    key='timepoint'
)

hour = st.slider(
    "Show hour:",
    min_value=0,
    max_value=aq.shape[2] - 1,
    value=0,
    step=1,
    key='hour'
)

# Update the locations DataFrame with the selected timepoint's AQ data
locations['pm25'] = [aq[timepoint][i][hour] for i in range(len(locations))]
locations['pm25'] = locations['pm25'].round(2)

def on_click(info):
    if info is not None and info.object is not None:
        selected_location.markdown(
            f"**Name:** {info.object['location']}  \n"
            f"**Latitude:** {info.object['latitude']}  \n"
            f"**Longitude:** {info.object['longitude']}"
        )

# Define a function to map PM2.5 values to color (e.g., green to red)
def pm25_to_color(pm25):
    if pm25 < 12:
        # Green
        return [0, 200, 30, 160]
    elif 12 <= pm25 <= 35:
        # Yellow
        return [255, 255, 0, 160]
    else:
        # Red
        return [255, 0, 0, 160]

locations['color'] = locations['pm25'].apply(pm25_to_color)

st.pydeck_chart(
    pdk.Deck(
        map_style='mapbox://styles/mapbox/streets-v11',
        initial_view_state=pdk.ViewState(
            latitude=locations['latitude'].mean(),
            longitude=locations['longitude'].mean(),
            zoom=9,
            pitch=0,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=locations,
                get_position='[longitude, latitude]',
                get_color='color',
                get_radius=500,
                pickable=True,
                on_click=on_click,
                auto_highlight=True,
            ),
        ],
        tooltip={
            "html": "<b>Name:</b> {location}<br/>"
                    "<b>Latitude:</b> {latitude}<br/>"
                    "<b>Longitude:</b> {longitude}<br/>"
                    "<b>PM 2.5:</b> {pm25:.2f}<br/>",
            "style": {"color": "white"}
        },
    )
)