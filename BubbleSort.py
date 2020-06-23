import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly
import plotly.graph_objs as go
import random
from dash.exceptions import PreventUpdate

colors = {
    'background': '#111111',
    'text': '#BEBEBE',
    'grid': '#333333'
}
app = dash.Dash(__name__)
selected_val = 40
the_colors = ['lightslategray', ]*selected_val
the_nums = [random.randint(10, 100) for i in range(selected_val)]

initial_trace = go.Bar(
    y = the_nums,
    marker_color = the_colors
)
app.layout = html.Div([
        dcc.Graph(id = 'sorter',
                 figure = {
                     'data' : [initial_trace],
                     'layout': go.Layout(
                         xaxis=dict(range=[0, len(the_nums)]),
                         yaxis=dict(range=[min(the_nums), 100]),
                         font=dict(color=colors['text']),
                         paper_bgcolor=colors['background'],
                         plot_bgcolor=colors['background'],
                         height = 600,
                         width = 1200,
                         hovermode='closest',
                         showlegend=True,
                         transition = {'duration': 500},
                     )
                 }),
    dcc.Interval(
    id = 'graph-update',
    interval = 1*500,
    n_intervals = 0),
    dcc.Store(id = 'i', data = 0),
    dcc.Store(id = 'j', data = 0),
    dcc.Store(id = 'k', data = selected_val-1),
]
)



@app.callback([Output('sorter', 'figure'),Output('i', 'data'), Output('j', 'data'), Output('k', 'data')],
              [Input('graph-update', 'n_intervals')],
             [State('i', 'data'), State('j', 'data'),State('k', 'data')],)
def bubbleSort(n, i, j, k):


    end_point = k-i
    the_colors[:end_point] = ['lightslategray', ]*end_point
    if i >= k:
        raise PreventUpdate
    if j == end_point:
        the_colors[j] = 'red'
        end_point = k-i
        j = 0
        i+=1
    # Here j is ZERO
    if the_nums[j]>the_nums[j+1]:
        the_colors[j] = 'blue'
        the_colors[j+1] = 'blue'
        the_nums[j], the_nums[j+1] = the_nums[j+1], the_nums[j] # interchange the value
    else:
        the_colors[j] = 'green'
        the_colors[j+1] = 'green'
    j+=1
    if i == k and j==1:
        the_colors[j] = 'red'
        the_colors[j-1] = 'red'

    print(i)


    trace = go.Bar(
    y = the_nums,
    marker_color = the_colors
    )
    return {'data' : [trace],
            'layout': go.Layout(
                         xaxis=dict(range=[0, len(the_nums)]),
                         #yaxis=dict(range=[min(the_nums), 100]),
                         font=dict(color=colors['text']),
                         paper_bgcolor=colors['background'],
                         plot_bgcolor=colors['background'],
                         height = 600,
                         width = 1200,
                         hovermode='closest',
                         showlegend=True,
                         transition = {'duration': 500},
                     )
                 }, i, j, k
if __name__ == '__main__':
    app.run_server(debug=False)
