import plotly.graph_objs as go 
import plotly.offline as pyo 
import pandas as pd 

data_path = r'C:\Users\Phillip.Warther\Documents\Udemy_course\Plotly-Dashboards-with-Dash-master\Data\abalone.csv'
dframe      = pd.read_csv(data_path)

data = [go.Histogram( 
    x=dframe['length'], 
    xbins=dict(
        start=0 ,
        end=1,
        size=0.02

    ))]

layout = go.Layout( title='Abalone Length')
figure = go.Figure( data=data , layout=layout)

pyo.plot(figure,filename='nyHistogram.html')