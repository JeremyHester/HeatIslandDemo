import streamlit as st
import pandas as pd
import bokeh
from bokeh.models import ColumnDataSource
from bokeh.palettes import Viridis256
from bokeh.transform import linear_cmap
from bokeh.plotting import figure, output_file, show
from bokeh.tile_providers import CARTODBPOSITRON_RETINA

def app():
    st.title("Heatmap")
    filepath = "https://raw.githubusercontent.com/JeremyHester/HeatIslandDemo/master/preliminarydata2.csv"
    data = pd.read_csv(filepath)

    # Get the data for the heatmap
    x = data['longitude']
    y = data['latitude']
    colors = data['temperature']

    # Create a color mapper based on temperature values
    color_mapper = linear_cmap(field_name='colors', palette=Viridis256, low=min(colors), high=max(colors))

    # Create the Bokeh figure
    heatmap = figure(width=700, height=500, x_range=(min(x), max(x)), y_range=(min(y), max(y)))
    heatmap.add_tile(bokeh.tile_providers.CARTODBPOSITRON_RETINA)

    # Add the heatmap to the figure
    heatmap.circle(x=x, y=y, color=color_mapper, source=ColumnDataSource({'x': x, 'y': y, 'colors': colors}), size=2, alpha=0.8)

    # Show the figure
    st.bokeh_chart(heatmap)

app()


####working partially code for color bar at top####
# import os 
# import streamlit as st
# import pandas as pd
# import numpy as np
# import folium
# import folium.plugins as plugins
# from branca.colormap import LinearColormap
# from folium.plugins import HeatMap
# import matplotlib.cm as cm

# def folium_html(m):
#    """Converts folium map to HTML"""
#    srcdoc = m._repr_html_()
#    return srcdoc

# def app():
#    st.title("Heatmap")
#    filepath = "https://raw.githubusercontent.com/JeremyHester/HeatIslandDemo/master/preliminarydata2.csv"
#    data = pd.read_csv(filepath)

#    # Find the first non-zero value for latitude and longitude
#    first_lat = data.loc[data['latitude']!=0]['latitude'].iloc[0]
#    first_long = data.loc[data['longitude']!=0]['longitude'].iloc[0]

#    # Create the map centered at the first non-zero latitude and longitude value
#    map_center = [first_lat, first_long]
#    my_map = folium.Map(location=map_center, zoom_start=15)
   
#    # Create a LinearColormap
#    colormap = LinearColormap(colors=['white', 'blue', 'green', 'yellow', 'red'], vmin=-20.0, vmax=120.0)

#    # Add the colormap to the map
#    my_map.add_child(colormap)

#    # Convert the colormap to a dictionary
#    colormap_dict = colormap.to_dict()

#    # Add the heatmap layer to the map
#    heat_data = [[row['latitude'], row['longitude'], row['temperature']] for index, row in data.iterrows()]
#    heat_map = folium.plugins.HeatMap(heat_data, gradient=colormap_dict, min_opacity=0.8)
#    heat_map.add_to(my_map)

#    for index, row in data.iterrows():
#       temp = row['temperature']
#       if temp < -20:
#           color = 'white'
#       elif -20 <= temp < 0:
#           color = 'blue'
#       elif 0 <= temp < 20:
#           color = 'green'
#       elif 20 <= temp < 40:
#           color = 'yellow'
#       else:
#           color = 'red'
#       folium.Marker([row['latitude'], row['longitude']], icon=folium.Icon(color=color)).add_to(my_map)
   
#    # Save map as HTML file
#    my_map.save('map.html')

#    # Load HTML file in Streamlit app
#    with open('map.html', 'r') as f:
#       html = f.read()
#    st.components.v1.html(html, width=700, height=500)

# app()

###end of working with bar on top and needing a layer###

####### "working" color ####

# # Find the first non-zero value for latitude and longitude
#    first_lat = data.loc[data['latitude']!=0]['latitude'].iloc[0]
#    first_long = data.loc[data['longitude']!=0]['longitude'].iloc[0]

#     # Create the map centered at the first non-zero latitude and longitude value
#    map_center = [first_lat, first_long]
#    my_map = folium.Map(location=map_center, zoom_start=12)

# #    # Add the heatmap layer to the map
#    heat_data = [[row['latitude'], row['longitude'], row['temperature']] for index, row in data.iterrows()]
#    heat_map = folium.plugins.HeatMap(heat_data)
#    heat_map.add_to(my_map)
#     #Save map as HTML file
#    my_map.save('map.html')

#    # Load HTML file in Streamlit app
#    with open('map.html', 'r') as f:
#       html = f.read()
#    st.components.v1.html(html, width=700, height=500)


###### "end of working color" #####









# import os 
# import streamlit as st
# import pandas as pd
# import numpy as np
# import folium
# import folium.plugins as plugins
# from branca.colormap import LinearColormap
# from folium.plugins import HeatMap
# import matplotlib.cm as cm

# #reconnecting


# def folium_html(m):
#    """Converts folium map to HTML"""
#    srcdoc = m._repr_html_()
#    return srcdoc


# def app():

#    st.title("Heatmap")
#    filepath = "https://raw.githubusercontent.com/JeremyHester/HeatIslandDemo/master/preliminarydata2.csv"
   
#    data = pd.read_csv(filepath)

#    # Find the first non-zero value for latitude and longitude
#    first_lat = data.loc[data['latitude']!=0]['latitude'].iloc[0]
#    first_long = data.loc[data['longitude']!=0]['longitude'].iloc[0]

#     # Create the map centered at the first non-zero latitude and longitude value
#    map_center = [first_lat, first_long]
#    my_map = folium.Map(location=map_center, zoom_start=15)
   
# #    # Create a LinearColormap
# #    colormap = LinearColormap(colors=['green', 'yellow', 'red'], vmin=0, vmax=120)

# #     # Add the colormap to the map
# #    my_map.add_child(colormap)

# #     # Convert the colormap to a dictionary
# #    colormap_dict = colormap.to_dict()

# #     # Save the map
# #    my_map.save('map.html')
   
# #Define the color gradient using the brunet colormap
#    gradient_ranges = [-20.0, 32.0, 50.0, 70.0, 90.0, 120.0]
#    gradient_colors = [cm.coolwarm(x) for x in range(0, 256, int(256/len(gradient_ranges)-1))]

#    cmap = LinearColormap(colors=gradient_colors, vmin=min(gradient_ranges), vmax=max(gradient_ranges))

# #Add the heatmap layer to the map
#    heat_data = [[row['latitude'], row['longitude'], row['temperature']] for index, row in data.iterrows()]
#    #heat_map = folium.plugins.HeatMap(heat_data, gradient=colormap_dict, min_opacity=0.8)
#    #heat_map = folium.plugins.HeatMap(heat_data, gradient=, min_opacity=0.8)
#    heat_map.add_to(my_map)

# # Save map as HTML file
#    my_map.save('map.html')

# # Load HTML file in Streamlit app
#    with open('map.html', 'r') as f:
#     html = f.read()
#    st.components.v1.html(html, width=700, height=500)
   
  
   
#    # Display the map using Streamlit
   # st.markdown(my_map._repr_html_(), unsafe_allow_html=True)


  
    
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
   

   
   
    
  
    
    
    
    
    
    
 
