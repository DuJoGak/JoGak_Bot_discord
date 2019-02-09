import discord

def matbread_help():
    embed=discord.Embed(title="마빵티콘 종류",description="""
        alphago = 미쳤습니까 휴먼?
        baldman = 빡빡머리 아저씨
        bty     = 변태야
        cowupper= 소름
        hate_1  = ㅈㄴ싫어
        hate_2  = 개시러
        itachi  = 탈주(별)
        lol     = ㅎ...
        love    = 사랑해
        Nofuture= 미래가 없어
        Question= ?????
        shipduck= 나도 쉽덕노래 들을래
        ttat    = 퉷
        youguys = 이놈시끼들
    """)
    
    embed.set_footer(text="==>마빵티콘 (이모지 이름) 으로 출력할수 있어요")
    return embed

def matbread_select(word):
    if word=="alphago":
        return "7icaaJS"
    elif word=="baldman":
        return "bkFPuof"
    elif word=="bty":
        return "zSl24o5"
    elif word=="cowupper":
        return "rGjj5Kh"
    elif word=="hate_1":
        return "3cqQQJg"
    elif word=="hate_2":
        return "a7tuQ7H"
    elif word=="itachi":
        return "5TlDWET"
    elif word=="lol":
        return "WJ4hLmo"
    elif word=="love":
        return "bT3Lg5G"
    elif word=="Nofuture":
        return "YAtEuQ6"
    elif word=="Question":
        return "9ELdEIC"
    elif word=="shipduck":
        return "eucaFHv"
    elif word=="sunggi":
        return "ylhDqVx"
    elif word=="ttat":
        return "mdCEeu4"
    elif word=="youguys":
        return "mXqyiNF"