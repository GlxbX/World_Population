from django.db import connection
import plotly.graph_objs as gobj 
import pandas as pd
from requests import request
from django.http.response import JsonResponse
import json
from .models import Population_by_countries as PBC


def IpadGeoMapView(request):
    def get_steps():
        steps = []
        for i in range(222):
            step = dict(method='restyle',
                args=[{  'z': [df[i + 1800]] }],
                label=i + 1800,
                )

            steps.append(step)
      


        return steps


    df = pd.DataFrame(list(PBC.objects.all().values()))

    df = df.pivot_table('data', ['country_name', 'code'], 'year')

    df.reset_index( drop=False, inplace=True )

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

    

    data = dict(
        type = 'choropleth', 
    locations = df['code'], 
    locationmode = 'ISO-3', 
    colorscale = scl, 
    autocolorscale=False,
    text = df['country_name'], 
    z = df[1800], 
    colorbar = {'title_text':'Population', 'title_font_color':'white', 'len':400, 'lenmode':'pixels','tickfont_color':'white'},
    )


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
        margin ={'l':115,'r':0,'b':50,'t':50},
        sliders=sliders
        ) 

    
    geomap = gobj.Figure(data=data, layout=layout).to_json() 


    if request.method == 'GET':
        return JsonResponse(geomap, safe=False)


        