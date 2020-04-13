import dash
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input, Output
import plotly.graph_objs as go 
import base64
import pandas as pd 
import os 
from numpy import arange


slider = html.Div([
    dcc.RangeSlider(
        id='slider', 
        min=-5,
        max=5,
        step=1.0,
        value = [ -2 , 2 ],
        marks = {int(i):i for i in arange(-5, 6 , step=1)}
    )
], style={'width':'50%'})

output = html.Div(id='output')

app = dash.Dash()

app.layout = html.Div(
    children = [ slider , output]
)

@app.callback(
    Output( 'output', 'children' ),
    [Input('slider','value')]
)
def multiply_slider(values):
    mul = values[0]*values[1]

    return html.H5( str(mul)) 

if __name__ == '__main__':
    app.run_server()
