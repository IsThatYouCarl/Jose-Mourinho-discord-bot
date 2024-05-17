This project involves creating a Discord bot named "Jose Mourinho" with football-related functionalities. 

![jose](https://github.com/IsThatYouCarl/Jose-Mourinho-discord-bot/assets/90243903/47989d64-7c7b-4bd2-93a0-7b87e0a0d0f9)

The project was initially inspired by the idea of a Jose Mourinho chatbot responding to specific messages with relevant gifs on my Discord server, so I can spam certain gifs at my friend when I dominate him in efootball 2024. 

It has expanded to include features such as:

1. Retrieving league table rankings for the top 5 European Leagues.
2. Gathering top scorer statistics for each league.
3. Providing information on upcoming matches for a specific team or within a competition/league (though somewhat limited by API key access restrictions).
4. A remind_match function that allows the bot to automatically set a reminder for the closeset match in the upcoming matches (/remind_match).
5. Different reminder functions that allows you to set a reminder at a certain time (/remind_at), in a certain period of time (/remind_in) and every certain period of time (/remind_every).  

To implement this in your own discord bot, you need to acquire your bot token and football API token from this website https://www.football-data.org/
Then create a .env file, store the discord bot token and football API key in the following format:

BOT_TOKEN = "your bot token" <br />
FOOTBALL_API_KEY = "your personal api key"

Then run jose.py and voila
