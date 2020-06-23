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
    dcc.Store(id = 'k', data = 0),
    dcc.Store(id = 'flag', data = True),
    dcc.Store(id = 'curr_size', data = 1),
    dcc.Store(id = 'left', data = 0),
    dcc.Store(id = 'mid', data = 1),
    dcc.Store(id = 'right', data = 1),
    dcc.Store(id = 'the_nums', data = the_nums),
    dcc.Store(id = 'n1', data = 0),
    dcc.Store(id = 'n2', data = 0),
    dcc.Store(id = 'L', data = the_nums),
    dcc.Store(id = 'R', data = the_nums),
    dcc.Store(id = 'the_nums1', data = the_nums),
    dcc.Store(id = 'the_colors', data = the_colors),


]
)

@app.callback([Output('sorter', 'figure'),Output('i', 'data'), Output('j', 'data'),
            Output('k', 'data'), Output('flag', 'data'), Output('curr_size', 'data'), Output('left', 'data'),
             Output('mid', 'data'), Output('right', 'data'),
              Output('the_nums', 'data'),Output('n1', 'data'), Output('n2', 'data'),Output('L', 'data'), Output('R', 'data'), Output('the_nums1', 'data'),
              Output('the_colors', 'data')],
              [Input('graph-update', 'n_intervals')],
             [State('i', 'data'), State('j', 'data'),
             State('k', 'data'),State('flag', 'data'),State('curr_size', 'data'),
             State('left', 'data'),State('mid', 'data'),State('right', 'data'),State('the_nums', 'data'),
             State('n1', 'data'),State('n2', 'data'),State('L', 'data'),State('R', 'data'),State('the_nums1', 'data'),State('the_colors', 'data')],)
def mergeSort(n, i, j, k, flag, curr_size, left, mid,right, the_nums,n1,n2, L, R, the_nums1, the_colors):
    left = int(left or 0)

    if flag:

        if curr_size > len(the_nums)-1:
            raise PreventUpdate
        if left >= len(the_nums)-1:
            curr_size = 2 * curr_size
            left = 0
        mid = min((left + curr_size - 1),len(the_nums)-1)
        right = min(2 * curr_size + left - 1,
                        len(the_nums) - 1)
        flag = False
        k = left
        the_colors[left: right+1 ]  = ['red',]*(right-left+1)
        print("Resetting i and j")

        n1 = mid - left + 1
        n2 = right - mid
        L = [0] * n1
        R = [0] * n2
        for i in range(0, n1):
            L[i] = the_nums1[left + i]
            the_colors[left+i] = 'crimson'
        for i in range(0, n2):
            R[i] = the_nums1[mid + i + 1]
            the_colors[mid+i+1] = 'crimson'

        i = 0
        j = 0
        print(L)
        print(R)


    if not flag:

        if i < n1 and j < n2:
            if L[i] > R[j]:
                the_colors[k] = 'red'
                the_nums1[k] = R[j]
                j += 1
            else:
                the_colors[k] = 'red'
                the_nums1[k] = L[i] # GOT OUT OF RANGE HERE
                i += 1
            k += 1


        else:
           if i < n1:
               the_colors[k] = 'red'
               the_nums1[k] = L[i]
               i += 1
           if j < n2:
               the_colors[k] = 'red'
               the_nums1[k] = R[j]
               j += 1
           k += 1

        if i == n1 and j == n2:
            print("FLAAAAAG")
            flag = True
            #the_colors = ['lightslategray',]*len(the_nums)
            left = left + curr_size*2
            the_colors = ['lightslategray',]*len(the_nums)

    if curr_size >= len(the_nums)-1:
        the_colors = ['red',]*len(the_nums)


    trace = go.Bar(
    y = the_nums1,
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
                 }, i, j, k, flag, curr_size,left, mid, right, the_nums,n1,n2,L,R, the_nums1, the_colors
if __name__ == '__main__':
    app.run_server(debug=False)
