import json
from team_id import TEAM_ID
import requests
import os
from dotenv import load_dotenv


load_dotenv()

team_id = TEAM_ID
teams = json.load(open("teamcodes.json"))

api_token = os.getenv('FOOTBALL_API_KEY')
headers = {'X-Auth-Token': api_token}

team_list = []
id_list = []

for team in teams: 
    team_list.append(team)

for id in team_id:
    id_list.append(team_id[id])

print(id_list)

# shortname = []

# max_retry = 10
# for id in id_list:
#     retry = 0
#     while retry < max_retry:
#         id_int = int(id)
#         url = f"http://api.football-data.org/v4/teams/{id_int}"
#         conn = requests.get(url, headers = headers)
#         if conn.status_code == 200:
#             data = conn.json()
#             shortName = data.get("shortName")
#             Name = data.get("name")
#             if shortName is None:
#                 shortname.append(Name)
#             else:
#                 shortname.append(shortName)
#             break
#         else:
#             retry +=1

# shortName = data.get("shortName")

# Name = data.get("name")
# if shortName is None:
#     print(Name)
# else:
#     print(Name)


# print(shortname)  
# for item1, item2 in zip(shortname, id_list):
#     print(f'{item1}:{item2}')


