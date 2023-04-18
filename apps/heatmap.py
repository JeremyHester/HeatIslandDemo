import os 
import streamlit as st
import pandas as pd
import numpy as np
import folium
import folium.plugins as plugins
from folium.plugins import HeatMap

#reconnecting


def folium_html(m):
   """Converts folium map to HTML"""
   srcdoc = m._repr_html_()
   return srcdoc


def app():

   st.title("Heatmap")
   filepath = "https://raw.githubusercontent.com/JeremyHester/HeatIslandDemo/master/preliminarydata2.csv"

   # Load data
   #df = pd.read_csv(filepath)

   # Create map object
   #m = folium.Map(location=[df['latitude'].iloc[0], df['longitude'].iloc[0]], zoom_start=15)

   # Create feature group for path walked
   #path = folium.FeatureGroup(name='Path Walked')
   #locations = list(zip(df['latitude'], df['longitude']))
   #path.add_child(folium.PolyLine(locations=locations, color='blue', weight=5))
   #m.add_child(path)

   # Create feature group for temperature data
   #temp_data = folium.FeatureGroup(name='Temperature Data')
   #temperatures = list(df['temperature'])
   #cmap = folium.LinearColormap(['blue', 'green', 'yellow', 'red'], vmin=79, vmax=87)
   #for location, temp in zip(locations, temperatures):
    #   temp_data.add_child(folium.Marker(location=location, icon=folium.Icon(color=cmap(temp), icon='info-sign')))
   #m.add_child(temp_data)

   # Add layer control
   #folium.LayerControl().add_to(m)

   # Save map as HTML file
   #m.save('map.html')

   # Load HTML file in Streamlit app
   #with open('map.html', 'r') as f:
    #  html = f.read()
   #st.components.v1.html(html, width=700, height=500)
   

   
   
   
   
   data = pd.read_csv(filepath)

   # Find the first non-zero value for latitude and longitude
   first_lat = data.loc[data['latitude']!=0]['latitude'].iloc[0]
   first_long = data.loc[data['longitude']!=0]['longitude'].iloc[0]

    # Create the map centered at the first non-zero latitude and longitude value
   map_center = [first_lat, first_long]
   my_map = folium.Map(location=map_center, zoom_start=16)

# Define the color gradient
   gradient = {0.2: 'blue', 0.4: 'cyan', 0.6: 'green', 0.8: 'yellow', 1.0: 'red'}

# Add the heatmap layer to the map
   heat_data = [[row['latitude'], row['longitude'], row['temperature']] for index, row in data.iterrows()]
   heat_map = folium.plugins.HeatMap(heat_data, gradient=gradient)
   heat_map.add_to(my_map)

# Save map as HTML file
   my_map.save('map.html')

# Load HTML file in Streamlit app
   with open('map.html', 'r') as f:
    html = f.read()
   st.components.v1.html(html, width=700, height=500)
   
  
   
#    # Display the map using Streamlit
   # st.markdown(my_map._repr_html_(), unsafe_allow_html=True)



# if __name__ == '__main__':
#     app()
   
   
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

  
    
    
    
    
    
    
    
    
    
    
 
