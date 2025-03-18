from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord import app_commands
import requests, json, random
import typing
import os
import re
import football_functions 
from football.teamcodes import Teams, Leagues, Team_Leagues, Seasons
from football.league_code import LEAGUE_CODE
from reminder.reminder import get_seconds_and_reason
import time
import asyncio
from datetime import datetime, timedelta

load_dotenv()

code = LEAGUE_CODE
links = json.load(open("gif.json"))
team_id = json.load(open("football\\teamcodes.json"))

text_channel_id = os.getenv('TEXT_CHANNEL_ID') 
voice_channel_id = os.getenv('VOICE_CHANNEL_ID')
bot_token = os.getenv('BOT_TOKEN')
guilds_id = discord.Object(id = int(os.getenv('GUILDS_ID')))

def check_time(time_unit):
    if len(time_unit) == 1:
        time_unit_new = f'0{time_unit}'
    else:
        time_unit_new = time_unit
    return time_unit_new

def run():
    bot = commands.Bot(command_prefix="", intents = discord.Intents.all(), case_insensitive = True)

    global loop_bool
    loop_bool = True

    global table_upcoming
    table_upcoming = ''

    @bot.event
    async def on_ready():
        bot.tree.copy_global_to(guild = guilds_id)
        await bot.tree.sync(guild = guilds_id)

    @bot.command(name = "Hello", aliases = ["Hey", "Yo", "Hi"])
    async def hello(ctx, *args):
        for word in args:
            if "jose" in word.lower():
                await ctx.send("Hello, I'm Jose Mourinho, I turn good players into great players and great teams into champions")

    @bot.command(name = "🤓", aliases = ["🤏"])
    async def emoji(ctx):
        await ctx.send("🗣️, quit the yapping lil bro🤫")

    @bot.command()
    async def wikhele(ctx):  
        await ctx.send("Is that W in the room with us together with my porto ucl run? I don't think so 🤫")

    @bot.command()
    async def fuck(ctx, *args):
        list_of_words = ["jose","you, Jose"]
        for word in args:
            if word.lower() in list_of_words:            
                await ctx.send("Hey show some respect, sree for me and two for zem, RESPECT, RESPECT")

    @bot.command(name = "yup", aliases = ["calma", "respect", "nospeak", "shush", "sui"])
    async def gif(ctx):
        gif_link = links.get(ctx.invoked_with.lower())
        gif_link_real = gif_link[0]
        await ctx.send(gif_link_real)

    @bot.command()
    async def spam(ctx, *args):
        if len(args) == 1:
            gif_link = links.get(args[0].lower())
            gif_link_real = gif_link[0]   
            for i in range(10):
                await ctx.send(gif_link_real)            
        elif len(args) == 2:
            gif_link = links.get(args[0].lower())
            gif_link_real = gif_link[0]
            number = args[1]
            if int(number) < 25:
                for i in range(int(number)):
                    await ctx.send(gif_link_real)
            else:
                await ctx.send("maximum number of spam allowed is 25, cope. I am Jose Mourinho")
        else:
            await ctx.send("Enter in correct syntax dumbass")

    @bot.command()
    async def image(ctx, *args):
        if len(args) == 1:
            new_code = args[0]
            await ctx.send(file = discord.File(football_functions.get_image(args[0])))
        else:
            await ctx.send("Mate just enter league, I am Jose Mourinho")


    @bot.tree.command()
    async def table(interaction: discord.Interaction, league_choice: typing.Literal["BL", "PL", "LL", "SA", "FL"], year:Seasons):   
        await interaction.response.send_message(f"hollup, I'm getting standings of {league_choice}")
            
        table = football_functions.get_table(code[league_choice], str(year.value))
        await interaction.channel.send(table)

    @bot.tree.command()
    async def upcomingteammatch(interaction: discord.Interaction, team_choice: Teams):   
        await interaction.response.send_message(f"hollup, I'm getting upcoming matches of {team_choice}")
        print(team_choice.name, team_choice.value)
        table = football_functions.get_upcoming_matches_for_team(team_choice.name, str(team_choice.value)) 

        global table_upcoming
        table_upcoming = table

        await interaction.channel.send(table)

    @bot.tree.command()
    async def upcomingcompetitionmatch(interaction: discord.Interaction, league_choice: Leagues):
        await interaction.response.send_message(f"hollup, I'm getting upcoming matches of {league_choice.name}")
        print(league_choice.name, league_choice.value)
        table = football_functions.get_upcoming_matches_for_competition(league_choice.name, league_choice.value) 

        global table_upcoming
        table_upcoming = table

        await interaction.channel.send(table)

    @bot.tree.command()
    async def topscorer(interaction: discord.Interaction, league_choice: Leagues):   
        await interaction.response.send_message(f"hollup, I'm getting top scorers of {league_choice.name}")
        print(league_choice.name, league_choice.value)
        scorer_table = football_functions.get_top_scorer(league_choice.value, None) 
        await interaction.channel.send(scorer_table)

    @bot.tree.command()
    async def remind_match(interaction: discord.Interaction):
        global table_upcoming

        if table_upcoming == '':
            await interaction.response.send_message("Which match you want me to remind?")
            return
        else:
            match_time = re.findall(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}[AP]M',table_upcoming)
            print(match_time)
            if match_time:
                match_time_at = 'These are the upcoming matches'
                for i, time in enumerate(match_time):
                    if i == len(match_time) - 1:
                        match_time_at += f' at {time}'
                    else:
                        match_time_at += f' at {time} and'       
                
                await interaction.response.send_message(f'{match_time_at}, setting reminder for the closest match at {match_time[0]}')

                datetime_obj = datetime.strptime(match_time[0], '%Y-%m-%d %I:%M%p')
                time_12hr = datetime.strftime(datetime_obj, '%Y-%m-%d %H:%M:%S')
   
                ctx = interaction.channel
                reason = f'upcoming match at {match_time[0]}'
                global loop_bool
                loop_bool = True

                asyncio.create_task(reminder_event(ctx, time_12hr, reason, False))
            else:
                await interaction.response.send_message(f"No upcoming matches currently")

    @bot.tree.command()   
    async def remind_every(interaction: discord.Interaction,h:str, m:str, s:str, reason:str):
        H = check_time(h)
        M = check_time(m)
        S = check_time(s)
        time_string = f'{H}:{M}:{S}'
        await interaction.response.send_message(f'aight, reminder every {time_string} for {reason}')
   
        ctx = interaction.channel
        time_12hr = timedelta(hours=int(H), minutes=int(M), seconds=int(S))
        global loop_bool
        loop_bool = True

        asyncio.create_task(reminder_continuous(ctx, time_12hr, reason))
    

    @bot.tree.command()   
    async def remind_in(interaction: discord.Interaction,h:str, m:str, s:str, reason:str):
        H = check_time(h)
        M = check_time(m)
        S = check_time(s)
        time_string = f'{H}:{M}:{S}'
        await interaction.response.send_message(f'aight, reminder in {time_string} for {reason}')

        ctx = interaction.channel
        time_12hr = timedelta(hours=int(H), minutes=int(M), seconds=int(S))
        global loop_bool
        loop_bool = True

        asyncio.create_task(reminder_event(ctx, time_12hr, reason, True))
        
    @bot.tree.command()
    async def remind_at(interaction: discord.Interaction, h:str, m:str, ampm: typing.Literal["AM", "PM"], reason:str):

        H = check_time(h)
        M = check_time(m)
        time_string = f'{H}:{M}{ampm}'
        await interaction.response.send_message(f'aight, reminder today at {time_string} for {reason}')

        ctx = interaction.channel
        time = datetime.strptime(time_string, "%I:%M%p")
        time_12hr = time.strftime("%Y-%m-%d %H:%M:%S")
        global loop_bool
        loop_bool = True

        asyncio.create_task(reminder_event(ctx, time_12hr, reason, False))

    @bot.tree.command()
    async def remind_stop(interaction: discord.Interaction):
        try:
            global loop_bool
            loop_bool = False
            await interaction.response.send_message("Alright, all reminders have been removed")
        except:
            print("No reminders currently")

    @bot.event
    async def reminder_event(channel, time_12hr, reason, in_or_at):
        global loop_bool
        if in_or_at is False:
            while loop_bool is True:      
                current_time =  time.strftime("%Y-%m-%d %H:%M:%S")
                if current_time >= time_12hr:
                    await channel.send(f'Hey, it is time for {reason}')
                    break        
                else:  
                    await asyncio.sleep(1)
                    continue

        elif in_or_at is True:      
            current_time_string = time.strftime("%H:%M:%S")
            current_time = datetime.strptime(current_time_string, '%H:%M:%S')      
            target_time = current_time + time_12hr

            while loop_bool is True:
                current_time_string = time.strftime("%H:%M:%S")
                current_time = datetime.strptime(current_time_string, '%H:%M:%S')  
                if current_time >= target_time:
                    await channel.send(f'Hey, it is time for {reason}')
                    break
                else:
                    await asyncio.sleep(1)
                    continue
          
        else:
            await channel.send("Some error mate")

    @bot.event
    async def reminder_continuous(channel, time_remind, reason):
        global loop_bool
        while loop_bool is True:
            current_time_string = time.strftime("%H:%M:%S")
            current_time = datetime.strptime(current_time_string, '%H:%M:%S')      
            target_time = current_time + time_remind
            print(current_time)
            print(target_time)
           
            while loop_bool is True:
                current_time_string = time.strftime("%H:%M:%S")
                current_time = datetime.strptime(current_time_string, '%H:%M:%S')      
                if current_time >= target_time:
                    await channel.send(f'Hey, it is time for {reason}')
                    break
                else:        
                    await asyncio.sleep(1)
                    continue

    bot.run(bot_token)

if __name__ == "__main__":
    run()



