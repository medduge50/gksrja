import discord, datetime, pytz, os, string, random

###################설정 하는 곳###################
token = os.environ["BOT_TOKEN"]

name = "DUKE STORE" #서버이름

role = "🌊ㆍ판매원" #권한 이름

footer = "Copyright 2021 DUKE STORE all rights reserved."

icon = "https://cdn.discordapp.com/attachments/850656914927779872/886508550103375922/9k.png" #사용할 봇 아이콘 

channelid = "886508628956303390" #error channel id

joinid = "886437230179135572" #join channel id

removeid = "886437433841967154" #remove channel id

dlswmdrole = "886440697220202526" #dlswmd role id rmaoid

rmaoid = "886479893733457970" #rmaoid
###################설정 하는 곳###################

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents) # discord.client를 client라는 변수로 추가

@client.event
async def on_member_join(member):
    member_joing = client.get_channel(int(joinid)) 
    embed = discord.Embed(timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x0000FF)    
    embed.add_field(name=f"{name} 환영 !", value=f"안녕하세요 ! **{member}**님! **{name}**에 오신것을 환영합니다.", inline=False)  
    embed.set_footer(text=footer)
    embed.set_thumbnail(url=icon)  
    await member_joing.send(member.mention ,embed=embed)    

@client.event
async def on_member_remove(member):
    member_remove = client.get_channel(int(removeid)) 
    embed = discord.Embed(timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x0000FF)    
    embed.add_field(name=f"{name} 환영 !", value=f"안녕히가세요 ! **{member}**님! 지금까지 즐거웠습니다 !", inline=False)  
    embed.set_footer(text=footer)
    embed.set_thumbnail(url=icon)  
    await member_remove.send(member.mention ,embed=embed)    

@client.event
async def on_connect(): #봇이 켜졌을때 반응
    print(f"BOT ON !") 
    game = discord.Game("관리봇 제작중") #상매 
    await client.change_presence(status=discord.Status.online, activity=game) #상매   

@client.event
async def on_message(message):   
    if message.content.startswith("!도움말"):
        try:
            target = discord.utils.get(message.guild.roles, name=f"{role}") 
            if not target in message.author.roles: 
                return
            if message.author.bot:
                return
            else:
                embed = discord.Embed(title=f'{name}',timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x0000FF)    
                embed.add_field(name="관리 명령어", value="!핑, !공지, !청소", inline=False)  
                embed.set_footer(text=footer)
                embed.set_thumbnail(url=icon)  
                await message.channel.send(embed=embed)

        except Exception as errorcode:
            error = client.get_channel(int(channelid)) 
            embed2 = discord.Embed(title=f'{name}', description=f'오류가 발생하였습니다.', color=0xFF0000)
            embed2.add_field(name="사용자", value=message.author, inline=False)    
            embed2.add_field(name="사용자 아이디", value=message.author.id, inline=False)  
            embed2.add_field(name="명령어", value=message.content, inline=False)      
            embed2.add_field(name="오류 코드", value=errorcode, inline=False)  
            await error.send(embed=embed2)
            embed3 = discord.Embed(title=f'{name}', description=f'오류가 발생하였습니다.', color=0xFF0000)
            await message.channel.send(embed=embed3)   

    if message.content.startswith("!공지"):
        try:
            try:
                content = message.content[4:]
                channeid,soure=content.split("&")
            except:
                embed3 = discord.Embed(title=f'{name}', description=f'채널 아이디와 공지할 내용을 보내주세요.', color=0xFF0000)
                return await message.channel.send(embed=embed3)                   
            target = discord.utils.get(message.guild.roles, name=f"{role}") 
            if not target in message.author.roles: 
                return
            if message.author.bot:
                return
            else:
                embed3 = discord.Embed(title=f'{name} NOTICE', description=f'에브리원을 활성화 할까요 ? [네/아니요]', color=0x0000FF)
                await message.channel.send(embed=embed3)          

                def check(msg):
                    return msg.author == message.author and msg.channel == message.channel 

                try:
                    msg = await client.wait_for("message", timeout=30, check=check) 
                except:
                    embed3 = discord.Embed(title=f'{name} NOTICE', description=f'30초 초과로 인하여 공지가 초기화 되었습니다.', color=0xFF0000)
                    return await message.channel.send(embed=embed3)   
                if msg.content == "아니요":
                    channel = client.get_channel(int(channeid)) 
                    embed = discord.Embed(title=f'{name} NOTICE', description=f'{soure}', timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x0000FF)    
                    embed.set_footer(text=footer)
                    embed.set_thumbnail(url=icon)  
                    return await channel.send(embed=embed)   
                else:             
                    if msg.content == "네":                          
                        channel = client.get_channel(int(channeid)) 
                        embed = discord.Embed(title=f'{name} NOTICE', description=f'{soure}', timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x0000FF)    
                        embed.set_footer(text=footer)
                        embed.set_thumbnail(url=icon)  
                        return await channel.send(f"@everyone" ,embed=embed)      
                    else:
                        embed3 = discord.Embed(title=f'{name} NOTICE', description=f'네/아니요를 보내주세요. 공지가 취소 되었습니다.', color=0xFF0000)
                        return await message.channel.send(embed=embed3)       

        except Exception as errorcode:
            error = client.get_channel(int(channelid)) 
            embed2 = discord.Embed(title=f'{name}', description=f'오류가 발생하였습니다.', color=0xFF0000)
            embed2.add_field(name="사용자", value=message.author, inline=False)    
            embed2.add_field(name="사용자 아이디", value=message.author.id, inline=False)  
            embed2.add_field(name="명령어", value=message.content, inline=False)      
            embed2.add_field(name="오류 코드", value=errorcode, inline=False)  
            await error.send(embed=embed2)
            embed3 = discord.Embed(title=f'{name}', description=f'오류가 발생하였습니다.', color=0xFF0000)
            return await message.channel.send(embed=embed3)          

    if message.content.startswith("!구매"):
        try:
            try:
                content = message.content[4:]
                channename,user=content.split("&")
            except:
                embed3 = discord.Embed(title=f'{name} 구매 로그', description=f'채널 아이디와 공지할 내용을 보내주세요.', color=0xFF0000)
                return await message.channel.send(embed=embed3)                   
            target = discord.utils.get(message.guild.roles, name=f"{role}") 
            if not target in message.author.roles: 
                return
            if message.author.bot:
                return
            else:
                error = client.get_channel(int(rmaoid))             
                embed = discord.Embed(timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x0000FF)    
                embed.add_field(name=f"{name} 구매 로그", value=f"**{user}**님 **{channename}**을(를) 구매해주셔서 감사합니다!", inline=False)  
                embed.set_footer(text=footer)
                embed.set_thumbnail(url=icon)  
                return await error.send(embed=embed)                             

        except Exception as errorcode:
            error = client.get_channel(int(channelid)) 
            embed2 = discord.Embed(title=f'{name}', description=f'오류가 발생하였습니다.', color=0xFF0000)
            embed2.add_field(name="사용자", value=message.author, inline=False)    
            embed2.add_field(name="사용자 아이디", value=message.author.id, inline=False)  
            embed2.add_field(name="명령어", value=message.content, inline=False)      
            embed2.add_field(name="오류 코드", value=errorcode, inline=False)  
            await error.send(embed=embed2)
            embed3 = discord.Embed(title=f'{name}', description=f'오류가 발생하였습니다.', color=0xFF0000)
            return await message.channel.send(embed=embed3)    

    if message.content.startswith("!인증"):
        try:
            if message.author.bot:
                return
            else:
                _LENGTH = 6
                string_pool = string.ascii_letters + string.digits
                result = "" 
                for i in range(_LENGTH) :
                    result += random.choice(string_pool)
                embed3 = discord.Embed(title=f'{name} 인증 시스템', description=f'30초안에 **{result}**를 보내주세요.', color=0x0000FF)
                await message.channel.send(embed=embed3)          

                def check(msg):
                    return msg.author == message.author and msg.channel == message.channel 

                try:
                    msg = await client.wait_for("message", timeout=30, check=check) 
                except:
                    embed3 = discord.Embed(title=f'{name} 인증 시스템', description=f'30초 초과로 인하여 인증 시스템이 종료되었습니다. 다시 시도해주세요.', color=0xFF0000)
                    return await message.channel.send(embed=embed3)    
                if msg.content == result:              
                    embed = discord.Embed(timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x0000FF)    
                    embed.add_field(name=f"{name} 인증 시스템", value=f"{message.author}님 감사합니다 ! 성공적으로 인증되셨습니다 !\n시민 권한이 지급 됩니다.", inline=False)  
                    embed.set_footer(text=footer)
                    embed.set_thumbnail(url=icon)  
                    await message.channel.send(message.author.mention ,embed=embed)
                    return await message.author.add_roles(discord.utils.get(message.guild.roles, id=int(dlswmdrole)))
                else:
                    embed3 = discord.Embed(title=f'{name} 인증 시스템', description=f'매세지가 틀렸습니다. 인증 시스템이 종료되었습니다. 다시 시도해주세요.', color=0xFF0000)
                    return await message.channel.send(embed=embed3)                        

        except Exception as errorcode:
                error = client.get_channel(int(channelid)) 
                embed2 = discord.Embed(title=f'{name}', description=f'오류가 발생하였습니다.', color=0xFF0000)
                embed2.add_field(name="사용자", value=message.author, inline=False)    
                embed2.add_field(name="사용자 아이디", value=message.author.id, inline=False)  
                embed2.add_field(name="명령어", value=message.content, inline=False)      
                embed2.add_field(name="오류 코드", value=errorcode, inline=False)  
                await error.send(embed=embed2)
                embed3 = discord.Embed(title=f'{name}', description=f'오류가 발생하였습니다.', color=0xFF0000)
                return await message.channel.send(embed=embed3)   

    if message.content.startswith("!청소"):
        try:
            target = discord.utils.get(message.guild.roles, name=f"{role}") 
            if not target in message.author.roles: 
                return
            if message.author.bot:
                return
            else:

                content = message.content[4:]            
                if content == "":
                    embed3 = discord.Embed(title=f'청소 안내', description=f'!청소 [제거할 매세지 개수]로 다시 시도해주세요 !', color=0xFF0000)
                    return await message.channel.send(embed=embed3)      
                else:                            
                    await message.channel.purge(limit=int(1))     
                    try:   
                        await message.channel.purge(limit=int(content))
                    except:
                        embed3 = discord.Embed(title=f'청소 안내', description=f'!청소 [제거할 매세지 개수]로 다시 시도해주세요 !', color=0xFF0000)
                        return await message.channel.send(embed=embed3)                              
                    embed = discord.Embed(timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x0000FF)    
                    embed.add_field(name="청소 안내", value=f"매세지 {content}개를 제거하였습니다.", inline=False)  
                    embed.set_footer(text=footer)
                    embed.set_thumbnail(url=icon)  
                    return await message.author.send(embed=embed)

        except Exception as errorcode:
            error = client.get_channel(int(channelid)) 
            embed2 = discord.Embed(title=f'{name}', description=f'오류가 발생하였습니다.', color=0xFF0000)
            embed2.add_field(name="사용자", value=message.author, inline=False)    
            embed2.add_field(name="사용자 아이디", value=message.author.id, inline=False)  
            embed2.add_field(name="명령어", value=message.content, inline=False)      
            embed2.add_field(name="오류 코드", value=errorcode, inline=False)  
            await error.send(embed=embed2)
            embed3 = discord.Embed(title=f'{name}', description=f'오류가 발생하였습니다.', color=0xFF0000)
            return await message.channel.send(embed=embed3)                                                      

    if message.content.startswith("!핑"):
        try:
            target = discord.utils.get(message.guild.roles, name=f"{role}") 
            if not target in message.author.roles: 
                return
            if message.author.bot:
                return
            else:
                embed = discord.Embed(title=f'{name}', description=f'퐁 !', color=0x0000FF)
                return await message.channel.send(embed=embed)

        except Exception as errorcode:
            error = client.get_channel(int(channelid)) 
            embed2 = discord.Embed(title=f'{name}', description=f'오류가 발생하였습니다.', color=0xFF0000)
            embed2.add_field(name="사용자", value=message.author, inline=False)    
            embed2.add_field(name="사용자 아이디", value=message.author.id, inline=False)  
            embed2.add_field(name="명령어", value=message.content, inline=False)      
            embed2.add_field(name="오류 코드", value=errorcode, inline=False)  
            await error.send(embed=embed2)
            embed3 = discord.Embed(title=f'{name}', description=f'오류가 발생하였습니다.', color=0xFF0000)
            return await message.channel.send(embed=embed3)



client.run(token) # token 


