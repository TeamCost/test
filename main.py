from PIL import Image
import discord, aiohttp, random, os
from discord.ext import commands, tasks
from itertools import cycle
from os import listdir
from random import choice
client = commands.Bot(command_prefix="$")
client.remove_command('help')
status = cycle(['with my balls-TeamCost#3960', 'with my developer-TeamCost#3960'])

@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    change_status.start()

@tasks.loop(seconds=9)
async def change_status():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(next(status)))

@client.command()
async def Omri(ctx):
    files = os.listdir(r"D:\arteom\פרטי\omri")
    lst = [discord.File(r"D:\arteom\פרטי\omri" + '\\' + file) for file in files]
    print(lst)
    await ctx.send(file=random.choice(lst))

@client.command()
async def Artium(ctx):
    files = os.listdir(r"D:\arteom\פרטי\artium")
    lst = [discord.File(r"D:\arteom\פרטי\artium" + '\\' + file) for file in files]
    print(lst)
    await ctx.send(file=random.choice(lst))

@client.command()
async def Nevo(ctx):
    files = os.listdir(r"D:\arteom\פרטי\nevo")
    lst = [discord.File(r"D:\arteom\פרטי\nevo" + '\\' + file) for file in files]
    print(lst)
    await ctx.send(file=random.choice(lst))
    await ctx.send("@everyone")

@client.command()
async def HotGirls(ctx):
    files = os.listdir(r"D:\arteom\פרטי\hot girls")
    lst = [discord.File(r"D:\arteom\פרטי\hot girls" + '\\' + file) for file in files]
    print(lst)
    await ctx.send(file=random.choice(lst))
    await ctx.send("@everyone")

@client.command()
async def Ilanosh2(ctx):
    files = os.listdir(r"D:\arteom\פרטי\ilanoshPremium")
    lst = [discord.File(r"D:\arteom\פרטי\ilanoshPremium" + '\\' + file) for file in files]
    print(lst)
    await ctx.send(file=random.choice(lst))
    await ctx.send("@everyone")

@client.command()
async def Ilanosh1(ctx):
    files = os.listdir(r"D:\arteom\פרטי\VIP Israeli- ilanosh")
    lst = [discord.File(r"D:\arteom\פרטי\VIP Israeli- ilanosh" + '\\' + file) for file in files]
    print(lst)
    await ctx.send(file=random.choice(lst))
    await ctx.send("@everyone")

@client.command()
async def Ilanosh(ctx):
    files = os.listdir(r"D:\arteom\פרטי\ilanosh")
    lst = [discord.File(r"D:\arteom\פרטי\ilanosh" + '\\' + file) for file in files]
    print(lst)
    await ctx.send(file=random.choice(lst))
    await ctx.send("@everyone")

@client.command()
async def Naruto(ctx):
    embed = discord.Embed(colour=discord.Colour.green(), title="Look at dis")
    reddit = ['Naruto', 'NarutoShinobiStriker', 'Boruto', 'narutomemes']
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f'https://www.reddit.com/r/{random.choice(reddit)}/new.json?sort=hot') as r:
            res = await r.json()
            print()
            embed.set_image(url=res['data']['children'][random.randint(0, 15)]['data']['url'])

            await ctx.send(embed=embed)

@client.command()
async def Hentai(ctx):
    embed = discord.Embed(colour=discord.Colour.green(), title="Look at dis")
    reddit = ['hentai', 'HentaiSource', 'hentaidankermemes']
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f'https://www.reddit.com/r/{random.choice(reddit)}/new.json?sort=hot') as r:
            res = await r.json()
            print()
            embed.set_image(url=res['data']['children'] [random.randint(0, 15)]['data']['url'])

            await ctx.send(embed=embed)

@client.command()
async def nsfw(ctx):
    embed = discord.Embed(colour=discord.Colour.green(), title="Take a nude")
    reddit = ['riasgremory', 'milf', 'LegalTeens', 'Just18', 'youngporn', 'Barelylegal', 'barelylegalteens', 'Blonde']
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f'https://www.reddit.com/r/{random.choice(reddit)}/new.json?sort=hot') as r:
            res = await r.json()
            print()
            embed.set_image(url=res['data']['children'][random.randint(0, 15)]['data']['url'])

            await ctx.send(embed=embed)

@client.command()
@commands.is_owner()
async def chatClear(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    channel = ctx.channel.purge

@client.command()
async def meme(ctx):
    embed = discord.Embed(colour=discord.Colour.green(), title="""Here's a meme""")
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'][random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)

@client.command()
@commands.is_owner()
@commands.has_role('owner')
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
@commands.is_owner()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)

@client.command()
@commands.is_owner()
async def unban(ctx, *,member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')

@client.command()
#@commands.has_role('🛠️')
async def dm(ctx, user: discord.User, *, msg):
    embed = discord.Embed(title=f"Direct message command:", description=f"Message was executed succesfully!.")
    await user.send(f"this message was send to: {user} from {ctx.author.mention}. the msg is: {msg}")
    await ctx.send(embed=embed)

@client.command()
async def h(ctx):
    embed = discord.Embed(title="Help commands",
                          description="Commands this is the commands u need to know about our bot that TeamCost#6969 with Reven8e.sh#9290 was created", color=0x1100ff)
    embed.set_author(name="Artium Bot", url="https://discord.gg/Gg8VwKZW",
                     icon_url="https://cdn.discordapp.com/attachments/798669204102184980/806978264798855178/unknown.png")
    embed.add_field(name="help",
                    value="this is the command that open u the commands panel, this command was created by TeamCost#3960", inline=False)
    embed.add_field(name="Hentai",
                    value="this is the command that shows hentai photos, this command was created by Reven8e.sh#9290", inline=False)
    embed.add_field(name="Naruto",
                    value="this is the command that shows Naruto photos, this command was created by TeamCost#3960",
                    inline=False)
    embed.add_field(name="nsfw",
                    value="this is the command that sends nudes, this command was created by Reven8e.sh#9290", inline=False)
    embed.add_field(name="meme",
                    value="this is the command that sends cool memes from the internet, this command was created by Reven8e.sh#9290", inline=False)
    embed.add_field(name="EggPlan",
                    value="this is the command that sends cool eggplan photos from the internet, this command was created by TeamCost#3960", inline=False)
    embed.add_field(name="Duck",
                    value="this is the command that sends cool duck photos from the internet, this command was created by TeamCost#3960",
                    inline=False)
    embed.add_field(name="chatClear",
                    value="this is the command that clears the chat, this command was created by TeamCost#3960",
                    inline=False)
    embed.add_field(name="dm",
                    value="this is the command send dm to someone you choice, this command was created by TeamCost#3960",
                    inline=False)
    embed.add_field(name="join",
                    value="this is the command that make the dj bot enter your voice-channel", inline=False)
    embed.add_field(name="leave",
                    value="this is the command that make the dj bot leave your voice-channel", inline=False)
    embed.add_field(name="play",
                    value="this is the command that make the dj bot play a song", inline=False)
    embed.set_footer(text="©Artium Bot - Join our discord server https://discord.gg/Gg8VwKZW")
    embed.add_field(name=ctx.author.display_name, value="did it solved your problem? ~If u still don't have an answer pls contact the staff")
    await ctx.send(embed=embed)

client.run("NzQwMjU5MDA1NjYxODM5Mzgx.XymZ7A.0GZHMvu1aa_1DWOnUKaJKDTtLK4")