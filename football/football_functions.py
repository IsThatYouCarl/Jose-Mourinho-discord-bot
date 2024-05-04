import http.client
import requests
import os
from dotenv import load_dotenv
from football.league_code import LEAGUE_CODE
from football.team_id import TEAM_ID
import json
import datetime

load_dotenv()

api_token = os.getenv('FOOTBALL_API_KEY')
league_code = LEAGUE_CODE
team_id = json.load(open("football\\teamcodes.json"))
headers = {'X-Auth-Token': api_token}

def convert_time(time):
    original_datetime = datetime.datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")
    new_datetime = original_datetime + datetime.timedelta(hours=8)
    converted_timestamp = new_datetime.strftime("%Y-%m-%d %I:%M%p")

    return converted_timestamp



def get_image (code):
    if code in ['PL', 'L1', 'BL', 'LL', 'SA']:
        return f"football/logos/{code}.jpg"
    else:
        return None
    
def get_current_season(url_code):
    url = f"https://api.football-data.org/v4/competitions/{url_code}/standings"
    conn = requests.get(url, headers = headers)
    data = conn.json()
    filter = data.get("filters")
    current_season = filter["season"]
    return current_season

def get_table (url_code, season):
    current_season = get_current_season(url_code)
    if url_code in league_code.values():   
        if season == None or season == current_season:
            url = f"https://api.football-data.org/v4/competitions/{url_code}/standings"
        
        else:
            url = f"https://api.football-data.org/v4/competitions/{url_code}/standings?season={season}&matchday=38"

        conn = requests.get(url, headers = headers)
        data = conn.json()

        #standings is a dictionary
        standings = data.get("standings")
        standings_data = standings[0]['table']

        str_re = '```\nLEAGUE: ' + str(data['competition']['name']) +\
                 ' ' * (45 - 2 - 8 - 10 - len(str(data['competition']['name']))) +\
                 'MATCHDAY: ' + str(data['season']['currentMatchday']) + '\n'
        str_re += '╔════╤════════════════════════════╤════╤════╤════╤════╤═════╤═════╗\n'
        str_re += '║ SN │            TEAM            │ M  │ W  │ D  │ L  │ PTS │ GD  ║\n'
        str_re += '╠════╪════════════════════════════╪════╪════╪════╪════╪═════╪═════╣\n'

        for team in standings_data:
            text ='║ %-2d │ %-26s │ %-2d │ %-2d │ %-2d │ %-2d │ %-3d │ %+-3d ║\n'\
                % (team['position'], data.get(team['team']['shortName'], team['team']['shortName'][:26])[:26], team['playedGames'], team['won'],
                    team['draw'], team['lost'], team['points'], team['goalDifference'])

            str_re += text

        str_re += '╚════╧════════════════════════════╧════╧════╧════╧════╧═════╧═════╝```'
       
    else:
        return "Invalid code"
    
    return str_re


def get_top_scorer(url_code, season):
    current_season = get_current_season(url_code)
    if url_code in league_code.values():   
        if season == None or season == current_season:
            url = f"https://api.football-data.org/v4/competitions/{url_code}/scorers"
        else:
            url = f"https://api.football-data.org/v4/competitions/{url_code}/scorers?season={season}"

        conn = requests.get(url, headers = headers)
        data = conn.json()

        #standings is a dictionary
        scorers_data = data.get("scorers")

        str_re = '```\nLEAGUE: ' + str(data['competition']['name']) +\
                    ' ' * (45 - 2 - 8 - 10 - len(str(data['competition']['name']))) +\
                    'SEASON: ' + str(data['filters']['season']) + '\n'
        str_re += '╔════╤══════════════════════════╤══════════════════════════╤════╤════╤════╗\n'
        str_re += '║ SN │          PLAYER          │          TEAM            │ G  │ A  │ MP ║\n'
        str_re += '╠════╪══════════════════════════╪══════════════════════════╪════╪════╪════╣\n'

        for i, scorer_data in enumerate(scorers_data):
            text ='║ %-2d │ %-24s │ %-24s │ %-2d │ %-2d │ %+-2d ║\n'\
                % (i+1, scorer_data['player']['name'][:26], scorer_data['team']['shortName'], scorer_data['goals'],scorer_data['assists'], 5)

            str_re += text

        str_re += '╚════╧══════════════════════════╧══════════════════════════╧════╧════╧════╝```'
        
    else:
        return "Invalid code"
    return str_re

def get_upcoming_matches(input_team, team_code, competition_id):
    if team_code in team_id.values():    
        if competition_id == None:
            url = f"http://api.football-data.org/v4/teams/{int(team_code)}/matches?status=SCHEDULED"

        else:
            url = f"http://api.football-data.org/v4/teams/{int(team_code)}/matches?status=SCHEDULED&competitions={competition_id}"

        conn = requests.get(url, headers = headers)
        data = conn.json()

        match_data = data.get("matches")
        
        str_re = '```\nTEAM: ' + input_team + '\n'
        str_re += '╔══════════════════════════╤══════════════════════════╤══════════════════════════╤══════════════════════╗\n'
        str_re += '║        COMPETITION       │          HOMETEAM        │          AWAYTEAM        │         TIME         ║\n'
        str_re += '╠══════════════════════════╪══════════════════════════╪══════════════════════════╪══════════════════════╣\n'

        for i, match in enumerate(match_data):
            text ='║ %-24s │ %-24s │ %-24s │ %20s ║\n'\
                % (match["competition"]["name"], match["homeTeam"]["shortName"], match["awayTeam"]["shortName"], convert_time(match["utcDate"]))

            str_re += text

        str_re += '╚══════════════════════════╧══════════════════════════╧══════════════════════════╧══════════════════════╝```'
    else:
        return "Invalid code"
    
    return str_re

# table = get_upcoming_matches("Chelsea", "3", None)
# print(table)
























    # def path_to_image_html(path):
    #     return '<img src="'+ path + '" width="40" >'

     # pd.set_option('display.max_colwidth', None)
    
    # df["emblem"] = images
    
    # format_dict = {}
    # format_dict["emblem"] = path_to_image_html
    
    # html_data = df.to_html(escape=False, formatters=format_dict, index=False)
    # img = BytesIO()

    # exists = True
    # i = 1
    
    # while exists:
    #     if os.path.exists(f"D:\\jose-mourinho bot\\football\\image\\temp{i}.png"):
    #         i+=1
    #     else:
    #         exists = False

    # imgkit.from_string(html_data, f"D\\jose-mourinho bot\\football\\images\\temp{i}.png", config = config)

    # # with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:

    # #     imgkit.from_string(html_data, temp_file.name, config=config)     
    # #     # Read the image data from the temporary file into a BytesIO object
    # #     temp_file.seek(0)
    # #     img_bytes = BytesIO(temp_file.read())

    # # os.unlink("temp.png")
    
    # return f"D\\jose-mourinho bot\\football\\images\\temp{i}.png"
  

    # # # img.seek(0)
    # # # imgkit.from_string(html_data, 'out.png', config = config) 
    
    # return img

# img.show()