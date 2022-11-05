from django.db import connection
import plotly.graph_objs as gobj 
import pandas as pd
from requests import request
from django.http.response import JsonResponse



def IpadGeoMapView(request):

    def getSliders():
        steps = []
        for i in range(18):
            step = dict(method='restyle',
                        args=[{'z': [df['year{}'.format(i + 2000)]]}],
                        label='{}'.format(i + 2000)
                        )
        
            steps.append(step)

        sliders = [dict(active=0,
                        currentvalue={"prefix": "Ipad index in "},
                        pad={"t": 50},
                        steps=steps,
                        font={'color':'white'}) ]
        return sliders

    #SQLquery
    qry = 'SELECT main_Ipad.year2000, main_Ipad.year2001, main_Ipad.year2002, main_Ipad.year2003, main_Ipad.year2004, main_Ipad.year2005, main_Ipad.year2006, main_Ipad.year2007, main_Ipad.year2008, main_Ipad.year2009, main_Ipad.year2010, main_Ipad.year2011, main_Ipad.year2012, main_Ipad.year2013, main_Ipad.year2014, main_Ipad.year2015, main_Ipad.year2016,main_Ipad.year2017,main_Ipad.avg1, main_Ipad.avg2, main_Country.country_name FROM main_Ipad, main_Country WHERE main_Ipad.country_id = main_Country.id'

    #Dataframe
    df = pd.read_sql_query(qry, connection)


    data = dict(
        type = 'choropleth', 
    locations = df['country_name'], 
    locationmode = 'country names', 
    colorscale = 'Greens', 
    text = df['country_name'], 
    z =df['year2000'] , 
    colorbar = {'title_text':'Ipad index', 'title_font_color':'white', 'len':200, 'lenmode':'pixels','tickfont_color':'white'},
    )

    sliders = getSliders()
   
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
        margin ={'l':115,'r':0,'b':150,'t':50},
        sliders=sliders
        ) 

    geomap = gobj.Figure(data=[data], layout=layout).to_json() 

    if request.method == 'GET':
        return JsonResponse(geomap, safe=False)

        
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

    sliders = [dict(active=0,
                        currentvalue={"prefix": "Population in "},
                        pad={"t": 50},
                        steps=get_steps(),
                        font={'color':'white'}) ]
   
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
        margin ={'l':115,'r':0,'b':150,'t':50},
        sliders=sliders
        ) 

    geomap = gobj.Figure(data=data_slider, layout=layout).to_json() 

    if request.method == 'GET':
        return JsonResponse(geomap, safe=False)

