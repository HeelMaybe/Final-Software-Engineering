import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df1 = pd.read_csv('../Datasets/LocalAreaUnemploymentStatistics.csv')
df2 = pd.read_csv('../Datasets/2020_LocalAreaUnemploymentStatistics.csv')

app = dash.Dash()


# Line Chart
data_2019linechart =[go.Scatter(x=df1['Date'], y=df1['Percentage'], mode='lines', name='2019')]

data_2020linechart =data = [go.Scatter(x=df2['Date'], y=df2['Percentage'], mode='lines', name='2020')]




# 2019-2020 Unemployment Multi Line Chart

trace1 = go.Scatter(x=df1['Month'], y=df1['2019Percentage'], mode='lines', name='2019')
trace2 = go.Scatter(x=df1['Month'], y=df1['2020Percentage'], mode='lines', name='2020')
data_multilinechart = [trace1,trace2]

# Layout
app.layout = html.Div(children=[
   html.H1(children='Python Dash',
           style={
               'textAlign': 'center',
               'color': '#ef3e18'
           }
           ),
   html.Div('Web dashboard for Data Visualization using Python', style={'textAlign': 'center'}),
   html.Div('North Carolina Unemployment Data', style={'textAlign': 'center'}),
   html.Br(),
   html.Br(),

html.Hr(style={'color': '#7FDBFF'}),
html.H3('2019 Line chart', style={'color': '#df1e56'}),
html.Div('This line chart represents the percentage of unemployment for North Carolina in 2019'),
dcc.Graph(id='graph1',
         figure={
             'data': data_2019linechart,
             'layout': go.Layout(title='Local percentage of unemployment in 2019', xaxis_title="Date",
                   yaxis_title="Percent of unemployment")
             }
         ),

html.Hr(style={'color': '#7FDBFF'}),
html.H3('2020 Line chart', style={'color': '#df1e56'}),
html.Div('This line chart represents the percentage of unemployment for North Carolina in 2020'),
dcc.Graph(id='graph2',
         figure={
             'data': data_2020linechart,
             'layout': go.Layout(title='Local percentage of unemployment in 2020', xaxis_title="Date",
                   yaxis_title="Percent of unemployment")
             }
         ),

html.Hr(style={'color': '#7FDBFF'}),
html.H3('2019-2020 Multi Line chart', style={'color': '#df1e56'}),
html.Div('This multiline chart represents the percentage of unemployment for North Carolina from 2019-2020'),
dcc.Graph(id='graph5',
         figure={
             'data': data_multilinechart,
             'layout': go.Layout(title='Local percentage of unemployment in 2019-2020', xaxis_title="Date", yaxis_title="Percent of unemployment")
         }
         ),
])

if __name__ == '__main__':
   app.run_server()

