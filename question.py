from quiz import Quiz 
from answer import Answer
from imdb import IMDb
from random import randrange
import level_one_questions
import level_two_questions
import level_two_three_questions
import level_three_questions
import random

class Question:
    def __init__(self):
        self.ques = ""
        self.answer_true = ""
        self.answers_false = {}
        self._last_false_key = 0

    def add_answer_false(self, false_answer):        
        self.answers_false[self._last_false_key] = false_answer
        self._last_false_key += 1
        return self._last_false_key

    def get_length_false(self):
        return len(self.answers_false)

    def get_question(self):
        return self.ques
    
    def get_answer_true(self):
        return self.answer_true
    
    def get_answer_false(self, answer_key):
        return self.answers_false.get(answer_key)

    ##def select_question(self):
        ##level_one_questions.topMoviesYearOne()

###topMoviesYear
###level_1 question (easy) 
###there are 3 years between selections 
    def level_one(self,top,moviesDB):
        rand_arr = random.sample(range(0,3),1)
        random_question = rand_arr[0]
        if random_question == 0:
            my_arr = level_one_questions.topMoviesYearOne(top,moviesDB)
        elif random_question == 1:
            my_arr = level_one_questions.topMoviesDirectorsOne(top,moviesDB)
        elif random_question == 2:
            my_arr = level_one_questions.topMoviesActorOne(top,moviesDB)
        
        self.ques = my_arr[0]
        self.answer_true = my_arr[1]
        for i in range(2,len(my_arr)):
            self.add_answer_false(my_arr[i])
        
           


    def level_two(self,top,moviesDB):
        rand_arr = random.sample(range(0,5),1)
        random_question = rand_arr[0]
        if random_question == 0:
            my_arr = level_two_questions.topMoviesYearTwo(top,moviesDB)
        elif random_question == 1:
            my_arr = level_two_questions.topMoviesNotCastTwo(top,moviesDB)  
        elif random_question == 2:
            my_arr = level_two_questions.topMoviesRoleTwo(top,moviesDB)  
        elif random_question == 3:
            my_arr = level_two_questions.topMoviesActorMovieTwo(top,moviesDB)
        elif random_question == 4:
            my_arr = level_two_questions.topMoviesCastTwo(top,moviesDB) 

        self.ques = my_arr[0]
        self.answer_true = my_arr[1]
        for i in range(2,len(my_arr)):
            self.add_answer_false(my_arr[i])

    def level_two_three(self,top,moviesDB): 
        rand_arr = random.sample(range(0,2),1)
        random_question = rand_arr[0]
        if random_question == 0:
            my_arr = level_two_three_questions.topMoviesActorTwoThree(top,moviesDB)
        elif random_question == 1:
            my_arr = level_two_three_questions.topMoviesDirectorsTwoThree(top,moviesDB)
        
        self.ques = my_arr[0]
        self.answer_true = my_arr[1]
        for i in range(2,len(my_arr)):
            self.add_answer_false(my_arr[i])

    def level_three(self,top,moviesDB):
        rand_arr = random.sample(range(0,5),1)
        random_question = rand_arr[0]
        if random_question == 0:
            my_arr = level_three_questions.topMoviesYearThree(top,moviesDB)
        elif random_question == 1:
            my_arr = level_three_questions.topMoviesNotCastThree(top,moviesDB)
        elif random_question == 2:
            my_arr = level_three_questions.topMoviesRoleThree(top,moviesDB)        
        elif random_question == 3:
            my_arr = level_three_questions.topMoviesActorMovieThree(top,moviesDB)
        elif random_question == 4:
            my_arr = level_three_questions.topMoviesCastThree(top,moviesDB)

        self.ques = my_arr[0]
        self.answer_true = my_arr[1]
        for i in range(2,len(my_arr)):
            self.add_answer_false(my_arr[i])                          