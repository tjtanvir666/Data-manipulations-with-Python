"""Automation of weather and traffic data collection based on coordinates of locations
   
   API = Open Weather Map , Google Distance Matrix
   Author = Tanvir Hossain 
   email = tjtanvir666@gmail.com

"""






################################# Import the necessary libraries ################################
import numpy as np
import requests
import json
from datetime import datetime
import pprint
import pandas as pd




# this is the list of locations we have and the distance coordinates for the distance matrix that were hardcoded.

loclist =  ['Cheras', 'Sandakan', 'Kajang', 'Seremban', 'Kuantan', 'Tawau', 'Kuala Terengganu', 'Miri', 'Kota Bharu', 
'Selayang Baru', 'Subang Jaya', 'Kuala Lumpur', 'Klang', 'Johor Bahru', 'Ampang', 'Ipoh', 'Shah Alam', 'Kuching', 
'Petaling Jaya', 'Kota Kinabalu', 'George Town', 'Iskandar Puteri', 'Melaka ', 'Alor Setar', 'Bintulu', 'Kampung Baru Subang',
'Kota Bharu', 'Sungai Petani', 'Taiping', 'Bukit Mertajam', 'Sepang', 'Sibu', 'Kulim', 'Kluang', 'Skudai', 'Batu Pahat', 
'Kampung Pasir Gudang Baru', 'Kampung Sungai Ara', 'Tasek Glugor', 'Muar', 'Rawang', 'Butterworth', 'Lahad Datu', 'Semenyih',
'Port Dickson', 'Cukai', 'Putatan', 'Keningau', 'Ulu Tiram', 'Victoria', 'Taman Senai', 'Donggongon', 'Segamat', 
'Kampong Baharu Balakong', 'Perai', 'Kangar', 'Kulai', 'Jitra', 'Teluk Intan', 'Semporna', 'Putra Heights', 'Temerluh',
'Kampong Dungun', 'Simpang Empat', 'Kuala Selangor', 'Kampung Bukit Baharu', 'Bandar Labuan', 'Kota Tinggi', 'Pontian Kechil',
'Putrajaya', 'Bentong Town', 'Banting', 'Bedong', 'Batu Gajah', 'Mentekab', 'Nibong Tebal', 'Raub', 'Kampong Pangkal Kalong',
'Lumut', 'Kuala Kangsar', 'Klebang Besar', 'Kampung Ayer Keroh', 'Kampung Baharu Nilai', 'Tangkak', 'Jerantut', 'Kudat', 
'Pekan', 'Bahau', 'Bakri', 'Kuah', 'Bidur', 'Sarikei', 'Kampong Masjid Tanah', 'Tanah Merah', 'Serendah', 'Tampin', 
'Tapah Road', 'Parit Buntar', 'Simanggang', 'Permatang Kuching', 'Yong Peng', 'Sungai Besar', 'Limbang', 'Sungai Udang',
'Batu Berendam', 'Jenjarum', 'Kertih', 'Tanjung Tokong', 'Ladang Seri Kundang', 'Pekan Nenas', 'Peringat', 'Batu Arang',
'Tanjung Sepat', 'Mersing', 'Labis', 'Marang', 'Kuang', 'Paka', 'Bagan Serai', 'Alor Gajah', 'Batang Berjuntai', 
'Pelabuhan Klang', 'Batu Ferringhi', 'Gua Musang', 'Kuala Pilah', 'Ranau', 'Papar', 'Kampong Kadok', 'Kuala Kedah', 
'Kampar', 'Pasir Mas', 'Kampung Simpang Renggam', 'Parit Raja', 'Bukit Rambai', 'Sabak Bernam', 'Kepala Batas', 
'Kampung Tanjung Karang', 'Pantai Remis', 'Gurun', 'Beaufort', 'Kapit', 'Kinarut', 'Kampung Ayer Molek', 'Kuala Lipis',
'Pantai Cenang', 'Bemban', 'Kuala Perlis', 'Sungai Pelek New Village', 'Jertih', 'Kelapa Sawit', 'Buloh Kasap', 'Kota Belud',
'Kampung Bukit Tinggi', 'Tumpat', 'Kuala Sungai Baru', 'Juru', 'Pulau Sebang', 'Chaah', 'Ayer Hangat', 'Telaga Batu',
'Padang Mat Sirat', 'Taman Rajawali', 'Tanah Rata']


originList = ['3.105768, 101.715448', '5.839319, 118.116308', '2.991559, 101.787757', '2.724119, 101.932328', 
              '3.820882, 103.329190', '4.262185, 117.892673', '5.329034, 103.141363', '4.413783, 114.008027', 
              '6.125200, 102.240797', '3.208642, 101.640314', '3.056805, 101.583711', '3.154792, 101.710993', 
              '3.045467, 101.448585', '1.493519, 103.756294', '3.150286, 101.734089', '4.590321, 101.083404', 
              '3.069259, 101.517040', '1.558780, 110.345125', '3.105978, 101.644349', '5.979613, 116.073387', 
              '5.415615, 100.329268', '1.427055, 103.638804', '2.197080, 102.240415', '6.124170, 100.368033', 
              '3.166936, 113.030943', '3.149877, 101.535095', '6.125664, 102.238602', '5.644827, 100.491015', 
              '4.846619, 100.735841', '5.364246, 100.457759', '2.693213, 101.750353', '2.291600, 111.826412', 
              '5.370844, 100.553354', '2.035854, 103.321936', '1.545747, 103.660014', '1.849186, 102.937706', 
              '1.473463, 103.878967', '5.327720, 100.274414', '5.480420, 100.496637', '2.041929, 102.567964', 
              '3.321799, 101.576658', '5.394542, 100.373809', '5.020933, 118.326201', '2.950101, 101.842300', 
              '2.521226, 101.795273', '4.248530, 103.415624', '5.884386, 116.051037', '5.330091, 116.154413', 
              '1.604713, 103.821915', '5.277049, 115.242968', '1.600956, 103.640193', '5.908712, 116.101375', 
              '2.506640, 102.816490', '3.031533, 101.750393', '5.378693, 100.384053', '6.439258, 100.193265', 
              '1.655428, 103.606523', '6.267962, 100.418278', '4.022212, 101.026240', '4.479857, 118.611296', 
              '2.994738, 101.567746', '3.449655, 102.417469', '3.217083, 101.318535', '2.434517, 102.184780', 
              '3.339628, 101.249979', '2.216515, 102.284461', '5.290254, 115.267293', '1.731315, 103.901311', 
              '1.487496, 103.390578', '2.905137, 101.677160', '3.517828, 101.900402', '2.815510, 101.498527', 
              '5.726142, 100.510261', '4.472287, 101.037404', '3.484737, 102.350037', '5.171337, 100.477869', 
              '3.789439, 101.853587', '5.916335, 102.214399', '4.233735, 100.630448', '4.772207, 100.941900', 
              '2.218638, 102.198091', '2.266487, 102.281450', '2.801681, 101.796630', '2.268538, 102.540899', 
              '3.936554, 102.366655', '6.889470, 116.844672', '3.490114, 103.392606', '2.809882, 102.396563', 
              '2.051782, 102.666923', '6.325826, 99.844969', '4.115975, 101.282106', '2.130260, 111.524742', 
              '2.349884, 102.114899', '5.722118, 100.392378', '3.366510, 101.607005', '2.468052, 102.237294', 
              '4.172406, 101.197345', '5.130701, 100.488694', '1.246521, 111.454469', '5.462308, 100.382634', 
              '2.010742, 103.068337', '3.675912, 100.985425', '4.744346, 115.001928', '2.314298, 102.129679', 
              '2.245939, 102.248217', '2.883486, 101.503113', '4.512914, 103.446911', '5.447879, 100.305399', 
              '3.285342, 101.517530', '1.509135, 103.515767', '5.987414, 102.297651', '3.312107, 101.489875', 
              '2.659804, 101.564215', '2.426912, 103.834955', '2.385201, 103.021745', '5.206948, 103.205309', 
              '3.255824, 101.554280', '4.636765, 103.436538', '5.013243, 100.527234', '2.384545, 102.208206', 
              '3.382195, 101.419005', '3.003397, 101.395786', '5.470518, 100.249889', '4.880789, 101.964089', 
              '2.741951, 102.248646', '5.951456, 116.667792', '5.733695, 115.932742', '6.001634, 102.250963', 
              '6.106487, 100.294694', '4.308041, 101.149435', '6.049664, 102.141408', '1.827739, 103.298295', 
              '1.869368, 103.111003', '2.260183, 102.184348', '3.765769, 100.988252', '5.513266, 100.427297', 
              '3.425487, 101.186208', '4.456181, 100.626612', '5.816438, 100.474814', '5.353378, 115.745855', 
              '2.016907, 112.941330', '5.823094, 116.048297', '2.215134, 102.327890', '4.185383, 102.054926', 
              '6.299373, 99.721247', '2.269397, 102.376291', '6.402020, 100.136695', '2.650076, 101.702299', 
              '5.738042, 102.496706', '1.680095, 103.523240', '2.553305, 102.765363', '6.350239, 116.430836', 
              '3.349938, 101.818581', '6.197883, 102.166558', '2.358425, 102.036015', '5.315906, 100.439280', 
              '2.446942, 102.230118', '2.246170, 103.042407', '6.428995, 99.808533', '5.463150, 100.230763', 
              '6.349125, 99.731225', '5.889285, 118.041997', '4.471204, 101.379313']

destList = ['3.107233, 101.716458', '5.840197, 118.117920', '2.990069, 101.788762', '2.723786, 101.933958', 
            '3.819618, 103.329201', '4.263603, 117.892869', '5.330140, 103.140778', '4.414901, 114.009036', 
            '6.125749, 102.239295', '3.210444, 101.640261', '3.056805, 101.585511', '3.153324, 101.711964', 
            '3.047248, 101.448889', '1.495052, 103.755302', '3.151470, 101.733344', '4.591851, 101.083270', 
            '3.068606, 101.518284', '1.557182, 110.344245', '3.105812, 101.642622', '5.977959, 116.072507', 
            '5.416681, 100.330443', '1.426551, 103.640294', '2.195847, 102.240624', '6.122890, 100.368210', 
            '3.165693, 113.032241', '3.149915, 101.533260', '6.125754, 102.239283', '5.643556, 100.491401', 
            '4.847768, 100.737241', '5.363856, 100.455984', '2.692302, 101.750482', '2.290739, 111.826211', 
            '5.370810, 100.554666', '2.035350, 103.320477', '1.546578, 103.658887', '1.849845, 102.936100', 
            '1.472289, 103.878002', '5.326978, 100.273491', '5.479609, 100.498230', '2.042979, 102.566682', 
            '3.320358, 101.576594', '5.395304, 100.374842', '5.021606, 118.327585', '2.948370, 101.842916', 
            '2.522727, 101.794313', '4.250039, 103.416719', '5.883223, 116.050136', '5.328724, 116.155346', 
            '1.604337, 103.823814', '5.276699, 115.241726', '1.600549, 103.641700', '5.906962, 116.101450', 
            '2.506608, 102.815329', '3.033317, 101.750087', '5.377159, 100.383199', '6.438911, 100.194493', 
            '1.656816, 103.605962', '6.268484, 100.416835', '4.023588, 101.026412', '4.480221, 118.611795', 
            '2.995729, 101.566936', '3.450678, 102.417329', '3.217171, 101.316714', '2.436276, 102.184474', 
            '3.340646, 101.249437', '2.215250, 102.284654', '5.289057, 115.268602', '1.733122, 103.901405', 
            '1.486585, 103.389591', '2.906504, 101.676311', '3.516580, 101.900199', '2.816946, 101.499740', 
            '5.727557, 100.509467', '4.470656, 101.036626', '3.485599, 102.348476', '5.169676, 100.477756', 
            '3.791184, 101.853136', '5.915977, 102.216164', '4.232365, 100.630083', '4.772287, 100.940623', 
            '2.218600, 102.199507', '2.265568, 102.279923', '2.803095, 101.797058', '2.267097, 102.540108', 
            '3.936405, 102.366430', '6.889771, 116.842980', '3.490124, 103.393668', '2.808714, 102.395866', 
            '2.050002, 102.666681', '6.326540, 99.843188', '4.116704, 101.283299', '2.129727, 111.523015', 
            '2.349782, 102.116615', '5.720925, 100.392355', '3.365829, 101.606017', '2.467446, 102.235623', 
            '4.170972, 101.198364', '5.131610, 100.487127', '1.247449, 111.452929', '5.463322, 100.381631', 
            '2.010925, 103.066578', '3.677267, 100.986555', '4.745662, 115.002094', '2.312526, 102.129398', 
            '2.247251, 102.246996', '2.884922, 101.501998', '4.514281, 103.448053', '5.446088, 100.305227', 
            '3.285187, 101.518801', '1.509628, 103.513954', '5.987910, 102.295891', '3.310410, 101.490400', 
            '2.659868, 101.562913', '2.428001, 103.835771', '2.383665, 103.020858', '5.205645, 103.205920', 
            '3.255031, 101.553143', '4.637460, 103.436967', '5.011789, 100.527438', '2.382980, 102.209118', 
            '3.382511, 101.417804', '3.002473, 101.396872', '5.469012, 100.250849', '4.879442, 101.965285', 
            '2.742085, 102.249902', '5.951147, 116.666719', '5.733561, 115.931669', '6.000013, 102.250164', 
            '6.107226, 100.293738', '4.307517, 101.150768', '6.049575, 102.139858', '1.827911, 103.299674', 
            '1.867941, 103.112151', '2.259604, 102.183544', '3.767268, 100.987114', '5.514841, 100.427839', 
            '3.424004, 101.185194', '4.455123, 100.625861', '5.817722, 100.475383', '5.353116, 115.747276', 
            '2.016501, 112.939911', '5.823315, 116.046589', '2.213799, 102.327713', '4.186968, 102.054190', 
            '6.299980, 99.719984', '2.267918, 102.377053', '6.400730, 100.136239', '2.648924, 101.700947', 
            '5.737711, 102.495043', '1.679451, 103.524935', '2.553632, 102.763942', '6.349722, 116.429299', 
            '3.350166, 101.816752', '6.198534, 102.167566', '2.359154, 102.034684', '5.315817, 100.437417', 
            '2.445639, 102.230638', '2.245753, 103.041140', '6.430658, 99.809155', '5.464554, 100.229605', 
            '6.350010, 99.729996', '5.890725, 118.040887', '4.470504, 101.377731']


#########################################################################  Functions for collecting the data ##############################################

                           ### the function that searches weather by the name of the location    

def nonCoordinates(loclist):
    address = 'https://openweathermap.org/data/2.5/find?callback=?&q='+loclist+',MY&type=like&sort=population&cnt=30&appid=b6907d289e10d714a6e88b30761fae22'
    #print(loclist)
    data = requests.get(address).text
    #print(data)
    data = data.strip("?()")
    data=json.loads(data)
    
    info_1 = {}
   

    for val in data["list"]:
        info_1 = {"Returned Location"             : val['name'],
                  "Actual Location"               : loclist,
                  "Country"                       : val['sys']['country'],
                  "Latitude"                      : val["coord"]["lat"], 
                  "Longitude"                     : val["coord"]["lon"],
                  "Date"                          : datetime.today().strftime('%m/%d/%Y'),
                  "Time"                          : datetime.today().strftime('%H:%M:%S'),
                  "Clouds(%)"                     : val['clouds']['all'],
                  "Temparature(in celcius)"       : round((10*(val['main']["temp"] - 273.15))/10, 2), #ROUNDING TO 2 DECIMAL PLACES
                  "Max_temp"                      : round((10*(val['main']["temp_max"] - 273.15))/10, 2),
                  "Min_temp"                      : round((10*(val['main']["temp_min"] - 273.15))/10, 2), 
                  "Humidity(%)"                   : val['main']["humidity"],
                  "Pressure(hpa)"                 : val['main']["pressure"],
                  #"Rain"                          : val["rain"]["3h"],
                  "Wind_Speed(m/s)"               : val["wind"]['speed']}
                  #"Wind_Direction(in degree)"     : val["wind"]["deg"]}
        for item in  val["weather"]:
            info_1.update( {"Weather_Condition"   : item["main"],
                      "Weather_Description" : item["description"]})
    return info_1

                             ### the funciton that searches weather by using the co-ordinates of the locations

def coordinates(loclist):  
  
    address = 'http://api.openweathermap.org/data/2.5/weather?lat={0}&lon={1}&units=metric&appid={2}'
    appid = 'c9b9201a18e08ae3bb54d622f55c6c14'

    if loclist == 'Selayang Baru':
        lat =  3.2140
        lon =   101.6356
        address = address.format(lat,lon,appid)

    elif loclist == 'Pantai Cenang':
        lat =  6.2956 
        lon =   99.7228
        address = address.format(lat,lon,appid)

    elif loclist == 'Ayer Hangat':
        lat =  6.4252 
        lon =   99.8069
        address = address.format(lat,lon,appid)

    elif loclist == 'Telaga Batu':
        lat =  5.467
        lon =   100.233
        address = address.format(lat,lon,appid)

    elif  loclist == 'Padang Mat Sirat':
        lat =  6.352057
        lon =   99.733603
        address = address.format(lat,lon,appid)

    elif  loclist == 'Taman Rajawali':
        lat =  5.889618
        lon =   118.041484
        address = address.format(lat,lon,appid)
    else: 
        return {}

    #print(loclist)
    data = requests.get(address).text
    #print(data)
    data = data.strip("?()")
    data=json.loads(data)
    
    info_1 = {}
    
    
    info_1 = {"Returned Location"             : data['name'],
              "Actual Location"               : loclist,
              "Country"                       : data['sys']['country'],
              "Latitude"                      : data["coord"]["lat"], 
              "Longitude"                     : data["coord"]["lon"],
              "Date"                          : datetime.today().strftime('%m/%d/%Y'),
              "Time"                          : datetime.today().strftime('%H:%M:%S'),
              "Clouds(%)"                     : data['clouds']['all'],
              "Temparature(in celcius)"       : data['main']["temp"], 
              "Max_temp"                      : data['main']["temp_max"],
              "Min_temp"                      : data['main']["temp_min"], 
              "Humidity(%)"                   : data['main']["humidity"],
              "Pressure(hpa)"                 : data['main']["pressure"],
              #"Rain"                          : data["rain"]["3h"],
              "Wind_Speed(m/s)"               : data["wind"]['speed']}
              #"Wind_Direction(in degree)"     : val["wind"]["deg"]}
    for item in  data["weather"]:
        info_1.update( {"Weather_Condition"   : item["main"],
                  "Weather_Description" : item["description"]})
    
    return info_1


def trafficUpdate(originList, destList ):
    traf_dif = []
    traf_label = []
    i = 0
    #while i<=5:
    while i<=len(originList)-1:
        #print("\n", i, "\n")
        # Google Distance Matrix base URL to which all other parameters are attached
        base_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'


        # Prepare the request details for the assembly into a request URL
        payload = {
                    'origins'        :  originList[i],
                    'destinations'   :  destList[i], 
                    'departure_time' :  'now',
                    'key'            :  'AIzaSyDisMSJlHVoeHyK_h7eo8A2sqdaHk33Pcs'
                   }
        # Assemble the URL and query the web service
        req = requests.get(base_url, params = payload).text
        data=json.loads(req)
        #print(data)
        
        #iterating through the api data
        for item in data['rows']:
            for elm in item['elements']:
                #print(elm['duration']['value'])
                duration_val       =  elm['duration']['value']
                duration_val_traf  =  elm['duration_in_traffic']['value']
                difference         =  duration_val_traf - duration_val
                traf_dif.append(difference)
                #print(traf_dif)
                
        #labeling the traffic
        if traf_dif[i] <= -1:
            traf_label.append("GREEN")
            #print(traf_label)

        elif traf_dif[i] >= 0 and traf_dif[i] <= 7:
            traf_label.append("YELLOW")
            #print(traf_label) 
            
        elif traf_dif[i] >= 8:
            traf_label.append("RED")
            #print(traf_label)    
        
        #incrementing i
        i += 1
    #traffic = [traf_dif, traf_label]
    #print(traf_label)
    return  traf_label
        

#########################################################################  main to call the function ##############################################
    
r = 0
info_dict = {}
date = datetime.today()
#print(date)
while r <= len(loclist)-1 :  #put in len(loclist)-1 for ittarating all the locations
    info_dict[r]= nonCoordinates(loclist[r])
    if info_dict[r] == {}:
        #print("\nI am empty: ", loclist[r] )
        info_dict[r] = coordinates(loclist[r])
    
    r+=1
    #print(r,"\n")

traffic_label = trafficUpdate(originList, destList)    
pprint.pprint( info_dict) 
#print(traffic_label)

##################################################################### Printing the data as .csv ###################################################

df = pd.DataFrame.from_dict(info_dict)
df = df.T
df['Traffic_status'] = pd.DataFrame(np.array(traffic_label))
df.reindex()
df.notnull()
name = str(datetime.today()).split(" ")
date_str = name[0]
time_str = name[1].replace(":",".")
name = date_str+" " + time_str + ".csv"
#print(time_str)
df.to_csv(r'G:\\MovingWalls\\weather-traffic\\' + name) 


############################################################ END of script ##############################################################################
     
   


