import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly
import plotly.graph_objs as go
import random
from dash.exceptions import PreventUpdate
from collections import deque

colors = {
    'background': '#111111',
    'text': '#BEBEBE',
    'grid': '#333333'
}
app = dash.Dash(__name__)
selected_val = 40
the_colors = ['lightslategray', ]*selected_val
the_nums = [random.randint(10, 100) for i in range(selected_val)]
stack = []
stack.append((0, len(the_nums)-1))

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
    interval = 1*400,
    n_intervals = 0),
    dcc.Store(id = 'stack', data = stack),
    dcc.Store(id = 'start', data = 0),
    dcc.Store(id = 'end', data = len(the_nums)-1),
    dcc.Store(id = 'pivot', data = 0),
    dcc.Store(id = 'pIndex', data = 0),
    dcc.Store(id = 'i', data = 0),
    dcc.Store(id = 'flag', data = True),
    dcc.Store(id = 'the_colors', data = the_colors),
]
)



@app.callback([Output('sorter', 'figure'),Output('stack', 'data'),Output('start', 'data'), Output('end', 'data'), Output('pivot', 'data')
              ,Output('pIndex', 'data'), Output('i', 'data'), Output('flag', 'data'), Output('the_colors', 'data')],
              [Input('graph-update', 'n_intervals')],
             [State('stack', 'data'), State('start', 'data'),State('end', 'data'),
             State('pivot', 'data'),State('pIndex', 'data'),State('i', 'data'),State('flag', 'data'),State('the_colors', 'data')])
def bubbleSort(n, stack, start, end, pivot, pIndex,i, flag, the_colors):
    print("TOP")
    print(i)
    print(flag)
    the_colors = ['lightslategray', ]*len(the_colors)
    the_colors[end] = 'red'
    if len(stack)==0 and flag:
        raise PreventUpdate
    if flag:

        print("here")
        start, end = stack.pop(-1)
        i = start
        pIndex = start
        pivot = the_nums[end]
        the_colors[end] = 'red'
        print(pivot)
        flag = False
    if not flag:
        if i == end:
            print("Serious swap")
            the_colors[pIndex] = 'red'
            the_colors[end] = 'red'
            the_nums[pIndex], the_nums[end] = the_nums[end], the_nums[pIndex]
            pivot = pIndex
            flag = True
        if the_nums[i]<=pivot:
            print("Conventional Swap")
            the_colors[pIndex] = 'green'
            #the_colors[i] = 'blue'
            the_nums[pIndex], the_nums[i] = the_nums[i], the_nums[pIndex]
            pIndex+=1
        else:
            the_colors[i] = 'blue'


        print(i)
        i+=1
    if flag:
        the_colors[:pIndex] = ['white',]*pIndex
        the_colors[pIndex+1:] = ['green',]*(len(the_nums)-pIndex)
        if pivot -1 > start:
            stack.append((start, pivot-1))
        if pivot +1<end:
            stack.append((pivot+1, end))
    if len(stack)==0 and flag:
        the_colors = ['red',]*len(the_colors)





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
                 }, stack, start, end, pivot, pIndex,i, flag,the_colors
if __name__ == '__main__':
    app.run_server(debug=False)
