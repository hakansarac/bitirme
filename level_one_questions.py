from imdb import IMDb
from random import randrange
import random
from data import Data
from flask import abort, render_template, current_app, request, redirect, url_for

###topMoviesYear
###level_1 question (easy) 
###there are 3 years between selections
def topMoviesYearOne(top,moviesDB):
    all_question = []
    #moviesDB = IMDb()
    #top = moviesDB.get_top250_movies()
    movieID = randrange(0,250)
    chance = 0
    ques = '{0} filmi hangi sene vizyona girmiştir?'.format(top[movieID]['title'])
    answer_true = top[movieID]['year']
    false_arr = []
    
    if answer_true>=2012 and answer_true<=2014:
        chance = randrange(3)        
    elif answer_true and answer_true<=2017:
        chance = randrange(2)
    elif answer_true>=2018:
        chance = randrange(1)
    else:
        chance = randrange(4)

            
    if chance == 0:
        false_arr.append(top[movieID]['year']-3)
        false_arr.append(top[movieID]['year']-6)
        false_arr.append(top[movieID]['year']-9)

                
    elif chance == 1:
        false_arr.append(top[movieID]['year']+3)
        false_arr.append(top[movieID]['year']-6)
        false_arr.append(top[movieID]['year']-3)

                
    elif chance == 2:
        false_arr.append(top[movieID]['year']+3)
        false_arr.append(top[movieID]['year']+6)
        false_arr.append(top[movieID]['year']-3)

                
    elif chance == 3:    
        false_arr.append(top[movieID]['year']+3)
        false_arr.append(top[movieID]['year']+6)
        false_arr.append(top[movieID]['year']+9)

    all_question.append(ques)
    all_question.append(answer_true)
    for i in range(len(false_arr)):
        all_question.append(false_arr[i])
    return all_question

##topMoviesDirectors
###level_1 question (easy) 
###false selections are actors/actresses in same movie
def topMoviesDirectorsOne(top,moviesDB):
    #moviesDB = IMDb()
    #top = moviesDB.get_top250_movies()
    movieID = randrange(0,250)
    movie = top[movieID]
    moviesDB.update(movie,info=['main'])
    all_question = []
    false_arr = []
    ques = '{1} yapımı olan {0} filminin yönetmeni kimdir?'.format(movie['title'],movie['year'])
    answer_true = movie['directors'][0]['name']
    directorCoun = len(movie['directors']) 
    answer_coun = 0
    roleCoun = len(movie['cast'])
    for c in range(roleCoun):
        flag_coun = 0
        for d in range(directorCoun):
            if movie['directors'][d]['name'] == movie['cast'][c]['name']: 
                flag_coun = flag_coun + 1

        if flag_coun == 0:
            answer_coun+=1            
            if answer_coun==1:
                false_arr.append(movie['cast'][c]['name'])
            elif answer_coun==2:
                false_arr.append(movie['cast'][c]['name'])
            elif answer_coun==3: 
                false_arr.append(movie['cast'][c]['name'])            
                break
            
    
                
                
                
    all_question.append(ques)
    all_question.append(answer_true)
    for i in range(len(false_arr)):
        all_question.append(false_arr[i])
    return all_question


##topMoviesActor
###level_1 question (easy) 
###true selection is among top five actor/actress
###false selections are from another movie
def topMoviesActorOne(top,moviesDB):
    #moviesDB = IMDb()
    #top = moviesDB.get_top250_movies()
    movieID = randrange(0,250)
    movie = top[movieID]
    moviesDB.update(movie,info=['main'])

    all_question = []
    false_arr = []
    rand = random.sample(range(0,5),4)
    one = rand[0]
    actor = movie['cast'][one]
    answer_true = actor
    role = actor.currentRole
    ques = 'Aşağıdakilerden hangisi {1} yapımı olan {0} filminde {2} adlı karakteri canlandıran oyuncudur?'.format(movie['title'],movie['year'],role)
    
    flag = True
    while flag:
        flag_coun = 0
        new_movieID = randrange(0,250)
        new_movie = top[new_movieID]
        moviesDB.update(new_movie,info=['main'])
        roleCoun = len(new_movie['cast'])                             
        if movie['title']!=new_movie['title']:                
            for c in range(roleCoun): 
                if new_movie['cast'][c]['name'] != movie['cast'][one]['name']:
                    flag_coun+=1
                    if flag_coun == 1:
                        false_arr.append(new_movie['cast'][c]['name'])
                    elif flag_coun == 2:
                        false_arr.append(new_movie['cast'][c]['name']) 
                    elif flag_coun == 3:
                        false_arr.append(new_movie['cast'][c]['name'])
                        flag=False
                        break
    all_question.append(ques)
    all_question.append(answer_true)
    for i in range(len(false_arr)):
        all_question.append(false_arr[i])
    return all_question