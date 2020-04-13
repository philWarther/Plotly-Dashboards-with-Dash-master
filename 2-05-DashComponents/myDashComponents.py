import dash
import dash_html_components as html 

app = dash.Dash()

app.layout = html.Div(
    ['This is the outermost html.Div() ',
    html.Div(
        ['This is an inner html.Div()'],
        style=dict(
            color='red'
        )
    ),
    html.Div(
        ['Another inner html.Div()'],
        style=dict(
            color='blue',
            border='2px red solid'
        )
    )] ,
    style=dict(
        color='green',
        border='2px green solid'
    ))









if __name__ == "__main__":
    app.run_server()