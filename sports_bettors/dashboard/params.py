import os
import pandas as pd

from config import Config

college_teams = set(pd.read_csv(os.path.join(Config.DATA_DIR, 'sports_bettors', 'curated', 'college_football',
                                             'df_curated.csv'))['team'])
nfl_teams = set(pd.read_csv(os.path.join(Config.DATA_DIR, 'sports_bettors', 'curated', 'nfl',
                                         'df_curated.csv'))['team'])

utils = {
    'empty_figure': {
        "layout": {
            "xaxis": {
                "visible": False
            },
            "yaxis": {
                "visible": False
            },
            "annotations": [
                {
                    "text": "No matching data found",
                    "xref": "paper",
                    "yref": "paper",
                    "showarrow": False,
                    "font": {
                        "size": 28
                    }
                }
            ]
        }
    },
    'no_show': {'display': 'none'},
    'show': {'display': 'block'}
}

params = {
    'v2': {
        'league-opts': [
            {'label': 'NFL', 'value': 'nfl'},
            {'label': 'College Football', 'value': 'college_football'}
        ],
        'team-opts': {
            'nfl': [{'label': team, 'value': team} for team in nfl_teams],
            'college_football': [{'label': team, 'value': team} for team in college_teams]
        },
        'feature-sets-opts': {
            'nfl': [
                {'label': 'Rushing', 'value': 'RushOnly'},
                {'label': 'Passing', 'value': 'PassOnly'},
                {'label': 'Offense', 'value': 'Offense'},
                {'label': 'Offense (Advantage)', 'value': 'OffenseAdv'},
                # {'label': 'Points Scored', 'value': 'PointsScored'},
            ],
            'college_football': [
                {'label': 'Rushing', 'value': 'RushOnly'},
                {'label': 'Passing', 'value': 'PassOnly'},
                {'label': 'Offense', 'value': 'Offense'},
                {'label': 'Offense (Advantage)', 'value': 'OffenseAdv'},
                {'label': 'Points Scored', 'value': 'PointsScored'}
            ]
        }
    }
}