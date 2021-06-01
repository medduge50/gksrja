import discord, datetime, pytz, os

notice = "836190313843916801"
guild = "🔰𝒜𝒟𝑀𝐼𝒩🔰"
state = "𝓗𝓪𝓷𝓰𝓾𝓶 𝓓𝓲𝓼𝓬𝓸𝓻𝓭 𝓢𝓮𝓻𝓿𝓮𝓻서버 관리중"
servername = "𝓗𝓪𝓷𝓰𝓾𝓶 𝓓𝓲𝓼𝓬𝓸𝓻𝓭 𝓢𝓮𝓻𝓿𝓮𝓻"
access_token = os.environ["BOT_TOKEN"]
client = discord.Client()

@client.event
async def on_ready(): 
    await client.change_presence(status=discord.Status.online)
    await client.change_presence(activity=discord.Game(f"{state}"))
    print("-------------------봇 정보-----------------------")
    print(" ")
    print("봇 닉네임 :", client.user.name)
    print("봇 아이디 :", client.user.id)
    print(" ")
    print("------------------------------------------------")
    print("호떡#9460")
    print("------------------------------------------------")

@client.event
async def on_message(message):      
    if message.content.startswith("!?도움말"):
        user = message.author
        target = discord.utils.get(message.guild.roles, name=f"{guild}") 
        if not target in message.author.roles: 
            return
        embed = discord.Embed(title="도움말",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
        embed.add_field(name="!?핑", value="봇에 핑을 알려주는 기능입니다 : )", inline=False) 
        embed.add_field(name="!?청소", value="사용되는 방에 모든 매세지를 삭제합니다.", inline=False)
        embed.add_field(name="!?공지", value="공지를 할수 있는 기능입니다, 자동적으로 '@everyone'되므로 적지 않으셔도 됩니다 : ) ", inline=False)             
        embed.set_footer(text="사용자 태그 : {} • {} 서버 관리봇 • Made by 호떡#9460".format(message.author, servername))
        embed.set_thumbnail(url="https://cdn.discordapp.com/icons/826727961699811349/7bce18ee48c31a3e25bd6482bd2ab10e.webp?size=128")
        await message.channel.send (embed=embed)
        await message.channel.send ("{}".format(message.author.mention))

    if message.content.startswith("!?핑"): 
        user = message.author
        target = discord.utils.get(message.guild.roles, name=f"{guild}") 
        if not target in message.author.roles: 

            return
        embed = discord.Embed(title="봇 핑 상태",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
        embed.add_field(name="핑 상태", value="퐁 !, {0}초".format(client.latency), inline=False) 
        embed.set_footer(text="사용자 태그 : {} • {} 서버 관리봇 • Made by 호떡#9460".format(message.author, servername))
        embed.set_thumbnail(url="https://cdn.discordapp.com/icons/826727961699811349/7bce18ee48c31a3e25bd6482bd2ab10e.webp?size=128")
        await message.channel.send (embed=embed)
        await message.channel.send ("{}".format(message.author.mention)) 

    if message.content.startswith("!?청소"): 
        user = message.author
        target = discord.utils.get(message.guild.roles, name=f"{guild}") 
        if not target in message.author.roles: 

            return
        await message.channel.purge(limit=1)
        await message.channel.purge(limit=int(100000000000000))
        embed = discord.Embed(title="{} 청소가 되었습니다!".format(servername) ,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
        embed.add_field(name="청소", value="모든 매세지(사진,링크 등등)가 전부 청소 되었습니다.", inline=False) 
        embed.set_footer(text="사용자 태그 : {} • {} 서버 관리봇 • Made by 호떡#9460".format(message.author, servername))
        embed.set_thumbnail(url="https://cdn.discordapp.com/icons/826727961699811349/7bce18ee48c31a3e25bd6482bd2ab10e.webp?size=128")
        await message.channel.send (embed=embed)
        await message.channel.send ("{}".format(message.author.mention)) 

    if message.content.startswith("!?공지"): 
        user = message.author
        sodyd = message.content[4:]
        channel = client.get_channel(int(notice))
        target = discord.utils.get(message.guild.roles, name=f"{guild}") 
        if not target in message.author.roles: 
            return
        embed = discord.Embed(title=f"{servername} 공지 사항", description="{}".format(sodyd),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
        embed.set_footer(text="담당관리자 : {} • {} 서버 관리봇 • Made by 호떡#9460".format(message.author, servername))
        embed.set_thumbnail(url="https://cdn.discordapp.com/icons/826727961699811349/7bce18ee48c31a3e25bd6482bd2ab10e.webp?size=128")
        await channel.send ("@everyone", embed=embed)
        await message.channel.send("{}, 성공적으로 내용이 전달되었습니다, 내용 : {}".format(message.author.mention, sodyd))

            
client.run(access_token)
