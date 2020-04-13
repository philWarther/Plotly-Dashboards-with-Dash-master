import pandas as pd 
import plotly.offline as pyo 
import plotly.graph_objects as go 

data_path = 'C:/Users/Phillip.Warther/Documents/Udemy_course/Plotly-Dashboards-with-Dash-master/Data/2010YumaAZ.csv'
dframe = pd.read_csv( data_path )
days = list( dframe.DAY.unique() )

data = [ go.Scatter(
    x= dframe[ dframe['DAY'] == day ]['LST_TIME'],
    y= dframe[ dframe['DAY'] == day ]['T_HR_AVG'],
    mode='lines+markers',
    name= day )
    for day in days
]

layout = go.Layout( title='Daily Temerature From Jun 1 - 7 in Yuma, Arizona')
figure = go.Figure( data=data , layout=layout)

pyo.plot( figure , filename='myLineChartExercise.html' )