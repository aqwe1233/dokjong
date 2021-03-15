import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("감시")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("!REDD"):
        await message.channel.send("안녕하세요")


    if message.content.startswith("!클랜원기록"):
        f = open("클랜원.txt", "w")
        f.write("RED CHANEL 곡예 코카콜라 감자포차 스타위한스타 zombie")
        f.close()

    if message.content.startswith("!클랜"):
        f = open("클랜원.txt")
        await message.channel.send(f.read())
        f.close()

    if message.content.startswith("!RED기록"):
        f = open("RED전적.txt", "w")
        f.write("닉네임:RED"+"레이팅:100"+"전적:0승0패"+"승률:100%")
        f.close()

    if message.content.startswith("!RED"):
        f = open("RED전적.txt")
        await message.channel.send(f.read())
        f.close()

    if message.content.startswith("!CHANEL기록"):
        f = open("CHANEL전적.txt", "w")
        f.write("닉네임:CHANEL" + "레이팅:100" + "전적:0승0패" + "승률:100%")
        f.close()

    if message.content.startswith("!CHANEL"):
        f = open("CHANEL전적.txt")
        await message.channel.send(f.read())
        f.close()

    if message.content.startswith("!곡예기록"):
        f = open("곡예전적.txt", "w")
        f.write("닉네임:곡예" + "레이팅:100" + "전적:0승0패" + "승률:100%")
        f.close()

    if message.content.startswith("!곡예"):
        f = open("곡예전적.txt")
        await message.channel.send(f.read())
        f.close()

    if message.content.startswith("!코카콜라기록"):
        f = open("코카콜라전적.txt", "w")
        f.write("닉네임:코카콜라" + "레이팅:100" + "전적:0승0패" + "승률:100%")
        f.close()

    if message.content.startswith("!코카콜라"):
        f = open("코카콜라전적.txt")
        await message.channel.send(f.read())
        f.close()

    if message.content.startswith("!감자포차기록"):
        f = open("감자포차전적.txt", "w")
        f.write("닉네임:감자포차" + "레이팅:100" + "전적:0승0패" + "승률:100%")
        f.close()

    if message.content.startswith("!감자포차"):
        f = open("감자포차전적.txt")
        await message.channel.send(f.read())
        f.close()

    if message.content.startswith("!스타위한스타기록"):
        f = open("스타위한스타전적.txt", "w")
        f.write("닉네임:스타위한스타" + "레이팅:100" + "전적:0승0패" + "승률:100%")
        f.close()

    if message.content.startswith("!스타위한스타"):
        f = open("스타위한스타전적.txt")
        await message.channel.send(f.read())
        f.close()

    if message.content.startswith("!zombie기록"):
        f = open("zombie전적.txt", "w")
        f.write("닉네임:zombie" + "레이팅:100" + "전적:0승0패" + "승률:100%")
        f.close()

    if message.content.startswith("!zombie"):
        f = open("zombie전적.txt")
        await message.channel.send(f.read())
        f.close()

    if message.content.startswith("!주간퀘스트기록"):
        f = open("주간퀘스트.txt", "w")
        f.write("쿨타임 도는중")
        f.close()

    if message.content.startswith("!주간퀘스트"):
        f = open("주간퀘스트.txt")
        await message.channel.send(f.read())
        f.close()

    if message.content.startswith("!주퀘"):
        f = open("주간퀘스트.txt")
        await message.channel.send(f.read())
        f.close()

    if message.content.startswith("!도움말기록"):
        f = open("도움말.txt", "w")
        f.write("RED CHANEL 곡예 코카콜라 감자포차 스타위한스타 zombie")
        f.close()

    if message.content.startswith("!도움말"):
        f = open("도움말.txt")
        await message.channel.send(f.read())
        f.close()

    if message.content.startswith("!이벤트기록"):
        f = open("이벤트.txt", "w")
        f.write("준비중")
        f.close()

    if message.content.startswith("!이벤트"):
        f = open("이벤트.txt")
        await message.channel.send(f.read())
        f.close()

    if message.content.startswith("!랭킹기록"):
        f = open("랭킹.txt", "w")
        f.write("준비중")
        f.close()

    if message.content.startswith("!랭킹"):
        f = open("랭킹.txt")
        await message.channel.send(f.read())
        f.close()

    
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
