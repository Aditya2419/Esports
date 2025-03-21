import dicords
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"Bot ready as {bot.user}")

@bot.command()
async def matches(ctx):
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        matches = response.json()
        for match in matches:
            summary = f"{match['name']} | {match['tournament']['name']} | {match['scheduled_at']}"
            await ctx.send(summary)

bot.run("YOUR_DISCORD_TOKEN")  # Get this from Discord Developer Portal