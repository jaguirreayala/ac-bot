import discord
from datetime import datetime, tzinfo
import os
from pytz import timezone
import pytz
from bottoken import *
from birthdays import *
from bugs import *
from fish import *

class acbot(discord.Client):
    async def on_ready(self):
        print('ac-bot has successfully logged in!'.format(self.user))  # successful login

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message)) # logging messages in console

        if message.content.startswith('!'):
            message.content = message.content.replace('!', '')

            if message.content == "help":
                await message.channel.send("Start commands with '!'")
                await message.channel.send("birthday <date/nodate> - find out the birthday of a specific villager / find out whose birthday is today")
                await message.channel.send("bug <name/noname> - find out bug information / get list of all available bugs")
                await message.channel.send("fish <name/noname> - find out fish information / get list of all available fish")
#######################################################################################################################################################################################################################
            if message.content.startswith("birthday"):  # get current date and find whose birthday it is
                if message.content == "birthday":
                    date = datetime.now(tz=pytz.utc)
                    date = date.astimezone(timezone('US/Pacific'))
                    day = date.strftime("%B") + " " + date.strftime("%-d")
                    #day = "January 27"
                    if type(d[day]) is tuple:
                        await message.channel.send(day + " is the birthday of " + d[day][0].title() + " and " + d[day][1].title() + "!")
                        pic = False
                        pic1 = False
                        for fname in os.listdir(path='vimages/'):
                            if d[day][0] in fname and not pic:
                                await message.channel.send(file=discord.File('vimages/' + fname))
                                pic = True
                            if d[day][1] in fname and not pic1:
                                await message.channel.send(file=discord.File('vimages/' + fname))
                                pic1 = True
                            if pic == pic1:
                                break
                    else:
                        await message.channel.send(day + " is the birthday of " + d[day].title() + "!")
                        for fname in os.listdir(path='vimages/'):
                            if d[day].title() in fname:
                                await message.channel.send(file=discord.File('vimages/' + fname))
                                break
                
                elif message.content != "birthday" or message.content != "birthday ":
                    message.content = message.content.replace('birthday ', '')
                    for key, value in d.items():
                        if type(value) is tuple:
                            if message.content == value[0]:
                                await message.channel.send(key + " is the birthday of " + value[0].title() + "!")
                                for fname in os.listdir(path='vimages/'):
                                    if value[0].title() in fname:
                                        await message.channel.send(file=discord.File('vimages/' + fname))
                                        break
                                break
                            if message.content == value[1]:
                                await message.channel.send(key + " is the birthday of " + value[1].title() + "!")
                                for fname in os.listdir(path='vimages/'):
                                    if value[1].title() in fname:
                                        await message.channel.send(file=discord.File('vimages/' + fname))
                                        break
                                break

                        elif value == message.content:
                            print(value)
                            await message.channel.send(key + " is the birthday of " + value.title() + "!")
                            for fname in os.listdir(path='vimages/'):
                                if value.title() in fname:
                                    await message.channel.send(file=discord.File('vimages/' + fname))
                                    break
                            break
####################################################################################################################################################################################################
            if message.content.startswith("bug"):  # bug info
                if message.content == "bug":  # if no bug specified 
                    bugs = ""
                    for keys in b.keys():
                        bugs += keys
                        bugs += '\n'
                    await message.channel.send(bugs)
                    await message.channel.send("Please specify what bug you want! Above is a list of the current bug info I have. Example: !bug bee")
                elif message.content != "bug" or message.content != "bug ":
                    message.content = message.content.replace('bug ', '')
                    await message.channel.send("The " + message.content.title() + " is worth " + b[message.content][0] + " bells and can be found " + b[message.content][1])
                    print(message.content)
                    # message.content = message.content.replace(' ', '-')
                    for fname in os.listdir(path='bimages/'):
                        if (message.content + ".jpg") == fname:
                            await message.channel.send(file=discord.File('bimages/' + fname))
                            break
########################################################################################################################################################################################################
            if message.content.startswith("fish"):  # fish info
                if message.content == "fish":  # if no fish specified
                    fishes = ""
                    for keys in f.keys():
                        fishes += keys
                        fishes += '\n'
                    await message.channel.send(fishes)
                    await message.channel.send("Please specify what fish you want! Above is a list of the current fish info I have. Example: !fish catfish")
                elif message.content != "fish" or message.content != "fish ":
                    message.content = message.content.replace('fish ', '')
                    await message.channel.send("The " + message.content.title() + " is worth " + f[message.content][0] + " bells and can be found in the " + f[message.content][1])
                    print(message.content)
                    for fname in os.listdir(path='fimages/'):
                        if (message.content + ".jpg") == fname:
                            await message.channel.send(file=discord.File('fimages/' + fname))
                            break

client = acbot()

client.run(token)