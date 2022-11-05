from django.db import connection
import plotly.graph_objs as gobj 
import pandas as pd
from requests import request
from django.http.response import JsonResponse
import json

def IpadGeoMapView(request):
    def get_steps():
        steps = []
        for i in range(len(data_slider)):
            step = dict(method='restyle',
                args=['visible', [False] * len(data_slider)],
                label=i + 1800)

            step['args'][1][i] = True
            steps.append(step)


        return steps

    #SQLquery
    qry = 'SELECT main_population_by_countries.country_name, main_population_by_countries.code, main_population_by_countries.year, main_population_by_countries.data from main_population_by_countries'

    #Dataframe
    df = pd.read_sql_query(qry, connection)

    scl = [ 
            [0, '#ffffff'],
            [0.002, '#eefbe9'],
            [0.0066, '#def6d5'],
            [0.02, '#cef0c2'],
            [0.066, '#b0e59f'],
            [0.2, '#94d881'],
            [0.66, '#6dc35a'],
            [1, '#008000'],
            ]

    year = 1800
    data_slider = []
    for year in df['year'].unique():
   
        df_segmented =  df[(df['year']== year)]

        
        high = df_segmented['data'].sort_values(ascending=False).iloc[0]
       
        data_each_yr = dict(
                        type='choropleth',
                        locations = df_segmented['code'],
                        z=df_segmented['data'],
                        locationmode='ISO-3',
                        colorscale = scl,
                        autocolorscale=False,
                        colorbar = dict(title_text='Population',
                                        title_font_color = 'white',
                                        len=400,
                                        lenmode='pixels',
                                        tickfont_color='white',
                                        tickmode = 'array',
                                        tickvals = [i for i in range(0,high,100*10**6)]
                                                                                    ))
                     

        data_slider.append(data_each_yr)


   
    layout = dict(
        geo = {
        'scope':'world','showframe':True,
        'showcoastlines':True,
        'projection_type':'equirectangular',
        'bgcolor':'LightBlue'
        },
        paper_bgcolor='rgb(29,32,62)',
        height = 635,
        width = 1488,
        margin ={'l':115,'r':0,'b':50,'t':50},
        ) 

    f = [gobj.Figure(data=data_slider[i],layout=layout).to_json() for i in range(221)]
    
    geomap = gobj.Figure(data=data_slider, layout=layout).to_json() 


    if request.method == 'GET':
        return JsonResponse(json.dumps(f), safe=False)
