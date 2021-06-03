#import libraries
import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output

#load in data
df = pd.read_csv('SamGovBot - Sheet1.csv')
df1 = df.copy()
del df['Description']
#df = df.drop('Description', inplace=True, axis=1)

#start the app
app = dash.Dash(__name__)

#App Layout
app.layout = html.Div([

    html.H1('Sam.Gov Bot', style={'text-align': 'left'}),

    dcc.Dropdown(
        id='Select Project',
        options=[
            {'label': 'Data Readiness for Artificial Intelligence Development (DRAID) Services', 'value': 'Data Readiness for Artificial Intelligence Development (DRAID) Services; Basic Ordering Agreement (BOA) for The Joint Artificial Intelligence Center (JAIC)'},
        ],
        placeholder="Select a project...",
        value='',
    ),

    html.Br(),

    dash_table.DataTable(
    style_cell={
        'textAlign': 'left',
        'whiteSpace': 'normal',
        'height': 'auto',
    },
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
    style_as_list_view=True,
    style_data_conditional=[
        {
            'if': {'row_index': 'odd'},
            'backgroundColor': 'rgb(230, 230, 230)'
        }
    ],
    style_header={
        'backgroundColor': 'rgb(230, 230, 230)',
        'fontWeight': 'bold'
    }),

    html.Div(id='output-container'),
    html.Br()

])

@app.callback(
    dash.dependencies.Output('output-container', 'figure'),
    [dash.dependencies.Input('Select Project', 'value')])
def update_output(value):

    container = 'The project chosen was: {}'.format(value)

    #dff = df.copy()
    #dff = dff[dff['Title'] == value]

    #children = '{}'.format(dff['Description'])
    return container#, children


if __name__ == '__main__':
    app.run_server(debug=True)
