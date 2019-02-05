import requests
from bs4 import BeautifulSoup as bs
import re

def search_daum_dic(word):
    r=requests.get('https://alldic.daum.net/search.do?q='+word)#검색 페이지 받아오기
    soup = bs(r.text, "html.parser")#파서객체로 변환
    mr = str(soup.find("meta", {"name":"twitter:description"}))#메타 태그 찾기
    mean = re.sub('<meta content="| " name="twitter:description"/>|" name="twitter:description"/>', '', mr)
    return mean.split()