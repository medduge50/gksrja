import discord, datetime, pytz, os, string, random

###################설정 하는 곳###################
token = os.environ["BOT_TOKEN"]

name = "FIRST 배포소" #서버이름

role = "🐬ㆍ운영팀" #권한 이름

role2 = "🔨ㆍ𝐌𝐀𝐈𝐍 𝐁𝐎𝐓" #권한 이름

tlalrole = "✅ㆍ손님" 

footer = "Copyright 2021 FIRST 배포소 all rights reserved."

icon = "https://cdn.discordapp.com/attachments/744096168442855445/894757257613561886/1625663903238.png" #사용할 봇 아이콘 

channelid = "894757320981094482" 

joinid = "876330143164014606" 

removeid = "876331295951708221"

dlswmdrole = "876402715213832222" 

Categories = "891708005559701515"
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
    embed.add_field(name=f"{name} 환영 !", value=f"안녕히가세요 ! **{member}**님", inline=False)  
    embed.set_footer(text=footer)
    embed.set_thumbnail(url=icon)  
    await member_remove.send(member.mention ,embed=embed)    

@client.event
async def on_connect(): #봇이 켜졌을때 반응
    try:
        file = "notice.txt"
        os.remove(file)
    except:
        pass
    print(f"BOT ON !") 
    game = discord.Game(name) #상매 
    await client.change_presence(status=discord.Status.online, activity=game) #상매   

@client.event
async def on_message(message):   
    if message.content.startswith("!업로더"):
        target = discord.utils.get(message.guild.roles, name=f"{role2}") 
        if not target in message.author.roles: 
            return
        #########################################################################
        content = message.content[27:]
        try:
            user = message.mentions[0]
        except:
            return await message.channel.send("유저를 맨션해주세요.\n예시 (!업로더 @맨션 사용할 이모지)")
        if content == "":
            return await message.channel.send("이모지를 적어주세요.\n예시 (!업로더 @맨션 사용할 이모지)")
        else:            
            cat = client.get_channel(int(Categories))
            dkdkrole = discord.utils.get(message.guild.roles, name=tlalrole)
            #########################################################################
            df = await cat.guild.create_category(f"╭━━━╯{content}{user.name}╰━━━╮", overwrites=None, reason=None)
            per = await cat.guild.create_text_channel(f"{content}ㆍ공지", category=df)   
            per2 = await cat.guild.create_text_channel(f"{content}ㆍ배포목록", category=df)     
            per3 = await cat.guild.create_text_channel(f"{content}ㆍ판매목록", category=df)          
            per4 = await cat.guild.create_text_channel(f"{content}ㆍ배포신청", category=df)       
            per5 = await cat.guild.create_text_channel(f"{content}ㆍ건의사항", category=df)    
            ######################################################################### 
            await per.set_permissions(message.guild.default_role, read_messages=False)
            await per2.set_permissions(message.guild.default_role, read_messages=False)
            await per3.set_permissions(message.guild.default_role, read_messages=False)
            await per4.set_permissions(message.guild.default_role, read_messages=False)
            await per5.set_permissions(message.guild.default_role, read_messages=False)
            #########################################################################
            await per.set_permissions(dkdkrole, read_messages=True, send_messages=False, read_message_history=True)
            #########################################################################
            await per2.set_permissions(dkdkrole, read_messages=True, send_messages=False, read_message_history=True)
            #########################################################################
            await per3.set_permissions(dkdkrole, read_messages=True, send_messages=False, read_message_history=True)
            #########################################################################
            await per4.set_permissions(dkdkrole, read_messages=True, send_messages=True, read_message_history=True)
            #########################################################################
            await per5.set_permissions(dkdkrole, read_messages=True, send_messages=False, read_message_history=True)
            #########################################################################
            await per.set_permissions(user, read_messages=True, send_messages=True, read_message_history=True)
            await per2.set_permissions(user, read_messages=True, send_messages=True, read_message_history=True)
            await per3.set_permissions(user, read_messages=True, send_messages=True, read_message_history=True)
            await per4.set_permissions(user, read_messages=True, send_messages=True, read_message_history=True)
            await per5.set_permissions(user, read_messages=True, send_messages=True, read_message_history=True)
            #########################################################################
            await per.send(f"{user.mention}")
            embed2 = discord.Embed(title=f'{name}', description=f'``{user}``님에 업로더 채널이 생성되었습니다.\n담당 관리진: {message.author}\n설정된 이모지: {content}', color=0x0000FF)
            await user.send(message.author.mention ,embed=embed2)
            try:
                await user.edit(nick=f"업로더ㅣ{user.name}")
            except:
                pass
            embed = discord.Embed(title=f'{name}', description=f'업로더 채널이 생성되었습니다.\n설정된 이모티콘: {content}\n설정된 업로더: {user}', color=0x0000FF)
            return await message.channel.send(f"{message.author.mention}", embed=embed)  
            
    if message.content.startswith("!도움말"):
        try:
            target = discord.utils.get(message.guild.roles, name=f"{role}") 
            if not target in message.author.roles: 
                return
            if message.author.bot:
                return
            else:
                embed = discord.Embed(title=f'{name}',timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x0000FF)    
                embed.add_field(name="관리 명령어", value="!핑, !공지, !채널지정, !청소, !업로더", inline=False)  
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

    if message.content.startswith("!채널지정"):
        try:
            if message.author.bot:
                return
            else:
                content = message.content[6:]
                target = discord.utils.get(message.guild.roles, name=f"{role}") 
                if not target in message.author.roles: 
                    return
                try:
                    file = open(f'notice.txt', 'r')
                    noticeid = file.read()
                    if noticeid == content:
                        embed3 = discord.Embed(title=f'{name} 채널 지정', description=f'이미 지정된 채널입니다.', color=0xFF0000)
                        return await message.channel.send(embed=embed3)                           
                    embed3 = discord.Embed(title=f'{name} 채널 지정', description=f'이미 지정된 채널은 {noticeid}입니다. {content}로 채널을 지정을 변경 하시겠습니까 ? [네/아니요]\n30초 안으로 보내주세요.', color=0x0000FF)
                    await message.channel.send(embed=embed3)          

                    def check(msg):
                        return msg.author == message.author and msg.channel == message.channel 

                    try:
                        msg = await client.wait_for("message", timeout=30, check=check) 
                    except:
                        embed3 = discord.Embed(title=f'{name} 채널 지정', description=f'30초 초과로 인하여 채널지정이 취소 되었습니다.', color=0xFF0000)
                        return await message.channel.send(embed=embed3)   
                    if msg.content == "아니요":
                        embed3 = discord.Embed(title=f'{name} 채널 지정', description=f'채널 지정이 취소 되었습니다.', color=0xFF0000)
                        return await message.channel.send(embed=embed3)   
                    else:
                        if msg.content == "네":
                            filename = f"notice.txt"
                            with open(filename, "w") as file:
                                file.write(f"{content}")
                                embed = discord.Embed(title=f'{name} 채널 지정', description=f'채널이 지정되었습니다.\n지정된 채널: {content}', timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x0000FF)    
                                embed.set_footer(text=footer)
                                embed.set_thumbnail(url=icon)  
                                return await message.channel.send(embed=embed)                               
                        else:
                            embed3 = discord.Embed(title=f'{name} 채널 지정', description=f'네/아니요를 보내주세요. 채널 지정이 취소되었습니다.', color=0xFF0000)
                            return await message.channel.send(embed=embed3)   
                except:
                    embed3 = discord.Embed(title=f'{name} 채널 지정', description=f'현재 지정된 채널이 없습니다. {content}로 채널을 지정 하시겠습니까 ? [네/아니요]\n30초 안으로 보내주세요.', color=0x0000FF)
                    await message.channel.send(embed=embed3)          

                    def check(msg):
                        return msg.author == message.author and msg.channel == message.channel 

                    try:
                        msg = await client.wait_for("message", timeout=30, check=check) 
                    except:
                        embed3 = discord.Embed(title=f'{name} 채널 지정', description=f'30초 초과로 인하여 채널지정이 취소 되었습니다.', color=0xFF0000)
                        return await message.channel.send(embed=embed3)   
                    if msg.content == "아니요":
                        embed3 = discord.Embed(title=f'{name} 채널 지정', description=f'채널 지정이 취소 되었습니다.', color=0xFF0000)
                        return await message.channel.send(embed=embed3)   
                    else:
                        if msg.content == "네":
                            filename = f"notice.txt"
                            with open(filename, "w") as file:
                                file.write(f"{content}")
                                embed = discord.Embed(title=f'{name} 채널 지정', description=f'채널이 지정되었습니다.\n지정된 채널: {content}', timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x0000FF)    
                                embed.set_footer(text=footer)
                                embed.set_thumbnail(url=icon)  
                                return await message.channel.send(embed=embed)                               
                        else:
                            embed3 = discord.Embed(title=f'{name} 채널 지정', description=f'네/아니요를 보내주세요. 채널 지정이 취소되었습니다.', color=0xFF0000)
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

    if message.content.startswith("!공지"):
        try:               
            target = discord.utils.get(message.guild.roles, name=f"{role}") 
            if not target in message.author.roles: 
                return
            if message.author.bot:
                return
            else:
                try:
                    content = message.content[4:]
                except:
                    embed3 = discord.Embed(title=f'{name}', description=f'공지할 내용을 제대로 다시 보내주세요.', color=0xFF0000)
                    return await message.channel.send(embed=embed3)   
                try:
                    file = open(f'notice.txt', 'r')
                    noticeid = file.read() 
                except:
                    embed3 = discord.Embed(title=f'{name} NOTICE', description=f'현재 지정된 채널이 없습니다.\n!채널지정 [지정할 채널 아이디]를 먼저 이용해주세요.', color=0x0000FF)
                    return await message.channel.send(embed=embed3)          
                embed3 = discord.Embed(title=f'{name} NOTICE', description=f'현재 지정된 채널은 {noticeid}입니다. 에브리원을 활성화 할까요 ? [네/아니요/취소]', color=0x0000FF)
                await message.channel.send(embed=embed3)          

                def check(msg):
                    return msg.author == message.author and msg.channel == message.channel 

                try:
                    msg = await client.wait_for("message", timeout=30, check=check) 
                except:
                    embed3 = discord.Embed(title=f'{name} NOTICE', description=f'30초 초과로 인하여 공지가 초기화 되었습니다.', color=0xFF0000)
                    return await message.channel.send(embed=embed3)   
                if msg.content == "아니요":
                    channel = client.get_channel(int(noticeid)) 
                    embed = discord.Embed(title=f'{name} NOTICE', description=f'{content}', timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x0000FF)    
                    embed.set_footer(text=footer)
                    embed.set_thumbnail(url=icon)  
                    try:
                        return await channel.send(embed=embed)  
                    except:
                        embed3 = discord.Embed(title=f'{name} NOTICE', description=f'지정된 채널 아이디에 문제가 있습니다. 다시 확인해주세요.', color=0xFF0000)
                        return await message.channel.send(embed=embed3)   
                else:             
                    if msg.content == "네":                          
                        channel = client.get_channel(int(noticeid)) 
                        embed = discord.Embed(title=f'{name} NOTICE', description=f'{content}', timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x0000FF)    
                        embed.set_footer(text=footer)
                        embed.set_thumbnail(url=icon)  
                        try:
                            return await channel.send(f"@everyone" ,embed=embed)   
                        except:
                            embed3 = discord.Embed(title=f'{name} NOTICE', description=f'지정된 채널 아이디에 문제가 있습니다. 다시 확인해주세요.', color=0xFF0000)
                            return await message.channel.send(embed=embed3)   
                    else:
                        if msg.content == "취소":
                            embed3 = discord.Embed(title=f'{name} NOTICE', description=f'공지가 취소 되었습니다.', color=0xFF0000)
                            return await message.channel.send(embed=embed3)   
                        else:
                            embed3 = discord.Embed(title=f'{name} NOTICE', description=f'네/아니요/취소를 보내주세요. 공지가 취소 되었습니다.', color=0xFF0000)
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
            target = discord.utils.get(message.guild.roles, name=f"{role2}") 
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

    if message.guild is None:   
        if message.author.bot:
            return
        else:
            try:
                file = open(f'{message.author.id}.txt', 'r')
                sodyd = file.read()
            except:
                #######################채널 생성#########################
                cat = client.get_channel(int(Categories))

                category = discord.utils.get(cat.guild.categories, id=int(Categories))

                channel = await cat.guild.create_text_channel(f"{message.author}ㅣ{message.author.id}", category=category)
                #######################채널 생성#########################
                    
                ########################문의자에게 안내매세지 전송#########################
                embed = discord.Embed(timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x0000FF)    
                embed.add_field(name=f"{name} 문의 센터", value=f"안녕하세요 {name}입니다. 문의센터를 이용해주셔서 감사합니다. 매세지가 전송 되었으니 기다려 주시면 감사하겠습니다.", inline=False)  
                embed.set_footer(text=footer)
                embed.set_thumbnail(url=icon)  
                await message.author.send(embed=embed) 
                #######################문의자에게 안내매세지 전송#########################

                #########################생성된 채널에 매세지전송#########################
                embed = discord.Embed(title=f'{name} 문의 센터', description=f'새로운 문의가 도착하였습니다.', timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x0000FF)    
                embed.add_field(name="사용자", value=message.author, inline=False)    
                embed.add_field(name="사용자 아이디", value=message.author.id, inline=False)  
                embed.add_field(name="문의 내용", value=message.content, inline=False)      
                embed.add_field(name="문의 정보", value=f"{message.channel.id}ㅣ{channel.id}", inline=False)      
                embed.set_footer(text=footer)
                embed.set_thumbnail(url=icon)  
                await channel.send(embed=embed)        
                ########################생성된 채널에 매세지전송#########################

                #########################txt생성#########################
                filename = f"{message.author.id}.txt"
                with open(filename, "w") as file:
                    file.write(f"{channel.id}")      
                filename = f"{channel.id}.txt"
                with open(filename, "w") as file:
                    file.write(f"{message.channel.id}") 
                filename = f"{channel.id}ㅣ2.txt"
                with open(filename, "w") as file:
                    file.write(f"{message.author.id}")  
                return   
                #########################txt생성#########################    

            #########################생성된 채널에 매세지전송#########################
            dm = client.get_channel(int(sodyd))    
            embed = discord.Embed(title=f'{name} 문의 센터', timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x0000FF)    
            embed.add_field(name="문의 내용", value=message.content, inline=False)      
            embed.set_footer(text=footer)
            embed.set_thumbnail(url=icon)  
            await dm.send(embed=embed)   
            return     
            #########################생성된 채널에 매세지전송#########################      

    if message.content.startswith("!문의종료"):
        if message.author.bot:
            return
        else:
            #########################txt확인#########################
            try:
                file = open(f'{message.channel.id}.txt', 'r')
                sodyd = file.read()
            except Exception:
                return None

            try:
                file = open(f'{message.channel.id}ㅣ2.txt', 'r')
                dkdk = file.read()
            except Exception:
                return None
            #########################txt확인#########################

            #########################문의센터 안내#########################
            channel = client.get_channel(int(sodyd))

            embed = discord.Embed(title=f'{name} 문의 센터', timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x0000FF)    
            embed.add_field(name="안내사항", value="잠시후 문의가 종료되며, 채널이 제거 됩니다.", inline=False)      
            embed.set_footer(text=footer)
            embed.set_thumbnail(url=icon)  
            await message.channel.send(embed=embed)

            embed = discord.Embed(title=f'{name} 문의 센터', timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x0000FF)    
            embed.add_field(name="안내사항", value=f"안녕하세요 {name}입니다. 담당 관리자가 현재 사용자의 문의를 종료하였습니다. 매세지를 다시 보내면 새로운 문의가 생성되니 심중히 보내주세요 !", inline=False)      
            embed.set_footer(text=footer)
            embed.set_thumbnail(url=icon)  
            await channel.send(embed=embed)     
            #########################문의센터 안내#########################

            #########################모든 설정 제거#########################
            file.close() # file 제거

            hh = client.get_channel(int(message.channel.id))
            try:
                await hh.delete() #채널 제거
            except:    
                pass
                return None   
            filename = f"{dkdk}.txt"
            filename2 = f"{message.channel.id}.txt"
            filename3 = f"{message.channel.id}ㅣ2.txt"
            os.remove(filename) #txt 제거
            os.remove(filename2) #txt 제거 
            os.remove(filename3) #txt 제거 
            #########################모든 설정 제거#########################             

    if message.content.startswith(""):
        if message.author.bot:
            return
        else:
            content = message.content # 보낸 매세지 확인
            #########################txt확인#########################
            try:
                file = open(f'{message.channel.id}.txt', 'r')
                sodyd = file.read()
            except Exception as e:
                return None   
            #########################txt확인#########################
            channel = client.get_channel(int(sodyd))

            embed = discord.Embed(title=f'{name} 문의 센터', timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x0000FF)    
            embed.add_field(name="문의 센터 답장", value=f"{content}", inline=False)      
            embed.set_footer(text=footer)
            embed.set_thumbnail(url=icon)  
            try:
                await channel.send(embed=embed)
            except:
                return await message.add_reaction("⛔")
            await message.add_reaction("✅")



client.run(token) # token 


