from imdb import IMDb
from random import randrange
import random


###level_3 question (hard) 
###there is 1 year between selections
def topMoviesYearThree():
    moviesDB = IMDb()
    top = moviesDB.get_top250_movies()
    movieID = randrange(0,250)
    chance = 0
    all_question = []
    false_arr = []
    ques = '{0} filmi hangi sene vizyona girmiştir?'.format(top[movieID]['title'])
    answer_true = top[movieID]['year']

    if answer_true==2018:
        chance = randrange(3)        
    elif answer_true==2019:
        chance = randrange(2)
    elif answer_true==2020:
        chance = randrange(1)
    else:
        chance = randrange(4)

    
    if chance == 0:
        false_arr.append(top[movieID]['year']-3)
        false_arr.append(top[movieID]['year']-2)
        false_arr.append(top[movieID]['year']-1)
    elif chance == 1:
        false_arr.append(top[movieID]['year']+1)
        false_arr.append(top[movieID]['year']-2)
        false_arr.append(top[movieID]['year']-1)
    elif chance == 2:
        false_arr.append(top[movieID]['year']+1)
        false_arr.append(top[movieID]['year']+2)
        false_arr.append(top[movieID]['year']-1)
    elif chance == 3:    
        false_arr.append(top[movieID]['year']+1)
        false_arr.append(top[movieID]['year']+2)
        false_arr.append(top[movieID]['year']+3)

    all_question.append(ques)
    all_question.append(answer_true)
    for i in range(len(false_arr)):
        all_question.append(false_arr[i])
    return all_question



###level_3 question (hard) 
###false selections are among top five actors/actresses in same movie
###true selection is an actor/actress from another movie of leading actor(if there are maximum 5 years between two movies of leading actor choose this year, or search another movie) 
def topMoviesNotCastThree():
    moviesDB = IMDb()
    top = moviesDB.get_top250_movies()
    isFind = False
    movieNum = 0
    movie = top[0]
    all_question = []
    false_arr = []
    while not isFind:
        movieID = randrange(0,250)
        movie = top[movieID]
        moviesDB.update(movie,info=['main'])
        moviesDB.update(movie['cast'][0])
        if list(movie['cast'][0]['filmography'][0])[0] == "actor":
            movieNum = len(movie['cast'][0]['filmography'][0]['actor'])
            isFind = True
        elif list(movie['cast'][0]['filmography'][0])[0] == "actress":
            movieNum = len(movie['cast'][0]['filmography'][0]['actress'])
            isFind = True
    
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
    moviesDB.update(movie['cast'][0])
    roleNum = len(movie['cast'])
    rand = random.sample(range(0,movieNum),movieNum)
    i = 0        
    flag=True        
    while flag and i < movieNum:
        coun = rand[i]
        i+=1   
        ##
        new_id = 0
        if list(movie['cast'][0]['filmography'][0])[0] == "actor":         
            new_id = movie['cast'][0]['filmography'][0]['actor'][coun].movieID
        elif list(movie['cast'][0]['filmography'][0])[0] == "actress":
            new_id = movie['cast'][0]['filmography'][0]['actress'][coun].movieID
        ##
        newMovie = moviesDB.get_movie(new_id)
        moviesDB.update(newMovie,info=['main'])
        roleCoun = len(newMovie['cast'])  
        if movie['year']+5>=newMovie['year'] and movie['year']-5<=newMovie['year'] and movie['title']!=newMovie['title']:                
            for c in range(roleCoun): 
                control_c = 0
                for j in range(roleNum):
                    if newMovie['cast'][c]['name'] == movie['cast'][j]['name']:
                        control_c +=1 
                if control_c == 0:
                    answer_true = newMovie['cast'][c]['name']
                    flag = False
                    break  
    i=0
    while flag and i < movieNum:
        coun = rand[i]
        i+=1            
        ##
        new_id = 0
        if list(movie['cast'][0]['filmography'][0])[0] == "actor":         
            new_id = movie['cast'][0]['filmography'][0]['actor'][coun].movieID
        elif list(movie['cast'][0]['filmography'][0])[0] == "actress":
            new_id = movie['cast'][0]['filmography'][0]['actress'][coun].movieID
        ##
        newMovie = moviesDB.get_movie(new_id)
        moviesDB.update(newMovie,info=['main'])
        roleCoun = len(newMovie['cast'])  
        if movie['title']!=newMovie['title']:                
            for c in range(roleCoun): 
                control_c = 0
                for j in range(roleNum):
                    if newMovie['cast'][c]['name'] == movie['cast'][j]['name']:
                        control_c +=1 
                if control_c == 0:
                    answer_true = newMovie['cast'][c]['name']
                    flag = False
                    break  
    
    all_question.append(ques)
    all_question.append(answer_true)
    for i in range(len(false_arr)):
        all_question.append(false_arr[i])
    return all_question
##topMoviesNotCast


###level_3 question (hard) 
###true selection is among top five role 
###false selections are among top five role from same movie 
def topMoviesRoleThree():
    moviesDB = IMDb()
    top = moviesDB.get_top250_movies()
    movieID = randrange(0,250)
    movie = top[movieID]
    moviesDB.update(movie,info=['main'])
    all_question = []
    false_arr = []
    rand = random.sample(range(0,5),4)
    one = rand[0]
    actor = movie['cast'][one]
    answer_true = actor.currentRole
    ques = 'Aşağıdakilerden hangisi {1} yapımı olan {0} filminde {2} adlı oyuncunun canlandırdığı karakterdir?'.format(movie['title'],movie['year'],movie['cast'][one])
    
    two = rand[1]
    actor = movie['cast'][two]
    false_arr.append(actor.currentRole)

    three = rand[2]
    actor = movie['cast'][three]
    false_arr.append(actor.currentRole)

    four = rand[3]
    actor = movie['cast'][four]
    false_arr.append(actor.currentRole)

    all_question.append(ques)
    all_question.append(answer_true)
    for i in range(len(false_arr)):
        all_question.append(false_arr[i])
    return all_question

##topMoviesRole






###level_3 question (hard) 
###true selection is chosen among another movies of other leading actor/actress
def topMoviesActorMovieThree():
    moviesDB = IMDb()
    top = moviesDB.get_top250_movies()
    isFind = False
    num = 0
    movieNum = 0
    movie = top[0]
    all_question = []
    false_arr = []
    rand = random.sample(range(0,5),2)
    index_one = rand[0] #actor
    index_two = rand[1]
    while not isFind:
        movieID = randrange(0,250)
        movie = top[movieID]
        moviesDB.update(movie,info=['main'])
        moviesDB.update(movie['cast'][index_one])
        moviesDB.update(movie['cast'][index_two])
        if list(movie['cast'][index_one]['filmography'][0])[0] == "actor":
            if list(movie['cast'][index_two]['filmography'][0])[0] == "actor":
                num = len(movie['cast'][index_one]['filmography'][0]['actor'])
                movieNum = len(movie['cast'][index_two]['filmography'][0]['actor'])
                isFind = True
            elif list(movie['cast'][index_two]['filmography'][0])[0] == "actress":
                num = len(movie['cast'][index_one]['filmography'][0]['actor'])
                movieNum = len(movie['cast'][index_two]['filmography'][0]['actress'])
                isFind = True
        elif list(movie['cast'][index_one]['filmography'][0])[0] == "actress":
            if list(movie['cast'][index_two]['filmography'][0])[0] == "actor":
                num = len(movie['cast'][index_one]['filmography'][0]['actress'])
                movieNum = len(movie['cast'][index_two]['filmography'][0]['actor'])
                isFind = True
            elif list(movie['cast'][index_two]['filmography'][0])[0] == "actress":
                num = len(movie['cast'][index_one]['filmography'][0]['actress'])
                movieNum = len(movie['cast'][index_two]['filmography'][0]['actress'])
                isFind = True
    
    actor = movie['cast'][index_one]
    ques = '{0} isimli oyuncu aşağıdaki filmlerden hangisinde rol almamıştır?'.format(actor)

    
       
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
    rand = random.sample(range(0,movieNum),movieNum)
    flag = True
    i = 0
    while flag and i < movieNum:
        coun = rand[i]
        i+=1   
        new_id = 0
        if list(movie['cast'][index_two]['filmography'][0])[0] == "actor":         
            new_id = movie['cast'][index_two]['filmography'][0]['actor'][coun].movieID
        elif list(movie['cast'][index_two]['filmography'][0])[0] == "actress":
            new_id = movie['cast'][index_two]['filmography'][0]['actress'][coun].movieID         
        #new_id = movie['cast'][index_two]['filmography'][0]['actor'][coun].movieID
        newMovie = moviesDB.get_movie(new_id)
        moviesDB.update(newMovie,info=['main'])
        roleCoun = len(newMovie['cast'])  
                        
        for c in range(roleCoun): 
            control_c = 0
            if newMovie['cast'][c]['name'] == actor['name']:
                control_c +=1               
        if control_c == 0:
            answer_true = newMovie['title']
            flag = False
            break

    all_question.append(ques)
    all_question.append(answer_true)
    for i in range(len(false_arr)):
        all_question.append(false_arr[i])
    return all_question
##topMoviesActorMovie





##level_3 question (hard)
##true selection is from top three actor/actress of movie
##false selections are leading actor/actress from other three movies of leading actor/actress of asked movie

def topMoviesCastThree():
    moviesDB = IMDb()
    top = moviesDB.get_top250_movies()
    isFind = False
    movieNum = 0
    movie = top[0]
    all_question = []
    false_arr = []
    index = 0
    while not isFind:
        movieID = randrange(0,250)
        movie = top[movieID]
        moviesDB.update(movie,info=['main'])
        rand = random.sample(range(0,3),1)
        index = rand[0]
        moviesDB.update(movie['cast'][index])
        moviesDB.update(movie['cast'][0])
        if list(movie['cast'][index]['filmography'][0])[0] == "actor":
            if list(movie['cast'][0]['filmography'][0])[0] == "actor":
                movieNum = len(movie['cast'][0]['filmography'][0]['actor'])
                isFind = True
            elif list(movie['cast'][0]['filmography'][0])[0] == "actress":
                movieNum = len(movie['cast'][0]['filmography'][0]['actress'])
                isFind = True
        elif list(movie['cast'][index]['filmography'][0])[0] == "actress":
            if list(movie['cast'][0]['filmography'][0])[0] == "actor":
                movieNum = len(movie['cast'][0]['filmography'][0]['actor'])
                isFind = True
            elif list(movie['cast'][0]['filmography'][0])[0] == "actress":
                movieNum = len(movie['cast'][0]['filmography'][0]['actress'])
                isFind = True

    ques = 'Aşağıdakilerden hangisi {1} yapımı olan {0} filminde oynamıştır?'.format(movie['title'],movie['year'])        
    
    answer_true = movie['cast'][index]['name']   

    
    roleNum = len(movie['cast'])
    #moviesDB.update(movie)
    #movieNum = len(movie['cast'][0]['filmography'][0]['actor'])
    rand = random.sample(range(0,movieNum),movieNum)
    i = 0      
    flag=True        
    while flag and i < movieNum:
        coun = rand[i]
        i+=1      
        new_id = 0
        if list(movie['cast'][0]['filmography'][0])[0] == "actor":         
            new_id = movie['cast'][0]['filmography'][0]['actor'][coun].movieID
        elif list(movie['cast'][0]['filmography'][0])[0] == "actress":
            new_id = movie['cast'][0]['filmography'][0]['actress'][coun].movieID      
        #new_id = movie['cast'][0]['filmography'][0]['actor'][coun].movieID
        newMovie = moviesDB.get_movie(new_id)
        moviesDB.update(newMovie,info=['main'])
        roleCoun = len(newMovie['cast'])  
        if movie['title']!=newMovie['title']:                
            for c in range(roleCoun): 
                control_c = 0
                for j in range(roleNum):
                    if newMovie['cast'][c]['name'] == movie['cast'][j]['name']:
                        control_c +=1 
                if control_c == 0:
                    false_arr.append(newMovie['cast'][c]['name'])
                    flag = False
                    break

    flag=True        
    while flag and i < movieNum:
        coun = rand[i]
        i+=1            
        new_id = 0
        if list(movie['cast'][0]['filmography'][0])[0] == "actor":         
            new_id = movie['cast'][0]['filmography'][0]['actor'][coun].movieID
        elif list(movie['cast'][0]['filmography'][0])[0] == "actress":
            new_id = movie['cast'][0]['filmography'][0]['actress'][coun].movieID      
        #new_id = movie['cast'][0]['filmography'][0]['actor'][coun].movieID
        newMovie = moviesDB.get_movie(new_id)
        moviesDB.update(newMovie,info=['main'])
        roleCoun = len(newMovie['cast'])  
        if movie['title']!=newMovie['title']:                
            for c in range(roleCoun): 
                control_c = 0
                for j in range(roleNum):
                    if newMovie['cast'][c]['name'] == movie['cast'][j]['name']:
                        control_c +=1 
                if control_c == 0:
                    false_arr.append(newMovie['cast'][c]['name'])
                    flag = False
                    break

    flag=True        
    while flag and i < movieNum:
        coun = rand[i]
        i+=1            
        new_id = 0
        if list(movie['cast'][0]['filmography'][0])[0] == "actor":         
            new_id = movie['cast'][0]['filmography'][0]['actor'][coun].movieID
        elif list(movie['cast'][0]['filmography'][0])[0] == "actress":
            new_id = movie['cast'][0]['filmography'][0]['actress'][coun].movieID      
        #new_id = movie['cast'][0]['filmography'][0]['actor'][coun].movieID
        newMovie = moviesDB.get_movie(new_id)
        moviesDB.update(newMovie,info=['main'])
        roleCoun = len(newMovie['cast'])  
        if movie['title']!=newMovie['title']:                
            for c in range(roleCoun): 
                control_c = 0
                for j in range(roleNum):
                    if newMovie['cast'][c]['name'] == movie['cast'][j]['name']:
                        control_c +=1 
                if control_c == 0:
                    false_arr.append(newMovie['cast'][c]['name'])
                    flag = False
                    break

    all_question.append(ques)
    all_question.append(answer_true)
    for i in range(len(false_arr)):
        all_question.append(false_arr[i])
    return all_question
##topMoviesCast