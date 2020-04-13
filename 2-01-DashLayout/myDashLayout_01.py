import dash 
import dash_core_components as dcc 
import dash_html_components as html 

app = dash.Dash()
colors = {
    'background':'#111111' ,
    'text':'#7fdbff'
}

#html.Div creates a division in the layout, and we provide a list of everything going into that division
app.layout = html.Div( children=[
    html.H1('Hello Dash',style=dict( #CSS calls
        textAlign='center',
        color=colors['text'])),

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
                plot_bgcolor=colors['background'],
                paper_bgcolor=colors['background'],
                font={'color':colors['text']},
                title='BAR PLOTS!'
            )
        ))
], style={'backgroundColor':colors['background']}
)

if __name__ == '__main__':
    app.run_server()