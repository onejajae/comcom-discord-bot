from discord.ext import commands


class Basic(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command(name="echo")
  async def echo(self, ctx, *, msg):
    await ctx.reply(msg)

  @commands.command(name="hello")
  async def hello(self, ctx):
    await ctx.send("Hello world")

  @commands.command(name="test")
  async def test(self, ctx):
    await ctx.send("test")

async def setup(bot):
  await bot.add_cog(Basic(bot))