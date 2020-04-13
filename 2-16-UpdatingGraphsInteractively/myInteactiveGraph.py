import plotly.graph_objs as go 
import dash
from dash.dependencies import Input , Output
import dash_core_components as dcc 
import dash_html_components as html 
import pandas as pd 
from numpy import random 

data_path = '../Data/mpg.csv'
dframe = pd.read_csv( data_path )
# add some jitter
dframe['year'] = random.uniform(low=-.5 , high=.5 , size=len(dframe)) + dframe['model_year']

app = dash.Dash()

app.layout = html.Div(
    [ html.Div(
        [dcc.Graph(
            id='mpg_scatter',
            figure = {
                'data':[
                    go.Scatter(
                        x=dframe['year'] + 1900,
                        y=dframe['mpg'],
                        text=dframe['name'],
                        hoverinfo='text + y + x',
                        mode='markers'
                    )
                ],
                'layout':go.Layout(
                    title='MPG Data',
                    xaxis={'title':'Model Year'},
                    yaxis={'title':'Miles/Gallon'},
                    hovermode='closest'
                )
            }
        )], style={'width':'50%', 'display':'inline-block '}),
    html.Div(
        [
            dcc.Graph(
                id='mpg_line',
                figure={
                    'data':[go.Scatter(
                        x=[0,1],
                        y=[0,1],
                        mode='lines')],
                    'layout':go.Layout(
                        title='Acceleration',
                        margin={'l':0}
                    )})], style={'width':'30%','display':'inline-block'} ),
    html.Div(
        [
            dcc.Markdown(
                id='mpg_stats',
                style={'width':'30%','display':'inline-block'}
            )
        ]
    )
        ]
    )    


@app.callback(
    Output('mpg_line','figure'),
    [Input('mpg_scatter','hoverData')]
)

def callback_graph(hoverData):
    v_index = hoverData['points'][0]['pointIndex']
    figure = {
        'data':[
            go.Scatter(
                x = [0,1],
                y = [0 , 60/dframe.iloc[v_index]['acceleration']],
                mode = 'lines',
                line={'width':2*dframe.iloc[v_index]['cylinders']}
            )],
        'layout':go.Layout(
            title = dframe.iloc[v_index]['name'],
            xaxis = {'visible':False},
            yaxis = {'visible':False, 'range':[0,60/dframe['acceleration'].min()]},
            margin = {'l':0},
            height = 300
            
        )
    }
    return figure 

@app.callback(
    Output('mpg_stats', 'children'),
    [Input('mpg_scatter','hoverData')]
)

def callback_stats( hoverData ):
    v_index = hoverData['points'][0]['pointIndex']
    stats = """
            {} cylinders\n
            {}cc displacement\n
            0 - 60 mph in {} seconds\n
    """.format(
        dframe.iloc[v_index]['cylinders'],
        dframe.iloc[v_index]['displacement'],
        dframe.iloc[v_index]['acceleration']
    )
    return stats


if __name__ == '__main__':
    app.run_server()