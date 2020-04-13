import pandas as pd 
import plotly.offline as pyo 
import plotly.graph_objs as go 
from plotly import tools

data_path = [
    r'C:\Users\Phillip.Warther\Documents\Udemy_course\Plotly-Dashboards-with-Dash-master\Data\2010SantaBarbaraCA.csv',
    r'C:\Users\Phillip.Warther\Documents\Udemy_course\Plotly-Dashboards-with-Dash-master\Data\2010SitkaAK.csv',
    r'C:\Users\Phillip.Warther\Documents\Udemy_course\Plotly-Dashboards-with-Dash-master\Data\2010YumaAZ.csv'
    ]
dframe = [ pd.read_csv( path ) for path in data_path]

data = [go.Heatmap(
    x= df['DAY'],
    y= df['LST_TIME'],
    z= df['T_HR_AVG'].values.tolist(),
    colorscale='Jet',
    zmin=5,
    zmax=40
    ) for df in dframe]


figure = tools.make_subplots(
    rows = 1 ,
    cols = 3 ,
    subplot_titles=['Santa Barbara','Sitka','Yuma'],
    shared_yaxes=True
)

for i, d in enumerate(data):
    figure.append_trace( d , 1 , i+1)

figure['layout'].update( title='Average Temp by Hour')

pyo.plot( figure , filename='mySubPlotHeatmap.html')