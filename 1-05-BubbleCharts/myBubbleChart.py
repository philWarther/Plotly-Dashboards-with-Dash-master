import pandas as pd 
import plotly.offline as pyo 
import plotly.graph_objects as go 

data_path = 'C:/Users/Phillip.Warther/Documents/Udemy_course/Plotly-Dashboards-with-Dash-master/Data/mpg.csv'
dframe = pd.read_csv( data_path )

data = [go.Scatter(
    x=dframe['horsepower'],
    y=dframe['mpg'] ,
    text=dframe['name'] ,
    mode='markers',
    marker=dict(size=20*dframe['weight']/dframe['weight'].max() ,
                color=dframe['cylinders'],
                showscale=True) 
)]

layout = go.Layout( title='Bubble Chart')
figure = go.Figure( data=data , layout=layout)

pyo.plot( figure , filename='myBubbleChart.html')