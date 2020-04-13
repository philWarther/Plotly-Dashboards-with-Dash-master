import pandas as pd 
import plotly.offline as pyo 
import plotly.graph_objects as go 

data_path = 'C:/Users/Phillip.Warther/Documents/Udemy_course/Plotly-Dashboards-with-Dash-master/Data/mpg.csv'
dframe = pd.read_csv( data_path )

data = [
    go.Scatter(
        x=dframe.groupby('model_year')['weight'].max().index, 
        y=dframe.groupby('model_year')['weight'].max().values,
        name='Maximum Weight',
        mode='lines' 
    ),
    go.Scatter(
        x=dframe.groupby('model_year')['weight'].mean().index, 
        y=dframe.groupby('model_year')['weight'].mean().values,
        name='Mean Weight',
        mode='lines' 
    ),
    go.Scatter(
        x=dframe.groupby('model_year')['weight'].min().index, 
        y=dframe.groupby('model_year')['weight'].min().values,
        name='Minimum Weight',
        mode='lines' 
    ),
    go.Scatter(
        x=dframe['model_year'],
        y=dframe['weight'] ,
        text=dframe['name'] ,
        mode='markers',
        name='Data',
        marker=dict(size=20*dframe['mpg']/dframe['mpg'].max() ,
                    color=dframe['displacement'],
                    showscale=False) 
    )
]
    

layout = go.Layout( title='Bubble Chart',showlegend=True)
figure = go.Figure( data=data , layout=layout)

pyo.plot( figure , filename='myBubbleChart.html')