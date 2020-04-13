import dash
import dash_core_components as dcc
import dash_html_components as html

"""
This is an example of Dash Core Components
for refernce: https://dash.plot.ly/dash-core-components/
"""
app = dash.Dash()

app.layout = html.Div([
    html.Label('Dropdown'),
    dcc.Dropdown(
        options=[
            dict(
                label='New York City',
                value='NYC'
                ),
            dict(
                label='San Francisco',
                value='SF'
                ),
            dict(
                label='Long Beach',
                value='LB'
            )],
            value='SF'), # This is a default value
    html.Label('Slider'),
    dcc.Slider(
        min=-10,
        max=10,
        step=0.5,
        value=0,
        marks={i: i for i in range(-10,10)}
        ),
    html.P( html.Label('Some Radio Items')),
    dcc.RadioItems(
        options=[
            dict(
                label='New York City',
                value='NYC'
                ),
            dict(
                label='San Francisco',
                value='SF'
                ),
            dict(
                label='Long Beach',
                value='LB'
            )],
            value='SF')
       
]
)


if __name__ == '__main__':
    app.run_server()
