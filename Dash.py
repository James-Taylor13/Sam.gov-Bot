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
df['Department'].astype(str)
df['Url'].astype(str)
df['Original Publish Date'].astype(str)
del df['Description']
df_top = df.head
print(df_top)
#df = df.drop('Description', inplace=True, axis=1)

#start the app
app = dash.Dash(__name__)

#App Layout
app.layout = html.Div([

    html.H1('Sam.Gov Bot', style={'font-family': 'monospace', 'text-align': 'left'}),

    dcc.Dropdown(
        id='Select Project',
        options=[
            {'label': 'Data Readiness for Artificial Intelligence Development (DRAID) Services', 'value': 'Data Readiness for Artificial Intelligence Development (DRAID) Services; Basic Ordering Agreement (BOA) for The Joint Artificial Intelligence Center (JAIC)'},
            {'label': 'TryAi', 'value': 'TryAi; Artificial Intelligence Demonstrations; Commercial Solutions Opening (CSO) for the Joint Artificial Intelligence Center (JAIC)'},
            {'label': 'Innovative & Transformative Commercial Artificial Intelligence (AI) Technologies', 'value': 'Innovative & Transformative Commercial Artificial Intelligence (AI) Technologies Commercial Solutions Opening (CSO)'},
            {'label': 'Special Notice - GVS OTA', 'value': 'Special Notice - GVS OTA, W15QKN-17-9-1025, RPP 21-04, Artificial Intelligence (AI) Enabled Crew Reduction'},
            {'label': 'Stratagem', 'value': 'Stratagem: Applying State-of-the-Art Artificial Intelligence and Machine Learning Approaches to Air Battle Management'},
            {'label': 'Advanced Tracking Architectures', 'value': 'ADVANCED TRACKING ARCHITECTURES USING ARTIFICIAL INTELLIGENCE (AI) (ATA-AI)'}

        ],
        placeholder="Select a project...",
        style={
            'font-family': 'monospace'},
        value='',
    ),

    html.Br(),

    dash_table.DataTable(
    style_cell={
        'font-family': 'monospace',
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
    html.Br(),
    html.Div(id='output_container')


])

@app.callback(
    dash.dependencies.Output('output_container', 'children'),
    [dash.dependencies.Input('Select Project', 'value')])
def update_output(value):

    container = 'The project chosen was: {}'.format(value)#, df.loc[df[value], 'Department'])#, df['Original Publish Date'], df['Url']) '\n Date:{}\n URL: {}' \n Project details: \n Department:{}

    df2=df[df['Title'] == value]
    df2['Department'].astype(str)
    df2['Url'].astype(str)
    df2['Original Publish Date'].astype(str)

    #details = 'PROJECT DETAILS:\n  Department: {}\n  Date: {}\n  URL: {}\n'.format(df2['Department'], df2['Original Publish Date'], df2['Url'])
    #dff = df.copy()
    #dff = dff[dff['Title'] == value]

    #children = '{}'.format(dff['Description'])
    return container#, details


if __name__ == '__main__':
    app.run_server(debug=True)
