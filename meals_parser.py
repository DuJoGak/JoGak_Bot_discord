import requests
from bs4 import BeautifulSoup
import datetime
import re
import PIL
from PIL import Image,ImageDraw,ImageFont,ImageTk
#import numpy as np
#import matplotlib.pyplot as plt

def find_Meals():
    dt=datetime.datetime.now()
    day=datetime.datetime.strftime(dt,'%Y.%m.%d')
    url = 'http://stu.ice.go.kr/sts_sci_md01_001.do?schulCode=E100000262&schulCrseScCode=4&schulKndScCode=04&schMmealScCode=2&schYmd='+day

    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        title=str(soup.select_one('#contents > div:nth-child(2) > table > tbody > tr:nth-child(2)'))
        title=title.replace("<tr>","")
        title = title.replace("<td class=\"textC\">", "")
        title = title.replace("<th scope=\"row\">중식</th>", "")
        title = title.replace("</td>", "")
        title = title.replace("<td class=\"textC last\"> \n</tr>", "")#띄어쓰기 때문에 이렇게 하드 코딩 제거를 해야만 함
        meals=title.split('\n')
        for i in range(len(meals)):
            meals[i]=meals[i].split('<br/>')
        for i in range(len(meals)):
            for j in range(len(meals[i])):
                meals[i][j] = re.sub(r'[0-9]+.','',meals[i][j])
        for i in range(len(meals)):
            for j in range(len(meals[i])):
                if meals[i][j]==' ':
                    meals[i].remove(' ')
            meals[i]=[x for x in meals[i] if x]
        compl_meals=[]
        for i in range(len(meals)):
            if meals[i]!=[]:
                compl_meals.append(meals[i])
        #print(compl_meals) 디버그단
    else :
        return response.status_code

    bg_img=Image.open('./img.jpg')
    selectedFont=ImageFont.truetype('./NotoSansCJKkr-Regular.otf',12)
    draw = ImageDraw.Draw(bg_img)
    #50,25px에서 시작, x+=150, y+=20
    x=55
    for i in range(len(compl_meals)):
        y = 30
        for j in range(len(compl_meals[i])):
            draw.text((x,y),compl_meals[i][j],fill=(0,0,0),font=selectedFont,align="center")
            y+=20
        x+=130

    bg_img.save("../Meals_parsed.jpg")
    return 0
    #plt.imshow(np.array(bg_img))
    #plt.show() #파싱 프리뷰 디버그용도
