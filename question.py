from quiz import Quiz 
from answer import Answer
from imdb import IMDb
from random import randrange
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

###topMoviesYear
###level_1 question (easy) 
###there are 3 years between selections 
    def topMoviesYearOne(self):
        moviesDB = IMDb()
        top = moviesDB.get_top250_movies()
        movieID = randrange(0,250)
        chance = 0
        self.ques = '{0} filmi hangi sene vizyona girmiştir?'.format(top[movieID]['title'])
        self.answer_true = top[movieID]['year']

        if self.answer_true>=2012 and self.answer_true<=2014:
            chance = randrange(3)        
        elif self.answer_true and self.answer_true<=2017:
            chance = randrange(2)
        elif self.answer_true>=2018:
            chance = randrange(1)
        else:
            chance = randrange(4)

        
        if chance == 0:
            self.add_answer_false(top[movieID]['year']-3)
            self.add_answer_false(top[movieID]['year']-6)
            self.add_answer_false(top[movieID]['year']-9)

            
        elif chance == 1:
            self.add_answer_false(top[movieID]['year']+3)
            self.add_answer_false(top[movieID]['year']-6)
            self.add_answer_false(top[movieID]['year']-3)

            
        elif chance == 2:
            self.add_answer_false(top[movieID]['year']+3)
            self.add_answer_false(top[movieID]['year']+6)
            self.add_answer_false(top[movieID]['year']-3)

            
        elif chance == 3:    
            self.add_answer_false(top[movieID]['year']+3)
            self.add_answer_false(top[movieID]['year']+6)
            self.add_answer_false(top[movieID]['year']+9)

           

###level_2 question (medium) 
###there are 2 years between selections
    def topMoviesYearTwo(self):
        moviesDB = IMDb()
        top = moviesDB.get_top250_movies()
        movieID = randrange(0,250)
        chance = 0
        self.ques = '{0} filmi hangi sene vizyona girmiştir?'.format(top[movieID]['title'])
        self.answer_true = top[movieID]['year']

        if self.answer_true>=2015 and self.answer_true<=2016:
            chance = randrange(3)        
        elif self.answer_true>=2017 and self.answer_true<=2018:
            chance = randrange(2)
        elif self.answer_true>=2019:
            chance = randrange(1)
        else:
            chance = randrange(4)

        
        if chance == 0:
            self.add_answer_false(top[movieID]['year']-6)
            self.add_answer_false(top[movieID]['year']-4)  
            self.add_answer_false(top[movieID]['year']-2)
        elif chance == 1:
            self.add_answer_false(top[movieID]['year']+2)
            self.add_answer_false(top[movieID]['year']-4)
            self.add_answer_false(top[movieID]['year']-2)
        elif chance == 2:
            self.add_answer_false(top[movieID]['year']+2)
            self.add_answer_false(top[movieID]['year']+4)
            self.add_answer_false(top[movieID]['year']-2)
        elif chance == 3:    
            self.add_answer_false(top[movieID]['year']+2)
            self.add_answer_false(top[movieID]['year']+4)
            self.add_answer_false(top[movieID]['year']+6)

###level_3 question (hard) 
###there is 1 year between selections
    def topMoviesYearThree(self):
        moviesDB = IMDb()
        top = moviesDB.get_top250_movies()
        movieID = randrange(0,250)
        chance = 0
        self.ques = '{0} filmi hangi sene vizyona girmiştir?'.format(top[movieID]['title'])
        self.answer_true = top[movieID]['year']

        if self.answer_true==2018:
            chance = randrange(3)        
        elif self.answer_true==2019:
            chance = randrange(2)
        elif self.answer_true==2020:
            chance = randrange(1)
        else:
            chance = randrange(4)

        
        if chance == 0:
            self.add_answer_false(top[movieID]['year']-3)
            self.add_answer_false(top[movieID]['year']-2)
            self.add_answer_false(top[movieID]['year']-1)
        elif chance == 1:
            self.add_answer_false(top[movieID]['year']+1)
            self.add_answer_false(top[movieID]['year']-2)
            self.add_answer_false(top[movieID]['year']-1)
        elif chance == 2:
            self.add_answer_false(top[movieID]['year']+1)
            self.add_answer_false(top[movieID]['year']+2)
            self.add_answer_false(top[movieID]['year']-1)
        elif chance == 3:    
            self.add_answer_false(top[movieID]['year']+1)
            self.add_answer_false(top[movieID]['year']+2)
            self.add_answer_false(top[movieID]['year']+3)
    
##topMoviesYear







##topMoviesDirectors
###level_1 question (easy) 
###false selections are actors/actresses in same movie
    def topMoviesDirectorsOne(self):
        moviesDB = IMDb()
        top = moviesDB.get_top250_movies()
        movieID = randrange(0,250)
        movie = top[movieID]
        moviesDB.update(movie,info=['main'])
        self.ques = '{1} yapımı olan {0} filminin yönetmeni kimdir?'.format(movie['title'],movie['year'])
        self.answer_true = movie['directors'][0]['name'] 
        answer_coun = 0
        roleCoun = len(movie['cast'])
        for c in range(roleCoun):
            control_c = 0
            for director in movie['directors']:
                if director == movie['cast'][c]['name']: 
                    control_c +=1
            if control_c == 0:
                answer_coun+=1
                if answer_coun==1:
                    self.add_answer_false(movie['cast'][c]['name'])
                elif answer_coun==2:
                    self.add_answer_false(movie['cast'][c]['name'])
                elif answer_coun==3: 
                    self.add_answer_false(movie['cast'][c]['name'])            
                    break

###level_2_3 question (medium-hard) 
###false selections are directors who directed movies same genres 
    def topMoviesDirectorsTwoThree(self):
        moviesDB = IMDb()
        top = moviesDB.get_top250_movies()
        movieID = randrange(0,250)
        movie = top[movieID]
        moviesDB.update(movie,info=['main'])
        self.ques = '{1} yapımı olan {0} filminin yönetmeni kimdir?'.format(movie['title'],movie['year'])
        self.answer_true = movie['directors'][0]['name'] 
        flag=True
        while flag:
            filmID = randrange(0,250)
            moviesDB.update(top[filmID],info=['main'])
            for genre in movie['genres']:
                for gen in top[filmID]['genres']:
                    if gen == genre:                        
                        film = top[filmID]
                        if film['directors'][0]['name'] != self.answer_true:
                            self.add_answer_false(film['directors'][0]['name'])                                               
                            flag = False
        flag=True
        while flag:
            filmID = randrange(0,250)
            moviesDB.update(top[filmID],info=['main'])
            for genre in movie['genres']:
                for gen in top[filmID]['genres']:
                    if gen == genre:                        
                        film = top[filmID]
                        if film['directors'][0]['name'] != self.answer_true and film['directors'][0]['name'] != self.answers_false[0]:
                            self.add_answer_false(film['directors'][0]['name'])
                            flag = False
        flag=True
        while flag:
            filmID = randrange(0,250)
            moviesDB.update(top[filmID],info=['main'])
            for genre in movie['genres']:
                for gen in top[filmID]['genres']:
                    if gen == genre:                        
                        film = top[filmID]
                        if film['directors'][0]['name'] != self.answer_true and film['directors'][0]['name'] != self.answers_false[0] and film['directors'][0]['name'] != self.answers_false[1]:
                            self.add_answer_false(film['directors'][0]['name'])
                            flag = False

##topMoviesDirectors






###level_2 question (medium) 
###false selections are among top five actors/actresses in movie
###true selection is first actor/actress from new random movie(harder one in level3)
##topMoviesNotCast
    def topMoviesNotCastTwo(self):
        moviesDB = IMDb()
        top = moviesDB.get_top250_movies()
        movieID = randrange(0,250)
        movie = top[movieID]
        moviesDB.update(movie,info=['main'])
        #moviesDB.update(movie['cast'][0])
        
        self.ques = 'Aşağıdakilerden hangisi {1} yapımı olan {0} filminin oyuncularından değildir?'.format(movie['title'],movie['year'])
        if len(movie['cast'])<5:
            self.add_answer_false(movie['cast'][0]['name'])
            self.add_answer_false(movie['cast'][1]['name'])
            self.add_answer_false(movie['cast'][2]['name'])
        else:
            rand = random.sample(range(0,5),3)
            index = rand[0]
            self.add_answer_false(movie['cast'][index]['name'])
            index = rand[1]
            self.add_answer_false(movie['cast'][index]['name'])
            index = rand[2]
            self.add_answer_false(movie['cast'][index]['name'])
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
                        self.answer_true = new_movie['cast'][c]['name']
                        flag = False
                        break

###level_3 question (hard) 
###false selections are among top five actors/actresses in same movie
###true selection is an actor/actress from another movie of leading actor(if there are maximum 5 years between two movies of leading actor choose this year, or search another movie) 
    def topMoviesNotCastThree(self):
        moviesDB = IMDb()
        top = moviesDB.get_top250_movies()
        isFind = False
        movieNum = 0
        movie = top[0]
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
        
        self.ques = 'Aşağıdakilerden hangisi {1} yapımı olan {0} filminin oyuncularından değildir?'.format(movie['title'],movie['year'])
        if len(movie['cast'])<5:
            self.add_answer_false(movie['cast'][0]['name'])
            self.add_answer_false(movie['cast'][1]['name'])
            self.add_answer_false(movie['cast'][2]['name'])
        else:
            rand = random.sample(range(0,5),3)
            index = rand[0]
            self.add_answer_false(movie['cast'][index]['name'])
            index = rand[1]
            self.add_answer_false(movie['cast'][index]['name'])
            index = rand[2]
            self.add_answer_false(movie['cast'][index]['name'])
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
                        self.answer_true = newMovie['cast'][c]['name']
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
                        self.answer_true = newMovie['cast'][c]['name']
                        flag = False
                        break  
##topMoviesNotCast









##topMoviesRole
###level_2 question (medium) 
###false selections are from another movie
    def topMoviesRoleTwo(self):
        moviesDB = IMDb()
        top = moviesDB.get_top250_movies()
        movieID = randrange(0,250)
        movie = top[movieID]
        moviesDB.update(movie,info=['main'])

        rand = random.sample(range(0,5),1)
        one = rand[0]
        actor = movie['cast'][one]
        self.answer_true = actor.currentRole
        self.ques = 'Aşağıdakilerden hangisi {1} yapımı olan {0} filminde {2} adlı oyuncunun canlandırdığı karakterdir?'.format(movie['title'],movie['year'],movie['cast'][one])
        
        new_movieID = randrange(0,250)
        new_movie = top[new_movieID]
        moviesDB.update(new_movie,info=['main'])
        if new_movie['title'] != new_movie['title']:
            actor = new_movie['cast'][0]
            self.add_answer_false(actor.currentRole)
            
            actor = new_movie['cast'][1]
            self.add_answer_false(actor.currentRole)
            
            actor = new_movie['cast'][2]
            self.add_answer_false(actor.currentRole)

###level_3 question (hard) 
###true selection is among top five role 
###false selections are among top five role from same movie 
    def topMoviesRoleThree(self):
        moviesDB = IMDb()
        top = moviesDB.get_top250_movies()
        movieID = randrange(0,250)
        movie = top[movieID]
        moviesDB.update(movie,info=['main'])

        rand = random.sample(range(0,5),4)
        one = rand[0]
        actor = movie['cast'][one]
        self.answer_true = actor.currentRole
        self.ques = 'Aşağıdakilerden hangisi {1} yapımı olan {0} filminde {2} adlı oyuncunun canlandırdığı karakterdir?'.format(movie['title'],movie['year'],movie['cast'][one])
        
        two = rand[1]
        actor = movie['cast'][two]
        self.add_answer_false(actor.currentRole)

        three = rand[2]
        actor = movie['cast'][three]
        self.add_answer_false(actor.currentRole)

        four = rand[3]
        actor = movie['cast'][four]
        self.add_answer_false(actor.currentRole)

##topMoviesRole











##topMoviesActor
###level_1 question (easy) 
###true selection is among top five actor/actress
###false selections are from another movie
    def topMoviesActorOne(self):
        moviesDB = IMDb()
        top = moviesDB.get_top250_movies()
        movieID = randrange(0,250)
        movie = top[movieID]
        moviesDB.update(movie,info=['main'])

        rand = random.sample(range(0,5),4)
        one = rand[0]
        actor = movie['cast'][one]
        self.answer_true = actor
        role = actor.currentRole
        self.ques = 'Aşağıdakilerden hangisi {1} yapımı olan {0} filminde {2} adlı karakteri canlandıran oyuncudur?'.format(movie['title'],movie['year'],role)
        
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
                            self.add_answer_false(new_movie['cast'][c]['name'])
                        elif flag_coun == 2:
                            self.add_answer_false(new_movie['cast'][c]['name']) 
                        elif flag_coun == 3:
                            self.add_answer_false(new_movie['cast'][c]['name'])
                            flag=False
                            break                        

###level_2_3 question (medium - hard) 
###true selection is among top five actor/actress
###false selections are from same movie
    def topMoviesActorTwoThree(self):
        moviesDB = IMDb()
        top = moviesDB.get_top250_movies()
        movieID = randrange(0,250)
        movie = top[movieID]
        moviesDB.update(movie,info=['main'])

        rand = random.sample(range(0,5),4)
        one = rand[0]
        actor = movie['cast'][one]
        self.answer_true = actor
        role = actor.currentRole
        self.ques = 'Aşağıdakilerden hangisi {1} yapımı olan {0} filminde {2} adlı karakteri canlandıran oyuncudur?'.format(movie['title'],movie['year'],role)
        
        two = rand[1]
        actor = movie['cast'][two]
        self.add_answer_false(actor)

        three = rand[2]
        actor = movie['cast'][three]
        self.add_answer_false(actor)

        four = rand[3]
        actor = movie['cast'][four]
        self.add_answer_false(actor)
##topMoviesActor








##topMoviesActorMovie
###level_2 question (medium) 
###true selection is chosen randomly
    def topMoviesActorMovieTwo(self):
        moviesDB = IMDb()
        top = moviesDB.get_top250_movies()
        isFind = False
        num = 0
        movie = top[0]
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
        self.ques = '{0} isimli oyuncu aşağıdaki filmlerden hangisinde rol almamıştır?'.format(actor)

       
        #moviesDB.update(movie['cast'][index])  
        #num = len(movie['cast'][index]['filmography'][0]['actor'])      #####KeyError: 'actor'   
        rand_index = random.sample(range(0,num),2) #movies of actor1        #############Sample larger than population or is negative
        self.add_answer_false(movie['title'])
        movie_index = rand_index[0]
        new_id = 0
        if list(movie['cast'][index_one]['filmography'][0])[0] == "actor":         
            new_id = movie['cast'][index_one]['filmography'][0]['actor'][movie_index].movieID
        elif list(movie['cast'][index_one]['filmography'][0])[0] == "actress":
            new_id = movie['cast'][index_one]['filmography'][0]['actress'][movie_index].movieID
        #new_id = movie['cast'][index]['filmography'][0]['actor'][movie_index].movieID
        newMovie = moviesDB.get_movie(new_id)
        self.add_answer_false(newMovie['title'])
        movie_index = rand_index[1]
        new_id = 0
        if list(movie['cast'][index_one]['filmography'][0])[0] == "actor":         
            new_id = movie['cast'][index_one]['filmography'][0]['actor'][movie_index].movieID
        elif list(movie['cast'][index_one]['filmography'][0])[0] == "actress":
            new_id = movie['cast'][index_one]['filmography'][0]['actress'][movie_index].movieID
        #new_id = movie['cast'][index]['filmography'][0]['actor'][movie_index].movieID
        newMovie = moviesDB.get_movie(new_id)
        self.add_answer_false(newMovie['title'])
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
                    self.answer_true = new_movie['title']
                    flag = False
                    break  


###level_3 question (hard) 
###true selection is chosen among another movies of other leading actor/actress
    def topMoviesActorMovieThree(self):
        moviesDB = IMDb()
        top = moviesDB.get_top250_movies()
        isFind = False
        num = 0
        movieNum = 0
        movie = top[0]
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
        #movieID = randrange(0,250)
        #movie = top[movieID]
        #moviesDB.update(movie,info=['main'])
        #rand = random.sample(range(0,5),2)

        #index = rand[0] #actor
        actor = movie['cast'][index_one]
        self.ques = '{0} isimli oyuncu aşağıdaki filmlerden hangisinde rol almamıştır?'.format(actor)

       
        #moviesDB.update(movie['cast'][index])  
        #num = len(movie['cast'][index]['filmography'][0]['actor'])      #####KeyError: 'actor'   
        rand_index = random.sample(range(0,num),2) #movies of actor1        #############Sample larger than population or is negative
        self.add_answer_false(movie['title'])
        movie_index = rand_index[0]
        new_id = 0
        if list(movie['cast'][index_one]['filmography'][0])[0] == "actor":         
            new_id = movie['cast'][index_one]['filmography'][0]['actor'][movie_index].movieID
        elif list(movie['cast'][index_one]['filmography'][0])[0] == "actress":
            new_id = movie['cast'][index_one]['filmography'][0]['actress'][movie_index].movieID
        #new_id = movie['cast'][index]['filmography'][0]['actor'][movie_index].movieID
        newMovie = moviesDB.get_movie(new_id)
        self.add_answer_false(newMovie['title'])
        movie_index = rand_index[1]
        new_id = 0
        if list(movie['cast'][index_one]['filmography'][0])[0] == "actor":         
            new_id = movie['cast'][index_one]['filmography'][0]['actor'][movie_index].movieID
        elif list(movie['cast'][index_one]['filmography'][0])[0] == "actress":
            new_id = movie['cast'][index_one]['filmography'][0]['actress'][movie_index].movieID
        #new_id = movie['cast'][index]['filmography'][0]['actor'][movie_index].movieID
        newMovie = moviesDB.get_movie(new_id)
        self.add_answer_false(newMovie['title'])
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
                self.answer_true = newMovie['title']
                flag = False
                break

##topMoviesActorMovie












##topMoviesCast    
##level_2 question (medium)
##true selection is from top three actor/actress of movie
##false selections from random other three movies 
    def topMoviesCastTwo(self):
        moviesDB = IMDb()
        top = moviesDB.get_top250_movies()
        movieID = randrange(0,250)
        movie = top[movieID]
        moviesDB.update(movie,info=['main'])
        rand = random.sample(range(0,3),1)
        index = rand[0]       

        self.ques = 'Aşağıdakilerden hangisi {1} yapımı olan {0} filminde oynamıştır?'.format(movie['title'],movie['year'])        
        
        self.answer_true = movie['cast'][index]['name']
        
        
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
                        self.add_answer_false(new_movie['cast'][c]['name'])
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
                        self.add_answer_false(new_movie['cast'][c]['name'])
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
                        self.add_answer_false(new_movie['cast'][c]['name'])
                        flag = False
                        break



##level_3 question (hard)
##true selection is from top three actor/actress of movie
##false selections are leading actor/actress from other three movies of leading actor/actress of asked movie

    def topMoviesCastThree(self):
        moviesDB = IMDb()
        top = moviesDB.get_top250_movies()
        isFind = False
        movieNum = 0
        movie = top[0]
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

        self.ques = 'Aşağıdakilerden hangisi {1} yapımı olan {0} filminde oynamıştır?'.format(movie['title'],movie['year'])        
        
        self.answer_true = movie['cast'][index]['name']   

        
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
                        self.add_answer_false(newMovie['cast'][c]['name'])
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
                        self.add_answer_false(newMovie['cast'][c]['name'])
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
                        self.add_answer_false(newMovie['cast'][c]['name'])
                        flag = False
                        break
##topMoviesCast