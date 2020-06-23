from flask import abort, render_template, current_app, request, redirect, url_for
from random import randrange
from quiz import Quiz 
from answer import Answer
from data import Data
from question import Question
from filmdata import TopMovies
from random import randrange
import random

def home_page():
    score_data = current_app.config["score_data"]
    score_data.reconstitute()
    return render_template("home.html")

def questions_page():
    score_data = current_app.config["score_data"]

    film_question = Question()
    quiz = Quiz()
    question = quiz.get_question()
    if score_data.get_flag():

        random_question = -1
        if score_data.get_level()==1:
            rand_arr = random.sample(range(0,2),1)
            random_question = rand_arr[0]
        elif score_data.get_level()==2:
            rand_arr = random.sample(range(2,5),1)
            random_question = rand_arr[0]
        else:
            rand_arr = random.sample(range(5,7),1)
            random_question = rand_arr[0]
        
        if random_question == 0:
            film_question.topMoviesYear()
        elif random_question == 1:
            film_question.topMoviesDirectors()
        elif random_question == 2:
            film_question.topMoviesCast()
        elif random_question == 3:
            film_question.topMoviesRole()
        elif random_question == 4:
            film_question.topMoviesActor()
        elif random_question == 5:
            film_question.topMoviesActorMovie() 
        elif random_question == 6:
            film_question.topMoviesCastOne()
        quiz.set_question(film_question.get_question())
        question = quiz.get_question()
        score_data.update_random(randrange(24))
        score_data.update_flag()
    else:
        score_data.update_flag()
    print(score_data.get_random())
    if score_data.get_random() == 0:
        quiz.add_answer(Answer(film_question.get_answer_one(),True))
        quiz.add_answer(Answer(film_question.get_answer_two(),False))
        quiz.add_answer(Answer(film_question.get_answer_three(),False))
        quiz.add_answer(Answer(film_question.get_answer_four(),False)) 
    elif score_data.get_random() == 1:
        quiz.add_answer(Answer(film_question.get_answer_one(),True))
        quiz.add_answer(Answer(film_question.get_answer_two(),False))
        quiz.add_answer(Answer(film_question.get_answer_four(),False))
        quiz.add_answer(Answer(film_question.get_answer_three(),False))
    elif score_data.get_random() == 2:
        quiz.add_answer(Answer(film_question.get_answer_one(),True))
        quiz.add_answer(Answer(film_question.get_answer_three(),False))
        quiz.add_answer(Answer(film_question.get_answer_two(),False))
        quiz.add_answer(Answer(film_question.get_answer_four(),False))
    elif score_data.get_random() == 3:
        quiz.add_answer(Answer(film_question.get_answer_one(),True))
        quiz.add_answer(Answer(film_question.get_answer_three(),False))
        quiz.add_answer(Answer(film_question.get_answer_four(),False))
        quiz.add_answer(Answer(film_question.get_answer_two(),False))
    elif score_data.get_random() == 4:
        quiz.add_answer(Answer(film_question.get_answer_one(),True))
        quiz.add_answer(Answer(film_question.get_answer_four(),False))
        quiz.add_answer(Answer(film_question.get_answer_three(),False))
        quiz.add_answer(Answer(film_question.get_answer_two(),False))
    elif score_data.get_random() == 5:
        quiz.add_answer(Answer(film_question.get_answer_one(),True))
        quiz.add_answer(Answer(film_question.get_answer_four(),False))
        quiz.add_answer(Answer(film_question.get_answer_two(),False))
        quiz.add_answer(Answer(film_question.get_answer_three(),False))
    elif score_data.get_random() == 6:
        quiz.add_answer(Answer(film_question.get_answer_two(),False))
        quiz.add_answer(Answer(film_question.get_answer_one(),True))
        quiz.add_answer(Answer(film_question.get_answer_three(),False))
        quiz.add_answer(Answer(film_question.get_answer_four(),False))
    elif score_data.get_random() == 7:
        quiz.add_answer(Answer(film_question.get_answer_two(),False))
        quiz.add_answer(Answer(film_question.get_answer_one(),True))
        quiz.add_answer(Answer(film_question.get_answer_four(),False))
        quiz.add_answer(Answer(film_question.get_answer_three(),False))
    elif score_data.get_random() == 8:
        quiz.add_answer(Answer(film_question.get_answer_two(),False))
        quiz.add_answer(Answer(film_question.get_answer_three(),False))
        quiz.add_answer(Answer(film_question.get_answer_four(),False))
        quiz.add_answer(Answer(film_question.get_answer_one(),True))
    elif score_data.get_random() == 9:
        quiz.add_answer(Answer(film_question.get_answer_two(),False))
        quiz.add_answer(Answer(film_question.get_answer_three(),False))
        quiz.add_answer(Answer(film_question.get_answer_one(),True))
        quiz.add_answer(Answer(film_question.get_answer_four(),False))
    elif score_data.get_random() == 10:
        quiz.add_answer(Answer(film_question.get_answer_two(),False))
        quiz.add_answer(Answer(film_question.get_answer_four(),False))
        quiz.add_answer(Answer(film_question.get_answer_one(),True))
        quiz.add_answer(Answer(film_question.get_answer_three(),False))
    elif score_data.get_random() == 11:
        quiz.add_answer(Answer(film_question.get_answer_two(),False))
        quiz.add_answer(Answer(film_question.get_answer_four(),False))
        quiz.add_answer(Answer(film_question.get_answer_three(),False))
        quiz.add_answer(Answer(film_question.get_answer_one(),True))
    elif score_data.get_random() == 12:
        quiz.add_answer(Answer(film_question.get_answer_three(),False))
        quiz.add_answer(Answer(film_question.get_answer_one(),True))
        quiz.add_answer(Answer(film_question.get_answer_four(),False))
        quiz.add_answer(Answer(film_question.get_answer_two(),False))
    elif score_data.get_random() == 13:
        quiz.add_answer(Answer(film_question.get_answer_three(),False))
        quiz.add_answer(Answer(film_question.get_answer_one(),True))
        quiz.add_answer(Answer(film_question.get_answer_two(),False))
        quiz.add_answer(Answer(film_question.get_answer_four(),False))
    elif score_data.get_random() == 14:
        quiz.add_answer(Answer(film_question.get_answer_three(),False))
        quiz.add_answer(Answer(film_question.get_answer_four(),False))
        quiz.add_answer(Answer(film_question.get_answer_one(),True))
        quiz.add_answer(Answer(film_question.get_answer_two(),False))
    elif score_data.get_random() == 15:
        quiz.add_answer(Answer(film_question.get_answer_three(),False))
        quiz.add_answer(Answer(film_question.get_answer_four(),False))
        quiz.add_answer(Answer(film_question.get_answer_two(),False))
        quiz.add_answer(Answer(film_question.get_answer_one(),True))
    elif score_data.get_random() == 16:
        quiz.add_answer(Answer(film_question.get_answer_three(),False))
        quiz.add_answer(Answer(film_question.get_answer_two(),False))
        quiz.add_answer(Answer(film_question.get_answer_four(),False))
        quiz.add_answer(Answer(film_question.get_answer_one(),True))
    elif score_data.get_random() == 17:
        quiz.add_answer(Answer(film_question.get_answer_three(),False))
        quiz.add_answer(Answer(film_question.get_answer_two(),False))
        quiz.add_answer(Answer(film_question.get_answer_one(),True))
        quiz.add_answer(Answer(film_question.get_answer_four(),False))
    elif score_data.get_random() == 18:
        quiz.add_answer(Answer(film_question.get_answer_four(),False))
        quiz.add_answer(Answer(film_question.get_answer_one(),True))
        quiz.add_answer(Answer(film_question.get_answer_three(),False))
        quiz.add_answer(Answer(film_question.get_answer_two(),False))
    elif score_data.get_random() == 19:
        quiz.add_answer(Answer(film_question.get_answer_four(),False))
        quiz.add_answer(Answer(film_question.get_answer_one(),True))
        quiz.add_answer(Answer(film_question.get_answer_two(),False))
        quiz.add_answer(Answer(film_question.get_answer_three(),False))
    elif score_data.get_random() == 20:
        quiz.add_answer(Answer(film_question.get_answer_four(),False))
        quiz.add_answer(Answer(film_question.get_answer_two(),False))
        quiz.add_answer(Answer(film_question.get_answer_three(),False))
        quiz.add_answer(Answer(film_question.get_answer_one(),True))
    elif score_data.get_random() == 21:
        quiz.add_answer(Answer(film_question.get_answer_four(),False))
        quiz.add_answer(Answer(film_question.get_answer_two(),False))
        quiz.add_answer(Answer(film_question.get_answer_one(),True))
        quiz.add_answer(Answer(film_question.get_answer_three(),False))
    elif score_data.get_random() == 22:
        quiz.add_answer(Answer(film_question.get_answer_four(),False))
        quiz.add_answer(Answer(film_question.get_answer_three(),False))
        quiz.add_answer(Answer(film_question.get_answer_one(),True))
        quiz.add_answer(Answer(film_question.get_answer_two(),False))
    elif score_data.get_random() == 23:
        quiz.add_answer(Answer(film_question.get_answer_four(),False))
        quiz.add_answer(Answer(film_question.get_answer_three(),False))
        quiz.add_answer(Answer(film_question.get_answer_two(),False))
        quiz.add_answer(Answer(film_question.get_answer_one(),True))

    answers = quiz.get_answers() 
    if request.method=="GET":           
        return render_template("questions.html",answers=answers,question=question,score_data=score_data)
    else:
        gamer_answer_keys = request.form.getlist("answer_keys")
        for gamer_answer_key in gamer_answer_keys:
            last_answer = quiz.get_answer(int(gamer_answer_key)) 
        if last_answer.answerisTrue():
            score_data.update_score()
            if score_data.get_score()%30 == 0 and score_data.get_score() > 0:
                score_data.update_level()
                if score_data.get_hearth()<3:
                    score_data.increase_hearth()
        else:
            score_data.decrease_hearth()  
            if(score_data.get_hearth()==0):                                
                return render_template("scorepage.html",score_data=score_data)
        return redirect(url_for("questions_page"))

def score_page():
    score_data = current_app.config["score_data"]
    return render_template("scorepage.html",score_data=score_data)