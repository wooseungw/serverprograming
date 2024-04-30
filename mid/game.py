from flask import Flask, render_template
app = Flask(__name__)

@app.route('/form')
def form():
    questions = ['name','age','email','phone']
    return render_template('form.html',questions=questions)

app.run(debug=True)