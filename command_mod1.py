import discord

def command_list_print():
    embed=discord.Embed(title="명령어 리스트",description="==>데스티니 : 개똥겜 \n ==>시즈 : 개갓겜 \n==>calculate (계산할것) : 사칙연산\n박준성 : 마빵 사진\n사전검색 (단어): 사전검색\\n 마빵티콘:마빵 이모티콘",color=0x00ff00)
    embed.set_footer(text="뭐요 어쩌라구요")
    return embed