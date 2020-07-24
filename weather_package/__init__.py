import requests
import pandas as pd
def forecast():
    print("Welcome to the Weather Forecasting Platform")
    city=input("Enter the City Name you want the forecast for: ")
    
    url='http://api.openweathermap.org/data/2.5/forecast?units=metric&appid=5f1aaab27154e9d7a4c6e81336e9266a&q='
    
    resurl = url + city
    
    weather=requests.get(resurl).json()
    ls={}
    for x in range(len(weather.get('list'))):
        ls[weather.get('list')[x].get('dt_txt')]=[weather.get('list')[x].get('main').get('temp'),
                                                 weather.get('list')[x].get('main').get('feels_like'),
                                                 weather.get('list')[x].get('main').get('temp_min'),
                                                 weather.get('list')[x].get('main').get('temp_max'),
                                                 weather.get('list')[x].get('main').get('pressure'),
                                                 weather.get('list')[x].get('main').get('sea_level'),
                                                 weather.get('list')[x].get('main').get('humidity'),
                                                 weather.get('list')[x].get('weather')[0].get('main'),
                                                 weather.get('list')[x].get('weather')[0].get('description'),
                                                 weather.get('list')[x].get('clouds').get('all'),
                                                 weather.get('list')[x].get('wind').get('speed'),
                                                 weather.get('list')[x].get('visibility'),
                                                 weather.get('list')[x].get('rain')]

    col_name=['Temp','Feels_Like','Temp_Min','Temp_Max','Pressure','Sea_Level','Humidity','Weather_Con','Description','Clouds','Wind_Speed','Visibility','Rain']
    df= pd.DataFrame(ls)
    df_t=df.T
    df_t.columns=col_name
    df_t.fillna('Not Available',inplace=True)
    return df_t
    
