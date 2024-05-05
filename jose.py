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
import enum

load_dotenv()

code = LEAGUE_CODE
links = json.load(open("gif.json"))
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







