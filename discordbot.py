import discord



client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("샤방샤방")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("별나비 안녕"):
        await message.channel.send("안녕하세영~")

    if message.content.startswith("별나비 하이"):
        await message.channel.send("하이!!")

    if message.content.startswith("별나비 울룰루"):
        await message.channel.send("삥뽕빵")

    if message.content.startswith("별나비 잘자"):
        await message.channel.send("제 꿈 꾸세영~")

    if message.content.startswith("별나비 잘가"):
        await message.channel.send("다음에 또 뵈여ㅠㅠ")

    if message.content.startswith("별나비 빠이"):
        await message.channel.send("빠빠이~")

    if message.content.startswith("별나비 서버주소"):
        await message.channel.send("https://discord.gg/bNQd8Re")

    if message.content.startswith("별나비 FMS"):
        await message.channel.send("**2020년 4월 1일**에 시작한 서버로, **잔납**님이 오너이십니다!!")

    if message.content.startswith("별나비 뭐해"):
        await message.channel.send("그러게여...ㅎ")

    if message.content.startswith("별나비 놀자"):
        await message.channel.send("전 바쁜몸이랍니다...")

    if message.content.startswith("별나비 놀아줘"):
        await message.channel.send("전 매우 바쁜몸이에영...")

    if message.content.startswith("별나비 사랑해"):
        await message.channel.send("어머나 저런...")

    if message.content.startswith("별나비 날씨"):
        await message.channel.send("오늘의 날씨는 **맑거나 안맑거나 보통이거나!!**")

    if message.content.startswith("별나비 지건"):
        await message.channel.send("**텟카이!**")

    if message.content.startswith("똥봇"):
        await message.channel.send("힝 ㅠㅠ")

    if message.content.startswith("별나비 유튜브"):
        await message.channel.send("https://www.youtube.com/?gl=KR&hl=ko")

    if message.content.startswith("별나비 사클"):
        await message.channel.send("https://soundcloud.com/")

    if message.content.startswith("별나비 오피지지"):
        await message.channel.send("https://www.op.gg/l=ko_KR")

    if message.content.startswith("별나비 포우"):
        await message.channel.send("http://fow.kr/")

    if message.content.startswith("별나비 넷플릭스"):
        await message.channel.send("https://www.netflix.com/kr/")

    if message.content.startswith("별나비 메이플"):
        await message.channel.send("https://maplestory.nexon.com/Home/Main")

    if message.content.startswith("별나비 Gusni"):
        await message.channel.send("https://soundcloud.com/gusals924")

    if message.content.startswith("별나비 창배"):
        await message.channel.send("https://soundcloud.com/changbaehackinssa")

    if message.content.startswith("별나비 TenP"):
        await message.channel.send("https://soundcloud.com/snue0d9av8tb")

    if message.content.startswith("별나비 YoungWeeboo"):
        await message.channel.send("https://soundcloud.com/youngweeboo")

    if message.content.startswith("별나비 YoungWeeboo"):
        await message.channel.send("https://www.youtube.com/channel/UC2z2nlLCJzmGTSu9MURVapw")

    if message.content == "별나비 임베드":
        embed = discord.Embed(title="메인 제목", description="설명", color=0xffff9c)
        embed.set_footer(text="하단 설명")
        await message.channel.send("할 말", embed=embed)

    if message.content == "별나비 명령어":
        embed = discord.Embed(title=":star: 별나비봇 명령어 :star:", description="명령어 사용법 : **별나비 + 명령어**", color=0xffff9c)
        embed.add_field(name="기본", value="`안녕`, `하이`, `잘가`, `빠이`, `잘자`, `울룰루`, `서버주소`, `FMS`, `뭐해`, `놀자`, `놀아줘`, `사랑해`, `지건`, `날씨`", inline=False)
        embed.add_field(name="사이트", value="`유튜브`, `사클`, `넷플릭스`, `오피지지`, `포우`, `메이플`", inline=False)
        embed.add_field(name="사클 및 유튜브", value="`Gusni`, `창배`, `TenP`, `YoungWeeboo`", inline=False)
        embed.set_thumbnail(url="https://i.imgur.com/UsiD3kY.png")
        embed.set_footer(text="※ 필요하신 기능이 있으시면 언제든지 말씀주세요 ※")
        await message.channel.send(embed=embed)

    if message.content.startswith("/채널메시지"):
        channel = message.content[7:25]
        msg = message.content[26:]
        await client.get_channel(int(channel)).send(msg)





client.run("NzI1MzkyNDU3ODMwODkxNjIy.XvS27Q.46_AKKwmKIgm6U-Pj29J_DIw7jU")




