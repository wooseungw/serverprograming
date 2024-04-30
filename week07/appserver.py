from flask import Flask, render_template, redirect, request
from pytube import YouTube
from moviepy.editor import *

app = Flask(__name__)

@app.route('/')
def index():
    return {'message': 'Hello, world!'}

@app.route('/graph')
def graph():    
    scores = [{"name":"홍길동", "score":[80,76, 89]},
              {"name":"이순신", "score":[90,100, 45]}
              ]
    return render_template("graph.html", scores=scores)

@app.route('/survey')
def survey():    
    surveys = ["영화의 캐스팅과 연기에 대해 어떻게 평가하시나요?", 
               "영화의 시각효과에 대한 평가는 어떠신가요",
                 "영화의 스토리와 전개 효과와 특수 가 만족스러웠나요?"]
    return render_template("survey.html", surveys=surveys)


cities = ["부산", "용인"]
urls = [    
]
@app.route('/weather')
def weather():    
    return render_template("weather.html", cities=cities)

@app.route('/weatheradd')
def weatherAdd():    
    city = request.args.get("city", "서울")
    cities.append(city)
    return redirect("/weather")

@app.route('/weatherdel')
def weatherDel():    
    city = request.args.get("city", "서울")
    cities.remove(city)
    return redirect("/weather")



@app.route('/youtube')
def youtube():    
    return render_template("youtube.html", urls=urls)


@app.route('/youtubeadd')
def youtubeAdd():    
    url = request.args.get("url", "")
    mp3 = request.args.get("mp3", "")
    yt = YouTube(url)
    stream = yt.streams.get_lowest_resolution()
    filename = yt.title[0:10].replace('"', "") + ".mp4"
    stream.download(filename='static/' + filename)
    if mp3 == "on" :        
        video = VideoFileClip('static/' + filename)
        mp3 = filename.replace(".mp4", "") + ".mp3" 
        video.audio.write_audiofile("static/" + mp3)
    urls.append({"mp4":filename, "mp3": mp3,"thumbnail":yt.thumbnail_url, "url":url, "title":yt.title, "description":yt.description, "length" : yt.length})

    return redirect("/youtube")


if __name__ == '__main__':
      app.run(port=3000, debug=True)

