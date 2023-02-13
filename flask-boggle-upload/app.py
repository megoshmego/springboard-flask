from boggle import Boggle
from flask import Flask, request, render_template, jsonify, session
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# DebugToolbar
app.debug = True
app.config['SECRET_KEY'] = 'megoshmego'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)


# instantiate game class
game_start = Boggle()


# set a route to render the main html page and set the session


@app.route('/')
def root():
    """ initialize session and render main page """
    board = game_start.make_board()
    session['board'] = board
    if 'game_count' not in session:
        session["top_score"] = 0
        session["game_count"] =0
    return render_template("board.html", board=board, top_score=session["top_score"], game_count=session["game_count"])


# set up a route to handle the request for guessing a game!
@app.route('/check-word')
def check_word():
    # board = session['board']
    word = request.args["word"]
    valid_word = game_start.check_valid_word(session['board'], word)
    return jsonify({"result": valid_word})


@app.route('/update-HighScore', methods=["POST"])
def post_score():
    score = request.json["score"]
    session["top_score"] = max(session["top_score"], score)
    session['game_count'] = session["game_count"] + 1
    result = {"top_score": session["top_score"], "games_played": session["game_count"]}
    response = jsonify(result)
    response.status_code = 201
    return response
    
