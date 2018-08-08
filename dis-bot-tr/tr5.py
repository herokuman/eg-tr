import discord
from bs4 import BeautifulSoup
import urllib.request
import codecs
import sys, io

client = discord.Client()


lalist = ["en","fr","es","de","ja","ko"]
flaglist = [":flag_gb:",":flag_fr:",":flag_es:",":flag_de:",":flag_jp:",":flag_kr:"]
alltrid = "476554313167142933"


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
   if client.user != message.author:

     if str(message.channel.id) == alltrid:
       mes = str(message.content)

       chars = list(mes)

       if len(chars) < 100:
         no = 0
         for lacode in lalist:
            url1 = "https://script.google.com/macros/s/AKfycbweJFfBqKUs5gGNnkV2xwTZtZPptI6ebEhcCU2_JvOmHwM2TCk/exec?text="
            url2 = "&source="
            url3 = "&target="
            urlga = url1 + urllib.parse.quote_plus(mes, encoding='utf-8') + url2 + "" + url3 + lacode
            html = urllib.request.urlopen(urlga)
            soup = BeautifulSoup(html, "html.parser")
            for s in soup(['script', 'style']):
              s.decompose()
            text = ' '.join(soup.stripped_strings)
            m = str(text)
            if no == 0:
              mm = flaglist[no] + "  " + "`" + m + "`" + "\n"
            else:
              mm = mm + flaglist[no] + "  " + "`" + m + "`" + "\n"
            no = no + 1

       else:
         mm = "`Error: The message is too long. Please write in 100 words or less.`"

       await client.send_message(message.channel, mm)


client.run("NDc2NTU1NzQ0NzkyMTUwMDE2.DkvTuA.eY8G1ECDQALu2pc_ec-hhER_bgM")