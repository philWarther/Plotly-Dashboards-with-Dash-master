import plotly.graph_objs as go 
import plotly.offline as pyo 
import plotly.figure_factory as ff 
import numpy as np 

hist_data   = [np.random.randn( 100*(i+1) ) + 2*i for i in range(4)]
group_data  = ['Data Sample {}'.format( i+1) for i in range(4)]

figure = ff.create_distplot( 
    hist_data=hist_data,
    group_labels=group_data,
    bin_size=[.2 for i in range(4)])

pyo.plot( figure , filename='myDistPlot.html')