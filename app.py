from dash import html, dcc, dash_table, Output, Input, State
import dash
import dash_bootstrap_components as dbc
import pandas as pd
import models
import re
import json
from dash.exceptions import PreventUpdate
from gradio_client import Client

feedback = pd.read_csv("feedback.csv", dtype=object)
feedback1 = pd.read_csv("feedback1.csv", dtype=object)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.VAPOR], suppress_callback_exceptions=True)

server = app.server

app.layout = dbc.Container(
    [
        dbc.Row([
            html.Label(
                "Compare Llama-3.1-8B-Instruct  VS Mistral-Nemo",
                style={
                    "font-family": "Times Roman",
                    "text-decoration": "underline",
                    "text-align": "center",
                    "color": "white",
                },
            )],
            style={"margin": "20px", "text-align": "center"},
            justify="center",
        ),
        html.Hr(),

        dbc.Row([
            html.Label(
                "Llama-3.1-8B-Instruct",
                style={
                    "font-family": "Times Roman",
                    "text-decoration": "underline",
                    "text-align": "center",
                    "color": "white",
                },
            )],
            style={"margin": "20px", "text-align": "center"},
            justify="center",
        ),

        dbc.Row([
            dbc.Col([
                dbc.Row([
                    dcc.Textarea(
                        id='text-input',
                        placeholder='Enter your text here...',
                        style={
                            'width': '100%',
                            'height': 300,
                            'borderRadius': '10px',
                            'padding': '20px',
                        }
                    ),
                    html.Br(),
                    dbc.Col([
                        dbc.Row([
                            dbc.Col([
                                dcc.Textarea(
                                    id='text-input0',
                                    value="",
                                    placeholder='Inference results...',
                                    style={
                                        'width': '100%',
                                        'height': 300,
                                        'borderRadius': '10px',
                                        'padding': '20px',
                                    }
                                ),
                            ], width=8, style={
                                "margin-right": "5px",
                                "margin-left": "5px",
                                "padding": "20px",
                            }),
                            dbc.Col([
                                dbc.Button("Inference", id="btn",  n_clicks=0, outline=True, color="primary", size="sm",
                                           className="me-1")
                            ], className="d-flex align-items-center justify-content-center", )
                        ])
                    ]),
                    html.Div([
                        html.Button(
                            '👍🏼 Like',
                            id='like-button',
                            value="I like the output",
                            n_clicks=0,
                            style={
                                'borderRadius': '10px',
                                'padding': '10px',
                                'backgroundColor': '#4CAF50',
                                'color': 'white'
                            }
                        ),
                        html.Button(
                            '👎🏼 Dislike',
                            id='dislike-button',
                            value="I like the output",
                            n_clicks=0,
                            style={
                                'borderRadius': '10px',
                                'padding': '10px',
                                'backgroundColor': '#FF5733',
                                'color': 'white'
                            }
                        )
                    ], style={'display': 'flex', 'justify-content': 'space-between'}),
                ]),
                html.Br(),
                dbc.Row([
                    html.Label(
                        "Feedback Dataset-RLHF",
                        style={
                            "font-family": "Times Roman",
                            "text-decoration": "underline",
                            "text-align": "center",
                            "color": "white",
                        },
                    )],
                    style={"margin": "5px", "text-align": "center"},
                    justify="center",
                ),
                dbc.Row([
                    html.Div([
                        dash_table.DataTable(
                            id='table',
                            columns=[{"name": i, "id": i, "renamable": True, "hideable": True} for i in
                                     feedback.columns],
                            data=feedback.to_dict('records'),
                            style_table={'overflowX': 'auto'},
                            export_format='xlsx',
                            editable=True,
                            include_headers_on_copy_paste=True,
                            sort_action='native',
                            page_action="native",
                            page_size=3,
                            style_cell={
                                'height': 'auto',
                                'minWidth': '140px',
                                'width': '150px',
                                'maxWidth': '180px',
                                'whiteSpace': 'normal',
                                'borderRadius': '10px',
                                'padding': '10px',
                                'backgroundColor': '#f0f0f0',
                                'color': 'black'
                            },
                            style_header={
                                'backgroundColor': '#4CAF50',
                                'color': 'white'
                            },
                            style_data={
                                'backgroundColor': '#f0f0f0',
                                'color': 'black'
                            }
                        ),
                        dcc.Store(id='table-data-store', data=feedback.to_dict('records')),
                    ])
                ]),
            ], style={
                "margin-right": "5px",
                "margin-left": "5px",
                "padding": "20px",
            }),
            html.Br(),
            dbc.Row([
                html.Label(
                    "Mistral-Nemo",
                    style={
                        "font-family": "Times Roman",
                        "text-decoration": "underline",
                        "text-align": "center",
                        "color": "white",
                    },
                )],
                style={"margin": "20px", "text-align": "center"},
                justify="center",
            ),
            dbc.Col([
                dbc.Row([
                    dcc.Textarea(
                        id='text-input1',
                        value="",
                        placeholder='Enter your text here...',
                        style={
                            'width': '100%',
                            'height': 300,
                            'borderRadius': '10px',
                            'padding': '20px',
                        }
                    ),
                    html.Br(),
                    dbc.Col([
                        dbc.Row([
                            dbc.Col([
                                dcc.Textarea(
                                    id='text-input11',
                                    placeholder='Inference results...',
                                    style={
                                        'width': '100%',
                                        'height': 300,
                                        'borderRadius': '10px',
                                        'padding': '20px',
                                    }
                                ),
                            ], style={
                                "margin-right": "10px",
                                'borderRadius': '10px',
                                "margin-left": "10px",
                                "padding": "20px",
                            }, width=8),
                            dbc.Col([
                                dbc.Button("Inference", id="btn1", n_clicks=0, outline=True, color="primary", size="sm",
                                           className="me-1")
                            ], className="d-flex align-items-center justify-content-center", )
                        ])
                    ]),
                    html.Div([
                        html.Button(
                            '👍🏼 Like',
                            id='like-button1',
                            value="I like the output",
                            n_clicks=0,
                            style={
                                'borderRadius': '10px',
                                'padding': '10px',
                                'backgroundColor': '#4CAF50',
                                'color': 'black'
                            }
                        ),
                        html.Button(
                            '👎🏼 Dislike',
                            id='dislike-button1',
                            value="I dont like the output",
                            n_clicks=0,
                            style={
                                'borderRadius': '10px',
                                'padding': '10px',
                                'backgroundColor': '#FF5733',
                                'color': 'black'
                            }
                        )
                    ], style={'display': 'flex', 'justify-content': 'space-between'})
                ]),
                html.Br(),
                dbc.Row([
                    html.Label(
                        "Feedback Dataset-RLHF",
                        style={
                            "font-family": "Times Roman",
                            "text-decoration": "underline",
                            "text-align": "center",
                            "color": "white",
                        },
                    )],
                    style={"margin": "5px", "text-align": "center"},
                    justify="center",
                ),
                dbc.Row([
                    html.Div([
                        dash_table.DataTable(
                            id='table1',
                            columns=[{"name": i, "id": i, "renamable": True, "hideable": True} for i in
                                     feedback1.columns],
                            data=feedback1.to_dict('records'),
                            style_table={'overflowX': 'auto'},
                            export_format='xlsx',
                            editable=True,
                            include_headers_on_copy_paste=True,
                            sort_action='native',
                            page_action="native",
                            page_size=3,
                            style_cell={
                                'height': 'auto',
                                'minWidth': '140px',
                                'width': '150px',
                                'maxWidth': '180px',
                                'whiteSpace': 'normal',
                                'borderRadius': '10px',
                                'padding': '10px',
                                'backgroundColor': '#f0f0f0',
                                'color': 'black'
                            },
                            style_header={
                                'backgroundColor': '#4CAF50',
                                'color': 'white'
                            },
                            style_data={
                                'backgroundColor': '#f0f0f0',
                                'color': 'black'
                            }
                        ),
                        dcc.Store(id='table-data-store1', data=feedback1.to_dict('records')),
                    ])
                ])
            ], style={
                "margin-right": "5px",
                "margin-left": "5px",
                "padding": "20px",
            })
        ]),
        html.Br(),

        dbc.Row([
            dbc.Col([
                html.P(id="dummy-element")
            ]),
            dbc.Col([

            ])
        ]),
    ],

    style={
        "display": "flex",
        "flex-direction": "column",
        "justify-content": "center",
        "align-items": "center",
        "width": "70%"
    },
    className="container-fluid",
)


@app.callback(
    Output('table-data-store1', 'data'),
    Input('table1', 'data'),
    prevent_initial_call=True
)
def update_store1_data(rows):
    updated_df = pd.DataFrame(rows)
    updated_df.to_csv("feedback1.csv", index=False)
    return rows


@app.callback(
    Output('table1', 'data'),
    Input('table-data-store1', 'modified_timestamp'),
    State('table-data-store1', 'data'),
    prevent_initial_call=True
)
def update_table1_data(ts, data):
    df = pd.read_csv("feedback1.csv")
    return df.to_dict('records')


@app.callback(
    Output('table-data-store', 'data'),
    Input('table', 'data'),
    prevent_initial_call=True
)
def update_store_data(rows):
    updated_df = pd.DataFrame(rows)
    updated_df.to_csv("feedback.csv", index=False)
    return rows


@app.callback(
    Output('table', 'data'),
    Input('table-data-store', 'modified_timestamp'),
    State('table-data-store', 'data'),
    prevent_initial_call=True
)
def update_table_data(ts, data):
    df = pd.read_csv("feedback.csv")
    return df.to_dict('records')


@app.callback(
    Output('dummy-element', 'children'),
    Input('like-button', 'n_clicks'),
    Input('dislike-button', 'n_clicks'),
    Input('like-button1', 'n_clicks'),
    Input('dislike-button1', 'n_clicks'),
    State('like-button', 'value'),
    State('dislike-button', 'value'),
    State('like-button1', 'value'),
    State('dislike-button1', 'value'),
    prevent_initial_call=True
)
def update_Like_And_Dontlike(like_clicks, dislike_clicks, like_clicks1, dislike_clicks1, st1, st2, st3, st4):
    if like_clicks:
        dicT = {"Input": [""], "Output": [""], "UserFeedback": [st1]}
        newDF = pd.DataFrame(dicT, dtype=object)
        feedback['UserFeedback'] = feedback['UserFeedback'].fillna(newDF['UserFeedback'][0])
        feedback.to_csv("feedback.csv", index=False, mode="a", header=False)
        return ""

    elif dislike_clicks:
        dicT = {"Input": [""], "Output": [""], "UserFeedback": [st2]}
        newDF = pd.DataFrame(dicT, dtype=object)
        feedback['UserFeedback'] = feedback['UserFeedback'].fillna(newDF['UserFeedback'][0])
        feedback.to_csv("feedback.csv", index=False, mode="a", header=False)
        return ""

    elif like_clicks1:
        dicT = {"Input": [""], "Output": [""], "UserFeedback": [st3]}
        newDF = pd.DataFrame(dicT, dtype=object)
        feedback1['UserFeedback'] = feedback1['UserFeedback'].fillna(newDF['UserFeedback'][0])
        feedback1.to_csv("feedback1.csv", index=False, mode="a", header=False)
        return ""

    elif dislike_clicks1:
        dicT = {"Input": [""], "Output": [""], "UserFeedback": [st4]}
        newDF = pd.DataFrame(dicT, dtype=object)
        feedback1['UserFeedback'] = feedback1['UserFeedback'].fillna(newDF['UserFeedback'][0])
        feedback1.to_csv("feedback1.csv", index=False, mode="a", header=False)
        return ""

    else:
        return ""


@app.callback(
    Output('text-input0', 'value'),
    Output('text-input11', 'value'),
    Input('btn', 'n_clicks'),
    Input('btn1', 'n_clicks'),
    State('text-input', 'value'),
    State('text-input1', 'value'),
    allow_duplicate=True,
    prevent_initial_call=True
)
def update_hidden_div(btn, btn1, text_inputValue, text_inputValue1):
    ctx = dash.callback_context
    if ctx.triggered:
        trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if trigger_id == "btn":
            result = models.llama(text_inputValue)
            dicT = {"Input": [text_inputValue], "Output": [result], "UserFeedback": [""]}
            newDF = pd.DataFrame(dicT, dtype=object)
            newDF.to_csv("feedback.csv", index=False, mode="a", header=False)
            return str(result), dash.no_update
        elif trigger_id == "btn1":
            result = models.mistralNemo(text_inputValue1)
            dicT = {"Input": [text_inputValue1], "Output": [result], "UserFeedback": [""]}
            newDF = pd.DataFrame(dicT, dtype=object)
            newDF.to_csv("feedback1.csv", index=False, mode="a", header=False)
            return dash.no_update, str(result)
    else:
        return dash.no_update, dash.no_update


if __name__ == "__main__":
    app.run_server(debug=True, port=5050)
