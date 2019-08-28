import sys
import pandas as pds
import pyproj
import simplekml

filepath = sys.argv[1]
df = pds.io.excel.read_excel(filepath, 'Raw', index_col=None)
kml = simplekml.Kml()
UTM28N = pyproj.Proj("+init=EPSG:32750")

icon_lookup = {
  "Office Site Management System alarm active - Data erratic, intermittent or incorrect. (2)": "http://maps.google.com/mapfiles/kml/paddle/wht-stars.png",
  "Autonomous Control Module Not Receiving GPS Correction alarm active - ": "http://maps.google.com/mapfiles/kml/paddle/red-stars.png",
  "Office Site Management System alarm active - Conditions not met. (19)": "http://maps.google.com/mapfiles/kml/paddle/grn-stars.png",
  "Office Site Management System alarm active - Abnormal Update. (9)": "http://maps.google.com/mapfiles/kml/paddle/ylw-stars.png"
}

for row in range(df.shape[0]):
  pnt = kml.newpoint()
  icon = pnt.style.iconstyle.icon.href

  desc = df.loc[row, 'Description']
  time = df.loc[row, 'Time']
  machine = df.loc[row,'Machine']
  event_code = df.loc[row, 'EventNumber-HE']
  x_coord = df.loc[row,'X']
  y_coord = df.loc[row,'Y']

  pnt.name = machine
  pnt.coords =[UTM28N(x_coord, y_coord, inverse=True)]
  pnt.description = f'{desc} {str(time)} Event Code: {str(event_code)}'
    
  if desc in icon_lookup:
    icon = icon_lookup[desc]
# Extract the full string of the KML
kml_string = kml.kml()
# Remove all new lines for easier use in Javascript
kml_string = kml_string.replace("\n", " ")
# Send to Javascript
print(kml_string)
sys.stdout.flush()