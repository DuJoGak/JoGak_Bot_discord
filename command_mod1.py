import discord

def command_list_print():
    embed=discord.Embed(title="명령어 리스트",description="""
    ==>데스티니 : 개똥겜
    ==>시즈 : 개갓겜
    ==>calculate (계산할것) : 사칙연산
    ==>박준성 : 마빵 사진
    ==>사전검색 (단어): 사전검색
    ==>마빵티콘:마빵 이모티콘
    ==>소인수분해 (수):(수)를 소인수분해""",color=0x00ff00)
    embed.set_footer(text="뭐요 어쩌라구요")
    return embed