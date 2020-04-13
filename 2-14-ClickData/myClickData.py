import pandas as pd 
import dash 
import dash_core_components as dcc 
import dash_html_components as html 
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State 
import json 
import base64
import os

data_path = r'C:\Users\Phillip.Warther\Documents\Udemy_course\Plotly-Dashboards-with-Dash-master\Data\wheels.csv'
dframe = pd.read_csv( data_path )

app = dash.Dash()

app.layout = html.Div(
    [
        html.Div(
            dcc.Graph(
                id='wheels-plot',
                figure={
                    'data':[
                        go.Scatter(
                            x=dframe['color'],
                            y=dframe['wheels'],
                            dy=1,
                            mode='markers',
                            marker={
                                'size':15
                            }
                        )
                    ],
                    'layout': go.Layout(
                        title='Test',
                        hovermode='closest'
                    )}
            ), style={'display':'inline-block','vertical-align':'top', 'float':'left'}
        ),
        html.Div(
            html.Img(
                id='hover-data',
                src='children',
                height=300,
                width='auto',
                style={'paddingTop':'35'}
            ),
            style={'width':'30%', 'display':'inline-block', 'vertical-align':'top'}
        )
    ]
)

def encode_image( image_file ):
    encoded = base64.b64encode( open( image_file , 'rb' ).read() )
    return 'data:image/png;base64,{}'.format( encoded.decode() )


@app.callback(
    Output('hover-data','src'),
    [Input('wheels-plot','clickData')]
)
def callback_image(clickData):
    wheel = clickData['points'][0]['y']
    color = clickData['points'][0]['x']
    path = './data/images/'
    image_file = dframe[ (dframe['wheels'] == wheel) & (dframe['color'] == color)]['image'].values[0]

    return encode_image( os.path.join( path , image_file ))

if __name__ =='__main__':
    app.run_server()