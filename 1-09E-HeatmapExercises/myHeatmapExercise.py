import pandas as pd 
import plotly.graph_objs as go 
import plotly.offline as pyo 
from plotly import tools 

data_path = r'C:\Users\Phillip.Warther\Documents\Udemy_course\Plotly-Dashboards-with-Dash-master\Data\flights.csv'
dframe = pd.read_csv( data_path )

data = [ go.Heatmap(
    x=dframe['year'],
    y=dframe['month'] ,
    z=dframe['passengers']
)]
layout = go.Layout(title='plane stuff')
figure = go.Figure( data=data , layout=layout)

pyo.plot( figure , filename='myHeatmapExcercise.py')