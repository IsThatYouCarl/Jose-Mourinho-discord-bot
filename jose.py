from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord import app_commands
import requests, json, random
import typing
import os
import re
import football.football_functions 
from football.teamcodes import Teams, Leagues
from football.league_code import LEAGUE_CODE
from reminder.reminder import get_seconds_and_reason
import time
import asyncio
import enum

load_dotenv()

code = LEAGUE_CODE
links = json.load(open("gif.json"))
dir = json.load(open("audio\\audio.json"))
team_id = json.load(open("football\\teamcodes.json"))

text_channel_id = os.getenv('TEXT_CHANNEL_ID') 
voice_channel_id = os.getenv('VOICE_CHANNEL_ID')
bot_token = os.getenv('BOT_TOKEN')
guilds_id = discord.Object(id = int(os.getenv('GUILDS_ID')))



def run():
    bot = commands.Bot(command_prefix="", intents = discord.Intents.all(), case_insensitive = True)

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
            await ctx.send(file = discord.File(football.football_functions.get_image(args[0])))
        else:
            await ctx.send("Mate just enter league, I am Jose Mourinho")


    @bot.tree.command()
    async def table(interaction: discord.Interaction, league_choice: typing.Literal["BL", "PL", "LL", "SA", "FL"]):   
        await interaction.response.send_message(f"hollup, I'm getting standings of {league_choice}")
            
        table = football.football_functions.get_table(code[league_choice], None) 
        await interaction.channel.send(table)

    @bot.tree.command()
    async def upcoming(interaction: discord.Interaction, league_choice: Teams):   
        await interaction.response.send_message(f"hollup, I'm getting upcoming matches of {league_choice}")
        print(league_choice.name, league_choice.value)
        table = football.football_functions.get_upcoming_matches(league_choice.name, str(league_choice.value), None) 
        await interaction.channel.send(table)

    @bot.tree.command()
    async def topscorer(interaction: discord.Interaction, league_choice: Leagues):   
        await interaction.response.send_message(f"hollup, I'm getting top scorers of {league_choice}")
        print(league_choice.name, league_choice.value)
        scorer_table = football.football_functions.get_top_scorer(league_choice.value, None) 
        await interaction.channel.send(scorer_table)

    bot.run(bot_token)

if __name__ == "__main__":
    run()





# intents = discord.Intents.default()
# intents.message_content = True

# client = discord.Client(intents=intents)
        
# def keep_words(text, words):   
#     result = [word for word in words if word in text]        
#     processed_word= ''
#     for item in result:
#         processed_word = processed_word + item
#     return processed_word

# def remove_space(word):
#     return ''.join(word.split())

# @client.event
# async def on_ready():
#     print("Hello, I'm the special one")


# @client.event
# async def on_message(message):
#     print(message.content)
#     if message.author == client.user:
#         return
    
#     for text in ["yup", "calma", "respect", "nospeak", "shush", "sui", "yaaaaa", "jaaaaa", "lmaoooo","it's all good"]:   
#         if message.content.lower().startswith('spam') and text in message.content.lower():
#             new_message = message.content.lower()
#             new_text = new_message.replace("spam", "").strip()
#             new_text = new_text.lower()        
#             lst = re.findall(r'\d+$', new_text)
            
#             if lst:
#                 last_digit = lst[0]
#                 new_new_text = new_text.replace(last_digit, '')
#                 gif_link = links.get(new_new_text)
#                 if int(last_digit) < 25:
#                     for i in range(int(last_digit)):
#                         await message.channel.send(random.choice(gif_link))
#                         print("printed in range of ", i)
#                 else:
#                     await message.channel.send("Lol maximum number of spam allowed is 25, cope")
#             else:
#                 gif_link = links.get(new_text)
#                 for i in range(8):
#                     await message.channel.send(random.choice(gif_link))
#                     print("printed in default range")

#         elif text in message.content.lower():
#             gif_link = links.get(text.lower())
#             await message.channel.send(random.choice(gif_link))

#     for text in ["projectiondeflectionreflection", "projectionreflectiondeflection", "deflectionprojectionreflection", "deflectionreflectionprojection", "reflectionprojectiondeflection", "reflectiondeflectionprojection"]:
#         if text in keep_words(message.content.lower(), ['projection', 'deflection', 'reflection']):
#             audio_dir = dir.get("projection, deflection, reflection")
#             await message.channel.send(file=discord.File(random.choice(audio_dir)))

#     for text in ["chinese", "overrated"]:
#         if text in message.content.lower():
#             channel = (client.get_channel(voice_channel_id) or await client.fetch_channel(voice_channel_id))
#             voice = await channel.connect()
#             # audio_dir = random.choice(dir.get(message.content.lower()))
#             source = FFmpegPCMAudio("GOAT.wav")
#             player = voice.play(source)
#             # file=discord.File(random.choice(audio_dir))

#     if message.content == "leave":
#         for voice in client.voice_clients:
#             if voice.guild == message.guild:
#                 await voice.disconnect()

#     if message.content == "EMBARASSING":
#         audio_dir = dir.get("EMBARASSING")
#         await message.channel.send(file=discord.File(random.choice(audio_dir)))

               
#     for text in ["the goat", "da goat", "goated"]:
#         if text in message.content.lower():
#             await message.channel.send("https://tenor.com/view/goat-gif-18600890")
#             audio_dir = dir.get("goat")
#             await message.channel.send(file=discord.File(random.choice(audio_dir)))

#     for text in ["hellojose", "hijose", "heyjose", "yojose"]:
#         if text in remove_space(message.content.lower()):
#             await message.channel.send("Hello, I'm Jose Mourinho, I turn good players into great players and great teams into champions")

#     for text in ["fuckyoujose"]:
#         if text in keep_words(message.content.lower(), ['fuck', 'you', 'jose']):
#             await message.channel.send("Hey show some respect, sree for me and two for zem, RESPECT, RESPECT")
#     for text in ["🤓", "🤏",]:
#         if text in message.content:
#             await message.channel.send("🗣️, quit the yapping lil bro🤫")
    
#     if "wikhele" in message.content.lower():
#         await message.channel.send("Is that W in the room with us together with my porto ucl run? I don't think so 🤫")

#     for text in code.keys():
#         if message.content.startswith("image") and text in message.content:
#             new_code = message.content.replace("image", "").strip()
#             await message.channel.send(file=discord.File(football.football_functions.get_image(new_code)))

#         if message.content.startswith("table") and text in message.content:
#             new_text = message.content.replace("table", "").strip()     
#             lst = re.findall(r'\d+$', new_text)
            
#             if lst:
#                 season = lst[0]
#                 new_code = new_text.replace(season, '').strip()
#                 url_code = code[new_code]
#                 await message.channel.send( football.football_functions.get_table(url_code, season))
                  
#             else:         
#                 new_code = new_text  
#                 url_code = code[new_code]
#                 await message.channel.send(football.football_functions.get_table(url_code, None))
     
#                     continue

#     for text in code.keys():
#         if message.content.startswith("image") and text in message.content:
#             new_code = message.content.replace("image", "").strip()
#             await message.channel.send(file=discord.File(football.football_functions.get_image(new_code)))

#         if message.content.startswith("table") and text in message.content:
#             new_text = message.content.replace("table", "").strip()     
#             lst = re.findall(r'\d+$', new_text)
            
#             if lst:
#                 season = lst[0]
#                 new_code = new_text.replace(season, '').strip()
#                 url_code = code[new_code]
#                 await message.channel.send( football.football_functions.get_table(url_code, season))
                  
#             else:         
#                 new_code = new_text  
#                 url_code = code[new_code]
#                 await message.channel.send(football.football_functions.get_table(url_code, None))
     
#                     continue


# for text in code.keys():
#         if message.content.startswith("image") and text in message.content:
#             new_code = message.content.replace("image", "").strip()
#             await message.channel.send(file=discord.File(football.football_functions.get_image(new_code)))

#         if message.content.startswith("table") and text in message.content:
#             new_text = message.content.replace("table", "").strip()     
#             lst = re.findall(r'\d+$', new_text)
            
#             if lst:
#                 season = lst[0]
#                 new_code = new_text.replace(season, '').strip()
#                 url_code = code[new_code]
#                 await message.channel.send( football.football_functions.get_table(url_code, season))
                  
#             else:         
#                 new_code = new_text  
#                 url_code = code[new_code]
#                 await message.channel.send(football.football_functions.get_table(url_code, None))


#     #question on stackoverflow
#     if message.content.startswith("remind"):
#         message_stripped = message.content.replace("remind", "").strip()
#         global flag
#         flag = True

#         if message_stripped.startswith("in"):
#             seconds, reason = get_seconds_and_reason(message.content)
#             time.sleep(seconds)
#             await message.channel.send(f"Hey, this is a reminder to {reason}")

#         if message_stripped.startswith("stop"):
#             flag= False

#         if message_stripped.startswith("every") :
#             while flag:
#                 seconds, reason = get_seconds_and_reason(message.content)
#                 time.sleep(seconds)
#                 if flag is False:
#                     break
#                 else:            
#                     await message.channel.send(f"Hey, this is a reminder to {reason}")         
#                     continue



# if __name__ == "__main__":
#     client.run(bot_token)


