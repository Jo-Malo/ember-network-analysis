import pandas as pd
import geopandas as gpd
import folium
from folium.plugins import HeatMap

# ── Load GTFS data ──────────────────────────────────────────────
print("Loading GTFS data...")
routes = pd.read_csv('gtfs_all/routes.txt')
trips = pd.read_csv('gtfs_all/trips.txt')
stops = pd.read_csv('gtfs_all/stops.txt')
stop_times = pd.read_csv('gtfs_all/stop_times.txt')
shapes = pd.read_csv('gtfs_all/shapes.txt')

# Filter to Ember only
ember_routes = routes[routes['agency_id'] == 'OP965']
ember_trips = trips[trips['route_id'].isin(ember_routes['route_id'])]
ember_shape_ids = ember_trips['shape_id'].unique()
ember_shapes = shapes[shapes['shape_id'].isin(ember_shape_ids)]
ember_stop_times = stop_times[stop_times['trip_id'].isin(ember_trips['trip_id'])]
ember_stop_ids = ember_stop_times['stop_id'].unique()
ember_stops = stops[stops['stop_id'].isin(ember_stop_ids)]

print(f"Ember routes: {len(ember_routes)}, Stops: {len(ember_stops)}")

# ── Load population data ─────────────────────────────────────────
print("Loading population data...")
gdf = gpd.read_file('dz_centroids/SG_DataZone_Cent_2022.shp')
gdf = gdf.to_crs(epsg=4326)
gdf['lat'] = gdf.geometry.y
gdf['lon'] = gdf.geometry.x

# ── Build map ────────────────────────────────────────────────────
print("Building map...")
m = folium.Map(location=[56.8, -4.0], zoom_start=7)

# Population heatmap layer
heat_data = [[row['lat'], row['lon'], row['totpop2022']] 
             for _, row in gdf.iterrows() 
             if pd.notna(row['totpop2022'])]

HeatMap(
    heat_data,
    name='Population density',
    min_opacity=0.3,
    max_zoom=12,
    radius=20,
    blur=25,
    gradient={0.2: 'blue', 0.4: 'lime', 0.6: 'yellow', 0.8: 'orange', 1.0: 'red'}
).add_to(m)

# Ember route shapes
for shape_id in ember_shape_ids:
    shape_data = ember_shapes[ember_shapes['shape_id'] == shape_id].sort_values('shape_pt_sequence')
    points = list(zip(shape_data['shape_pt_lat'], shape_data['shape_pt_lon']))
    if points:
        folium.PolyLine(
            points,
            color='white',
            weight=3,
            opacity=0.9
        ).add_to(m)

# Ember stops
for _, stop in ember_stops.iterrows():
    folium.CircleMarker(
        location=[stop['stop_lat'], stop['stop_lon']],
        radius=4,
        color='white',
        fill=True,
        fill_color='#00C851',
        fill_opacity=0.9,
        popup=folium.Popup(stop['stop_name'], max_width=200)
    ).add_to(m)

# Layer control
folium.LayerControl().add_to(m)

# Title and legend
title_html = '''
<div style="position: fixed; top: 10px; left: 50px; z-index: 1000; 
background-color: white; padding: 10px 15px; border-radius: 5px; 
box-shadow: 2px 2px 6px rgba(0,0,0,0.3); font-family: Arial;">
<h4 style="margin:0; color: #007E33;">🚌 Ember Network vs Population — Scotland</h4>
<p style="margin:4px 0 0 0; font-size:12px; color:#555;">
White lines = Ember routes &nbsp;|&nbsp; Green dots = stops
</p>
</div>

<div style="position: fixed; bottom: 30px; left: 50px; z-index: 1000; 
background-color: white; padding: 10px 15px; border-radius: 5px; 
box-shadow: 2px 2px 6px rgba(0,0,0,0.3); font-family: Arial; font-size: 12px;">
<b>Population density</b><br>
<div style="display:flex; align-items:center; margin-top:6px;">
  <div style="background: linear-gradient(to right, blue, lime, yellow, orange, red); 
  width: 150px; height: 12px; border-radius: 3px;"></div>
</div>
<div style="display:flex; justify-content:space-between; width:150px; margin-top:3px;">
  <span>Low</span><span>High</span>
</div>
</div>
'''
m.get_root().html.add_child(folium.Element(title_html))

m.save('ember_network.html')
print("Done! Open ember_network.html to view.")