from imdb import IMDb
from random import randrange
import random



###level_2_3 question (medium - hard) 
###true selection is among top five actor/actress
###false selections are from same movie
def topMoviesActorTwoThree(top,moviesDB):
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
    
    two = rand[1]
    actor = movie['cast'][two]
    false_arr.append(actor)

    three = rand[2]
    actor = movie['cast'][three]
    false_arr.append(actor)

    four = rand[3]
    actor = movie['cast'][four]
    false_arr.append(actor)

    all_question.append(ques)
    all_question.append(answer_true)
    for i in range(len(false_arr)):
        all_question.append(false_arr[i])
    return all_question
##topMoviesActor


###level_2_3 question (medium-hard) 
###false selections are directors who directed movies same genres 
def topMoviesDirectorsTwoThree(top,moviesDB):
    #moviesDB = IMDb()
    #top = moviesDB.get_top250_movies()
    movieID = randrange(0,250)
    movie = top[movieID]
    moviesDB.update(movie,info=['main'])
    all_question = []
    false_arr = []
    ques = '{1} yapımı olan {0} filminin yönetmeni kimdir?'.format(movie['title'],movie['year'])
    answer_true = movie['directors'][0]['name'] 
    flag=True
    while flag:
        filmID = randrange(0,250)
        moviesDB.update(top[filmID],info=['main'])
        for genre in movie['genres']:
            for gen in top[filmID]['genres']:
                if gen == genre:                        
                    film = top[filmID]
                    if film['directors'][0]['name'] != answer_true:
                        false_arr.append(film['directors'][0]['name'])                                               
                        flag = False
                        break
                if flag == False:
                    break 
    flag=True
    while flag:
        filmID = randrange(0,250)
        moviesDB.update(top[filmID],info=['main'])
        for genre in movie['genres']:
            for gen in top[filmID]['genres']:
                if gen == genre:                        
                    film = top[filmID]
                    if film['directors'][0]['name'] != answer_true and film['directors'][0]['name'] != false_arr[0]:
                        false_arr.append(film['directors'][0]['name'])
                        flag = False
                        break
                if flag == False:
                    break
    flag=True
    while flag:
        filmID = randrange(0,250)
        moviesDB.update(top[filmID],info=['main'])
        for genre in movie['genres']:
            for gen in top[filmID]['genres']:
                if gen == genre:                        
                    film = top[filmID]
                    if film['directors'][0]['name'] != answer_true and film['directors'][0]['name'] != false_arr[0] and film['directors'][0]['name'] != false_arr[1]:
                        false_arr.append(film['directors'][0]['name'])
                        flag = False
                        break
                if flag == False:
                    break

    all_question.append(ques)
    all_question.append(answer_true)
    for i in range(len(false_arr)):
        all_question.append(false_arr[i])
    return all_question
##topMoviesDirectors