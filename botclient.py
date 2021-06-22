from functools import update_wrapper
from ntpath import join
import discord, datetime, pytz, os, time, ctypes, webbrowser
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
kick = "841120653285392405"
guild = "총관리봇"
state = "모든 문의 디엠"
notice = "841128210330157146"
notice2 = "841120652659392556"
voting = "841128210330157146"
logs = "848501328044097566"
dkssudgktpdy = "841120652424642585"
dkssudgktpdy2 = "841120652424642586"
delete = "848501328044097566"
edit = "848501328044097566"
servericon = "https://cdn.discordapp.com/attachments/845894634072965172/846333308345647114/download.png"
newbiech = "841120652424642587"
newbiero = "841120650374021121"

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
async def on_member_join(member):
    date = datetime.datetime.utcfromtimestamp(((int(member.id) >> 22) + 1420070400000) / 1000) 
    member2 = client.get_channel(int(dkssudgktpdy))
    embed = discord.Embed(title='! 안녕하세요 !', description=f'안녕하세요 **{member.mention}**님, **{member.guild}**에 오신것을 환영합니다.',timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
    embed.add_field(name="디스코드 계정 생성일", value=""+str (date.year)+"년 "+str (date.month)+"월 "+str (date.day)+"일", inline=False) 
    embed.set_thumbnail(url=servericon)
    embed.set_footer(text=""+str(servername)+"")
    await member2.send(embed=embed)
    embed = discord.Embed(title='! 안녕하세요 !', description=f'안녕하세요, **{member.guild}**입니다. \n 인게임접속후 코드를 받은다음 "뉴비인증#코드"를 사용하여 인증절차 밝으실수 있습니다.',timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
    embed.set_footer(text=""+str(servername)+"")
    await member.send(embed=embed)

@client.event
async def on_member_remove(member):
    member2 = client.get_channel(int(dkssudgktpdy2))
    embed = discord.Embed(title='! 안녕히가세요 !', description=f'안녕히가세요 **{member.mention}**님 ㅠㅠㅠㅠㅠㅠㅠㅠㅠ',timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
    embed.set_footer(text=""+str(servername)+"")
    embed.set_thumbnail(url=servericon)
    await member2.send(embed=embed)

@client.event
async def on_message(message):    
    if message.content.startswith("!도움말"): 
        try:
            user = message.author
            Error = client.get_channel(int(logs))
            target = discord.utils.get(message.guild.roles, name=f"{guild}") 
            if not target in message.author.roles: 
                embed2 = discord.Embed(title="개인디엠을 확인해주세요.",color=0x800080)
                await message.channel.send (f"{message.author.mention}",embed=embed2)
                embed = discord.Embed(title="도움말 안내",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
                embed.add_field(name="유저 명령어", value="!핑,!내정보", inline=False) 
                embed.add_field(name="BOT V1", value="Made by 호떡#9460", inline=False) 
                embed.set_footer(text="{}".format(servername), icon_url=""+servericon + "")
                embed.set_thumbnail(url=servericon)
                await message.author.send (f"{message.author.mention}" ,embed=embed)
                return
            embed2 = discord.Embed(title="개인디엠을 확인해주세요.",color=0x800080)
            await message.channel.send (f"{message.author.mention}",embed=embed2)
            embed = discord.Embed(title="도움말 안내",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.add_field(name="관리 명령어", value="!공지 [내용], !투표 [내용], !청소 [매세지 개수], !역할추가 [맨션] [추가할 역할 이름], !역할제거 [맨션] [제거할 역할 이름], !별명변경 [맨션] [변경할 별명], !추방 [맨션] [사유], !차단 [맨션] [사유], !디엠 [맨션] [사유], !부팅, !종료, !리봇, !오픈준비", inline=False) 
            embed.add_field(name="유저 명령어", value="!핑,!내정보", inline=False) 
            embed.add_field(name="BOT V1", value="Made by 호떡#9460", inline=False) 
            embed.set_footer(text="{}".format(servername), icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.author.send (f"{message.author.mention}" ,embed=embed)
        except Exception as e:
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description="의도치 않는 오류가 발생하였습니다. \n 개발자에게 로그를 전송 합니다. \n 오류 해결이 될동안 사용하지 말아주세요.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.channel.send (embed=embed)
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n\n 오류코드 : {e} \n\n 사용된 매세지 : {message.content} \n\n 사용자 : {message.author}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await Error.send (embed=embed)    

    if message.content.startswith("!역할추가"): 
        try:
            try:
                user = message.mentions[0]
            except:
                embed = discord.Embed(title="유저를 맨션해주세요.",color=0x800080)
                await message.channel.send(f"{message.author.mention}" ,embed=embed)
                return None
            user = message.author
            hi = message.content[27:]
            Error = client.get_channel(int(logs))
            target = discord.utils.get(message.guild.roles, name=f"{guild}") 
            if not target in message.author.roles: 
                return
            embed2 = discord.Embed(title="개인디엠을 확인해주세요.",color=0x800080)
            await message.channel.send (f"{message.author.mention}",embed=embed2)
            embed = discord.Embed(title="역할 추가 명령어 안내", description=f"다른 사용자에게 역할을 추가하셨습니다.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.add_field(name="담당 관리자", value=f"{message.author}", inline=False) 
            embed.add_field(name="역할 추가자", value=f"{message.mentions[0]}", inline=False) 
            embed.add_field(name="추가된 역할", value=f"{hi}", inline=False) 
            embed.set_footer(text="{}".format(servername), icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            role = discord.utils.get(message.guild.roles, name=f"{hi}")
            await message.mentions[0].add_roles(role)
            await message.author.send (f"{message.author.mention}", embed=embed)     
        except Exception as e:
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description="의도치 않는 오류가 발생하였습니다. \n 개발자에게 로그를 전송 합니다. \n 오류 해결이 될동안 사용하지 말아주세요.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.channel.send (embed=embed)
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n\n 오류코드 : {e} \n\n 사용된 매세지 : {message.content} \n\n 사용자 : {message.author}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await Error.send (embed=embed)   

    if message.content.startswith("!역할제거"): 
        try:
            try:
                user = message.mentions[0]
            except:
                embed = discord.Embed(title="유저를 맨션해주세요.",color=0x800080)
                await message.channel.send(f"{message.author.mention}" ,embed=embed)
                return None
            user = message.author
            hi = message.content[27:]
            Error = client.get_channel(int(logs))
            target = discord.utils.get(message.guild.roles, name=f"{guild}") 
            if not target in message.author.roles: 
                return
            embed2 = discord.Embed(title="개인디엠을 확인해주세요.",color=0x800080)
            await message.channel.send (f"{message.author.mention}",embed=embed2)
            embed = discord.Embed(title="역할 제거 명령어 안내", description=f"다른 사용자에게 역할을 제거하셨습니다.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.add_field(name="담당 관리자", value=f"{message.author}", inline=False) 
            embed.add_field(name="역할 제거자", value=f"{message.mentions[0]}", inline=False) 
            embed.add_field(name="추가된 역할", value=f"{hi}", inline=False) 
            embed.set_footer(text="{}".format(servername), icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            role = discord.utils.get(message.guild.roles, name=f"{hi}")
            await message.mentions[0].remove_roles(role)
            await message.author.send (f"{message.author.mention}", embed=embed)     
        except Exception as e:
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description="의도치 않는 오류가 발생하였습니다. \n 개발자에게 로그를 전송 합니다. \n 오류 해결이 될동안 사용하지 말아주세요.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.channel.send (embed=embed)
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n\n 오류코드 : {e} \n\n 사용된 매세지 : {message.content} \n\n 사용자 : {message.author}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await Error.send (embed=embed)   

    if message.content.startswith("!별명변경"): 
        try:
            try:
                user = message.mentions[0]
            except:
                embed = discord.Embed(title="유저를 맨션해주세요.",color=0x800080)
                await message.channel.send(f"{message.author.mention}" ,embed=embed)
                return None
            user = message.author
            hi = message.content[27:]
            Error = client.get_channel(int(logs))
            target = discord.utils.get(message.guild.roles, name=f"{guild}") 
            if not target in message.author.roles: 
                return
            embed2 = discord.Embed(title="개인디엠을 확인해주세요.",color=0x800080)
            await message.channel.send (f"{message.author.mention}",embed=embed2)
            embed = discord.Embed(title="별명 변경 안내", description=f"다른 사용자에게 별명을 변경하셨습니다.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.add_field(name="담당 관리자", value=f"{message.author}", inline=False) 
            embed.add_field(name="별명 변경자", value=f"{message.mentions[0]}", inline=False) 
            embed.add_field(name="변경된 이름", value=f"{hi}", inline=False) 
            embed.set_footer(text="{}".format(servername), icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.mentions[0].edit(nick=f"{hi}")
            await message.author.send (f"{message.author.mention}", embed=embed)     
        except Exception as e:
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description="의도치 않는 오류가 발생하였습니다. \n 개발자에게 로그를 전송 합니다. \n 오류 해결이 될동안 사용하지 말아주세요.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.channel.send (embed=embed)
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n\n 오류코드 : {e} \n\n 사용된 매세지 : {message.content} \n\n 사용자 : {message.author}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await Error.send (embed=embed)  


    if message.content.startswith("!공지"): 
        try:
            user = message.author
            hi = message.content[4:]
            no = client.get_channel(int(notice))
            Error = client.get_channel(int(logs))
            target = discord.utils.get(message.guild.roles, name=f"{guild}") 
            if not target in message.author.roles: 
                return
            embed = discord.Embed(title="공지 사항", description=f"{hi}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text="{}".format(servername), icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await no.send ("@everyone", embed=embed)
            for i in message.guild.members:
                if i.bot == True:
                    pass
                else:
                    try:
                        hi = message.content[27:]
                        if message.author.guild_permissions.manage_messages:
                            embed2 = discord.Embed(color=0x800080, timestamp=datetime.datetime.now(pytz.timezone('UTC')))
                            embed2.add_field(name=f"공지 사항", value=f"{hi}", inline=False)
                            embed2.set_footer(text="{}".format(servername))
                            embed2.set_thumbnail(url=servericon)
                            await i.send (f"{message.author.mention}", embed=embed2)
                    except:
                        pass            
        except Exception as e:
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description="의도치 않는 오류가 발생하였습니다. \n 개발자에게 로그를 전송 합니다. \n 오류 해결이 될동안 사용하지 말아주세요.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.channel.send (embed=embed)
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n\n 오류코드 : {e} \n\n 사용된 매세지 : {message.content} \n\n 사용자 : {message.author}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await Error.send (embed=embed)   


    if message.content.startswith("!부팅"): 
        try:
            user = message.author
            no = client.get_channel(int(notice2))
            Error = client.get_channel(int(logs))
            target = discord.utils.get(message.guild.roles, name=f"{guild}") 
            if not target in message.author.roles: 
                return
            embed = discord.Embed(title="서버 상태 안내", description=f"**{servername}**서버가 성공적으로 부팅되었습니다. 접속하셔도 됩니다.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text="{}".format(servername), icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await no.send ("@everyone", embed=embed)
            for i in message.guild.members:
                if i.bot == True:
                    pass
                else:
                    try:
                        if message.author.guild_permissions.manage_messages:
                            embed2 = discord.Embed(color=0x800080, timestamp=datetime.datetime.now(pytz.timezone('UTC')))
                            embed2.add_field(name=f"서버 상태 안내", value=f"**{servername}**서버가 성공적으로 부팅되었습니다. 접속하셔도 됩니다.", inline=False)
                            embed2.set_footer(text="{}".format(servername))
                            embed2.set_thumbnail(url=servericon)
                            await i.send (f"{message.author.mention}", embed=embed2)
                    except:
                        pass            
        except Exception as e:
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description="의도치 않는 오류가 발생하였습니다. \n 개발자에게 로그를 전송 합니다. \n 오류 해결이 될동안 사용하지 말아주세요.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.channel.send (embed=embed)
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n\n 오류코드 : {e} \n\n 사용된 매세지 : {message.content} \n\n 사용자 : {message.author}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await Error.send (embed=embed)   

    if message.content.startswith("!종료"): 
        try:
            user = message.author
            no = client.get_channel(int(notice2))
            Error = client.get_channel(int(logs))
            target = discord.utils.get(message.guild.roles, name=f"{guild}") 
            if not target in message.author.roles: 
                return
            embed = discord.Embed(title="서버 상태 안내", description=f"**{servername}**서버가 종료되었습니다. 서버를 즐겨주셔서 감사합니다.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text="{}".format(servername), icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await no.send ("@everyone", embed=embed)
            for i in message.guild.members:
                if i.bot == True:
                    pass
                else:
                    try:
                        if message.author.guild_permissions.manage_messages:
                            embed2 = discord.Embed(color=0x800080, timestamp=datetime.datetime.now(pytz.timezone('UTC')))
                            embed2.add_field(name=f"서버 상태 안내", value=f"**{servername}**서버가 종료되었습니다. 서버를 즐겨주셔서 감사합니다.", inline=False)
                            embed2.set_footer(text="{}".format(servername))
                            embed2.set_thumbnail(url=servericon)
                            await i.send (f"{message.author.mention}", embed=embed2)
                    except:
                        pass            
        except Exception as e:
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description="의도치 않는 오류가 발생하였습니다. \n 개발자에게 로그를 전송 합니다. \n 오류 해결이 될동안 사용하지 말아주세요.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.channel.send (embed=embed)
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n\n 오류코드 : {e} \n\n 사용된 매세지 : {message.content} \n\n 사용자 : {message.author}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await Error.send (embed=embed)   

    if message.content.startswith("!리봇"): 
        try:
            user = message.author
            no = client.get_channel(int(notice2))
            Error = client.get_channel(int(logs))
            target = discord.utils.get(message.guild.roles, name=f"{guild}") 
            if not target in message.author.roles: 
                return
            embed = discord.Embed(title="서버 상태 안내", description=f"**{servername}**서버가 리봇중입니다. 아무런 접속 시도를 하지 말아주세요.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text="{}".format(servername), icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await no.send ("@everyone", embed=embed)
            for i in message.guild.members:
                if i.bot == True:
                    pass
                else:
                    try:
                        if message.author.guild_permissions.manage_messages:
                            embed2 = discord.Embed(color=0x800080, timestamp=datetime.datetime.now(pytz.timezone('UTC')))
                            embed2.add_field(name=f"서버 상태 안내", value=f"**{servername}**서버가 리봇중입니다. 아무런 접속 시도를 하지 말아주세요.", inline=False)
                            embed2.set_footer(text="{}".format(servername))
                            embed2.set_thumbnail(url=servericon)
                            await i.send (f"{message.author.mention}", embed=embed2)
                    except:
                        pass            
        except Exception as e:
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description="의도치 않는 오류가 발생하였습니다. \n 개발자에게 로그를 전송 합니다. \n 오류 해결이 될동안 사용하지 말아주세요.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.channel.send (embed=embed)
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n\n 오류코드 : {e} \n\n 사용된 매세지 : {message.content} \n\n 사용자 : {message.author}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await Error.send (embed=embed)   

    if message.content.startswith("!오픈준비"): 
        try:
            user = message.author
            no = client.get_channel(int(notice2))
            Error = client.get_channel(int(logs))
            target = discord.utils.get(message.guild.roles, name=f"{guild}") 
            if not target in message.author.roles: 
                return
            embed = discord.Embed(title="서버 상태 안내", description=f"안녕하세요 **{servername}**입니다. 현재 서버는 오픈 준비중에 있습니다. 타섭을 하시면서 기다려주시면 감사하겠습니다.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text="{}".format(servername), icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await no.send ("@everyone", embed=embed)
            for i in message.guild.members:
                if i.bot == True:
                    pass
                else:
                    try:
                        if message.author.guild_permissions.manage_messages:
                            embed2 = discord.Embed(color=0x800080, timestamp=datetime.datetime.now(pytz.timezone('UTC')))
                            embed2.add_field(name=f"서버 상태 안내", value=f"안녕하세요 **{servername}**입니다. 현재 서버는 오픈 준비중에 있습니다. 타섭을 하시면서 기다려주시면 감사하겠습니다.", inline=False)
                            embed2.set_footer(text="{}".format(servername))
                            embed2.set_thumbnail(url=servericon)
                            await i.send (f"{message.author.mention}", embed=embed2)
                    except:
                        pass            
        except Exception as e:
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description="의도치 않는 오류가 발생하였습니다. \n 개발자에게 로그를 전송 합니다. \n 오류 해결이 될동안 사용하지 말아주세요.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.channel.send (embed=embed)
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n\n 오류코드 : {e} \n\n 사용된 매세지 : {message.content} \n\n 사용자 : {message.author}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await Error.send (embed=embed) 

    if message.content.startswith("!디엠"): 
        try:
            try:
                user = message.mentions[0]
            except:
                embed = discord.Embed(title="유저를 맨션해주세요.",color=0x800080)
                await message.channel.send(f"{message.author.mention}" ,embed=embed)
                return None
            user = message.author
            hi = message.content[27:]
            Error = client.get_channel(int(logs))
            target = discord.utils.get(message.guild.roles, name=f"{guild}") 
            if not target in message.author.roles: 
                return
            embed2 = discord.Embed(title="개인디엠을 확인해주세요.",color=0x800080)
            await message.channel.send (f"{message.author.mention}",embed=embed2)
            embed = discord.Embed(title="운영진 안내", description=f"다른 사용자에게 봇을 이용하여 디엠을 보냈습니다.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.add_field(name="담당 관리자", value=f"{message.author}", inline=False) 
            embed.add_field(name="디엠 보낸사람", value=f"{message.mentions[0]}", inline=False) 
            embed.add_field(name="사유", value=f"{hi}", inline=False) 
            embed.set_footer(text="{}".format(servername), icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.author.send (f"{message.author.mention}", embed=embed)     
            embed = discord.Embed(title="운영진 안내",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.add_field(name="내용", value=f"{hi}".format(client.latency), inline=False) 
            embed.set_footer(text="{}".format(servername), icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.mentions[0].send (f"{message.author.mention}", embed=embed)     
        except Exception as e:
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description="의도치 않는 오류가 발생하였습니다. \n 개발자에게 로그를 전송 합니다. \n 오류 해결이 될동안 사용하지 말아주세요.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.channel.send (embed=embed)
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n\n 오류코드 : {e} \n\n 사용된 매세지 : {message.content} \n\n 사용자 : {message.author}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await Error.send (embed=embed)   


    if message.content.startswith("!청소"): 
        try:
            user = message.author   
            hi = message.content[4:]
            Error = client.get_channel(int(logs))
            target = discord.utils.get(message.guild.roles, name=f"{guild}") 
            if not target in message.author.roles: 
                return
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(hi))
            embed = discord.Embed(title="청소 안내", description=f"매세지를 성공적으로 삭제하였습니다.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.add_field(name="청소 매세지 개수", value=f"{hi}".format(client.latency), inline=False) 
            embed.add_field(name="청소된 채널 아이디", value=f"{message.channel.id}".format(client.latency), inline=False) 
            embed.set_footer(text="{}".format(servername), icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.author.send (f"{message.author.mention}", embed=embed)     
        except Exception as e:
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description="의도치 않는 오류가 발생하였습니다. \n 개발자에게 로그를 전송 합니다. \n 오류 해결이 될동안 사용하지 말아주세요.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.channel.send (embed=embed)
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n\n 오류코드 : {e} \n\n 사용된 매세지 : {message.content} \n\n 사용자 : {message.author}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await Error.send (embed=embed)   

    if message.content.startswith("!추방"): 
        try:
            try:
                user = message.mentions[0]
            except:
                embed = discord.Embed(title="유저를 맨션해주세요.",color=0x800080)
                await message.channel.send(f"{message.author.mention}" ,embed=embed)
                return None
            user = message.author
            hi = message.content[27:]
            Error = client.get_channel(int(logs))
            police = client.get_channel(int(kick))
            target = discord.utils.get(message.guild.roles, name=f"{guild}") 
            if not target in message.author.roles: 
                return
            embed2 = discord.Embed(title="개인디엠을 확인해주세요.",color=0x800080)
            await message.channel.send (f"{message.author.mention}",embed=embed2)
            embed = discord.Embed(title="추방 안내", description=f"사용자를 성공적으로 추방하였습니다.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.add_field(name="담당 관리자", value=f"{message.author}", inline=False) 
            embed.add_field(name="추방 대상", value=f"{message.mentions[0]}", inline=False) 
            embed.add_field(name="사유", value=f"{hi}", inline=False) 
            embed.set_footer(text="{}".format(servername), icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.author.send (f"{message.author.mention}", embed=embed)     
            embed2 = discord.Embed(title="추방 안내", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed2.add_field(name="담당 관리자", value=f"{message.author}", inline=False) 
            embed2.add_field(name="추방 대상", value=f"{message.mentions[0]}", inline=False) 
            embed2.add_field(name="사유", value=f"{hi}", inline=False) 
            embed2.set_footer(text="{}".format(servername), icon_url=""+servericon + "")
            embed2.set_thumbnail(url=servericon)
            await police.send (f"{message.author.mention}", embed=embed2)    
            await message.mentions[0].kick(reason=f'{hi}')  
        except Exception as e:
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description="의도치 않는 오류가 발생하였습니다. \n 개발자에게 로그를 전송 합니다. \n 오류 해결이 될동안 사용하지 말아주세요.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.channel.send (embed=embed)
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n\n 오류코드 : {e} \n\n 사용된 매세지 : {message.content} \n\n 사용자 : {message.author}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await Error.send (embed=embed)   

    if message.content.startswith("!차단"): 
        try:
            try:
                user = message.mentions[0]
            except:
                embed = discord.Embed(title="유저를 맨션해주세요.",color=0x800080)
                await message.channel.send(f"{message.author.mention}" ,embed=embed)
                return None
            user = message.author
            hi = message.content[27:]
            Error = client.get_channel(int(logs))
            police = client.get_channel(int(kick))
            target = discord.utils.get(message.guild.roles, name=f"{guild}") 
            if not target in message.author.roles: 
                return
            embed2 = discord.Embed(title="개인디엠을 확인해주세요.",color=0x800080)
            await message.channel.send (f"{message.author.mention}",embed=embed2)
            embed = discord.Embed(title="차단 안내", description=f"사용자를 성공적으로 차단하였습니다.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.add_field(name="담당 관리자", value=f"{message.author}", inline=False) 
            embed.add_field(name="차단 대상", value=f"{message.mentions[0]}", inline=False) 
            embed.add_field(name="사유", value=f"{hi}", inline=False) 
            embed.set_footer(text="{}".format(servername), icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.author.send (f"{message.author.mention}", embed=embed)     
            embed2 = discord.Embed(title="차단 안내", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed2.add_field(name="담당 관리자", value=f"{message.author}", inline=False) 
            embed2.add_field(name="차단 대상", value=f"{message.mentions[0]}", inline=False) 
            embed2.add_field(name="사유", value=f"{hi}", inline=False) 
            embed2.set_footer(text="{}".format(servername), icon_url=""+servericon + "")
            embed2.set_thumbnail(url=servericon)
            await police.send (f"{message.author.mention}", embed=embed2)    
            await message.mentions[0].ban(reason=f'{hi}')  
        except Exception as e:
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description="의도치 않는 오류가 발생하였습니다. \n 개발자에게 로그를 전송 합니다. \n 오류 해결이 될동안 사용하지 말아주세요.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.channel.send (embed=embed)
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n\n 오류코드 : {e} \n\n 사용된 매세지 : {message.content} \n\n 사용자 : {message.author}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await Error.send (embed=embed)   

    if message.content.startswith("!투표"): 
        try:
            user = message.author
            hi = message.content[4:]
            no = client.get_channel(int(voting))
            Error = client.get_channel(int(logs))
            target = discord.utils.get(message.guild.roles, name=f"{guild}") 
            if not target in message.author.roles: 
                return
            embed = discord.Embed(title="투표 사항", description=f"{hi}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text="{}".format(servername), icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            msg = await no.send ("@everyone", embed=embed)
            await msg.add_reaction('✅')
            await msg.add_reaction('⛔')
            for i in message.guild.members:
                if i.bot == True:
                    pass
                else:
                    try:
                        hi = message.content[4:]
                        if message.author.guild_permissions.manage_messages:
                            embed2 = discord.Embed(color=0x800080, timestamp=datetime.datetime.now(pytz.timezone('UTC')))
                            embed2.add_field(name=f"투표 사항", value=f"{hi}", inline=False)
                            embed2.set_footer(text="{}".format(servername))
                            embed2.set_thumbnail(url=servericon)
                            msg = await i.send (f"{message.author.mention}", embed=embed2)
                            await msg.add_reaction('✅')
                            await msg.add_reaction('⛔')
                    except:
                        pass            
        except Exception as e:
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description="의도치 않는 오류가 발생하였습니다. \n 개발자에게 로그를 전송 합니다. \n 오류 해결이 될동안 사용하지 말아주세요.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.channel.send (embed=embed)
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n\n 오류코드 : {e} \n\n 사용된 매세지 : {message.content} \n\n 사용자 : {message.author}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await Error.send (embed=embed)   

    if message.content.startswith("!핑"): 
        try:
            user = message.author
            Error = client.get_channel(int(logs))
            embed = discord.Embed(title="봇 핑 상태",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.add_field(name="핑 상태", value="퐁 !, {0}초".format(client.latency), inline=False) 
            embed.set_footer(text="{}".format(servername), icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.channel.send (f"{message.author.mention}" ,embed=embed)
        except Exception as e:
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description="의도치 않는 오류가 발생하였습니다. \n 개발자에게 로그를 전송 합니다. \n 오류 해결이 될동안 사용하지 말아주세요.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.channel.send (embed=embed)
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n\n 오류코드 : {e} \n\n 사용된 매세지 : {message.content} \n\n 사용자 : {message.author}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await Error.send (embed=embed)   
        
    if message.content.startswith("!내정보"): 
        try:
            user = message.author
            Error = client.get_channel(int(logs))
            date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000) 
            embed = discord.Embed(title=f"{user.name}님의 정보",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.add_field(name=f"{user.name}님의 태그", value=f"{message.author}", inline=False) 
            embed.add_field(name=f"{user.name}님의 아이디", value=f"{message.author.id}", inline=False) 
            embed.add_field(name=f"{user.name}님의 디스코드 가입일", value=""+str (date.year)+"년 "+str (date.month)+"월 "+str (date.day)+"일", inline=False) 
            embed.set_footer(text="{}".format(servername), icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.channel.send (f"{message.author.mention}" ,embed=embed)
        except Exception as e:
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description="의도치 않는 오류가 발생하였습니다. \n 개발자에게 로그를 전송 합니다. \n 오류 해결이 될동안 사용하지 말아주세요.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.channel.send (embed=embed)
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n\n 오류코드 : {e} \n\n 사용된 매세지 : {message.content} \n\n 사용자 : {message.author}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await Error.send (embed=embed)   


    if message.guild is None:
        try:           
            Error = client.get_channel(int(logs))
            date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000) 
            if message.author.bot:
                return
            else:
                embed = discord.Embed(title='문의가 왔습니다!', timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
                embed.add_field(name='전송자ㅣ내용', value=f"{message.author}ㅣ{message.content}", inline=False)
                embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
                embed3 = discord.Embed(timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
                embed3.add_field(name="문의 안내", value=f"전달 내용 : {message.content}", inline=False)
                embed3.set_footer(text=f"{servername}", icon_url=""+servericon + "")
                await message.author.send (embed=embed3)
                await client.get_channel(853937922256535552).send(f"<@{message.author.id}>", embed=embed)
                return
        except Exception as e:
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n 개발자에게 로그를 전송 합니다. \n 오류 해결이 될동안 사용하지 말아주세요.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.channel.send (embed=embed)
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n\n 오류코드 : {e} \n\n 사용된 매세지 : '문의 오류' \n\n 사용자 : {message.author}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await Error.send (embed=embed)

    if message.content.startswith("!답변"): 
        try:
            user = message.author
            date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000) 
            if not message.channel.id == 853937922256535552:
                return
            Error = client.get_channel(int(logs))
            target = discord.utils.get(message.guild.roles, name=f"{guild}") 
            if not target in message.author.roles: 
                return
            hi = message.content[27:]
            embed = discord.Embed(title='문의 답변이 왔습니다!', timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.add_field(name='내용', value=hi, inline=False)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            await message.mentions[0].send (embed=embed)
            await message.channel.send(f'`{message.mentions[0]}`에게 DM을 보냈습니다 내용: {hi}')
        except Exception as e:
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n 개발자에게 로그를 전송 합니다. \n 오류 해결이 될동안 사용하지 말아주세요.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.channel.send (embed=embed)
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n\n 오류코드 : {e} \n\n 사용된 매세지 : '문의 오류' \n\n 사용자 : {message.author}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await Error.send (embed=embed)

    if message.content.startswith("!문의종료"): 
        try:
            user = message.author
            Error = client.get_channel(int(logs))
            date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000) 
            if not message.channel.id == 853937922256535552:
                return
            target = discord.utils.get(message.guild.roles, name=f"{guild}") 
            if not target in message.author.roles: 
                return
            embed = discord.Embed(title='문의가 종료되었습니다.', timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x800080)
            embed.add_field(name='안내사항', value="담당 관리진이 문의를 종료 하였습니다. 매세지를 보내시면 새로운 문의가 생성되니 답장은 하지 말아주세요.", inline=False)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            msg1 = await message.mentions[0].send (embed=embed)
            await msg1.add_reaction('❌')    
            await message.mentions[0].send ("-------------------------------------------------------------------------------------------")
            await message.channel.send(f'`{message.mentions[0]}`에게 문의종료를 알렸습니다.')
        except Exception as e:
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n 개발자에게 로그를 전송 합니다. \n 오류 해결이 될동안 사용하지 말아주세요. \n\n 오류코드 : {e}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await message.channel.send (embed=embed)
            embed = discord.Embed(title="⛔봇 오류 발생⛔", description=f"의도치 않는 오류가 발생하였습니다. \n\n 오류코드 : {e} \n\n 사용된 매세지 : '문의 오류' \n\n 사용자 : {message.author}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.set_footer(text=f"{servername}", icon_url=""+servericon + "")
            embed.set_thumbnail(url=servericon)
            await Error.send (embed=embed)

try:
    client.run(token)
except discord.LoginFailure as e:
    ctypes.windll.user32.MessageBoxW(0, f"토큰을 제대로 적어주세요 ! \n\n 오류 코드 : {e}", "토큰 오류", 0)
    webbrowser.open('https://www.google.com/search?q=discord+token&oq=discord+token&aqs=chrome..69i57j0l4j69i60j69i61j69i60.2840j0j7&sourceid=chrome&ie=UTF-8')
except discord.PrivilegedIntentsRequired as e:
    ctypes.windll.user32.MessageBoxW(0, f"Gateway Intents에서 SERVER MEMBERS INTENT를 활성화 해주세요! \n\n 오류 코드 : {e}", "Gateway Intents 오류", 0)
    webbrowser.open('https://discordpy.readthedocs.io/en/latest/intents.html')
