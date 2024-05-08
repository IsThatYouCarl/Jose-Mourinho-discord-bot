import http.client
import requests
import os
from dotenv import load_dotenv
from football.league_code import LEAGUE_CODE
from football.database_code import DATABASE_CODE
import json
import csv
import datetime

load_dotenv()

api_token = os.getenv('FOOTBALL_API_KEY')
league_code = LEAGUE_CODE
database_code = DATABASE_CODE
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
    print(current_season)
    if url_code in league_code.values():   
        if int(season) == int(current_season):
            url = f"https://api.football-data.org/v4/competitions/{url_code}/standings"
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
            return str_re
        
        elif 1992 < int(season) < int(current_season):
            path = database_code[int(url_code)]
            with open(path, 'r') as csv_file:
                rows = []
                csv_reader = csv.DictReader(csv_file)
                for line in csv_reader:
                    if line['Season_End_Year'] == str(int(season)+1):
                        rows.append(line)
            print(rows)
               
            league = database_code[url_code]
            parts = league.split("\\")
            # Get the last part of the split string
            last_part = parts[-1]
            # Remove the ".csv" extension
            stripped_league = last_part.rstrip(".csv")
      
            str_re = '```\nLEAGUE: ' + str(stripped_league) +\
                 ' ' * (6) +'MATCHDAY: ' + '38' + 'SEASON:' + f'int{season} - {int(season)+1}'  + '\n'
            str_re += '╔════╤════════════════════════════╤════╤════╤════╤════╤═══════╤═════╗\n'
            str_re += '║ SN │            TEAM            │ M  │ W  │ D  │ L  │  PTS  │ GD  ║\n'
            str_re += '╠════╪════════════════════════════╪════╪════╪════╪════╪═══════╪═════╣\n'

            for row in rows:
                text ='║ %-2d │ %-26s │ %-2d │ %-2d │ %-2d │ %-2d │ %-5s │ %+-3d ║\n'\
                    % (int(row['Rank'].encode('latin1').decode('utf-8')), row['Team'].encode('latin1').decode('utf-8'), int(row['MP']), int(row['W']), int(row['D']),
                        int(row['L']), row['Pts'], int(row['GD']))

                str_re += text

            str_re += '╚════╧════════════════════════════╧════╧════╧════╧════╧═════╧═════╝```'
        
            return str_re
             
    else:
        return "Invalid code"


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

