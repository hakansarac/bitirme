from flask import Flask, render_template
import views
from quiz import Quiz 
from data import Data
from random import randrange

from question import Question

def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")
    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/questions", view_func=views.questions_page, methods=["GET", "POST"])
    app.add_url_rule("/score", view_func=views.score_page)
    app.add_url_rule("/levelup", view_func=views.level_up_page)
    app.add_url_rule("/beforelevelup", view_func=views.before_level_up_page)
    app.add_url_rule("/wrong", view_func=views.wrong_answer_page)
    app.add_url_rule("/lastheart", view_func=views.last_heart_page)
    app.add_url_rule("/true", view_func=views.true_answer_page)
    score_data = Data()
    
    app.config["score_data"] = score_data
    return app



if __name__ == '__main__':
    app = create_app()
    port = app.config.get("PORT", 5000)
    app.run(host='0.0.0.0', port=port)