from flask import Flask, request, render_template
from random import choice, randint
from flask_debugtoolbar import DebugToolbarExtension
app = Flask(__name__)


app.config['SECRET_KEY'] = "mego"
debug = DebugToolbarExtension(app)

@app.route('/')
def home():
    return "Hello there!"
if __name__ == '__main__':
    app.run(debug=True)
    
@app.route('/jinja')
def say_jinja():
    return render_template("jinja.html")

@app.route('/form')
def show_form():
    return render_template("form.html")


COMPLIMENTS = ["COOL", "CLEVER", "TENACIOUS", "PYTHONIC", "AWESOME"]

@app.route('/greet')
def get_greeting():   #make sure to put this in the route you want to send this to, see form.html ln 11
    username = request.args["username"]
    nice_thing = choice(COMPLIMENTS)
    return render_template("greet.html", username=username, compliments=nice_thing)

@app.route('/lucky')
def lucky_number():
    num = randint(1, 10)
    return render_template('lucky.html', lucky_num=num, msg="You are so lucky!")

@app.route('/spell/<word>')
def spell_word(word):
    caps_word = word.upper()
    return render_template("spellword.html", word=caps_word)