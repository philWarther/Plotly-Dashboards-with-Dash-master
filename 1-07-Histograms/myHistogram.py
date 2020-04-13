import plotly.graph_objs as go 
import plotly.offline as pyo 
import pandas as pd 

data_path = r'C:\Users\Phillip.Warther\Documents\Udemy_course\Plotly-Dashboards-with-Dash-master\Data\mpg.csv'
dframe      = pd.read_csv(data_path)

data = [go.Histogram( 
    x=dframe['mpg'], 
    xbins=dict(
        start=0 ,
        end=50,
        size=2

    ))]

layout = go.Layout( title='Miles Per Gallon')
figure = go.Figure( data=data , layout=layout)

pyo.plot(figure,filename='nyHistogram.html')