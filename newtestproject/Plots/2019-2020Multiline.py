import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/LocalAreaUnemploymentStatistics.csv')
#df['Date'] = pd.to_datetime(df['date'])

# Preparing data
trace1 = go.Scatter(x=df['Month'], y=df['2019Percentage'], mode='lines', name='2019')
trace2 = go.Scatter(x=df['Month'], y=df['2020Percentage'], mode='lines', name='2020')
data = [trace1,trace2]


# Preparing layout
layout = go.Layout(title='Local Unemployment by year', xaxis_title="Date",
                   yaxis_title="Percent of unemployment")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='Weathermultilinechart.html')