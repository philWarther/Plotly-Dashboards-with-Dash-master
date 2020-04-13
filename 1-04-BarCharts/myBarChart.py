import pandas as pd 
import plotly.offline as pyo 
import plotly.graph_objects as go 


data_path = 'C:/Users/Phillip.Warther/Documents/Udemy_course/Plotly-Dashboards-with-Dash-master/Data/2018WinterOlympics.csv'
dframe = pd.read_csv( data_path )

data = [ go.Bar(
    x= dframe['NOC'],
    y= dframe[x[0]],
    name= x[0] +' medals',
    marker = dict( color=x[1] )

) for x in [('Gold', '#FFD700'), ('Silver','#9EA0A1') , ('Bronze', '#CD7F32')]]

layout = go.Layout( title='Medals by type',barmode='stack')

figure = go.Figure( data=data , layout=layout )
pyo.plot( figure , filename='myBarChart.html' )
