# %%
import geopandas as gpd
import plotly.express as px
import pandas as pd
import json

# %%
def convert_shp_geojson(shp_path):
    """Create and save GeoJSON file from SHP file to the same directory.

    Args:
        shp_path (str): Path of SHP file
    """    

    # Convert shapefile to geojson

    map_df = gpd.read_file(shp_path)

    # Write GeoJSON file, adding index number to match data frame later

    geojson_path = shp_path.replace(".shp", ".json")

    map_df.to_file(geojson_path, driver="GeoJSON", index=1)

    

#%%

risiko_shp_path = "prototype/WGS84/Flaechennutzung_RisikoHQ100.shp"
shp_path = risiko_shp_path

convert_shp_geojson(shp_path)
# %%
