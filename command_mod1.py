import discord

def command_list_print():
    embed=discord.Embed(title="명령어 리스트",description="""
    ==>calculate (계산할것) : 사칙연산
    ==>사전검색 (단어): 사전검색
    ==>소인수분해 (수):(수)를 소인수분해
    ==>인남급식 : 이번주 인천남고 급식을 표시합니다. """,color=0x00ff00)
    embed.set_footer(text="뭐요 어쩌라구요")
    return embed