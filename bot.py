#사용하는 라이브러리
import asyncio
from discord.ext import commands
import discord
#import commands
import datetime
import random
import os
import Search_dic as search_mod
import command_mod1 as command_list
import matbread_emoji as matbread
import So_in_su as sis
import meals_parser as parse
import token_private

now=datetime.datetime.now()
intents=discord.Intents.default()
intents.members=True
bot = commands.Bot(command_prefix='==>', description='==>커맨드 to show commands')
token=token_private.distoken

@bot.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(bot.user.name)
    print(bot.user.id)
    print("==========")
    activity = discord.Game(name="==>커맨드를 통해 명령어를 확인")
    await bot.change_presence(status=discord.Status.idle, activity=activity)

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(round(bot.latency,4)*1000)}ms')

@bot.command(description='뭔갈 고를때')
async def 선택(ctx,*choices: str):
    """Chooses between multiple times"""
    await ctx.send(random.choice(choices))

@bot.command(description='인천남고의 급식을 일주일치 가져온다.')
async def 인남급식(ctx):
    if parse.find_Meals()==0:
        img=discord.File("Meals_parsed.jpg",filename="image.jpg")
        embed=discord.Embed(title="인남급식",color=0x000000)
        embed.set_image(url="attachment://image.jpg")
        await ctx.send(embed=embed,file=img)
    else:
        await ctx.send("Find some bugs!")

bot.run(token)
'''
@app.event
async def on_message(message):
    chat_log = open("log.txt", 'a')
    try:
        if message.content.startswith("==>"):
            print(message.content + " on " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
            chat_log.write(
                message.content + " on " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second) + "\n")
            if type(message.channel) == commands.channel.PrivateChannel:
                await app.send_message(message.channel, "다이렉트 메시지는 지원하지 않습니다.")
                return None
            if message.content == "==>커맨드":
                await app.send_message(message.channel, embed=command_list.command_list_print())

            if message.content == "==>데스티니":
                await app.send_message(message.channel, "개똥겜")

            if message.content.startswith("==>시즈"):
                call = message.content[6:] + " 야 시즈하자"
                await app.send_message(message.channel, call)

            if message.content.startswith("==>calculate"):
                sum = eval(message.content[12:])
                await app.send_message(message.channel, sum)

            if message.content == "==>채널 확인":
                print(message.channel)
                await app.send_message(message.channel, message.channel)
                await app.send_message(message.channel, type(message.channel))

            if message.content.startswith("==>사전검색"):
                word = message.content[8:]
                mean = search_mod.search_daum_dic(word)
                embed = commands.Embed(title=word, description=str(mean), color=0x00ff00)
                embed.set_footer(text="powered by daum dictionary")
                await app.send_message(message.channel, embed=embed)

            if message.content.startswith("==>마빵티콘"):
                if (message.content == "==>마빵티콘"):
                    embed = matbread.matbread_help()
                    await app.send_message(message.channel, embed=embed)
                    return None
                word = message.content[8:]
                code = matbread.matbread_select(word)
                embed = commands.Embed()
                embed.set_image(url=str("https://i.imgur.com/" + str(code) + ".png"))
                await app.send_message(message.channel, embed=embed)

            if message.content.startswith("==>소인수분해"):
                num = int(message.content[9:])
                print(num)
                word = sis.so_in_su(num)
                await app.send_message(message.channel, word)

            if message.content == "==>박준성":
                url = 'https://i.imgur.com/'
                code = ['cM4rTlw', 'mBWCb1s', '8Uj7zWf', 'g5PeI4l']
                rand = random.randint(0, 3)
                embed = commands.Embed(title="마빵", color=0x00ff00)
                embed.set_footer(text="마빵 사진 기부는 언제든 @두조가기#2254 dm 주세요")
                embed.set_image(url=str(url + code[rand] + ".jpg"))
                await app.send_message(message.channel, embed=embed)

            if message.content == "==>태보해":
                await app.send_message(message.channel, "@==(^o^)@")
                await app.send_message(message.channel, "@=(^o^)=@")
                await app.send_message(message.channel, "@(^o^)==@")

            if message.content == "==>왜구루냥":
                url = 'https://i.imgur.com/2cRDHJw.jpg'
                embed = commands.Embed(title="왜구루냥?", color=0x00ff00)
                embed.set_image(url=url)
                await app.send_message(message.channel, embed=embed)

        else:
            return None
    except Exception as e:
        await app.send_message(message.channel, "오류가 발생했습니다.")
        await app.send_message(message.channel, "-> error Code: " + str(e))
        chat_log.write("-> Error Code: " + str(e) + "\n")
    chat_log.close()
app.run(token)
'''
