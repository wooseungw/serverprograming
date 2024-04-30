from fastapi import FastAPI
from bs4 import BeautifulSoup
from urllib import request, parse

app = FastAPI()

@app.get("/api/weather")
def weather(city : str = ""):
    # 네이버 url에서 날씨 정보 가져오기
    url = "https://search.naver.com/search.naver?&query="
    # 네이버 주소 뒤에 검색어를 붙여서 검색
    url = url + parse.quote_plus(city + "날씨")    
    # 네이버 날씨 페이지를 읽기, 저장
    soup = BeautifulSoup(request.urlopen(url).read(), "html.parser")
    # 온도, 날씨 정보, 센서 정보 가져오기
    temperature = soup.select("div.temperature_text > strong")
    info = soup.select("div.temperature_info > p")
    sensor = soup.select("div.temperature_info > dl")    
    return {"temperature":temperature[0].text, "info":info[0].text, "sensor": sensor[0].text}