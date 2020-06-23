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
the_nums = [random.randint(10, 500) for i in range(selected_val)]

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
                         yaxis=dict(range=[min(the_nums), 500]),
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
    dcc.Store(id = 'j', data = 1),
    dcc.Store(id = 'k', data = selected_val),
    dcc.Store(id = 'flag', data = True),
    dcc.Store(id = 'min_index', data = 0),
]
)



@app.callback([Output('sorter', 'figure'),Output('i', 'data'), Output('j', 'data'),
            Output('k', 'data'), Output('flag', 'data'), Output('min_index', 'data')],
              [Input('graph-update', 'n_intervals')],
             [State('i', 'data'), State('j', 'data'),
             State('k', 'data'),State('flag', 'data'),State('min_index', 'data')],)
def SelectionSort(n, i, j, k, flag, min_index):

    # set i to the first element
    # find the smallest element in the remainder of the array
    # exchange that element with this ith element
    # i will go from start of array to end, incrementing only when j hits the boundary
    # if i hits the boundary its the exception raised

    # initial element (denoted by i)--> RED
    # make all the array GREY with each pass, only the minIndex always needs to be red
    # while we go through an element in j, make it CRIMSON
    # if this element is smaller than minIndex's element. Make minIndex = j = BLUE
    # SWAP when j has hit its boundary condition
    if i>=k or min_index>=k:
        raise PreventUpdate
    end_point = k-i
    the_colors[i:] = ['lightslategray']*end_point
    the_colors[i] = 'white'
    if flag:
        min_index = i
    the_colors[min_index] = 'white'
    if j==k:
        the_colors[i] = 'red'
        the_nums[min_index], the_nums[i] = the_nums[i], the_nums[min_index]
        i+=1
        if i == k:
            the_colors[i-1] = 'red'
        j = i
        flag = True
        # swap opertion here
    if i<k:
        the_colors[j] = 'crimson'
        if the_nums[min_index]>the_nums[j]:
            the_colors[min_index] = 'lightslategray'
            min_index = j
            flag = False
            the_colors[min_index] = 'green'

    j+=1
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
                 }, i, j, k, flag, min_index
if __name__ == '__main__':
    app.run_server(debug=False)
