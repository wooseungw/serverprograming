from flask import Flask, render_template, redirect, request

app = Flask(__name__)
cities = ["부산", "용인"]

@app.route('/')
def weather():
    # 메인화면    
    return render_template("weather.html", cities=cities)
#추가 기능
@app.route('/add')
def add():
    city = request.args.get("city", "서울")
    cities.append(city)
    return redirect("/")

# 삭제 기능
@app.route('/del')
def delete():
    city = request.args.get("city", "서울")
    cities.remove(city)
    return redirect("/")

if __name__ == '__main__':
      app.run(port=3000, debug=True)
