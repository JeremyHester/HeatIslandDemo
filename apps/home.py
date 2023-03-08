import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("Home")

    st.markdown(
        """
  Use the Heatmap tab to view your map and the Data Set to see the raw data 

    """
    )

    m = leafmap.Map(locate_control=True)
    m.add_basemap("ROADMAP")
    m.to_streamlit(height=700)
