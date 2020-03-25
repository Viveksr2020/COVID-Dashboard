
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
    
    import numpy as np # library to handle data in a vectorized manner
    
    import pandas as pd # library for data analsysis
    
    pd.set_option('display.max_columns', None)
    
    pd.set_option('display.max_rows', None)
    
    import json # library to handle JSON files
    
    #!conda install -c conda-forge geopy --yes # uncomment this line if you haven't completed the Foursquare API lab
    
    from geopy.geocoders import Nominatim # convert an address into latitude and longitude values
    
    import requests # library to handle requests
    
    from pandas.io.json import json_normalize # tranform JSON file into a pandas dataframe
    
    # Matplotlib and associated plotting modules
    
    import matplotlib.cm as cm
    
    import matplotlib.colors as colors
    
    # import k-means from clustering stage
    
    from sklearn.cluster import KMeans
    
    #from sklearn.datasets.samples_generator import make_blobs
    
    #!conda install -c conda-forge folium=0.5.0 --yes # uncomment this line if you haven't completed the Foursquare API lab
    
    import folium # map rendering library
    
    from bs4 import BeautifulSoup
    
    import lxml
    
    print('Libraries imported.')
    
    ###############################
    from bs4 import BeautifulSoup
    
    import googlemaps
    
    import pprint
    
    import time
    
    ##from GoogleMAPsAPIKey import get_api_key
    import geopandas as geoo
    
    import numpy as np
    
    import pandas as pd
    
    from shapely.geometry import Point
    
    import folium 
    from datetime import date
    import missingno as msn
    
    import seaborn as sns
    
    import matplotlib.pyplot as plt
    
    #import rhinoscriptsytnax as rs 
    import os
    
    import requests
    
    import pandas as pand
    
    from geopy.exc import GeocoderTimedOut
    
    ##API_KEY = get_api_key()
    
    ##gmaps=googlemap.client(key=API_KEY)
    
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
    
    PostCodeArray =[]
    
    URL= "https://www.mohfw.gov.in/"
    
    data=[]
    valid_headers = ['Sr_no', 'State', 'Indian_cases', 'Total_foreign_cases','Cured','Death', 'lat','longi']
    page = requests.get(URL)
    #print(page.content)
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    soupstring = soup.find(class_="content newtab")
    
    # rows = soupstring.find_all('tr')
    #           # print("number of rows" + str(len(rows)))
    # for row in rows:
    #     cols = row.find_all('td')
    #     cols = [ele.text.strip() for ele in cols]
    #     data.append([ele for ele in cols if ele])
    #       
    # print(data)
    # #     for x in range(1, len(data)):
    # # print(soup)
    
    
    SL_No=[]
    State=[]
    Indian_cases=[]
    Total_foreign_cases=[]
    Cured=[]
    Death=[]
    lat=[]
    longi=[]
    total_cases =''
    
    #print("number of tables"+ str(len(data_tables)))
    
    
    # data = []
    #print(data_tables)
    with open('ListofCoronoCasesIndia.csv', 'w') as writefile:
      
          writefile.write('SL_No' + ',' + 'State'  + ','+ 'Indian_cases' + ','+ 'Total_foreign_cases'+ ','+'Cured'+',' + 'Death'+ ','+ str(lat) + ','+str(longi))
      
          writefile.write("\n")                     ### this is next line character so write in next line
     
          #filename= "CVIndia_" + str(date.today())+ ".html"
          m = folium.Map(location=[20.593683, 78.962883])
          m.fit_bounds([[33.778175,76.576172],[7.873054,80.771797]])
          folium.Map( location=[20.593683, 78.962883],zoom_start=13)
          m.save("CVIndia.html")
     
          rows = soupstring.find_all('tr')
          #print("number of rows" + str(len(rows)))
          for row in rows:
              cols = row.find_all('td')
              cols = [ele.text.strip() for ele in cols]
              data.append([ele for ele in cols if ele])
    
          print(data)
          for x in range(1,len(data)-1):
        
            print("x"+ str(x))
            Sl_no= data[x][0]
            print("Sl_no:" + Sl_no)
            State= data[x][1]
            print("State:" + State)
            Indian_cases= data[x][2]
            print("Indian_cases:" + Indian_cases)
            Total_foreign_cases= data[x][3]
            print("Total_foreign_cases:" + Total_foreign_cases)
            Cured= data[x][4]
            print("Cured:" + Cured)
            Death= data[x][5]
            print("Death:" + Death)
            
            
            geocode_result = gmaps.geocode(State.strip()+','+ 'India')
            lati = geocode_result[0]['geometry']['location']['lat']
            longi = geocode_result[0]['geometry']['location']['lng']
            lat= lati
            print("lat:" + str(lat))
            long= longi
            print("long:" + str(longi))
    
             
            Indian_cases= Indian_cases.replace('+','')
            Total_foreign_cases= Total_foreign_cases.replace(',','')
            Cured= Cured.replace(',','')
            Death= Death.replace(',','')
            
             
          #  total_Cases = 'India National:'+ str(Indian_cases)+ '\n'+ 'Foreign Cases:'+ str(Total_foreign_cases)+'\n' +'Total Cured:'+ str(Cured)+'\n'+ 'Death:'+ str(Death)
            Indian_cases = int(Indian_cases) 
            if Indian_cases== None:
               Indian_cases = 0
            #   totalcases= totalcases+ NumofPatient
            if Indian_cases <= 5:
                   #totalcases= totalcases+ NumofPatient
                   #print("less than 5") 
                   total_Cases ='India National:'+ str(Indian_cases)+"\n"
                   total_Cases= total_Cases+ 'Foreign Cases:'+ str(Total_foreign_cases)+"\n"
                   total_Cases= total_Cases+'Total Cured:'+ str(Cured)+"\n"
                   total_Cases= total_Cases+ 'Death:'+ str(Death)
                   print(total_Cases)
                   folium.Marker([lati,longi],
                          popup= total_Cases,
                          tooltip=State,
                          icon=folium.Icon(color='green',icon ='leaf')).add_to(m)
                           
            else:
                if  Indian_cases > 5 and Indian_cases < 10 :
                      #print("between 5 and 10")
                      #totalcases= totalcases+ NumofPatient
                      total_Cases ='India National:'+ str(Indian_cases)+"\n"
                      total_Cases= total_Cases+ 'Foreign Cases:'+ str(Total_foreign_cases)+"\n"
                      total_Cases= total_Cases+'Total Cured:'+ str(Cured)+"\n"
                      total_Cases= total_Cases+ 'Death:'+ str(Death)
                      print(total_Cases)
                      folium.Marker([lati,longi],
                          popup= total_Cases,
                          tooltip=State,
                          icon=folium.Icon(color='orange',icon ='cloud')).add_to(m)                         
      
                else:
                      Indian_cases > 10
                      #print("greater than 10")
                      #totalcases= totalcases+ NumofPatient
                      total_Cases ='India National:'+ str(Indian_cases)+"\n"
                      total_Cases= total_Cases+ 'Foreign Cases:'+ str(Total_foreign_cases)+"\n"
                      total_Cases= total_Cases+'Total Cured:'+ str(Cured)+"\n"
                      total_Cases= total_Cases+ 'Death:'+ str(Death)
                      print(total_Cases)
                      folium.Marker([lati,longi],
                          popup= total_Cases,
                          tooltip=State,
                          icon=folium.Icon(color='red',icon ='cloud')).add_to(m)  
                           
     
            legend_html =   '''
                    <div style="position: fixed; 
                                bottom: 50px; left: 50px; width: 200px; height: 120px; 
                                border:2px solid grey; z-index:9999; font-size:14px;
                                ">&nbsp; Colour Legend <br>
                                  &nbsp; New cases >5 & < 10 &nbsp; <i class="fa fa-map-marker fa-2x" style="color:orange"></i><br>
                                  &nbsp; new cases >10 &nbsp; <i class="fa fa-map-marker fa-2x" style="color:red"></i>
                    </div>
                    ''' 
     
            m.get_root().html.add_child(folium.Element(legend_html))
                     
                
              
                
     
            m.save("CVIndia.html") 
     
                
                
            writefile.write(str(SL_No) + ',' + str(State)  + ','+ str(Indian_cases) + ','+ str(Total_foreign_cases)+ ','+str(Cured) +',' + str(Death)+ ','+ str(lat) + ','+str(longi))
      
            writefile.write("\n") 
                
    

sched.add_job(generateHTML,'interval',minutes=1) 
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
    
    
    aboslute_path_to_schema = os.path.join(os.getcwd(), "CVIndia.html")
    #print(aboslute_path_to_schema)
    with open(aboslute_path_to_schema, 'r') as content_file:
         html = content_file.read()
         #print(html)
         self.wfile.write(bytes(html, "utf8"))
    return
#print(MyHttpRequestHandler) 
handler_object = MyHttpRequestHandler
 

httpd = HTTPServer(('', 8081), handler_object)
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
