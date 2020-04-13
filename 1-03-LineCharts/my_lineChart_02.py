import pandas as pd 
import plotly.offline as pyo 
import plotly.graph_objects as go 

dframe = pd.read_csv( '../SourceData/nst-est2017-alldata.csv')
dframe2 = dframe[ dframe['DIVISION'] == '1']
dframe2.set_index('NAME', inplace=True)

dframe3 = dframe2[ [col for col in dframe2.columns if col.startswith( 'POP')]]
dframe3.columns = [col[-4:] for col in dframe3.columns]
data = [ go.Scatter( 
    x=dframe3.columns , 
    y=dframe3.loc[state] , 
    mode='lines+markers' , 
    name= state ) 
    for state in dframe3.index ]

figure = go.Figure( data=data )
pyo.plot( figure , filename='my_lineChart_pd.html')