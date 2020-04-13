import plotly.graph_objs as go 
import plotly.offline as pyo 
import plotly.figure_factory as ff 
import numpy as np 

snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]

hist_data=[snodgrass,twain]
group_data=['Snodgrass','Twain']

figure = ff.create_distplot( 
    hist_data=hist_data,
    group_labels=group_data ,
    bin_size=[ 0.005 for i in range( len(hist_data))])

pyo.plot( figure , filename='myDistPlot_02.html')