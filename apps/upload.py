import os
#import geopandas as gpd
import streamlit as st
import pandas as pd


def app():

    st.title("Raw Data Collected")
   
# Define the file path for the CSV file
    filepath = "https://raw.githubusercontent.com/JeremyHester/HeatIslandDemo/master/preliminarydata2.csv"

   # Load data
    df = pd.read_csv(filepath)

# Define container with centered layout
    container = st.container()
    with container:
    # Define columns
     left_column, right_column = st.beta_columns(2)
    # Display DataFrame in the left column
    with left_column:
        st.write(df, height=500)
    # Add filter in the right column
    with right_column:
        st.write("Filter by column")
        column = st.selectbox("Select a column", df.columns)
        value = st.text_input("Enter a value")
        filtered_df = df[df[column] == value]
        st.write(filtered_df, height=300)
    
    

  

# Read the CSV file into a DataFrame
#df = pd.read_csv(file_path)

# Convert the date and time columns to datetime format
#df['datetime'] = pd.to_datetime(df['date'] + ' ' + df['time'])

# Drop the original date and time columns
#df.drop(['date', 'time'], axis=1, inplace=True)

# Generate a correlation matrix for the DataFrame
#corr_matrix = df.corr()

# Create a heatmap of the correlation matrix using Seaborn
#fig, ax = plt.subplots(figsize=(10,10))
#sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)

# Display the heatmap in the app
#st.pyplot(fig)
    
    
    
    
    
    
    #row1_col1, row1_col2 = st.columns([2, 1])
    #width = 950
    #height = 600

    #with row1_col2:

     #   backend = st.selectbox(
       #     "Select a plotting backend", ["folium", "kepler.gl", "pydeck"], index=2
      #  )

       # if backend == "folium":
        #    import leafmap.foliumap as leafmap
        #elif backend == "kepler.gl":
         #   import leafmap.kepler as leafmap
        #elif backend == "pydeck":
         #   import leafmap.deck as leafmap

        #url = st.text_input(
         #   "Enter a URL to a vector dataset",
          #  "https://github.com/JeremyHester",
        #)

        #data = st.file_uploader(
         #   "Upload a vector dataset", type=["geojson", "kml", "zip", "tab"]
        #)

        #container = st.container()

        #if data or url:
         #   if data:
          #      file_path = save_uploaded_file(data, data.name)
           #     layer_name = os.path.splitext(data.name)[0]
            #elif url:
             #   file_path = url
              #  layer_name = url.split("/")[-1].split(".")[0]

            #with row1_col1:
             #   if file_path.lower().endswith(".kml"):
              #      gpd.io.file.fiona.drvsupport.supported_drivers["KML"] = "rw"
               #     gdf = gpd.read_file(file_path, driver="KML")
                #else:
                 #   gdf = gpd.read_file(file_path)
                #lon, lat = leafmap.gdf_centroid(gdf)
                #if backend == "pydeck":

                   # column_names = gdf.columns.values.tolist()
                   # random_column = None
                   # with container:
                   #     random_color = st.checkbox("Apply random colors", True)
                    #    if random_color:
                     #       random_column = st.selectbox(
                      #          "Select a column to apply random colors", column_names
                       #     )

                    #m = leafmap.Map(center=(40, -100))
                    # m = leafmap.Map(center=(lat, lon))
                    #m.add_gdf(gdf, random_color_column=random_column)
                    #st.pydeck_chart(m)

                #else:
                 #   m = leafmap.Map(center=(lat, lon), draw_export=True)
                  #  m.add_gdf(gdf, layer_name=layer_name)
                   # if backend == "folium":
                    #    m.zoom_to_gdf(gdf)
                    #m.to_streamlit(width=width, height=height)

        #else:
         #   with row1_col1:
          #      m = leafmap.Map()
           #     st.pydeck_chart(m)
