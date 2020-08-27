from flask import abort, render_template, current_app, request, redirect, url_for
from random import randrange
from quiz import Quiz 
from answer import Answer
from data import Data
from question import Question
from filmdata import TopMovies
from random import randrange
import random
#import level_one_questions


def home_page():
    score_data = current_app.config["score_data"]
    score_data.reconstitute()
    return render_template("home.html")

def questions_page():
    score_data = current_app.config["score_data"]

    film_question = Question()
    #quiz = Quiz()
    question = score_data.get_question() 
    if score_data.get_flag():

        if score_data.get_length_answer()>0:
            score_data.delete_all_answers()

        
        ##select question randomly according to level
        if score_data.get_level()==1:
            film_question.level_one(score_data.get_top_imdb(),score_data.get_moviesdb())
        elif score_data.get_level()==2:
            rand_arr = random.sample(range(0,2),1)
            if rand_arr[0] == 0:
                film_question.level_two(score_data.get_top_imdb(),score_data.get_moviesdb())
            else:
                film_question.level_two_three(score_data.get_top_imdb(),score_data.get_moviesdb())
        else:
            rand_arr = random.sample(range(0,2),1)
            if rand_arr[0] == 0:
                film_question.level_three(score_data.get_top_imdb(),score_data.get_moviesdb())
            else:
                film_question.level_two_three(score_data.get_top_imdb(),score_data.get_moviesdb())       

        temp_arr = []  ##temp array to hold answers before setting selections randomly  
        temp_arr.append(Answer(film_question.get_answer_true(),True))
        for i in range(film_question.get_length_false()):
            temp_arr.append(Answer(film_question.get_answer_false(i),False))
        
        rand_arr = random.sample(range(0,film_question.get_length_false()+1),film_question.get_length_false()+1)

        
        for i in range(film_question.get_length_false()+1):        
            score_data.add_answer(temp_arr[rand_arr[i]])
        
        
        

        score_data.set_question(film_question.get_question())
        question = score_data.get_question()

        score_data.update_question_number()
        score_data.update_flag()
    else:
        score_data.update_flag()
    
    

    

    answers = score_data.get_answers()
    if request.method=="GET":           
        return render_template("questions.html",answers=answers,question=question,score_data=score_data)
    else:
        gamer_answer_keys = request.form.getlist("answer_keys")
        for gamer_answer_key in gamer_answer_keys:
            last_answer = score_data.get_answer(int(gamer_answer_key)) 
        if last_answer.answerisTrue():   ##if answer is true, update score and upgrade level per 30 points and also if competitor has less than 3 hearth then give one more hearth 
            score_data.update_score()
            if score_data.get_score()%30 == 0 and score_data.get_score() > 0:
                score_data.update_level()
                if score_data.get_hearth()<3:
                    score_data.increase_hearth()
                return render_template("levelup.html",score_data=score_data)
            if score_data.get_score()%30 == 20 and score_data.get_score() > 0:
                return render_template("beforelevup.html",score_data=score_data)
            else:
                return render_template("trueanswer.html",score_data=score_data)
        else:                              ##if answer is false, decrease hearth of competitor and if there is no hearth after this operation, end the game
            score_data.decrease_hearth()  
            if(score_data.get_hearth()>0):
                return render_template("wronganswer.html",answers=answers,score_data=score_data)
            if(score_data.get_hearth()==0):                                
                return render_template("scorepage.html",score_data=score_data)        
        return redirect(url_for("questions_page"))

def score_page():
    score_data = current_app.config["score_data"]
    return render_template("scorepage.html",score_data=score_data)

def level_up_page():
    score_data = current_app.config["score_data"]
    return render_template("levelup.html",score_data=score_data)

def before_level_up_page():
    score_data = current_app.config["score_data"]
    return render_template("beforelevup.html",score_data=score_data)

def wrong_answer_page():
    score_data = current_app.config["score_data"]
    return render_template("wronganswer.html",answers=answers,score_data=score_data)

def true_answer_page():
    score_data = current_app.config["score_data"]
    return render_template("trueanswer.html",score_data=score_data)