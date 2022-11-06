from discord.ext import commands


class Basic(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.Cog.listener()
  async def on_member_join(self, member):
    channel = member.guild.system_channel
    if channel is not None:
      await channel.send(f'Welcome {member.mention}.')

  @commands.command(name="echo")
  async def echo(self, ctx, *, msg):
    await ctx.send(msg)

  @commands.command(name="hello")
  async def hello(self, ctx):
    await ctx.send("Hello world")

  @commands.command(name="test")
  async def test(self, ctx):
    await ctx.send("test")

async def setup(bot):
  await bot.add_cog(Basic(bot))