import pandas as pd 
import plotly.offline as pyo 
import plotly.graph_objects as go 

data_path = 'C:/Users/Phillip.Warther/Documents/Udemy_course/Plotly-Dashboards-with-Dash-master/Data/mocksurvey.csv'
dframe = pd.read_csv( data_path )

data = [ go.Bar( 
    x= dframe[ dframe.columns[0]] , 
    y= dframe[ response ],
    name= response)
    for response in dframe.columns[1:]
    ]

layout= go.Layout(title='Survey Responses',barmode='stack')
figure= go.Figure(data=data,layout=layout)

pyo.plot( figure , filename='myBarChartExercise.html')