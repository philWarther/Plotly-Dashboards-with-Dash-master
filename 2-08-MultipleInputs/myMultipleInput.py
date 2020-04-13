import pandas as pd 
import dash 
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input, Output 
import plotly.graph_objs as go 

data_path = r'C:\Users\Phillip.Warther\Documents\Udemy_course\Plotly-Dashboards-with-Dash-master\Data\mpg.csv'
dframe = pd.read_csv( data_path )

app = dash.Dash()

features = [ x for x in dframe.columns if x !='name']


app.layout = html.Div(
    [
        html.Div(
            [
                dcc.Dropdown(
                    id='xaxis',
                    options = [ {'label':i.title() , 'value':i } for i in features],
                    value = 'displacement'
                )
            ],style={'width':'48%', 'display':'inline-block'},
            title='x axis values'
        ),
        html.Div(
            [
                dcc.Dropdown(
                    id='yaxis',
                    options = [ {'label':i , 'value':i } for i in features],
                    value = 'mpg'

                )
            ],style={'width':'48%', 'display':'inline-block'},
            title='y axis values'
        ),
        dcc.Graph(
            id='feature-graphic'
        )
    ],style={'padding':10}
)

@app.callback(
    Output('feature-graphic', 'figure'),
    [Input('xaxis','value'), Input('yaxis','value')]
)
def update_graph( xaxis_name , yaxis_name ):
    data = [go.Scatter(
        x= dframe[xaxis_name],
        y= dframe[yaxis_name],
        mode='markers',
        text=dframe['name'],
        marker=dict(size=15,opacity=0.5)
    )]
    layout = go.Layout(
        title='MPG Dashboard',
        xaxis=dict(
            title=xaxis_name
        ),
        yaxis=dict(
            title=yaxis_name
        ),
        hovermode='closest'
    )
    return{
        'data': data ,
        'layout': layout 
        }

if __name__ == '__main__':
    app.run_server()
