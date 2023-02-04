'''Dash Tutorial from https://dash.plotly.com/'''

from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

app = Dash(__name__)

markdown_text = '''
## Dash and Markdown
___

*Dash* can be written in **markdown**.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
```Check out their``` [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
'''
fig = px.scatter(df, x='gdp per capita', y='life expectancy',
                 size='population', color='continent', hover_name='country',
                 log_x=True, size_max=60)

app.layout = html.Div([
    dcc.Markdown(children=markdown_text),
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
