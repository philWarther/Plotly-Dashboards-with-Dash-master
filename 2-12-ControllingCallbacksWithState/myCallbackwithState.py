import dash
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input, Output, State 
import plotly.graph_objs as go 
import base64
import pandas as pd 
import os 
from numpy import arange

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(
        id='number-in',
        value=1,
        style={'fontsize':24}),
    html.Button(
        id='submit',
        n_clicks=0 ,
        children='Submit',
        style={'fontsize':24}),
    html.H1(id='number-out')
])

@app.callback(
    Output('number-out','children'),
    [Input('submit','n_clicks')],
    [State('number-in','value')]
)


def output(n_clicks,number):
    return '{} was typed, and button was clicked {} times'.format( number , n_clicks)


if __name__ == '__main__':
    app.run_server()
