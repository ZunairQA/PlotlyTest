from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('WLD_RTFP_country_2024-04-08.csv')
print(df)

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Hi, Graham', style={'textAlign':'center'}),
    html.H4(children='Inflation in seemingly random developing nations', style={'textAlign':'center'}),
    dcc.Dropdown(df.country.unique(), id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x='date', y='Inflation')

if __name__ == '__main__':
    app.run(debug=False)
