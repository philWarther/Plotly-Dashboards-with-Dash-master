import dash 
import dash_core_components as dcc 
import dash_html_components as html 
import plotly.graph_objs as go 
import pandas as pd 

"""
This is a basic implementation of inserting a plotly scatter plot into a Dash dashboard
"""

# Define data
data_path = r'C:\Users\Phillip.Warther\Documents\Udemy_course\Plotly-Dashboards-with-Dash-master\Data\OldFaithful.csv'
dframe = pd.read_csv( data_path )

"""
x=X
y=Y (Duration)
hover = date
"""

data = [go.Scatter(
    x=dframe['X'],
    y=dframe['Y'],
    mode='markers'
)]

layout = go.Layout(
    title='Old Faithful Eruption Intervals v Durations',
    xaxis={'title':'Duration of eruption (in minutes)'},
    yaxis={'title':'Interval until next eruption (in minutes) '}
)

# Defining Dash application

app = dash.Dash()

app.layout = html.Div([
     dcc.Graph(
          id='plot_01', 
          figure=dict(
              data=data,
              layout=layout)
              )
])
if __name__ == '__main__':
    app.run_server()