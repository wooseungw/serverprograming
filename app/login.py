from flask import Flask, request, jsonify, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/loginform')
def loginform():
    html = """
        <form action="/login">
            <input type="id" name="userid" /><br>
            <input type="password" name="password" />
            <input type="submit" value="로그인">
        </form>
    """
    return html 

@app.route('/login')
def login():
    userid = request.args.get('userid','None')
    password = request.args.get('password','None')
    if userid == password:
        return "로그인 성공"
    else:
        return "로그인 실패"

app.run(port=8080, debug=True)