import pandas as pd
import numpy as np
import streamlit as st
import pydeck as pdk
from streamlit_datetime_picker import date_time_picker

def main():
    locations = pd.read_csv('locations.csv')
    aq = np.load('pred_aq_1_week.npy')

    st.title("AlohaAir Locations Map")

    datetime_value = date_time_picker("Select Date and Time",
                                       format ="YYYY-MM-DD hh A",
                                       minDate=pd.Timestamp('2024-01-01 00:00:00'),
                                       maxDate=pd.Timestamp('2024-10-05 08:00:00'),
                                       value=pd.Timestamp('2024-01-01 00:00:00'),
                                       key='datetime_picker',
                                       timeUnit='hour')

    start_time = datetime_value.replace(tzinfo=None)
    end_time = start_time + pd.Timedelta(hours=aq.shape[2] - 1)
    
    time_difference = start_time - pd.Timestamp('2024-01-01 00:00:00', tz=None)
    timepoint = int(time_difference.total_seconds() / 3600)
    print(timepoint)


    selected_location = st.empty()

    # timepoint = st.slider(
    #     "Show timepoint:",
    #     min_value=0,
    #     max_value=aq.shape[0] - 1,
    #     value=0,
    #     step=1,
    #     key='timepoint'
    # )

    hour_slider = st.slider(
        "Show hour:",
        min_value=start_time,
        max_value=end_time,
        value=start_time,
        step=pd.Timedelta(hours=1),
        key='hour',
        format="MMM Do h A"
    )
    hour = int((hour_slider - start_time).total_seconds() / 3600)

    # Update the locations DataFrame with the selected timepoint's AQ data
    locations['pm25'] = [aq[timepoint][i][hour] for i in range(len(locations))]
    locations['pm25_rounded'] = locations['pm25'].round(2).astype(str) + ' µg/m³'

    def on_click(info):
        if info is not None and info.object is not None:
            selected_location.markdown(
                f"**Name:** {info.object['location']}  \n"
                f"**Latitude:** {info.object['latitude']}  \n"
                f"**Longitude:** {info.object['longitude']}"
            )

    # Define a function to map PM2.5 values to color (e.g., green to red)
    def pm25_to_color(pm25):
        if pm25 <= 12:
            # Green
            return [0, 200, 30, 160]
        elif 12 < pm25 <= 35.4:
            # Yellow
            return [255, 255, 0, 160]
        elif 35.4 < pm25 <= 55.4:
            # Orange
            return [255, 165, 0, 160]
        elif 55.4 < pm25 <= 150.4:
            # Red
            return [255, 0, 0, 160]
        elif 150.4 < pm25 <= 250.4:
            # Purple
            return [128, 0, 128, 160]
        else:
            # Dark Red
            return [139, 0, 0, 160]

    locations['color'] = locations['pm25'].apply(pm25_to_color)

    st.pydeck_chart(
        pdk.Deck(
            map_style='road',
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
                        "<b>PM 2.5:</b> {pm25_rounded}<br/>",
                "style": {"color": "white"}
            },
        )
    )

if __name__ == "__main__":
    main()