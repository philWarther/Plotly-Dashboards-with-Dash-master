import plotly.graph_objs as go 
import plotly.offline as pyo 
import plotly.figure_factory as ff 
import pandas as pd

data_path   = r'C:\Users\Phillip.Warther\Documents\Udemy_course\Plotly-Dashboards-with-Dash-master\Data\iris.csv'
dframe      = pd.read_csv( data_path)

classes     = dframe['class'].unique()

hist_data       = [ dframe[ dframe['class']==c]['petal_length'] for c in classes]
group_labels    = [c.split('-')[-1] for c in classes ]

figure = ff.create_distplot( 
    hist_data=hist_data,
    group_labels=group_labels,
    bin_size=[.2 for c in classes])

pyo.plot( figure , filename='myDistPlot.html')