from asyncore import poll
from bs4 import BeautifulSoup
import requests

def poll_crawler(page_num:int):
    """
    여론조사심의위원회 - 여론조사결과 등록현황 페이지에서 
    """
    for page in range(page_num):
        page += 1 
        url = "https://www.nesdc.go.kr/portal/bbs/B0000005/list.do?menuNo=200467&searchTime=&sdate=&edate=&pdate=&pollGubuncd=&searchCnd=&searchWrd=&pageIndex={}".format(page)
        r = requests.get(url)
        data = r.text 
        soup = BeautifulSoup(data, "html5lib")
        bd_list = soup.find("div", "bd_list") # 지정한 문서 영역 파싱 
        return bd_list 

    
print(poll_crawler(5))