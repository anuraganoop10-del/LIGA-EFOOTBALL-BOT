import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
print(f"LIGA Auction Bot is online as {bot.user}")

@bot.command()
async def ping(ctx):
await ctx.send("LIGA Auction Bot is online! ⚽💛🖤")

@bot.command()
async def auction(ctx, *, player: str):
embed = discord.Embed(
title=f"⚽ LIGA AUCTION: {player}",
description="🔴 BIDDING IS OPEN!",
color=0xF1C40F
)
embed.add_field(name="Current Bid", value="No bids yet", inline=True)
embed.add_field(name="Highest Bidder", value="None", inline=True)
await ctx.send(embed=embed)

if not TOKEN:
raise RuntimeError("DISCORD_TOKEN is missing from the environment")

bot.run(TOKEN)