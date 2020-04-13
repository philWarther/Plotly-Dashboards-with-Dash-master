import pandas as pd 
import plotly.offline as pyo 
import plotly.graph_objs as go 

data_path = r'C:\Users\Phillip.Warther\Documents\Udemy_course\Plotly-Dashboards-with-Dash-master\Data\2010SantaBarbaraCA.csv'
dframe = pd.read_csv( data_path )

data = [go.Heatmap(
    x= dframe['DAY'],
    y= dframe['LST_TIME'],
    z= dframe['T_HR_AVG'].values.tolist(),
    colorscale='jet'
)]

layout = go.Layout( title='Santa Barbara Temp')
figure = go.Figure( data=data)

pyo.plot( figure , filename='myHeatmap.html')