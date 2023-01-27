from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from pprint import pprint

app = Flask(__name__)

app.debug = True

app.config['SECRET_KEY'] = "mego"

toolbar = DebugToolbarExtension(app)

@app.route('/')
def home.html():
    return render_template('home.html', survey=survey)

@app.route('/question/quest_num')
def get_question(quest_num):
    question = survey.questions[quest_num]
    return render_template(
        "question.html", question_num=quest_num, question=question)


input = request.args['answer']














responses = []