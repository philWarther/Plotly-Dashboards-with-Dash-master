import plotly.graph_objs as go
import plotly.offline as pyo 
import pandas as pd

snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]


data = [go.Box(
    y=snodgrass,
    boxpoints='outliers',
    jitter=0.2 ,
    pointpos= 0.0,
    name='snodgrass'
    ),
    go.Box(
        y=twain,
        boxpoints='outliers',
        name='Twain'
    )]

pyo.plot(data , filename='myBoxPlot.html')
