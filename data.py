from imdb import IMDb
from answer import Answer
from random import randrange
import random
class Data:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.hearth = 3
        self.flag = True
        self.random = 0
        self.answers = {}
        self.rand_arr = {}
        self.question = ""
        self._last_answer_key = 0
        self.answer_number = 0
        self.question_number = 0
        self.moviesDB = IMDb()
        self.top = self.moviesDB.get_top250_movies()


    def get_top_imdb(self):
        return self.top

    def get_moviesdb(self):
        return self.moviesDB

    def reconstitute(self):
        self.score = 0
        self.level = 1
        self.hearth = 3
        self.question_number = 0

    def update_score(self):
        self.score = self.score + 10

    def update_level(self):
        self.level = self.level + 1
    
    def update_question_number(self):
        self.question_number = self.question_number + 1

    def increase_hearth(self):
        self.hearth = self.hearth + 1
        
    def decrease_hearth(self):
        self.hearth = self.hearth - 1

    def get_hearth(self):
        return self.hearth 

    def get_level(self):
        return self.level

    def get_score(self):
        return self.score

    def get_flag(self):
        return self.flag

    def get_random(self):
        return self.random 

    def update_flag(self):
        if(self.flag==True):
            self.flag = False
        else:
            self.flag = True
    
    def update_random(self,rand):
        self.random = rand


    
    def add_answer(self, answer):        
        self.answers[self._last_answer_key] = answer
        self._last_answer_key += 1
        return self._last_answer_key

    def delete_answer(self, answer_key):
        if answer_key in self.answers:
            del self.answers[answer_key]

    def get_answer(self, answer_key):
        answer = self.answers.get(answer_key)
        if answer is None:
            return None
        answer_ = Answer(answer.selection,answer.is_true)
        return answer_
    
    def set_question(self, question):
        self.question = question

    def get_question(self):
        return self.question

    def get_answers(self):
        answers = []
        for answer_key, answer in self.answers.items():
            answer_ = Answer(answer.selection,answer.is_true)
            answers.append((answer_key, answer_))
        return answers

    def get_length_answer(self):
        return len(self.answers)

    def update_rand_arr(self,number):
        self.rand_arr = random.sample(range(0,number),number)

    def set_answer_number(self,number):
        self.answer_number = number

    def get_answer_number(self):
        return self.answer_number

    def delete_all_answers(self):
        self.answers = {}
        

   
