from dash import Dash, html, dash_table, dcc
import plotly.express as px
import pandas as pd
import gzip

# data handling 
with gzip.open('calendar.csv.gz', 'rt') as f:
    calendar = pd.read_csv(f)

df_ratios = calendar.available.value_counts(normalize = True)
df_ratios = df_ratios.reset_index()
df_ratios['status'] = df_ratios['available'].apply(lambda x: 'Reserved' if x == 'f' else 'Available')
# initialization 
app = Dash()

# layout
app.layout = [
    html.Div(children='Arbnb Availability in Stockholm in 2025'),
    dcc.Graph(figure=px.bar(df_ratios, x = 'status', y = 'proportion', 
              title= 'Figure 1: Overall  Availability of Listings in Stockholm in 2025 as of 1 April',
              labels = {'status': 'Status', 'proportion': ' ' },
              range_y = [0, .7]))
]

# launch the app
if __name__ == '__main__':
    app.run(debug=True)