import streamlit as st
import leafmap.leafmap as leafmap


def app():

    st.title("Heatmap")

    filepath = "https://raw.githubusercontent.com/JeremyHester/HeatIslandDemo/master/preliminarydata.csv"
   # m = leafmap.Map(tiles="stamentoner")
    m = leafmap.Map()
    m.add_basemap("Stamen.Toner")
    m.add_heatmap(
    filepath,
    latitude="latitude",
    longitude='longitude',
    value="pop_max",
    name="Heat map",
    radius=20,
    )
    m.to_streamlit(height=700)
