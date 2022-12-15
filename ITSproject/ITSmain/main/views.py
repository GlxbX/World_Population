from django.db import connection
import plotly.graph_objs as gobj 
import pandas as pd
from requests import request
from django.http.response import JsonResponse
import json
from .models import Population_by_countries as PBC
from .models import World_population as WP
from abc import ABCMeta, abstractmethod


class PlotlyChart(metaclass=ABCMeta):
    def __init__(self, model):
        pass

    @abstractmethod
    def construct_data(self):
        pass

    @abstractmethod
    def construct_layout(self):
        pass

    @abstractmethod
    def get_final_chart_in_json(self):
        pass

class GeomapChart(PlotlyChart):
    def __init__(self,model):
        self._model = model
        self._df = pd.DataFrame(list(self._model.objects.all().values()))
        self._df = self._df.pivot_table('data', ['country_name', 'code'], 'year')
        self._df.reset_index( drop=False, inplace=True )

    def construct_data(self):
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
        locations = self._df['code'], 
        locationmode = 'ISO-3', 
        colorscale = scl, 
        autocolorscale=False,
        text = self._df['country_name'], 
        z = self._df[1800], 
        colorbar = {'title_text':'Population', 'title_font_color':'white', 'len':400, 'lenmode':'pixels','tickfont_color':'white'},
        )
        return data

    def construct_layout(self):
        sliders = [dict(active=0,
                        currentvalue={"prefix": "Population in "},
                        pad={"t": 50},
                        steps=self.get_steps(),
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
        return layout
    
    def get_final_chart_in_json(self):
        geomap = gobj.Figure(data=self.construct_data(), layout=self.construct_layout()).to_json()
        return geomap

    def get_steps(self):
        steps = []
        for i in range(222):
            step = dict(method='restyle',
                args=[{  'z': [self._df[i + 1800]] }],
                label=i + 1800,
                )

            steps.append(step)
        return steps

class WorldLineChart(PlotlyChart):
    def __init__(self,model):
        self._model = model
        self._df = pd.DataFrame(list(self._model.objects.all().values()))


    def construct_data(self):
        x_data = self._df['year']
        y_data = self._df['data']
        data = dict(
            x=x_data,y=y_data
        )
        return data

    def construct_layout(self):
        layout = dict(
            title='World population 1800-2021',
            xaxis_title='Year',
            yaxis_title='Population'
        )
        return layout

   
    def get_final_chart_in_json(self):
        world_line_chart = gobj.Figure(data=self.construct_data(), layout=self.construct_layout()).to_json()
        return world_line_chart



def IpadGeoMapView(request):

    Chart = GeomapChart(PBC)
    geomap = Chart.get_final_chart_in_json()

    if request.method == 'GET':
        return JsonResponse(geomap, safe=False)

def WorldLineChartView(request):

    Chart = WorldLineChart(WP)
    world_line_chart = Chart.get_final_chart_in_json()

    if request.method == 'GET':
        return JsonResponse(world_line_chart, safe=False)
        