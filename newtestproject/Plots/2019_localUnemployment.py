import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

#Draw a heatmap to represent the recorded max temperature  on day of week and month of year.
# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/LocalAreaUnemploymentStatistics.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Preparing data
data = [go.Scatter(x=df['Date'], y=df['Percentage'], mode='lines', name='2019')]
# Preparing layout
layout = go.Layout(title='Local Unemployment by year', xaxis_title="Date",
                   yaxis_title="Percent of unemployment")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='localUnemployment.html')
 