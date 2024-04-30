from fastapi import FastAPI
from bs4 import BeautifulSoup
import urllib

app = FastAPI()

@app.get("/api/weather")
def weather(city : str = ""):
    url = "https://search.naver.com/search.naver?&query="
    url = url + urllib.parse.quote_plus(city + "날씨")    
    print(url)
    soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")

    temperature = soup.select("div.temperature_text > strong")
    info = soup.select("div.temperature_info > p")
    sensor = soup.select("div.temperature_info > dl")    
    return {"temperature":temperature[0].text, "info":info[0].text, "sensor": sensor[0].text}
    
    
