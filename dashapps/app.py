from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash(__name__)

header = dbc.Nav([
    html.Button(className="navbar-toggler navbar-toggler-right border-0"),
    dbc.Row([
        dbc.Col([
            html.A(
            children = [
                html.I(className="fa d-inline fa-lg fa-stop-circle-o"),
                html.B("Cinemat'Teach")
            ], className="navbar-brand d-none d-md-block", style={'color': "white"}),
        ], width=3),
        dbc.Col([
            html.Nav([
                dbc.NavItem(dbc.NavLink("Acceuil", active=True, href="#")),
                dbc.NavItem(dbc.NavLink("Modules", active=False, href="#")),
                dbc.NavItem(dbc.NavLink("Dashboard", active=False, href="#"))  
            ],className="navbar-nav")
            
        ], width=4),
        dbc.Col([
            dbc.NavItem(dbc.NavLink(html.I(className="fa fa-user fa-fw"), active=True, href="#")),
        ], width=1)
    ],justify="between",)
], className="navbar navbar-expand-md navbar-dark bg-primary")

app.layout = html.Div([
    header
])

if __name__ == '__main__':
    app.run(debug=True)