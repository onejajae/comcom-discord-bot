import asyncio
import json
import os

import discord
from discord.ext import commands

with open("config.json") as f:
  config  = json.load(f)

intents = discord.Intents.default()
intents.message_content = True

cmd_prefix = config["prefix"]
bot = commands.Bot(cmd_prefix, intents=intents)

async def load_cogs(cogs_path="cogs"):
  for file in os.listdir(cogs_path):
    if file.endswith(".py"):
      await bot.load_extension(f"cogs.{file.split('.')[0]}")
      print(f'{file} is successfully loaded')


asyncio.run(load_cogs())
bot.run(config["token"])