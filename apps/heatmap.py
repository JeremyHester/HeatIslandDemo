import os 
import streamlit as st
import pandas as pd
import folium.plugins as plugins
from folium.plugins import HeatMap


def app():

   st.title("Heatmap")
   filepath = "https://raw.githubusercontent.com/JeremyHester/HeatIslandDemo/master/preliminarydata.csv"
   data = pd.read_csv(filepath, header= None)
   map_center = [data['latitude'][0], data['longitude'][0]]
   heat_map = folium.Map(location=map_center, zoom_start=12)

   # Create a HeatMap object and add it to the map
   heatmap_data = data[['latitude', 'longitude', 'temperature']]
   heatmap_data = heatmap_data.dropna()  # Remove rows with missing data
   heatmap_data = heatmap_data.values.tolist()
   HeatMap(heatmap_data, name='Temperature Heatmap').add_to(heat_map)

   # Add layer control to the map
   folium.LayerControl().add_to(heat_map)

   # Display the map using Streamlit
   st.write(heat_map._repr_html_(), unsafe_allow_html=True)
   
   
  # df = pd.read_csv("filepath")

   # Select the desired columns
 #  df = df.loc[:, ['date', 'time', 'temperature', 'humidity', 'latitude', 'longitude', 'satellites']]

   # Drop rows with missing data
 #  df = df.dropna()
   
 #  dfCopy = df.copy()

 #  dfCopy.loc[:,'LATITUDE'] = ((dfCopy.loc[:, 'LATITUDE']*10).apply(np.floor))/10
 #  dfCopy.loc[:,'LONGITUDE'] = ((dfCopy.loc[:, 'LONGITUDE']*10).apply(np.floor))/10
 #  dfCopy.loc[:,'LatLonRange'] = dfCopy.loc[:,'LATITUDE'].map(str) + '-' + dfCopy.loc[:, 'LONGITUDE'].map(str)

 #  df_grouped = dfCopy.groupby(['LatLonRange', 'LATITUDE', 'LONGITUDE'])

 #  df_grouped.head()
   
   
#   df_folium = pd.DataFrame({'Lat':fire_count['LATITUDE'],'Long':fire_count['LONGITUDE'],'Count':fire_count['count']})

#   df_folium['weight'] = df_folium['Count'] / df_folium['Count'].abs().max()

 #  def generateBaseMap(loc, zoom=4, tiles='OpenStreetMap', crs='ESPG2263'):
 #  return folium.Map(location=loc,
  #                 control_scale=True, 
  #                 zoom_start=zoom,
  #                 tiles=tiles)
 # 
#   base_map = generateBaseMap([39, -98] )

#  map_values1 = df_folium[['Lat','Long','weight']]

 #  data = map_values1.values.tolist()
           
 #  hm = HeatMap(data,gradient={0.1: 'blue', 0.3: 'lime', 0.5: 'yellow', 0.7: 'orange', 1: 'red'}, 
 #               min_opacity=0.05, 
 #               max_opacity=0.9, 
 #               radius=25,
 #               use_local_extrema=False)#.add_to(base_map)

 #  base_map.add_child(hm)

  
    
    
    
    
    
    
    
    
    
    
 
