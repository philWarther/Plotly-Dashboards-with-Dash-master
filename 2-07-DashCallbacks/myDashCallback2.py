import dash
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input, Output
import plotly.graph_objs as go 

import pandas as pd 

data_path = r'C:\Users\Phillip.Warther\Documents\Udemy_course\Plotly-Dashboards-with-Dash-master\Data\gapminderDataFiveYear.csv'
dframe = pd.read_csv( data_path)

app = dash.Dash()
year_options = [{'label':str(year) , 'value':year} for year in dframe['year'].unique()]

app.layout = html.Div(
    [
        dcc.Graph(id='graph'),
        dcc.Dropdown(
            id='year-picker', # the input function of the callback points here
            options=year_options,
            value= dframe['year'].min() # the input function of the callback grabs this value by name
            )
            
    ]

)
@app.callback(
    Output('graph','figure'), # this point the update to id:'graph', 
    [Input('year-picker','value')]
)
def update_figure( selected_year):
    filtered_dframe = dframe[ dframe['year'] == selected_year ]
    data = [go.Scatter(
        x = filtered_dframe[ filtered_dframe['continent'] == continent_name ]['gdpPercap'] , 
        y = filtered_dframe[ filtered_dframe['continent'] == continent_name ]['lifeExp'],
        mode='markers',
        opacity=0.7,
        marker=dict(size=15),
        name=continent_name
    ) for continent_name in filtered_dframe['continent'].unique()]

    return {
        'data':data , 
        'layout':go.Layout(
            title='My Plot',
            xaxis=dict(
                title='GDP Per Capita',
                type='log'
            ),
            yaxis=dict(
                title='Life Expectancy'
            )
        )}

if __name__ == '__main__':
    app.run_server()
