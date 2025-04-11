import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

def run_interactive_dashboard(data: pd.DataFrame, x: str, y: str, title: str = "Interaktiver Scatterplot"):
    app = dash.Dash(__name__)
    fig = px.scatter(data, x=x, y=y)
    app.layout = html.Div([
        html.H1(title),
        dcc.Graph(figure=fig)
    ])
    app.run_server(debug=True)
