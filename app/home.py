from flask import Flask, request, jsonify, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def h():
    data = {"공지사항":"https://web.kangnam.ac.kr/menu/f19069e6134f8f8aa7f689a4a675e66f.do",
            "행사/안내":"https://web.kangnam.ac.kr/menu/e4058249224f49ab163131ce104214fb.do",
            "인공지능학과 공지":"https://ace.kangnam.ac.kr/menu/f3a3bfbbc5715e4180657f71177d8bcf.do?encMenuSeq=184c634d3db29e58344d70cd8f2c4d38 ",
            "ICT융합공학부 공지":"https://sae.kangnam.ac.kr/menu/e408e5e7c9f27b8c0d5eeb9e68528b48.do",
            }
    
    return "hello^^^^"

@app.route('/test')
def test():
    return "<h1>Test</h1>"

@app.route('/test2')
def test2():
    return "<h1>Test222</h1>"

@app.route('/test3/sub')
def test3sub():
    return "<h1>Testsub</h1>"

@app.route('/s5/<name>')
def s5(name):
    return "<h1>name=" + name  + "</h1>"

@app.route('/s6/<name>/<age>')
def s6(name, age):
    return "<h1>name=" + name  +  "/" + age + "</h1>"


@app.route('/image')
def image():
    return "hello!!<img src=/static/sunset.jpg width=200> "
    
    
@app.route('/banner')
def banner(): 

    data = [ 
            ["daum.jpg", "http://www.daum.net"], 
            ["naver.jpg", "http://www.naver.net"], 
            ["google.jpg", "http://www.google.com"],
            ["sunset.jpg", "http://www."] 
            ]
    
    html = "<h1>My Homepage</h1>"
    for d in data :
        html +=  f"<a href={d[1]}><img  src='/static/{d[0]}' width='100' height=70 ></a>\n"

    return html

cnt = 1
@app.route('/count')
def count():
    global cnt
    cnt += 1
    return f"count={cnt}"

@app.route('/weather')
def weather():
    cities = ['부산','서울','일산']
    html = ""
    for city in cities:
        html += f"<a href=https://search.naver.com/search.naver?query={city}+날씨>{city} 날씨</a><br>"
    return html
@app.route('/count2')
def count2():
    global cnt
    cnt += 1

    html = "count="
    for i in str(cnt) :
        html +=  "<img src=/static/" + i + ".png width=20 height=20 />"

    return html
    


@app.route('/loginform')
def loginform():
    return """
        <form action="/login" method="get" />
            <input type="text" name="userid" />
            <input type="password" name="pwd" />
            <input type="submit" value="login">
        </form>
    """

@app.route('/login')
def login():
    #userid = request.args.get("userid") 
    #userid = request.args["userid"] 
    userid = request.args.get("userid", "") 
    pwd = request.args.get("pwd") 
    if userid == pwd :  return hello(name = userid)
    return loginform()

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name = None):
    return render_template('names.html',name = name)

@app.route('/loginform2')
def loginform2():
    return """
        <form action="/login2" method="post" />
         <input type="text" name="userid" />
         <input type="password" name="pwd" />
         <input type="submit" value="login">
        </form>
    """

@app.route('/login2', methods=["POST"])
def login2():
    #userid = request.form["userid"] 
    userid = request.form.get("userid") 
    pwd = request.form["pwd"] 

    if userid == pwd :  return (hello(name = escape(userid)))
    return loginform()


if __name__ == '__main__':
      app.run(port=8080, debug=True)