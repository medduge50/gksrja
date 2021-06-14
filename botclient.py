from functools import update_wrapper
from ntpath import join
import discord, datetime, pytz, os, time
from discord.widget import WidgetChannel
from discord.flags import Intents
from discord import channel
from discord.ext import commands

def times():
    return time.time()


intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)
dirfolder = os.getcwd()
token = os.environ["BOT_TOKEN"]
servername = "루크"
serverclient = "connect 103.156.22.67"
guild = "총관리봇"
state = "모든 문의 디엠"
notice = "841128210330157146"
logs = "848501328044097566"
dkssudgktpdy = "841120652424642585"
dkssudgktpdy2 = "841120652424642586"
delete = "848501328044097566"
edit = "848501328044097566"
servericon = "https://cdn.discordapp.com/attachments/845894634072965172/846333308345647114/download.png"

@client.event
async def on_connect(): 
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
async def on_message_delete(message):
    y = datetime.datetime.now().year
    m = datetime.datetime.now().month
    d = datetime.datetime.now().day
    h = datetime.datetime.now().hour
    min = datetime.datetime.now().minute
    bot_logs = delete
    embed = discord.Embed(title='자동 기록 내용', description="{}님께서 매세지를 삭제 하셨습니다.".format(message.author), color=0x00ff00)
    embed.add_field(name='유저 태그', value=f'{message.author}', inline=False)
    embed.add_field(name='유저 아이디', value=f'{message.author.id}', inline=False)
    embed.add_field(name='채널 아이디', value=f'{message.channel.id}', inline=False)
    embed.add_field(name='내용', value=message.content, inline=False)
    embed.add_field(name='매세지 아이디', value=f'{message.id}')
    embed.add_field(name='날짜', value=f"{y}년 {m}월 {d}일 {h}시 {min}분", inline=False)
    embed.set_footer(text="자동 로그 전송 • Ruke SERVER".format(servername))
    await client.get_channel(int(bot_logs)).send(embed=embed)

@client.event
async def on_message_edit(before, after):
    if before.author.bot:
        return
    else:
        y = datetime.datetime.now().year
        m = datetime.datetime.now().month
        d = datetime.datetime.now().day
        h = datetime.datetime.now().hour
        min = datetime.datetime.now().minute
        bot_logs = edit
        embed = discord.Embed(title='자동 기록 내용', description="{}님께서 매세지를 수정 하셨습니다.".format(before.author), color=0x00ff00)
        embed.add_field(name='유저 태그', value=f'{before.author}', inline=False)
        embed.add_field(name='유저 아이디', value=f'{before.author.id}', inline=False)
        embed.add_field(name='수정 전', value=before.content + "\u200b", inline=True)
        embed.add_field(name='수정 후', value=after.content + "\u200b", inline=True)
        embed.add_field(name='날짜', value=f"{y}년 {m}월 {d}일 {h}시 {min}분", inline=False)
        embed.set_footer(text="자동 로그 전송 • Ruke SERVER".format(servername))
        await client.get_channel(int(bot_logs)).send(embed=embed)

@client.event
async def on_member_join(member):
    member2 = client.get_channel(int(dkssudgktpdy))
    embed = discord.Embed(title='! 안녕하세요 !', description=f'안녕하세요 **{member.mention}**님, **{member.guild}**에 오신것을 환영합니다. 서버 규칙 한번씩 읽어주시면 감사하겠습니다.',timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
    embed.set_footer(text="Ruke SERVER")
    embed.set_thumbnail(url=servericon)
    await member2.send(embed=embed)
    embed = discord.Embed(title='! 안녕하세요 !', description=f'안녕하세요, **{member.guild}**입니다. 서버 규칙 한번씩 읽어주시면 감사하겠습니다.',timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
    embed.set_footer(text="Ruke SERVER")
    await member.send(embed=embed)

@client.event
async def on_member_remove(member):
    member2 = client.get_channel(int(dkssudgktpdy2))
    embed = discord.Embed(title='! 안녕히가세요 !', description=f'안녕히가세요 **{member.mention}**님 ㅠㅠㅠㅠㅠㅠㅠㅠㅠ',timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
    embed.set_footer(text="Ruke SERVER")
    embed.set_thumbnail(url=servericon)
    await member2.send(embed=embed)

@client.event
async def on_message(message):      
    if message.content.startswith("!?도움말"):
        try:
            user = message.author
            channel2 = client.get_channel(int(logs))
            target = discord.utils.get(message.guild.roles, name=f"{guild}") 
            if not target in message.author.roles: 
                embed = discord.Embed(title="도움말",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.add_field(name="!?출근", value="출근을 할수 있는 기능입니다 : ) ", inline=False)
                embed.add_field(name="!?퇴근", value="퇴근을 할수 있는 기능입니다 : ) ", inline=False)           
                embed.set_footer(text="사용자 태그 : {} • Made by 호떡#9460".format(message.author, servername))
                embed.set_thumbnail(url=user.avatar_url)
                await message.channel.send (embed=embed)
                await message.channel.send ("{}".format(message.author.mention))
    ####################################################################################################################################################################
                embed = discord.Embed(title="자동 기록 내용", description="{}님께서 도움말 명령어를 사용하셨습니다.".format(message.author), timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="{} 서버 자동 로그 전송 • Made by 호떡#9460".format(servername))
                embed.set_thumbnail(url=servericon)
                await channel2.send (embed=embed)
                return
            embed = discord.Embed(title="도움말",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
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
            embed = discord.Embed(title="자동 기록 내용", description="{}님께서 도움말 명령어를 사용하셨습니다.".format(message.author), timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="{} 서버 자동 로그 전송 • Made by 호떡#9460".format(servername))
            embed.set_thumbnail(url=servericon)
            await channel2.send (embed=embed)
        except Exception as e:
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n 개발자에게 로그를 전송 합니다. \n 오류 해결이 될동안 사용하지 말아주세요. \n\n 오류코드 : {e}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.set_footer(text="루크 서버 • Made by 호떡#9460", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.channel.send (embed=embed)
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n\n 오류코드 : {e} \n\n 사용된 매세지 : '문의 오류' \n\n 사용자 : {message.author}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.set_footer(text="루크 서버 • Made by 호떡#9460", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await channel2.send (embed=embed)

    if message.content.startswith("!?핑"): 
        try:
            user = message.author
            channel2 = client.get_channel(int(logs))
            target = discord.utils.get(message.guild.roles, name=f"{guild}") 
            if not target in message.author.roles: 
                return
            embed = discord.Embed(title="봇 핑 상태",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.add_field(name="핑 상태", value="퐁 !, {0}초".format(client.latency), inline=False) 
            embed.set_footer(text="사용자 태그 : {} • Made by 호떡#9460".format(message.author, servername))
            embed.set_thumbnail(url=user.avatar_url)
            await message.channel.send (embed=embed)
            await message.channel.send ("{}".format(message.author.mention)) 
    ####################################################################################################################################################################
            embed = discord.Embed(title="자동 기록 내용", description="{}님께서 핑 명령어를 사용하셨습니다.".format(message.author), timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="{} 서버 자동 로그 전송 • Made by 호떡#9460".format(servername))
            embed.set_thumbnail(url=servericon)
            await channel2.send (embed=embed)
        except Exception as e:
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n 개발자에게 로그를 전송 합니다. \n 오류 해결이 될동안 사용하지 말아주세요. \n\n 오류코드 : {e}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.set_footer(text="루크 서버 • Made by 호떡#9460", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.channel.send (embed=embed)
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n\n 오류코드 : {e} \n\n 사용된 매세지 : '문의 오류' \n\n 사용자 : {message.author}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.set_footer(text="루크 서버 • Made by 호떡#9460", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await channel2.send (embed=embed)


    if message.content.startswith("!?청소"): 
        try:  
            user = message.author
            channel2 = client.get_channel(int(logs))
            target = discord.utils.get(message.guild.roles, name=f"{guild}") 
            if not target in message.author.roles: 
                return
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(100000000000000))
            embed = discord.Embed(title="{} 청소가 되었습니다!".format(servername) ,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.add_field(name="청소", value="모든 매세지(사진,링크 등등)가 전부 청소 되었습니다.", inline=False) 
            embed.set_footer(text="사용자 태그 : {} • Made by 호떡#9460".format(message.author, servername))
            embed.set_thumbnail(url=servericon)
            await message.channel.send (embed=embed)
            await message.channel.send ("{}".format(message.author.mention)) 
    ####################################################################################################################################################################
            embed = discord.Embed(title="자동 기록 내용", description="{}님께서 청소 명령어를 사용하셨습니다.".format(message.author), timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="{} 서버 자동 로그 전송 • Made by 호떡#9460".format(servername))
            embed.set_thumbnail(url=servericon)
            await channel2.send (embed=embed)
        except Exception as e:
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n 개발자에게 로그를 전송 합니다. \n 오류 해결이 될동안 사용하지 말아주세요. \n\n 오류코드 : {e}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.set_footer(text="루크 서버 • Made by 호떡#9460", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.channel.send (embed=embed)
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n\n 오류코드 : {e} \n\n 사용된 매세지 : '문의 오류' \n\n 사용자 : {message.author}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.set_footer(text="루크 서버 • Made by 호떡#9460", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await channel2.send (embed=embed)

    if message.content.startswith("!?온"): 
        try:  
            user = message.author
            channel2 = client.get_channel(int(logs))
            target = discord.utils.get(message.guild.roles, name=f"{guild}") 
            if not target in message.author.roles: 
                return
            embed = discord.Embed(title=""+servername + " 서버가 온 되었습니다!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.add_field(name="서버 온!", value="서버에 접속하셔도 좋습니다 !", inline=False) 
            embed.add_field(name="서버 주소", value="FIVEM 실행 - > F8키 클릭 - > "+serverclient + " 복사 붙혀넣기 하기 !", inline=False) 
            embed.set_footer(text="사용자 태그 : {} • Made by 호떡#9460".format(message.author, servername))
            embed.set_thumbnail(url=servericon)
            await message.channel.send ("@everyone")
            await message.channel.send (embed=embed)
    ####################################################################################################################################################################
            embed = discord.Embed(title="자동 기록 내용", description="{}님께서 서버온 명령어를 사용하셨습니다.".format(message.author), timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="{} 서버 자동 로그 전송 • Made by 호떡#9460".format(servername))
            embed.set_thumbnail(url=servericon)
            await channel2.send (embed=embed)
        except Exception as e:
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n 개발자에게 로그를 전송 합니다. \n 오류 해결이 될동안 사용하지 말아주세요. \n\n 오류코드 : {e}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.set_footer(text="루크 서버 • Made by 호떡#9460", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.channel.send (embed=embed)
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n\n 오류코드 : {e} \n\n 사용된 매세지 : '문의 오류' \n\n 사용자 : {message.author}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.set_footer(text="루크 서버 • Made by 호떡#9460", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await channel2.send (embed=embed)

    if message.content.startswith("!?오프"): 
        try:  
            user = message.author
            channel2 = client.get_channel(int(logs))
            target = discord.utils.get(message.guild.roles, name=f"{guild}") 
            if not target in message.author.roles: 
                return
            embed = discord.Embed(title=""+servername + " 서버가 종료 되었습니다!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.add_field(name="서버 종료!", value="서버가 닫혀있습니다 ! 접속을 시도 하지 말아주세요 !", inline=False) 
            embed.set_footer(text="사용자 태그 : {} • Made by 호떡#9460".format(message.author, servername))
            embed.set_thumbnail(url=servericon)
            await message.channel.send ("@everyone")
            await message.channel.send (embed=embed)
    ####################################################################################################################################################################
            embed = discord.Embed(title="자동 기록 내용", description="{}님께서 서버오프 명령어를 사용하셨습니다.".format(message.author), timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="{} 서버 자동 로그 전송 • Made by 호떡#9460".format(servername))
            embed.set_thumbnail(url=servericon)
            await channel2.send (embed=embed)
        except Exception as e:
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n 개발자에게 로그를 전송 합니다. \n 오류 해결이 될동안 사용하지 말아주세요. \n\n 오류코드 : {e}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.set_footer(text="루크 서버 • Made by 호떡#9460", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.channel.send (embed=embed)
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n\n 오류코드 : {e} \n\n 사용된 매세지 : '문의 오류' \n\n 사용자 : {message.author}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.set_footer(text="루크 서버 • Made by 호떡#9460", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await channel2.send (embed=embed)

    if message.content.startswith("!?리붓"): 
        try:  
            user = message.author
            channel2 = client.get_channel(int(logs))
            target = discord.utils.get(message.guild.roles, name=f"{guild}") 
            if not target in message.author.roles: 
                return
            embed = discord.Embed(title=""+servername + " 서버가 리붓 하고 있습니다 !",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.add_field(name="서버 리붓!", value="서버가 리붓 중에 있습니다 ! 접속을 시도 하지 말아주세요 !", inline=False) 
            embed.add_field(name="서버 주소", value="FIVEM 실행 - > F8키 클릭 - > "+serverclient + " 복사 붙혀넣기 하기 !", inline=False) 
            embed.set_footer(text="사용자 태그 : {} • Made by 호떡#9460".format(message.author, servername))
            embed.set_thumbnail(url=servericon)
            await message.channel.send ("@everyone")
            await message.channel.send (embed=embed)
    ####################################################################################################################################################################
            embed = discord.Embed(title="자동 기록 내용", description="{}님께서 서버리붓 명령어를 사용하셨습니다.".format(message.author), timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="{} 서버 자동 로그 전송 • Made by 호떡#9460".format(servername))
            embed.set_thumbnail(url=servericon)
            await channel2.send (embed=embed)
        except Exception as e:
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n 개발자에게 로그를 전송 합니다. \n 오류 해결이 될동안 사용하지 말아주세요. \n\n 오류코드 : {e}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.set_footer(text="루크 서버 • Made by 호떡#9460", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.channel.send (embed=embed)
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n\n 오류코드 : {e} \n\n 사용된 매세지 : '문의 오류' \n\n 사용자 : {message.author}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.set_footer(text="루크 서버 • Made by 호떡#9460", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await channel2.send (embed=embed)

    if message.content.startswith("!?공지"): 
        try:  
            user = message.author
            channel2 = client.get_channel(int(logs))
            sodyd = message.content[4:]
            channel = client.get_channel(int(notice))
            target = discord.utils.get(message.guild.roles, name=f"{guild}") 
            if not target in message.author.roles: 
                return
            embed = discord.Embed(title=f"{servername} 공지 사항", description="{}".format(sodyd),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="담당관리자 : {} • Made by 호떡#9460".format(message.author, servername))
            embed.set_thumbnail(url=servericon)
            await channel.send (embed=embed)
            await channel.send ("@everyone")
            await message.channel.send("{}, 성공적으로 공지 내용이 전달되었습니다, 내용 : {}".format(message.author.mention, sodyd))
    ####################################################################################################################################################################
            embed = discord.Embed(title="자동 기록 내용", description="{}님께서 공지 명령어를 사용하셨습니다. \n 내용 : {}".format(message.author, sodyd), timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="{} 서버 자동 로그 전송 • Made by 호떡#9460".format(servername))
            embed.set_thumbnail(url=servericon)
            await channel2.send (embed=embed)
        except Exception as e:
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n 개발자에게 로그를 전송 합니다. \n 오류 해결이 될동안 사용하지 말아주세요. \n\n 오류코드 : {e}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.set_footer(text="루크 서버 • Made by 호떡#9460", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.channel.send (embed=embed)
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n\n 오류코드 : {e} \n\n 사용된 매세지 : '문의 오류' \n\n 사용자 : {message.author}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.set_footer(text="루크 서버 • Made by 호떡#9460", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await channel2.send (embed=embed)

    if message.content == "!?출근":    
        try:  
            user = message.author  
            channel2 = client.get_channel(int(logs))
            embed = discord.Embed(title="출근을 하셨습니다 ! ",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.add_field(name="출근", value=""+str(message.author) + "님께서 출근 하셨습니다.", inline=False) 
            embed.set_footer(text="사용자 태그 : {} • Made by 호떡#9460".format(message.author, servername))
            embed.set_thumbnail(url=user.avatar_url)
            await message.channel.send ("{}".format(message.author.mention))
            await message.channel.send (embed=embed)
####################################################################################################################################################################
            embed = discord.Embed(title="자동 기록 내용", description="{}님께서 서버출근 명령어를 사용하셨습니다.".format(message.author), timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="{} 서버 자동 로그 전송 • Made by 호떡#9460".format(servername))
            embed.set_thumbnail(url=servericon)
            await channel2.send (embed=embed)
        except Exception as e:
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n 개발자에게 로그를 전송 합니다. \n 오류 해결이 될동안 사용하지 말아주세요. \n\n 오류코드 : {e}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.set_footer(text="루크 서버 • Made by 호떡#9460", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.channel.send (embed=embed)
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n\n 오류코드 : {e} \n\n 사용된 매세지 : '문의 오류' \n\n 사용자 : {message.author}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.set_footer(text="루크 서버 • Made by 호떡#9460", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await channel2.send (embed=embed)

    if message.content == "!?퇴근":     
        try:
            user = message.author
            channel2 = client.get_channel(int(logs))
            embed = discord.Embed(title="퇴근을 하셨습니다 ! ",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.add_field(name="퇴근", value=""+str(message.author) + "님께서 퇴근 하셨습니다.", inline=False) 
            embed.set_footer(text="사용자 태그 : {} • Made by 호떡#9460".format(message.author, servername))
            embed.set_thumbnail(url=user.avatar_url)
            await message.channel.send ("{}".format(message.author.mention))
            await message.channel.send (embed=embed)
####################################################################################################################################################################
            embed = discord.Embed(title="자동 기록 내용", description="{}님께서 서버퇴근 명령어를 사용하셨습니다.".format(message.author), timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="{} 서버 자동 로그 전송 • Made by 호떡#9460".format(servername))
            embed.set_thumbnail(url=servericon)
            await channel2.send (embed=embed)
        except Exception as e:
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n 개발자에게 로그를 전송 합니다. \n 오류 해결이 될동안 사용하지 말아주세요. \n\n 오류코드 : {e}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.set_footer(text="루크 서버 • Made by 호떡#9460", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.channel.send (embed=embed)
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n\n 오류코드 : {e} \n\n 사용된 매세지 : '문의 오류' \n\n 사용자 : {message.author}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.set_footer(text="루크 서버 • Made by 호떡#9460", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await channel2.send (embed=embed)

    if message.content.startswith("!?투표"): 
        try:
            user = message.author
            channel2 = client.get_channel(int(logs))
            sodyd2 = message.content[4:]
            channel = client.get_channel(int(notice))
            target = discord.utils.get(message.guild.roles, name=f"{guild}") 
            if not target in message.author.roles: 
                return
            embed = discord.Embed(title=f"{servername} 서버 투표", description="투표 내용 : {} \n [찬성 👍],[반대 👎]".format(sodyd2),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="담당관리자 : {} • Made by 호떡#9460".format(message.author, servername))
            embed.set_thumbnail(url=servericon)
            msg = await channel.send (embed=embed)
            await msg.add_reaction('👍')
            await msg.add_reaction('👎')
            await channel.send ("@everyone")
            await message.channel.send("{}, 성공적으로 투표 내용이 전달되었습니다, 내용 : {}".format(message.author.mention, sodyd2))
    ####################################################################################################################################################################
            embed = discord.Embed(title="자동 기록 내용", description="{}님께서 투표 명령어를 사용하셨습니다. \n 투표내용 : {}".format(message.author, sodyd2), timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="{} 서버 자동 로그 전송 • Made by 호떡#9460".format(servername))
            embed.set_thumbnail(url=servericon)
            await channel2.send (embed=embed) 
        except Exception as e:
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n 개발자에게 로그를 전송 합니다. \n 오류 해결이 될동안 사용하지 말아주세요. \n\n 오류코드 : {e}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.set_footer(text="루크 서버 • Made by 호떡#9460", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.channel.send (embed=embed)
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n\n 오류코드 : {e} \n\n 사용된 매세지 : '문의 오류' \n\n 사용자 : {message.author}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.set_footer(text="루크 서버 • Made by 호떡#9460", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await channel2.send (embed=embed)

    if message.guild is None:
        try:
            channel2 = client.get_channel(int(logs))
            date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000) 
            if message.author.bot:
                return
            else:
                embed = discord.Embed(title='문의가 왔습니다!', timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.add_field(name='전송자', value=message.author, inline=False)
                embed.add_field(name='전송자 id', value=message.author.id, inline=False)
                embed.add_field(name='내용', value=message.content, inline=False)
                embed.set_footer(text="루크 서버 • Made by 호떡#9460", icon_url=""+servericon + "")
                embed3 = discord.Embed(timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed3.add_field(name="안내", value=f"문의사항이 전달되었습니다 전달 내용 : {message.content}", inline=False)
                embed3.set_footer(text="루크 서버 • Made by 호떡#9460", icon_url=""+servericon + "")
                await client.get_channel(853937922256535552).send(f"!?답변 <@{message.author.id}> [할말] 을 통해 답장을 보내주세요!")
                await client.get_channel(853937922256535552).send(f"!?문의종료 <@{message.author.id}>를 통해 문의를 종료 할수 있습니다!", embed=embed)
                await client.get_channel(853937922256535552).send("-------------------------------------------------------------------------------------------")
                msg1 = await message.author.send (embed=embed3)
                await msg1.add_reaction('✅')
    ####################################################################################################################################################################
                embed2 = discord.Embed(title="자동 기록 내용", description=f"문의봇, 내용: {message.content}".format(message.author), timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed2.add_field(name="사용자 태그", value=f"{message.author}", inline=False) 
                embed2.add_field(name="사용자 아이디", value=f"{message.author.id}", inline=False) 
                embed2.set_footer(text="자동 로그 전송 • 루크 서버 • Made by 호떡#9460M".format(servername))
                embed2.set_thumbnail(url=servericon)
                await channel2.send (embed=embed2)
                return
        except Exception as e:
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n 개발자에게 로그를 전송 합니다. \n 오류 해결이 될동안 사용하지 말아주세요. \n\n 오류코드 : {e}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.set_footer(text="루크 서버 • Made by 호떡#9460", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.channel.send (embed=embed)
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n\n 오류코드 : {e} \n\n 사용된 매세지 : '문의 오류' \n\n 사용자 : {message.author}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.set_footer(text="루크 서버 • Made by 호떡#9460", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await channel2.send (embed=embed)

    if message.content.startswith("!?답변"): 
        try:
            user = message.author
            date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000) 
            channel2 = client.get_channel(int(logs))
            target = discord.utils.get(message.guild.roles, name=f"{guild}") 
            if not target in message.author.roles: 
                return
            hi = message.content[27:]
            embed = discord.Embed(title='문의 답변이 왔습니다!', timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.add_field(name='내용', value=hi, inline=False)
            embed.set_footer(text="루크 서버 • Made by 호떡#9460", icon_url=""+servericon + "")
            await message.mentions[0].send (embed=embed)
            await message.channel.send(f'`{message.mentions[0]}`에게 DM을 보냈습니다 내용: {hi}')
    ####################################################################################################################################################################
            embed2 = discord.Embed(title="자동 기록 내용", description=f"문의봇, 답변내용: {hi}".format(message.author), timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed2.add_field(name="사용자 태그", value=f"{message.author}", inline=False) 
            embed2.add_field(name="사용자 아이디", value=f"{message.author.id}", inline=False) 
            embed2.set_footer(text="자동 로그 전송 • 루크 서버 • Made by 호떡#9460M".format(servername))
            embed2.set_thumbnail(url=servericon)
            await channel2.send (embed=embed2)
        except Exception as e:
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n 개발자에게 로그를 전송 합니다. \n 오류 해결이 될동안 사용하지 말아주세요. \n\n 오류코드 : {e}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.set_footer(text="루크 서버 • Made by 호떡#9460", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.channel.send (embed=embed)
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n\n 오류코드 : {e} \n\n 사용된 매세지 : '문의 오류' \n\n 사용자 : {message.author}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.set_footer(text="루크 서버 • Made by 호떡#9460", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await channel2.send (embed=embed)

    if message.content.startswith("!?문의종료"): 
        try:
            user = message.author
            date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000) 
            channel2 = client.get_channel(int(logs))
            target = discord.utils.get(message.guild.roles, name=f"{guild}") 
            if not target in message.author.roles: 
                return
            embed = discord.Embed(title='문의가 종료되었습니다.', timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.add_field(name='안내사항', value="담당 관리진이 문의를 종료 하였습니다. 매세지를 보내시면 새로운 문의가 생성되니 답장은 하지 말아주세요.", inline=False)
            embed.set_footer(text="루크 서버 • Made by 호떡#9460", icon_url=""+servericon + "")
            msg1 = await message.mentions[0].send (embed=embed)
            await msg1.add_reaction('❌')    
            await message.mentions[0].send ("-------------------------------------------------------------------------------------------")
            await message.channel.send(f'`{message.mentions[0]}`에게 문의종료를 알렸습니다.')
    ####################################################################################################################################################################
            embed2 = discord.Embed(title="자동 기록 내용", description=f"문의종료".format(message.author), timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed2.add_field(name="사용자 태그", value=f"{message.author}", inline=False) 
            embed2.add_field(name="사용자 아이디", value=f"{message.author.id}", inline=False) 
            embed2.set_footer(text="자동 로그 전송 • 루크 서버 • Made by 호떡#9460M".format(servername))
            embed2.set_thumbnail(url=servericon)
            await channel2.send (embed=embed2)
        except Exception as e:
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n 개발자에게 로그를 전송 합니다. \n 오류 해결이 될동안 사용하지 말아주세요. \n\n 오류코드 : {e}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.set_footer(text="루크 서버 • Made by 호떡#9460", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.channel.send (embed=embed)
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n\n 오류코드 : {e} \n\n 사용된 매세지 : '문의 오류' \n\n 사용자 : {message.author}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.set_footer(text="루크 서버 • Made by 호떡#9460", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await channel2.send (embed=embed)

client.run(token)
