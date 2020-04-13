import dash 
import dash_core_components as dcc 
import dash_html_components as html 

app = dash.Dash()

#html.Div creates a division in the layout, and we provide a list of everything going into that division
app.layout = html.Div( children=[
    html.H1('Hello Dash'),
    html.Div('Dash: Web Dashboards with Python'),
    dcc.Graph(
        id='example' , 
        figure= dict(
            data=[ dict(
                x=[1,2,3],
                y=[4,2,1],
                type='bar',
                name='SF'
            ),
            dict(
                x=[1,2,3],
                y=[7,4,6],
                type='bar',
                name='NYC')],           
            layout=dict(
                title='BAR PLOTS!'
            )
        ))
])

if __name__ == '__main__':
    app.run_server()