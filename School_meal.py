import requests
from bs4 import BeautifulSoup as bs
import re
import datetime

def school_meal(dtime):
    dtime=int(dtime)
    dt=datetime.datetime.now()
    day=datetime.datetime.strftime(dt,'%Y%m')
    r=requests.get('https://stu.ice.go.kr/sts_sci_md00_001.do?schulCode=E100000262&schulCrseScCode=4&schulKndScCode=4&schYm='+str(day)+'&')
    soup=bs(r.text,"html.parser")
    all_tbodys=soup.find_all("tbody")
    meals=str(all_tbodys)
    meals=meals.replace("<tbody>","")
    meals=meals.replace("<td class=""last"">","")
    meals=meals.replace("<td>","")
    meals=meals.replace("</td>","")
    meals=meals.replace("<tr>","")
    meals=meals.replace("</tr>","")
    meals=meals.replace("</div>","")
    meals=meals.replace('<td class="last">',"")
    meals=meals.replace("<br/>","\n")
    meals=meals.replace(str(dtime),str(day)+str(dtime))
    meals=meals.split("<div>")    
    return meals[dtime+5]
