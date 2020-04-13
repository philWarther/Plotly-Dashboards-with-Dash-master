import plotly.graph_objs as go
import plotly.offline as pyo 
import pandas as pd

data_path = r'C:\Users\Phillip.Warther\Documents\Udemy_course\Plotly-Dashboards-with-Dash-master\Data\abalone.csv'
dframe = pd.read_csv( data_path )

data = [go.Box(
    y= dframe['rings'].sample( 30 ),
    boxpoints='outliers',
    jitter=0.2 ,
    pointpos= 0.0,
    name='Random Sample {}'.format(i)
    ) for i in range(3)
]

pyo.plot(data , filename='myBoxPlot.html')
