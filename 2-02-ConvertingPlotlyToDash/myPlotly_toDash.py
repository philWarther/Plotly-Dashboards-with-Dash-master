import dash 
import dash_core_components as dcc 
import dash_html_components as html 
import plotly.graph_objs as go 
import numpy as np 

"""
This is a basic implementation of inserting a plotly scatter plot into a Dash dashboard
"""

app = dash.Dash()

# Define data
np.random.seed( 42 )
random_x = np.random.randint( 1 , 101 , 100 )
random_y = np.random.randint( 50 , 151 , 100 )

# Define Plotly Graph objects
data_list = [
    go.Scatter(
    x=random_x,
    y=random_y,
    mode='markers',
    marker = dict(
        size=12,
        color='rgb( 51,204,153)',
        symbol='pentagon',
        line={'width':2}
    )
)]

layout_01 = go.Layout(
    title='My Scatter Plot',
    xaxis={'title':'X Title'},
    yaxis={'title':'Y Title'})

# Define Dash application layout
app.layout = html.Div(
     dcc.Graph(
          id='plot_01', 
          figure=dict(
              data=data_list,
              layout=layout_01
          )))

if __name__ == '__main__':
    app.run_server()