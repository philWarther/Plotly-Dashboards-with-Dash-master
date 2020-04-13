import plotly.graph_objs as go
import plotly.offline as pyo 
import pandas as pd

# set up an array of 20 data points, with 20 as the median value
y = [1,14,14,15,16,18,18,19,19,20,20,23,24,26,27,27,28,29,33,54]


data = [go.Box(
    y=y,
    boxpoints='outliers',
    jitter=0.2 ,
    pointpos= 0.0,
    name='test data'
)]

pyo.plot(data , filename='myBoxPlot.html')
