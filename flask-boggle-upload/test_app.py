from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle

testing_board = [
                ["M", "O", "T", "L", "M",],
                ["N", "E", "W", "C", "E",],
                ["O", "R", "P", "K", "H",],
                ["C", "J", "M", "W", "U",],
                ["N", "S", "Z", "K", "X",]
]
game_start = Boggle()


class BoggleTestCase(TestCase):
    # def setUp(self):
    #     app.config["TESTING"] = True;
    #     app.config["DEBUG"] = False

    # test root route
    def test_home(self):
        """  test root route and session initializintion   """
        with app.test_client() as client:
            response = client.get('/')
            
            session["board"] = testing_board
            self.assertEqual(response.status_code, 200)
            self.assertEqual(session["top_score "],  0)
            self.assertEqual(session["game_count"],  0)
            self.assertEqual(session["board"], testing_board)

    def test_words(self):
        """ testing check-word route against testing board  """
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session["board"] = testing_board
                # test a valid word on board
            response = client.get('/check-word?word=term')
            result = response.get_json()
            self.assertEqual(response.json["result"], "ok")
            # test a valid word not on board
            response = client.get('/check-word?word=right')
            result = response.get_json()
            self.assertEqual(response.json["result"], "not-on-board")
            
            # test a non-valid word
            response = client.get('/check-word?word=mzwk')
            result = response.get_json()
            self.assertEqual(response.json["result"], "not-word")

    def test_updates(self):
        with app.test_client() as client:
            # import pdb
            # pdb.set_trace()
            with client.session_transaction() as change_session:
                change_session["top_score "] = 97
                change_session["game_count"] = 108
            response = client.post("/update-HighScore", json={"score": 55})
            result = response.get_json()
            self.assertEqual(response.status_code, 201)
            # high_score & game_count is greater
            self.assertGreater(result["top_score "], 9)
            self.assertGreater(result["next_game"], 17)
            # high_score & game_count is less
            self.assertLess(result["top_score "], 42)
            self.assertLess(result["next_game"], 3)
