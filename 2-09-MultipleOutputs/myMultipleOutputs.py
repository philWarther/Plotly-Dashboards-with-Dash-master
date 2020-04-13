import dash
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input, Output
import plotly.graph_objs as go 
import base64
import pandas as pd 
import os 



data_path = r'C:\Users\Phillip.Warther\Documents\Udemy_course\Plotly-Dashboards-with-Dash-master\Data\wheels.csv'
dframe = pd.read_csv( data_path )

app = dash.Dash()

def encode_image( image_file ):
    encoded = base64.b64encode(open(image_file,'rb').read() )
    return 'data:image/png;base64,{}'.format( encoded.decode() )


app.layout = html.Div([
    dcc.RadioItems(
        id='wheels',
        options=[{'label':i , 'value':i } for i in dframe['wheels'].unique() ] ,
        value=1),
    html.Div(id='wheels-out'),
    html.Hr(),
    dcc.RadioItems(
        id='colors',
        options=[{'label':i , 'value':i } for i in dframe['color'].unique() ] ,
        value='blue'),
    html.Div(id='colors-out'),
    html.Img(
        id='display-image',
        src='children',
        height=300
    )
], style=dict(
    fontFamily='helvetica',
    fontSize=18
))

@app.callback(
    Output('wheels-out', 'children'),
    [Input('wheels', 'value')]
)
def callback_a(wheels_value):
    return 'You chose {}'.format( wheels_value )

@app.callback(
    Output('colors-out', 'children'),
    [Input('colors', 'value')]
)
def callback_b(colors_value) :
    return 'You chose {}'.format( colors_value)    


@app.callback(
    Output('display-image', 'src'),
    [Input('wheels', 'value'),
    Input('colors', 'value')]
)
def callback_image(wheels_value,colors_value):
    path = os.path.join( 
        '../data/images/', 
        dframe[(dframe['wheels'] == wheels_value) & (dframe['color'] == colors_value )]['image'].values[0] )
    return encode_image( path )



if __name__ == '__main__':
    app.run_server()