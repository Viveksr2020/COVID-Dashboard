
from http.server import HTTPServer,BaseHTTPRequestHandler,SimpleHTTPRequestHandler

import sys
import os 
from _io import BytesIO
#import Coronavirus
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
#from Coronavirus import filename

sched = BackgroundScheduler()

def generateHTML():

    
    import numpy as np  # library to handle data in a vectorized manner
    
    import pandas as pd  # library for data analsysis
    
    pd.set_option('display.max_columns', None)
    
    pd.set_option('display.max_rows', None)
    
    import json  # library to handle JSON files
    
    # !conda install -c conda-forge geopy --yes # uncomment this line if you haven't completed the Foursquare API lab
    
    from geopy.geocoders import Nominatim  # convert an address into latitude and longitude values
    
    import requests  # library to handle requests
    
    from pandas.io.json import json_normalize  # tranform JSON file into a pandas dataframe
    
    # Matplotlib and associated plotting modules
    
    import matplotlib.cm as cm
    
    import matplotlib.colors as colors
    
    # import k-means from clustering stage
    
    from sklearn.cluster import KMeans
    
    # from sklearn.datasets.samples_generator import make_blobs
    
    # !conda install -c conda-forge folium=0.5.0 --yes # uncomment this line if you haven't completed the Foursquare API lab
    
    import folium  # map rendering library
    
    from bs4 import BeautifulSoup
    
    import lxml
    
    print('Libraries imported.')
    
    ####################################
    
    from bs4 import BeautifulSoup
    
    import googlemaps
    
    import pprint
    
    import time
    
    # #from GoogleMAPsAPIKey import get_api_key
    import geopandas as geoo
    
    import numpy as np
    
    import pandas as pd
    
    from shapely.geometry import Point
    
    import folium 
    from datetime import date
    import missingno as msn
    
    import seaborn as sns
    
    import matplotlib.pyplot as plt
    
    # import rhinoscriptsytnax as rs 
    import os
    
    import requests
    
    import pandas as pand
    
    from geopy.exc import GeocoderTimedOut
    
    # #API_KEY = get_api_key()
    
    # #gmaps=googlemap.client(key=API_KEY)
    
    import googlemaps
    
    from datetime import datetime
    
    from googlemaps import Client
    
    gmaps = googlemaps.Client(key='AIzaSyDdD-JCrFejxneJWEGj8JuNJpcGfANjB0w')
    
    #===============================================================================
    # def do_geocode(address):
    # 
    #     try:
    # 
    #         return geolocator.geocode(address)
    # 
    #     except GeocoderTimedOut:
    # 
    #         return do_geocode(address)
    #===============================================================================
    
    column_names = ['Postalcode', 'Latitude', 'Longitude']
    
    dfListofPostCodes = {}
    
    PostCodeArray = []
    
    URL = "https://www.cambridge-news.co.uk/news/uk-world-news/coronavirus-cases-england-county-region-17901168"
    
    page = requests.get(URL)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # #print(soup)
    
    # #soupstring = soup.find("div class=html-embed")
    
    Locality_Name = ''
    
    postal_town = ''
    
    Admin_level1 = ''
    
    Admin_level2 = ''
    
    postal_code = ''
    Route_Name = ''
    
    # country = pd.read_csv('/Users/arneshsrivastava/eclipse-workspace/ListofCoronoCases.csv')
    
    #filename = "CV_" + str(date.today()) + ".html"
    
    m = folium.Map(location=[51.509350, -0.595450])
    folium.Map(location=[51.509350, -0.595450], zoom_start=13)
    # m.save(filename)
    totalcases = 0
    StrScriptAll = soup.find_all("p")
    
    # with open('ListofCoronoCases.csv', 'w') as writefile:
    #  
    #      writefile.write('address' + ',' + 'lat' + ',' + 'longi' + ',' +
    #  
    #                            'Route_Name' + ','  + 'Locality_Name' + ',' + 'postal_town' + ','+
    #  
    #                            'Admin_level3' + ','  + 'Admin_level2' + ',' + 'Admin_level1' + ','+ 'country' + ','+ 'NumofPatient')
    #  
    #      writefile.write("\n")                     ### this is next line character so write in next line
    
    for list in range(11, len(StrScriptAll) - 2):  # ## this provides list like [a, b, c...]
    
               jsonData = StrScriptAll[list]  # ## this picks up the first <a href="/sl09rr">SL0 9RR Market Lane</a>,
    
               dataText1 = jsonData.get_text(separator=" ")  # ## this picks up the value of SL0 9RR Market Lane
    
               address = dataText1  # ## assign the value to address
               
               last_char_index = address.rfind(" ")
               
               NumofPatient = address[last_char_index + 1:]
               
               address = address[:(last_char_index)]
               
               geocode_result = gmaps.geocode(address.strip() + ',' + 'United Kingdom')
               lati = geocode_result[0]['geometry']['location']['lat']
               longi = geocode_result[0]['geometry']['location']['lng']
               address = address.replace(',', '', 1)
               
               #print(len(geocode_result[0]['address_components']))
               #print(address)
               for i in range(len(geocode_result[0]['address_components'])):
    
                         print(str(i)+ 'loop'+ geocode_result[0]['address_components'][i]['types'][0])
    
                         if (geocode_result[0]['address_components'][i]['types'][0] == "route"):
    
                             Route_Name = geocode_result[0]['address_components'][i]['long_name']
    
                             # print('Route_Name:' + " "+ Route_Name)
    
                         else:
    
                             if  (geocode_result[0]['address_components'][i]['types'][0] == "locality"): 
    
                                 Locality_Name = geocode_result[0]['address_components'][i]['long_name']
    
                                 # #print('Locality_Name:' + " "+ Locality_Name)
    
                             else:
    
                                 if  (geocode_result[0]['address_components'][i]['types'][0] == "postal_town"): 
    
                                     postal_town = geocode_result[0]['address_components'][i]['long_name']
    
                                     # #print('postal_town:' + " "+ postal_town)
    
                                 else:
    
                                     if (geocode_result[0]['address_components'][i]['types'][0] == "administrative_area_level_3"):
    
                                        Admin_level3 = geocode_result[0]['address_components'][i]['long_name']
    
                                        Admin_level3 = Admin_level3.replace(',', '', 1)
                                        # print('administrative_area_level_3:' + " "+ Admin_level3 )
    
                                     else:
    
                                        if  (geocode_result[0]['address_components'][i]['types'][0] == "administrative_area_level_2"): 
    
                                            Admin_level2 = geocode_result[0]['address_components'][i]['long_name']
    
                                            # print('administrative_area_level_2:' + " "+ Admin_level2)
    
                                        else:
    
                                            if  (geocode_result[0]['address_components'][i]['types'][0] == "administrative_area_level_1"): 
    
                                                Admin_level1 = geocode_result[0]['address_components'][i]['long_name']
    
                                                # print('administrative_area_level_1:' + " "+ Admin_level1)
    
                                            else:
    
                                                if (geocode_result[0]['address_components'][i]['types'][0] == "country"):
    
                                                    country = geocode_result[0]['address_components'][i]['long_name'] 
    
                                                    # print('Country:' + " "+ country)
                  
               # if NumofPatient.isalnum() == True:
               if NumofPatient == '1*':
                  NumofPatient = 1
                  
               NumofPatient = int(NumofPatient) 
               totalcases = totalcases + NumofPatient
               if NumofPatient <= 5:
                   # totalcases= totalcases+ NumofPatient
                   # print("less than 5") 
                   folium.Marker([lati, longi],
                          popup=address,
                          tooltip=NumofPatient,
                          icon=folium.Icon(color='green', icon='leaf')).add_to(m)
                          
               else:
                  if  NumofPatient > 5 and NumofPatient < 10 :
                      # print("between 5 and 10")
                      # totalcases= totalcases+ NumofPatient
                      folium.Marker([lati, longi],
                          popup=address,
                          tooltip=NumofPatient,
                          icon=folium.Icon(color='orange', icon='cloud')).add_to(m)                         
     
                  else:
                      NumofPatient > 10
                      # print("greater than 10")
                      # totalcases= totalcases+ NumofPatient
                      folium.Marker([lati, longi],
                          popup=address,
                          tooltip=NumofPatient,
                          icon=folium.Icon(color='red', icon='cloud')).add_to(m)  
                          
               folium.CircleMarker(
                      location=[51.509350, -0.595450],
                      radius=40,
                      popup="Slough" + "Total Cases in UK:" + str(totalcases),
                      color='#428bca',
                      fill=False
                      # fill_color= 'lightgreen'
                      # icon_color = 'darkblue'
                          ).add_to(m)
    #            folium.CircleMarker(
    #                   location= [51.509350, -0.595450],
    #                   radius= 300,
    #                   popup="Total Cases" + str(totalcases),
    #                   color =color1,
    #                   fill = False
    #                   #fill_color= 'lightgreen'
    #                   #icon_color = 'darkblue'
    #                       ).add_to(m)
               
               legend_html = '''
                    <div style="position: fixed; 
                                bottom: 50px; left: 50px; width: 150px; height: 90px; 
                                border:2px solid grey; z-index:9999; font-size:14px;
                                ">&nbsp; Color Legend <br>
                                  &nbsp; Patient >5 & < 10 &nbsp; <i class="fa fa-map-marker fa-2x" style="color:orange"></i><br>
                                  &nbsp; Patient >10 &nbsp; <i class="fa fa-map-marker fa-2x" style="color:red"></i>
                    </div>
                    ''' 
    
               m.get_root().html.add_child(folium.Element(legend_html))
    
               m.save("CVUKCases.html") 
               
    #            writefile.write(address + ',' + str(lati) + ',' + str(longi) + ',' + Route_Name + ','  + str(Locality_Name) + ',' + postal_town + ','+
    #                             Admin_level3 + ','  + Admin_level2 + ',' + Admin_level1 + ','+ country + ','+ str(NumofPatient))
    #  
    #            writefile.write("\n")                     ### this is next line character so write in next line
    
               
    

sched.add_job(generateHTML,'interval',minutes=24) 
sched.start()   

class MyHttpRequestHandler(SimpleHTTPRequestHandler):
    
  def do_GET(self):
    self.send_response(200)
    #print(self)
    self.send_header("Content-type", "text/html")
    self.end_headers()
    #print(self.end_headers())
    
## call your code here to Generate your local html file and name it test.htm ########
    #execfile('/Users/arneshsrivastava/eclipse-workspace/Slough Post Code Project/testmodule')
    
    # Program to cancel the timer 
    
    
    aboslute_path_to_schema = os.path.join(os.getcwd(), "CVUKCases.html")
    #print(aboslute_path_to_schema)
    with open(aboslute_path_to_schema, 'r') as content_file:
         html = content_file.read()
         #print(html)
         self.wfile.write(bytes(html, "utf8"))
    return
#print(MyHttpRequestHandler) 
handler_object = MyHttpRequestHandler
 

httpd = HTTPServer(('', 8080), handler_object)
httpd.serve_forever()
     
     
                 
#             writefile.write(str(SL_No) + ',' + str(State)  + ','+ str(Indian_cases) + ','+ str(Total_foreign_cases)+ ','+str(Cured) +',' + str(Death)+ ','+ str(lat) + ','+str(longi))
#        
#             writefile.write("\n") 
                 
#     return
    # print(data_tables)
#     with open('ListofCoronoCasesIndia.csv', 'w') as writefile:
#        
#           writefile.write('SL_No' + ',' + 'State'  + ','+ 'Indian_cases' + ','+ 'Total_foreign_cases'+ ','+'Cured'+',' + 'Death'+ ','+ str(lat) + ','+str(longi))
#        
#           writefile.write("\n")                     ### this is next line character so write in next line
