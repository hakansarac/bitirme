from imdb import IMDb
from random import randrange
import random


###topMoviesYear
###level_2 question (medium) 
###there are 2 years between selections
def topMoviesYearTwo(top,moviesDB):
    #moviesDB = IMDb()
    #top = moviesDB.get_top250_movies()
    movieID = randrange(0,250)
    chance = 0
    all_question = []
    false_arr = []
    ques = '{0} filmi hangi sene vizyona girmiştir?'.format(top[movieID]['title'])
    answer_true = top[movieID]['year']

    if answer_true>=2015 and answer_true<=2016:
        chance = randrange(3)        
    elif answer_true>=2017 and answer_true<=2018:
        chance = randrange(2)
    elif answer_true>=2019:
        chance = randrange(1)
    else:
        chance = randrange(4)

    
    if chance == 0:
        false_arr.append(top[movieID]['year']-6)
        false_arr.append(top[movieID]['year']-4)  
        false_arr.append(top[movieID]['year']-2)
    elif chance == 1:
        false_arr.append(top[movieID]['year']+2)
        false_arr.append(top[movieID]['year']-4)
        false_arr.append(top[movieID]['year']-2)
    elif chance == 2:
        false_arr.append(top[movieID]['year']+2)
        false_arr.append(top[movieID]['year']+4)
        false_arr.append(top[movieID]['year']-2)
    elif chance == 3:    
        false_arr.append(top[movieID]['year']+2)
        false_arr.append(top[movieID]['year']+4)
        false_arr.append(top[movieID]['year']+6)
    
    all_question.append(ques)
    all_question.append(answer_true)
    for i in range(len(false_arr)):
        all_question.append(false_arr[i])
    return all_question


###level_2 question (medium) 
###false selections are among top five actors/actresses in movie
###true selection is first actor/actress from new random movie(harder one in level3)
##topMoviesNotCast
def topMoviesNotCastTwo(top,moviesDB):
    #moviesDB = IMDb()
    #top = moviesDB.get_top250_movies()
    movieID = randrange(0,250)
    movie = top[movieID]
    moviesDB.update(movie,info=['main'])
    #moviesDB.update(movie['cast'][0])
    all_question = []
    false_arr = []
    
    ques = 'Aşağıdakilerden hangisi {1} yapımı olan {0} filminin oyuncularından değildir?'.format(movie['title'],movie['year'])
    if len(movie['cast'])<5:
        false_arr.append(movie['cast'][0]['name'])
        false_arr.append(movie['cast'][1]['name'])
        false_arr.append(movie['cast'][2]['name'])
    else:
        rand = random.sample(range(0,5),3)
        index = rand[0]
        false_arr.append(movie['cast'][index]['name'])
        index = rand[1]
        false_arr.append(movie['cast'][index]['name'])
        index = rand[2]
        false_arr.append(movie['cast'][index]['name'])
    #moviesDB.update(movie['cast'][0])
    roleNum = len(movie['cast'])
    flag = True
    while flag:
        new_movieID = randrange(0,250)
        new_movie = top[new_movieID]
        moviesDB.update(new_movie,info=['main'])            
        roleCoun = len(new_movie['cast'])                             
        if movie['title']!=new_movie['title']:                
            for c in range(roleCoun): 
                control_c = 0
                for j in range(roleNum):
                    if new_movie['cast'][c]['name'] == movie['cast'][j]['name']:
                        control_c +=1 
                if control_c == 0:
                    answer_true = new_movie['cast'][c]['name']
                    flag = False
                    break
    
    all_question.append(ques)
    all_question.append(answer_true)
    for i in range(len(false_arr)):
        all_question.append(false_arr[i])
    return all_question


##topMoviesRole
###level_2 question (medium) 
###false selections are from another movie
def topMoviesRoleTwo(top,moviesDB):
    #moviesDB = IMDb()
    #top = moviesDB.get_top250_movies()
    movieID = randrange(0,250)
    movie = top[movieID]
    moviesDB.update(movie,info=['main'])
    all_question = []
    false_arr = []
    rand = random.sample(range(0,5),1)
    one = rand[0]
    actor = movie['cast'][one]
    answer_true = actor.currentRole
    ques = 'Aşağıdakilerden hangisi {1} yapımı olan {0} filminde {2} adlı oyuncunun canlandırdığı karakterdir?'.format(movie['title'],movie['year'],movie['cast'][one])
    
    new_movieID = randrange(0,250)
    new_movie = top[new_movieID]
    moviesDB.update(new_movie,info=['main'])
    if new_movie['title'] != new_movie['title']:
        actor = new_movie['cast'][0]
        false_arr.append(actor.currentRole)
        
        actor = new_movie['cast'][1]
        false_arr.append(actor.currentRole)
        
        actor = new_movie['cast'][2]
        false_arr.append(actor.currentRole)

    all_question.append(ques)
    all_question.append(answer_true)
    for i in range(len(false_arr)):
        all_question.append(false_arr[i])
    return all_question


##topMoviesActorMovie
###level_2 question (medium) 
###true selection is chosen randomly
def topMoviesActorMovieTwo(top,moviesDB):
    #moviesDB = IMDb()
    #top = moviesDB.get_top250_movies()
    isFind = False
    num = 0
    movie = top[0]
    all_question = []
    false_arr = []
    rand = random.sample(range(0,5),1)
    index_one = rand[0] #actor
    while not isFind:
        movieID = randrange(0,250)
        movie = top[movieID]
        moviesDB.update(movie,info=['main'])
        moviesDB.update(movie['cast'][index_one])
        if list(movie['cast'][index_one]['filmography'][0])[0] == "actor":                
            num = len(movie['cast'][index_one]['filmography'][0]['actor'])                    
            isFind = True
        elif list(movie['cast'][index_one]['filmography'][0])[0] == "actress":                
            num = len(movie['cast'][index_one]['filmography'][0]['actress'])
            isFind = True
            
    #movieID = randrange(0,250)
    #movie = top[movieID]
    #moviesDB.update(movie,info=['main'])
    #rand = random.sample(range(0,5),2)

    #index = rand[0] #actor
    actor = movie['cast'][index_one]
    ques = '{0} isimli oyuncu aşağıdaki filmlerden hangisinde rol almamıştır?'.format(actor)

    
    #moviesDB.update(movie['cast'][index])  
    #num = len(movie['cast'][index]['filmography'][0]['actor'])      #####KeyError: 'actor'   
    rand_index = random.sample(range(0,num),2) #movies of actor1        #############Sample larger than population or is negative
    false_arr.append(movie['title'])
    movie_index = rand_index[0]
    new_id = 0
    if list(movie['cast'][index_one]['filmography'][0])[0] == "actor":         
        new_id = movie['cast'][index_one]['filmography'][0]['actor'][movie_index].movieID
    elif list(movie['cast'][index_one]['filmography'][0])[0] == "actress":
        new_id = movie['cast'][index_one]['filmography'][0]['actress'][movie_index].movieID
    #new_id = movie['cast'][index]['filmography'][0]['actor'][movie_index].movieID
    newMovie = moviesDB.get_movie(new_id)
    false_arr.append(newMovie['title'])
    movie_index = rand_index[1]
    new_id = 0
    if list(movie['cast'][index_one]['filmography'][0])[0] == "actor":         
        new_id = movie['cast'][index_one]['filmography'][0]['actor'][movie_index].movieID
    elif list(movie['cast'][index_one]['filmography'][0])[0] == "actress":
        new_id = movie['cast'][index_one]['filmography'][0]['actress'][movie_index].movieID
    #new_id = movie['cast'][index]['filmography'][0]['actor'][movie_index].movieID
    newMovie = moviesDB.get_movie(new_id)
    false_arr.append(newMovie['title'])
    #actor_two = movie['cast'][index_two]
    #moviesDB.update(movie['cast'][index_two])
    #movieNum = len(movie['cast'][index_two]['filmography'][0]['actor'])     #####KeyError: 'actor'   
    flag = True
    while flag:
        flag_coun = 0
        new_movieID = randrange(0,250)
        new_movie = top[new_movieID]
        moviesDB.update(new_movie,info=['main'])
        roleCoun = len(new_movie['cast'])                             
        if movie['title']!=new_movie['title']:                
            for c in range(roleCoun): 
                if new_movie['cast'][c]['name'] == movie['cast'][index_one]['name']:
                    flag_coun+=1
            if flag_coun == 0:
                answer_true = new_movie['title']
                flag = False
                break  
    
    all_question.append(ques)
    all_question.append(answer_true)
    for i in range(len(false_arr)):
        all_question.append(false_arr[i])
    return all_question


##topMoviesCast    
##level_2 question (medium)
##true selection is from top three actor/actress of movie
##false selections from random other three movies 
def topMoviesCastTwo(top,moviesDB):
    #moviesDB = IMDb()
    #top = moviesDB.get_top250_movies()
    movieID = randrange(0,250)
    movie = top[movieID]
    moviesDB.update(movie,info=['main'])
    all_question = []
    false_arr = []
    rand = random.sample(range(0,3),1)
    index = rand[0]       

    ques = 'Aşağıdakilerden hangisi {1} yapımı olan {0} filminde oynamıştır?'.format(movie['title'],movie['year'])        
    
    answer_true = movie['cast'][index]['name']
    
    
    roleNum = len(movie['cast'])
    flag = True
    while flag:
        new_movieID = randrange(0,250)
        new_movie = top[new_movieID]
        moviesDB.update(new_movie,info=['main'])            
        roleCoun = len(new_movie['cast'])                             
        if movie['title']!=new_movie['title']:                
            for c in range(roleCoun): 
                control_c = 0
                for j in range(roleNum):
                    if new_movie['cast'][c]['name'] == movie['cast'][j]['name']:
                        control_c +=1 
                if control_c == 0:
                    false_arr.append(new_movie['cast'][c]['name'])
                    flag = False
                    break
    
    flag = True
    while flag:
        new_movieID = randrange(0,250)
        new_movie = top[new_movieID]
        moviesDB.update(new_movie,info=['main'])            
        roleCoun = len(new_movie['cast'])                             
        if movie['title']!=new_movie['title']:                
            for c in range(roleCoun): 
                control_c = 0
                for j in range(roleNum):
                    if new_movie['cast'][c]['name'] == movie['cast'][j]['name']:
                        control_c +=1 
                if control_c == 0:
                    false_arr.append(new_movie['cast'][c]['name'])
                    flag = False
                    break
    
    flag = True
    while flag:
        new_movieID = randrange(0,250)
        new_movie = top[new_movieID]
        moviesDB.update(new_movie,info=['main'])            
        roleCoun = len(new_movie['cast'])                             
        if movie['title']!=new_movie['title']:                
            for c in range(roleCoun): 
                control_c = 0
                for j in range(roleNum):
                    if new_movie['cast'][c]['name'] == movie['cast'][j]['name']:
                        control_c +=1 
                if control_c == 0:
                    false_arr.append(new_movie['cast'][c]['name'])
                    flag = False
                    break

    all_question.append(ques)
    all_question.append(answer_true)
    for i in range(len(false_arr)):
        all_question.append(false_arr[i])
    return all_question