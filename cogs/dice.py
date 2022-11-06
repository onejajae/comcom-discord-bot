from discord.ext import commands
import random


class Dice(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command(name="roll", aliases=["dice"])
  async def roll(self, ctx):
    await ctx.reply(f'{random.randint(1, 6)}')

async def setup(bot):
  await bot.add_cog(Dice(bot))