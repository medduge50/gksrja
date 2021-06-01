from functools import update_wrapper
from ntpath import join
import discord, datetime, pytz, os
from discord.widget import WidgetChannel
from discord.flags import Intents
from discord import channel
from discord.ext import commands

Intents = discord.Intents.default()
Intents.members=True
client = discord.Client(Intents=Intents)

token = os.environ["BOT_TOKEN"]
servername = "루크"
serverclient = "connect 103.156.22.67"
guild = "총관리봇"
state = "!?도움말"
notice = "841128210330157146"
logs = "848501328044097566"
servericon = "https://cdn.discordapp.com/attachments/845894634072965172/846333308345647114/download.png"

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
        channel2 = client.get_channel(int(logs))
        target = discord.utils.get(message.guild.roles, name=f"{guild}") 
        if not target in message.author.roles: 
            embed = discord.Embed(title="도움말",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.add_field(name="!?출근", value="출근을 할수 있는 기능입니다 : ) ", inline=False)
            embed.add_field(name="!?퇴근", value="퇴근을 할수 있는 기능입니다 : ) ", inline=False)           
            embed.set_footer(text="사용자 태그 : {} • Made by 호떡#9460".format(message.author, servername))
            embed.set_thumbnail(url=user.avatar_url)
            await message.channel.send (embed=embed)
            await message.channel.send ("{}".format(message.author.mention))
####################################################################################################################################################################
            embed = discord.Embed(title="자동 기록 내용", description="{}님께서 도움말 명령어를 사용하셨습니다.".format(message.author), timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.set_footer(text="{} 서버 자동 로그 전송 • Made by 호떡#9460".format(servername))
            embed.set_thumbnail(url=servericon)
            await channel2.send (embed=embed)
            return
        embed = discord.Embed(title="도움말",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
        embed.add_field(name="!?핑", value="봇에 핑을 알려주는 기능입니다 : )", inline=False) 
        embed.add_field(name="!?온", value="서버가 온되었다는것을 공지 할수 있는 기능입니다 : ) ", inline=False)
        embed.add_field(name="!?오프", value="서버가 닫혔다는것을 공지 할수 있는 기능입니다 : ) ", inline=False)
        embed.add_field(name="!?리붓", value="서버가 리붓중이라는 것을  공지 할수 있는 기능입니다 : ) ", inline=False)
        embed.add_field(name="!?출근", value="출근을 할수 있는 기능입니다 : ) ", inline=False)
        embed.add_field(name="!?퇴근", value="퇴근을 할수 있는 기능입니다 : ) ", inline=False)
        embed.add_field(name="!?투표", value="투표를 할수 있는 기능입니다, 자동적으로 '@everyone'되므로 적지 않으셔도 됩니다 : ) ", inline=False)
        embed.add_field(name="!?공지", value="공지를 할수 있는 기능입니다, 자동적으로 '@everyone'되므로 적지 않으셔도 됩니다 : ) ", inline=False)                
        embed.set_footer(text="사용자 태그 : {} • Made by 호떡#9460".format(message.author, servername))
        embed.set_thumbnail(url=user.avatar_url)
        await message.channel.send (embed=embed)
        await message.channel.send ("{}".format(message.author.mention))
####################################################################################################################################################################
        embed = discord.Embed(title="자동 기록 내용", description="{}님께서 도움말 명령어를 사용하셨습니다.".format(message.author), timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
        embed.set_footer(text="{} 서버 자동 로그 전송 • Made by 호떡#9460".format(servername))
        embed.set_thumbnail(url=servericon)
        await channel2.send (embed=embed)

    if message.content.startswith("!?핑"): 
        user = message.author
        channel2 = client.get_channel(int(logs))
        target = discord.utils.get(message.guild.roles, name=f"{guild}") 
        if not target in message.author.roles: 
            return
        embed = discord.Embed(title="봇 핑 상태",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
        embed.add_field(name="핑 상태", value="퐁 !, {0}초".format(client.latency), inline=False) 
        embed.set_footer(text="사용자 태그 : {} • Made by 호떡#9460".format(message.author, servername))
        embed.set_thumbnail(url=user.avatar_url)
        await message.channel.send (embed=embed)
        await message.channel.send ("{}".format(message.author.mention)) 
####################################################################################################################################################################
        embed = discord.Embed(title="자동 기록 내용", description="{}님께서 핑 명령어를 사용하셨습니다.".format(message.author), timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
        embed.set_footer(text="{} 서버 자동 로그 전송 • Made by 호떡#9460".format(servername))
        embed.set_thumbnail(url=servericon)
        await channel2.send (embed=embed)

    if message.content.startswith("!?청소"): 
        user = message.author
        channel2 = client.get_channel(int(logs))
        target = discord.utils.get(message.guild.roles, name=f"{guild}") 
        if not target in message.author.roles: 
            return
        await message.channel.purge(limit=1)
        await message.channel.purge(limit=int(100000000000000))
        embed = discord.Embed(title="{} 청소가 되었습니다!".format(servername) ,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
        embed.add_field(name="청소", value="모든 매세지(사진,링크 등등)가 전부 청소 되었습니다.", inline=False) 
        embed.set_footer(text="사용자 태그 : {} • Made by 호떡#9460".format(message.author, servername))
        embed.set_thumbnail(url=servericon)
        await message.channel.send (embed=embed)
        await message.channel.send ("{}".format(message.author.mention)) 
####################################################################################################################################################################
        embed = discord.Embed(title="자동 기록 내용", description="{}님께서 청소 명령어를 사용하셨습니다.".format(message.author), timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
        embed.set_footer(text="{} 서버 자동 로그 전송 • Made by 호떡#9460".format(servername))
        embed.set_thumbnail(url=servericon)
        await channel2.send (embed=embed)

    if message.content.startswith("!?온"): 
        user = message.author
        channel2 = client.get_channel(int(logs))
        target = discord.utils.get(message.guild.roles, name=f"{guild}") 
        if not target in message.author.roles: 
            return
        embed = discord.Embed(title=""+servername + " 서버가 온 되었습니다!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
        embed.add_field(name="서버 온!", value="서버에 접속하셔도 좋습니다 !", inline=False) 
        embed.add_field(name="서버 주소", value="FIVEM 실행 - > F8키 클릭 - > "+serverclient + " 복사 붙혀넣기 하기 !", inline=False) 
        embed.set_footer(text="사용자 태그 : {} • Made by 호떡#9460".format(message.author, servername))
        embed.set_thumbnail(url=servericon)
        await message.channel.send ("@everyone")
        await message.channel.send (embed=embed)
####################################################################################################################################################################
        embed = discord.Embed(title="자동 기록 내용", description="{}님께서 서버온 명령어를 사용하셨습니다.".format(message.author), timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
        embed.set_footer(text="{} 서버 자동 로그 전송 • Made by 호떡#9460".format(servername))
        embed.set_thumbnail(url=servericon)
        await channel2.send (embed=embed)

    if message.content.startswith("!?오프"): 
        user = message.author
        channel2 = client.get_channel(int(logs))
        target = discord.utils.get(message.guild.roles, name=f"{guild}") 
        if not target in message.author.roles: 
            return
        embed = discord.Embed(title=""+servername + " 서버가 종료 되었습니다!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
        embed.add_field(name="서버 종료!", value="서버가 닫혀있습니다 ! 접속을 시도 하지 말아주세요 !", inline=False) 
        embed.set_footer(text="사용자 태그 : {} • Made by 호떡#9460".format(message.author, servername))
        embed.set_thumbnail(url=servericon)
        await message.channel.send ("@everyone")
        await message.channel.send (embed=embed)
####################################################################################################################################################################
        embed = discord.Embed(title="자동 기록 내용", description="{}님께서 서버오프 명령어를 사용하셨습니다.".format(message.author), timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
        embed.set_footer(text="{} 서버 자동 로그 전송 • Made by 호떡#9460".format(servername))
        embed.set_thumbnail(url=servericon)
        await channel2.send (embed=embed)

    if message.content.startswith("!?리붓"): 
        user = message.author
        channel2 = client.get_channel(int(logs))
        target = discord.utils.get(message.guild.roles, name=f"{guild}") 
        if not target in message.author.roles: 
            return
        embed = discord.Embed(title=""+servername + " 서버가 리붓 하고 있습니다 !",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
        embed.add_field(name="서버 리붓!", value="서버가 리붓 중에 있습니다 ! 접속을 시도 하지 말아주세요 !", inline=False) 
        embed.add_field(name="서버 주소", value="FIVEM 실행 - > F8키 클릭 - > "+serverclient + " 복사 붙혀넣기 하기 !", inline=False) 
        embed.set_footer(text="사용자 태그 : {} • Made by 호떡#9460".format(message.author, servername))
        embed.set_thumbnail(url=servericon)
        await message.channel.send ("@everyone")
        await message.channel.send (embed=embed)
####################################################################################################################################################################
        embed = discord.Embed(title="자동 기록 내용", description="{}님께서 서버리붓 명령어를 사용하셨습니다.".format(message.author), timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
        embed.set_footer(text="{} 서버 자동 로그 전송 • Made by 호떡#9460".format(servername))
        embed.set_thumbnail(url=servericon)
        await channel2.send (embed=embed)

    if message.content.startswith("!?공지"): 
        user = message.author
        channel2 = client.get_channel(int(logs))
        sodyd = message.content[4:]
        channel = client.get_channel(int(notice))
        target = discord.utils.get(message.guild.roles, name=f"{guild}") 
        if not target in message.author.roles: 
            return
        embed = discord.Embed(title=f"{servername} 공지 사항", description="{}".format(sodyd),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
        embed.set_footer(text="담당관리자 : {} • Made by 호떡#9460".format(message.author, servername))
        embed.set_thumbnail(url=servericon)
        await channel.send ("@everyone", embed=embed)
        await message.channel.send("{}, 성공적으로 공지 내용이 전달되었습니다, 내용 : {}".format(message.author.mention, sodyd))
####################################################################################################################################################################
        embed = discord.Embed(title="자동 기록 내용", description="{}님께서 공지 명령어를 사용하셨습니다. \n 내용 : {}".format(message.author, sodyd), timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
        embed.set_footer(text="{} 서버 자동 로그 전송 • Made by 호떡#9460".format(servername))
        embed.set_thumbnail(url=servericon)
        await channel2.send (embed=embed)

    if message.content == "!?출근":      
            user = message.author  
            channel2 = client.get_channel(int(logs))
            embed = discord.Embed(title="출근을 하셨습니다 ! ",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.add_field(name="출근", value=""+str(message.author) + "님께서 출근 하셨습니다.", inline=False) 
            embed.set_footer(text="사용자 태그 : {} • Made by 호떡#9460".format(message.author, servername))
            embed.set_thumbnail(url=user.avatar_url)
            await message.channel.send ("{}".format(message.author.mention))
            await message.channel.send (embed=embed)
####################################################################################################################################################################
            embed = discord.Embed(title="자동 기록 내용", description="{}님께서 서버출근 명령어를 사용하셨습니다.".format(message.author), timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.set_footer(text="{} 서버 자동 로그 전송 • Made by 호떡#9460".format(servername))
            embed.set_thumbnail(url=servericon)
            await channel2.send (embed=embed)

    if message.content == "!?퇴근":        
            user = message.author
            channel2 = client.get_channel(int(logs))
            embed = discord.Embed(title="퇴근을 하셨습니다 ! ",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.add_field(name="퇴근", value=""+str(message.author) + "님께서 퇴근 하셨습니다.", inline=False) 
            embed.set_footer(text="사용자 태그 : {} • Made by 호떡#9460".format(message.author, servername))
            embed.set_thumbnail(url=user.avatar_url)
            await message.channel.send ("{}".format(message.author.mention))
            await message.channel.send (embed=embed)
####################################################################################################################################################################
            embed = discord.Embed(title="자동 기록 내용", description="{}님께서 서버퇴근 명령어를 사용하셨습니다.".format(message.author), timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.set_footer(text="{} 서버 자동 로그 전송 • Made by 호떡#9460".format(servername))
            embed.set_thumbnail(url=servericon)
            await channel2.send (embed=embed)

    if message.content.startswith("!?투표"): 
        user = message.author
        channel2 = client.get_channel(int(logs))
        sodyd2 = message.content[4:]
        channel = client.get_channel(int(notice))
        target = discord.utils.get(message.guild.roles, name=f"{guild}") 
        if not target in message.author.roles: 
            return
        embed = discord.Embed(title=f"{servername} 서버 투표", description="투표 내용 : {} \n [찬성 👍],[반대 👎]".format(sodyd2),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
        embed.set_footer(text="담당관리자 : {} • Made by 호떡#9460".format(message.author, servername))
        embed.set_thumbnail(url=servericon)
        msg = await message.channel.send (embed=embed)
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')
        await channel.send ("@everyone")
        await message.channel.send("{}, 성공적으로 투표 내용이 전달되었습니다, 내용 : {}".format(message.author.mention, sodyd2))
####################################################################################################################################################################
        embed = discord.Embed(title="자동 기록 내용", description="{}님께서 투표 명령어를 사용하셨습니다. \n 투표내용 : {}".format(message.author, sodyd2), timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
        embed.set_footer(text="{} 서버 자동 로그 전송 • Made by 호떡#9460".format(servername))
        embed.set_thumbnail(url=servericon)
        await channel2.send (embed=embed) 

client.run(token)
