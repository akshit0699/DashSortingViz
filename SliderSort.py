import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly
import plotly.graph_objs as go
import random
from dash.exceptions import PreventUpdate
from datetime import datetime
colors = {
    'background': '#111111',
    'text': '#BEBEBE',
    'grid': '#333333'
}
external_sheet = ["https://codepen.io/akshit0699/pen/MWKEEWm"]
app = dash.Dash(__name__, external_stylesheets=external_sheet)
selected_val = 20
print(selected_val)
the_colors = ['lightslategray', ]*selected_val
the_nums = [random.randint(10, 100) for i in range(selected_val)]


initial_trace = go.Bar(
    y = the_nums,
    marker_color = the_colors
)

fig_bubble = {
    'data' : [initial_trace],
    'layout': go.Layout(
        font=dict(color=colors['text']),
        paper_bgcolor=colors['background'],
        plot_bgcolor=colors['background'],
        height = 600,
        hovermode='closest',

    )
}
fig_selection= {
    'data' : [initial_trace],
    'layout': go.Layout(
        font=dict(color=colors['text']),
        paper_bgcolor=colors['background'],
        plot_bgcolor=colors['background'],
        height = 600,
        hovermode='closest',
        orientation = 90
    )
}
fig_merge = {
    'data' : [initial_trace],
    'layout': go.Layout(
        font=dict(color=colors['text']),
        paper_bgcolor=colors['background'],
        plot_bgcolor=colors['background'],
        height = 600,
        hovermode='closest',

    )
}
fig_quick = {
    'data' : [initial_trace],
    'layout': go.Layout(
        font=dict(color=colors['text']),
        paper_bgcolor=colors['background'],
        plot_bgcolor=colors['background'],
        height = 600,
        hovermode='closest',

    )
}
app.layout =html.Div(id = 'intro', style= {'backgroundColor': colors['background'] },
children=[
        html.Div(children='DASH SORTER',
        style={
            'textAlign': 'center',
            'color': colors['text'],
            'fontSize': 60,
            'fontWeight': 900,
            'height': '70px'
            }
        ),
        html.Div(
        id = "first_row",
        children = [
        html.Div(
            style = { 'width': '100%', 'height': '100%','backgroundColor':colors['background'],
                            'display': 'inline-block','text-align': 'center'},
            children = [
                html.Button('SLIDE TO CHOOSE THE SIZE OF ARRAY AND PRESS HERE WHEN YOU ARE SATISFIED WITH THE RANDOMNESS TO BEGIN SORTING!'
                , id='start', n_clicks=0, style = {'text-align': 'center', 'fontSize': 25,'backgroundColor':colors['background'],
                                                   'marginBottom': '4%','marginTop': '2%', 'height': '50px' ,'color': 'crimson'}),
                           ]),
            ]),
    dcc.Slider(
                    id='my-slider',
                    min=0,
                    max=100,
                    step=5,
                    value=20,

                ),


    html.Div(
    id = "first-two-names",
    children = [
        html.Div(
            style = { 'width': '50%', 'height': '50%',
                            'display': 'inline-block','fontSize': 30, 'height': '50px','marginTop': '2.8%'},
            children = [
                html.Div(children='BUBBLE SORT',
                style={
                    'textAlign': 'center',
                    'color': colors['text'],
                    'fontSize': 40,
                    'fontWeight': 500,

                    }
                )

            ]),
        html.Div(
            style = { 'width': '50%', 'height': '50%',
                            'display': 'inline-block','fontSize': 30, 'height': '50px','marginTop': '2.8%'},
            children = [
                html.Div(children='SELECTION SORT',
                style={
                    'textAlign': 'center',
                    'color': colors['text'],
                    'fontSize': 40,
                    'fontWeight': 500,

                    }
                )

            ]),


    ]
    ),

    html.Div(
    id = "first-two-stats",
    children = [
        html.Div(
            style = { 'width': '50%', 'height': '100%',
                            'display': 'inline-block','fontSize': 20, 'height': '30px','marginTop': '2.8%'},
            children = [
                html.Div(
                id = 'ops-b', style={'textAlign': 'center',
            'color': colors['text'],}
                )
            ]),
            html.Div(
                style = {'width': '50%','height': '100%',
                                'display': 'inline-block','fontSize': 20, 'height': '30px','marginTop': '2.8%'},
                children = [
                    html.Div(
                    id = 'ops-s', style={'textAlign': 'center',
            'color': colors['text'],}
                    )]
                )

    ]
    ),
    html.Div(
    id = "first-two-sorts",
    children = [
        html.Div(
            style = { 'width': '50%', 'height': '100%','backgroundColor':colors['background'],
                            'display': 'inline-block',},
            children = [
                html.Div(
                dcc.Graph(id = 'fig_bubble', figure = fig_bubble)
                )
            ]),
            html.Div(
                style = {'width': '50%','height': '100%', 'backgroundColor':colors['background'],
                                'display': 'inline-block',},
                children = [
                    html.Div(
                    dcc.Graph(id = 'fig_selection', figure = fig_selection)
                    )]
                )

    ]
    ),
    html.Div(
    id = "next-two-names",
    children = [
        html.Div(
            style = { 'width': '50%', 'height': '50%',
                            'display': 'inline-block','fontSize': 30, 'height': '50px','marginTop': '2.8%'},
            children = [
                html.Div(children='MERGE SORT',
                style={
                    'textAlign': 'center',
                    'color': colors['text'],
                    'fontSize': 40,
                    'fontWeight': 500,

                    }
                )

            ]),
        html.Div(
            style = { 'width': '50%', 'height': '50%',
                            'display': 'inline-block','fontSize': 30, 'height': '50px','marginTop': '2.8%'},
            children = [
                html.Div(children='QUICK SORT',
                style={
                    'textAlign': 'center',
                    'color': colors['text'],
                    'fontSize': 40,
                    'fontWeight': 500,

                    }
                )

            ]),


    ]
    ),
    html.Div(
    id = "next-two-stats",
    children = [
        html.Div(
            style = { 'width': '50%', 'height': '100%',
                            'display': 'inline-block','fontSize': 20, 'height': '30px','marginTop': '2.8%'},
            children = [
                html.Div(
                id = 'ops-m', style={'textAlign': 'center',
            'color': colors['text'],}
                )
            ]),
            html.Div(
                style = {'width': '50%','height': '100%',
                                'display': 'inline-block','fontSize': 20, 'height': '30px','marginTop': '2.8%'},
                children = [
                    html.Div(
                    id = 'ops-q', style={'textAlign': 'center',
            'color': colors['text'],}
                    )]
                )

    ]
    ),
    html.Div(
    id = "last-two-sorts",
    children = [
        html.Div(
            style = { 'width': '50%', 'height': '100%','backgroundColor':colors['background'],
                            'display': 'inline-block',},
            children = [
                html.Div(
                dcc.Graph(id = 'fig_merge', figure = fig_merge)
                )
            ]),
            html.Div(
                style = {'width': '50%','height': '100%', 'backgroundColor':colors['background'],
                                'display': 'inline-block',},
                children = [
                    html.Div(
                    dcc.Graph(id = 'fig_quick', figure = fig_quick)
                    )]
                )

    ]
    ),

    html.Div(
    id = 'display',
    style = {'display': 'none'}
    ),
    dcc.Interval(
    id = 'graph-update',
    interval = 1*400,
    n_intervals = 0),

    dcc.Store(id = 'bubble-data', data = (0,0,selected_val-1,the_nums,the_colors, True,-1)),
    dcc.Store(id = 'selection-data', data = (0,1,selected_val, True, 0,the_nums,the_colors, True,-1)),
    dcc.Store(id = 'merge-data', data = (0,0,0,True,1,0,1,1,the_nums,0,0,the_nums,the_nums,the_nums,the_colors,True,-1)),
    dcc.Store(id = 'quick-data', data = ([(0,selected_val-1)],0,selected_val-1,0,0,0,True,the_colors,the_nums,True,-1))

]
)

@app.callback(dash.dependencies.Output('display', 'children'),
    [dash.dependencies.Input('my-slider', 'value')])
def make_updations(value):
    global selected_val
    selected_val = value
    return None
@app.callback([Output('fig_bubble', 'figure'),Output('bubble-data', 'data'),Output('ops-b', 'children')],
              [Input('graph-update', 'n_intervals'),Input('start', 'n_clicks')],
             [State('bubble-data', 'data')],)
def bubbleSort(n, n_clicks,data):

    i,j,k,the_nums,the_colors,flag,var = data
    if flag:
        if selected_val != 20:
            k = selected_val-1
            the_colors = ['lightslategray', ]*selected_val
            the_nums = [random.randint(10, 100) for i in range(selected_val)]

    if n_clicks:
        var+=1
        flag = False
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

    display_string = "Comparisions made: " + str(var)
    trace = go.Bar(
    y = the_nums,
    marker_color = the_colors
    )
    return {'data' : [trace],
            'layout': go.Layout(
                         font=dict(color=colors['text']),
                         paper_bgcolor=colors['background'],
                         plot_bgcolor=colors['background'],
                         height = 600
                     )
                 }, (i,j,k,the_nums,the_colors,flag, var), display_string


@app.callback([Output('fig_selection', 'figure'),Output('selection-data', 'data'),Output('ops-s', 'children')],
                [Input('graph-update', 'n_intervals'),Input('start', 'n_clicks')],
             [State('selection-data', 'data')],)
def SelectionSort(n, n_clicks, data):
    i, j, k, flag1, min_index, the_nums, the_colors, flag, var = data
    if flag:
        if selected_val!=20:
            k = selected_val
            the_colors = ['lightslategray', ]*selected_val
            the_nums = [random.randint(10, 100) for i in range(selected_val)]
    if n_clicks:
        var+=1
        flag = False
        if i>=k or min_index>=k:
            raise PreventUpdate
        end_point = k-i
        the_colors[i:] = ['lightslategray']*end_point
        the_colors[i] = 'white'
        if flag1:
            min_index = i
        the_colors[min_index] = 'white'
        if j==k:
            the_colors[i] = 'red'
            the_nums[min_index], the_nums[i] = the_nums[i], the_nums[min_index]
            i+=1
            if i == k:
                the_colors[i-1] = 'red'
            j = i
            flag1 = True
            # swap opertion here
        if i<k:
            the_colors[j] = 'crimson'
            if the_nums[min_index]>the_nums[j]:
                the_colors[min_index] = 'lightslategray'
                min_index = j
                flag1 = False
                the_colors[min_index] = 'green'

        j+=1
    display_string = "Comparisions made: " + str(var)
    trace = go.Bar(
    y = the_nums,
    marker_color = the_colors
    )
    return {'data' : [trace],
            'layout': go.Layout(
                         font=dict(color=colors['text']),
                         paper_bgcolor=colors['background'],
                         plot_bgcolor=colors['background'],
                         height = 600,
                     )
                 }, (i, j, k, flag1, min_index,the_nums, the_colors, flag,var), display_string


@app.callback([Output('fig_merge', 'figure'),Output('merge-data', 'data'),Output('ops-m', 'children')],
              [Input('graph-update', 'n_intervals'),Input('start', 'n_clicks')],
             [State('merge-data', 'data')],)
def mergeSort(n, n_clicks, data):
    i, j, k, flag1, curr_size, left, mid,right, the_nums,n1,n2, L, R, the_nums1, the_colors,flag,var = data
    if flag:
        if selected_val!=20:
            the_colors = ['lightslategray', ]*selected_val
            the_nums = [random.randint(10, 100) for i in range(selected_val)]
            L = R= the_nums1 = the_nums

    if n_clicks:
        var+=1
        flag = False
        left = int(left or 0)
        if flag1:
            if curr_size > selected_val-1:
                raise PreventUpdate
            if left >= selected_val-1:
                curr_size = 2 * curr_size
                left = 0
            mid = min((left + curr_size - 1),selected_val-1)
            right = min(2 * curr_size + left - 1,
                            selected_val - 1)
            flag1 = False
            k = left
            the_colors[left: right+1 ]  = ['red',]*(right-left+1)

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
        if not flag1:

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
                flag1 = True
                #the_colors = ['lightslategray',]*len(the_nums)
                left = left + curr_size*2
                the_colors = ['lightslategray',]*selected_val

        if curr_size >= selected_val-1:
            the_colors = ['red',]*selected_val

    display_string = "Comparisions made: " + str(var)
    trace = go.Bar(
    y = the_nums1,
    marker_color = the_colors
    )
    return {'data' : [trace],
            'layout': go.Layout(
                         font=dict(color=colors['text']),
                         paper_bgcolor=colors['background'],
                         plot_bgcolor=colors['background'],
                         height = 600,
                    )
                 }, (i, j, k, flag1, curr_size,left, mid, right, the_nums,n1,n2,L,R, the_nums1, the_colors,flag,var),display_string


@app.callback([Output('fig_quick', 'figure'),Output('quick-data', 'data'),Output('ops-q', 'children')],
              [Input('graph-update', 'n_intervals'),Input('start', 'n_clicks')],
             [State('quick-data', 'data')],)
def quickSort(n, n_clicks, data):
    quick_stack, start, end, pivot, pIndex,i, flag1, the_colors,the_nums, flag,var = data
    if flag:
        if selected_val!=20:
            the_colors = ['lightslategray', ]*selected_val
            the_nums = [random.randint(10, 100) for i in range(selected_val)]
            end = selected_val-1

            quick_stack = [(0, selected_val-1)]
    if n_clicks:
        var+=1
        flag = False
        the_colors = ['lightslategray', ]*len(the_colors)
        the_colors[end] = 'red'
        if len(quick_stack)==0 and flag1:
            raise PreventUpdate
        if flag1:

            start, end = quick_stack.pop(-1)
            i = start
            pIndex = start
            pivot = the_nums[end]
            the_colors[end] = 'red'
            print(pivot)
            flag1 = False
        if not flag1:
            if i == end:
                the_colors[pIndex] = 'red'
                the_colors[end] = 'red'
                the_nums[pIndex], the_nums[end] = the_nums[end], the_nums[pIndex]
                pivot = pIndex
                flag1 = True
            if the_nums[i]<=pivot:
                the_colors[pIndex] = 'green'
                the_nums[pIndex], the_nums[i] = the_nums[i], the_nums[pIndex]
                pIndex+=1
            else:
                the_colors[i] = 'blue'

            i+=1
        if flag1:
            the_colors[:pIndex] = ['white',]*pIndex
            the_colors[pIndex+1:] = ['green',]*(len(the_nums)-pIndex)
            if pivot -1 > start:
                quick_stack.append((start, pivot-1))
            if pivot +1<end:
                quick_stack.append((pivot+1, end))
        if len(quick_stack)==0 and flag1:
            the_colors = ['red',]*len(the_colors)
    display_string = "Comparisions made: " + str(var)
    trace = go.Bar(
    y = the_nums,
    marker_color = the_colors
    )
    return {'data' : [trace],
            'layout': go.Layout(
                         font=dict(color=colors['text']),
                         paper_bgcolor=colors['background'],
                         plot_bgcolor=colors['background'],
                         height = 600,
                     )
                 }, (quick_stack, start, end, pivot, pIndex,i, flag1,the_colors,the_nums, flag,var),display_string

if __name__ == '__main__':
    app.run_server(debug= False)
