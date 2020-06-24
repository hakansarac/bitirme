from quiz import Quiz 
from answer import Answer
from imdb import IMDb
from random import randrange
import random

class Question:
    def __init__(self):
        self.ques = ""
        self.answerOne = ""
        self.answerTwo = ""
        self.answerThree = ""
        self.answerFour = ""


###topMoviesYear
    def topMoviesYearOne(self):
        moviesDB = IMDb()
        top = moviesDB.get_top250_movies()
        movieID = randrange(0,250)
        chance = 0
        self.ques = '{0} filmi hangi sene vizyona girmiştir?'.format(top[movieID]['title'])
        self.answerOne = top[movieID]['year']

        if self.answerOne>=2012 and self.answerOne<=2014:
            chance = randrange(3)        
        elif self.answerOne>=2015 and self.answerOne<=2017:
            chance = randrange(2)
        elif self.answerOne>=2018:
            chance = randrange(1)
        else:
            chance = randrange(4)

        
        if chance == 0:
            self.answerTwo = top[movieID]['year']-3
            self.answerThree = top[movieID]['year']-6
            self.answerFour = top[movieID]['year']-9
        elif chance == 1:
            self.answerTwo = top[movieID]['year']+3
            self.answerThree = top[movieID]['year']-6
            self.answerFour = top[movieID]['year']-3
        elif chance == 2:
            self.answerTwo = top[movieID]['year']+3
            self.answerThree = top[movieID]['year']+6
            self.answerFour = top[movieID]['year']-3
        elif chance == 3:    
            self.answerTwo = top[movieID]['year']+3
            self.answerThree = top[movieID]['year']+6
            self.answerFour = top[movieID]['year']+9


    def topMoviesYearTwo(self):
        moviesDB = IMDb()
        top = moviesDB.get_top250_movies()
        movieID = randrange(0,250)
        chance = 0
        self.ques = '{0} filmi hangi sene vizyona girmiştir?'.format(top[movieID]['title'])
        self.answerOne = top[movieID]['year']

        if self.answerOne>=2015 and self.answerOne<=2016:
            chance = randrange(3)        
        elif self.answerOne>=2017 and self.answerOne<=2018:
            chance = randrange(2)
        elif self.answerOne>=2019:
            chance = randrange(1)
        else:
            chance = randrange(4)

        
        if chance == 0:
            self.answerTwo = top[movieID]['year']-6
            self.answerThree = top[movieID]['year']-4
            self.answerFour = top[movieID]['year']-2
        elif chance == 1:
            self.answerTwo = top[movieID]['year']+2
            self.answerThree = top[movieID]['year']-4
            self.answerFour = top[movieID]['year']-2
        elif chance == 2:
            self.answerTwo = top[movieID]['year']+2
            self.answerThree = top[movieID]['year']+4
            self.answerFour = top[movieID]['year']-2
        elif chance == 3:    
            self.answerTwo = top[movieID]['year']+2
            self.answerThree = top[movieID]['year']+4
            self.answerFour = top[movieID]['year']+6


    def topMoviesYearThree(self):
        moviesDB = IMDb()
        top = moviesDB.get_top250_movies()
        movieID = randrange(0,250)
        chance = 0
        self.ques = '{0} filmi hangi sene vizyona girmiştir?'.format(top[movieID]['title'])
        self.answerOne = top[movieID]['year']

        if self.answerOne==2018:
            chance = randrange(3)        
        elif self.answerOne==2019:
            chance = randrange(2)
        elif self.answerOne==2020:
            chance = randrange(1)
        else:
            chance = randrange(4)

        
        if chance == 0:
            self.answerTwo = top[movieID]['year']-3
            self.answerThree = top[movieID]['year']-2
            self.answerFour = top[movieID]['year']-1
        elif chance == 1:
            self.answerTwo = top[movieID]['year']+1
            self.answerThree = top[movieID]['year']-2
            self.answerFour = top[movieID]['year']-1
        elif chance == 2:
            self.answerTwo = top[movieID]['year']+1
            self.answerThree = top[movieID]['year']+2
            self.answerFour = top[movieID]['year']-1
        elif chance == 3:    
            self.answerTwo = top[movieID]['year']+1
            self.answerThree = top[movieID]['year']+2
            self.answerFour = top[movieID]['year']+3
    
##topMoviesYear







##topMoviesDirectors
    def topMoviesDirectorsOne(self):
        moviesDB = IMDb()
        top = moviesDB.get_top250_movies()
        movieID = randrange(0,250)
        movie = top[movieID]
        moviesDB.update(movie,info=['main'])
        self.ques = '{1} yapımı olan {0} filminin yönetmeni kimdir?'.format(movie['title'],movie['year'])
        self.answerOne = movie['directors'][0]['name'] 
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
                    self.answerTwo = movie['cast'][c]['name']
                elif answer_coun==2:
                    self.answerThree = movie['cast'][c]['name']
                elif answer_coun==3: 
                    self.answerFour = movie['cast'][c]['name']            
                    break

    def topMoviesDirectorsTwoThree(self):
        moviesDB = IMDb()
        top = moviesDB.get_top250_movies()
        movieID = randrange(0,250)
        movie = top[movieID]
        moviesDB.update(movie,info=['main'])
        self.ques = '{1} yapımı olan {0} filminin yönetmeni kimdir?'.format(movie['title'],movie['year'])
        self.answerOne = movie['directors'][0]['name'] 
        flag=True
        while flag:
            filmID = randrange(0,250)
            moviesDB.update(top[filmID],info=['main'])
            for genre in movie['genres']:
                for gen in top[filmID]['genres']:
                    if gen == genre:                        
                        film = top[filmID]
                        if film['directors'][0]['name'] != self.answerOne:
                            self.answerTwo = film['directors'][0]['name']                                               
                            flag = False
        flag=True
        while flag:
            filmID = randrange(0,250)
            moviesDB.update(top[filmID],info=['main'])
            for genre in movie['genres']:
                for gen in top[filmID]['genres']:
                    if gen == genre:                        
                        film = top[filmID]
                        if film['directors'][0]['name'] != self.answerOne and film['directors'][0]['name'] != self.answerTwo:
                            self.answerThree = film['directors'][0]['name']
                            flag = False
        flag=True
        while flag:
            filmID = randrange(0,250)
            moviesDB.update(top[filmID],info=['main'])
            for genre in movie['genres']:
                for gen in top[filmID]['genres']:
                    if gen == genre:                        
                        film = top[filmID]
                        if film['directors'][0]['name'] != self.answerOne and film['directors'][0]['name'] != self.answerTwo and film['directors'][0]['name'] != self.answerThree:
                            self.answerFour = film['directors'][0]['name']
                            flag = False

##topMoviesDirectors







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
            self.answerTwo = movie['cast'][0]['name']
            self.answerThree = movie['cast'][1]['name']
            self.answerFour = movie['cast'][2]['name']
        else:
            rand = random.sample(range(0,5),3)
            index = rand[0]
            self.answerTwo = movie['cast'][index]['name']
            index = rand[1]
            self.answerThree = movie['cast'][index]['name']
            index = rand[2]
            self.answerFour = movie['cast'][index]['name']
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
                        if newMovie['cast'][c]['name'] == movie['cast'][j]['name']:
                            control_c +=1 
                    if control_c == 0:
                        self.answerOne = newMovie['cast'][c]['name']
                        flag = False
                        break


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
            self.answerTwo = movie['cast'][0]['name']
            self.answerThree = movie['cast'][1]['name']
            self.answerFour = movie['cast'][2]['name']
        else:
            rand = random.sample(range(0,5),3)
            index = rand[0]
            self.answerTwo = movie['cast'][index]['name']
            index = rand[1]
            self.answerThree = movie['cast'][index]['name']
            index = rand[2]
            self.answerFour = movie['cast'][index]['name']
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
                        self.answerOne = newMovie['cast'][c]['name']
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
                        self.answerOne = newMovie['cast'][c]['name']
                        flag = False
                        break  
##topMoviesNotCast









##topMoviesRole
    def topMoviesRoleTwo(self):
        moviesDB = IMDb()
        top = moviesDB.get_top250_movies()
        movieID = randrange(0,250)
        movie = top[movieID]
        moviesDB.update(movie,info=['main'])

        rand = random.sample(range(0,5),1)
        one = rand[0]
        actor = movie['cast'][one]
        self.answerOne = actor.currentRole
        self.ques = 'Aşağıdakilerden hangisi {1} yapımı olan {0} filminde {2} adlı oyuncunun canlandırdığı karakterdir?'.format(movie['title'],movie['year'],movie['cast'][one])
        
        new_movieID = randrange(0,250)
        new_movie = top[new_movieID]
        moviesDB.update(new_movie,info=['main'])
        if new_movie['title'] != new_movie['title']:
            actor = new_movie['cast'][0]
            self.answerTwo = actor.currentRole
            
            actor = new_movie['cast'][1]
            self.answerThree = actor.currentRole
            
            actor = new_movie['cast'][2]
            self.answerFour = actor.currentRole


    def topMoviesRoleThree(self):
        moviesDB = IMDb()
        top = moviesDB.get_top250_movies()
        movieID = randrange(0,250)
        movie = top[movieID]
        moviesDB.update(movie,info=['main'])

        rand = random.sample(range(0,5),4)
        one = rand[0]
        actor = movie['cast'][one]
        self.answerOne = actor.currentRole
        self.ques = 'Aşağıdakilerden hangisi {1} yapımı olan {0} filminde {2} adlı oyuncunun canlandırdığı karakterdir?'.format(movie['title'],movie['year'],movie['cast'][one])
        
        two = rand[1]
        actor = movie['cast'][two]
        self.answerTwo = actor.currentRole

        three = rand[2]
        actor = movie['cast'][three]
        self.answerThree = actor.currentRole

        four = rand[3]
        actor = movie['cast'][four]
        self.answerFour = actor.currentRole

##topMoviesRole











##topMoviesActor
    def topMoviesActorOne(self):
        moviesDB = IMDb()
        top = moviesDB.get_top250_movies()
        movieID = randrange(0,250)
        movie = top[movieID]
        moviesDB.update(movie,info=['main'])

        rand = random.sample(range(0,5),4)
        one = rand[0]
        actor = movie['cast'][one]
        self.answerOne = actor
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
                            self.answerTwo = new_movie['cast'][c]['name']
                        elif flag_coun == 2:
                            self.answerThree = new_movie['cast'][c]['name'] 
                        elif flag_coun == 3:
                            self.answerFour = new_movie['cast'][c]['name']
                            flag=False
                            break                        


    def topMoviesActorTwoThree(self):
        moviesDB = IMDb()
        top = moviesDB.get_top250_movies()
        movieID = randrange(0,250)
        movie = top[movieID]
        moviesDB.update(movie,info=['main'])

        rand = random.sample(range(0,5),4)
        one = rand[0]
        actor = movie['cast'][one]
        self.answerOne = actor
        role = actor.currentRole
        self.ques = 'Aşağıdakilerden hangisi {1} yapımı olan {0} filminde {2} adlı karakteri canlandıran oyuncudur?'.format(movie['title'],movie['year'],role)
        
        two = rand[1]
        actor = movie['cast'][two]
        self.answerTwo = actor

        three = rand[2]
        actor = movie['cast'][three]
        self.answerThree = actor

        four = rand[3]
        actor = movie['cast'][four]
        self.answerFour = actor
##topMoviesActor








##topMoviesActorMovie
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
        self.answerTwo = movie['title']
        movie_index = rand_index[0]
        new_id = 0
        if list(movie['cast'][index_one]['filmography'][0])[0] == "actor":         
            new_id = movie['cast'][index_one]['filmography'][0]['actor'][movie_index].movieID
        elif list(movie['cast'][index_one]['filmography'][0])[0] == "actress":
            new_id = movie['cast'][index_one]['filmography'][0]['actress'][movie_index].movieID
        #new_id = movie['cast'][index]['filmography'][0]['actor'][movie_index].movieID
        newMovie = moviesDB.get_movie(new_id)
        self.answerThree = newMovie['title']
        movie_index = rand_index[1]
        new_id = 0
        if list(movie['cast'][index_one]['filmography'][0])[0] == "actor":         
            new_id = movie['cast'][index_one]['filmography'][0]['actor'][movie_index].movieID
        elif list(movie['cast'][index_one]['filmography'][0])[0] == "actress":
            new_id = movie['cast'][index_one]['filmography'][0]['actress'][movie_index].movieID
        #new_id = movie['cast'][index]['filmography'][0]['actor'][movie_index].movieID
        newMovie = moviesDB.get_movie(new_id)
        self.answerFour = newMovie['title']
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
                    self.answerOne = new_movie['title']
                    flag = False
                    break  


##
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
        self.answerTwo = movie['title']
        movie_index = rand_index[0]
        new_id = 0
        if list(movie['cast'][index_one]['filmography'][0])[0] == "actor":         
            new_id = movie['cast'][index_one]['filmography'][0]['actor'][movie_index].movieID
        elif list(movie['cast'][index_one]['filmography'][0])[0] == "actress":
            new_id = movie['cast'][index_one]['filmography'][0]['actress'][movie_index].movieID
        #new_id = movie['cast'][index]['filmography'][0]['actor'][movie_index].movieID
        newMovie = moviesDB.get_movie(new_id)
        self.answerThree = newMovie['title']
        movie_index = rand_index[1]
        new_id = 0
        if list(movie['cast'][index_one]['filmography'][0])[0] == "actor":         
            new_id = movie['cast'][index_one]['filmography'][0]['actor'][movie_index].movieID
        elif list(movie['cast'][index_one]['filmography'][0])[0] == "actress":
            new_id = movie['cast'][index_one]['filmography'][0]['actress'][movie_index].movieID
        #new_id = movie['cast'][index]['filmography'][0]['actor'][movie_index].movieID
        newMovie = moviesDB.get_movie(new_id)
        self.answerFour = newMovie['title']
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
                self.answerOne = newMovie['title']
                flag = False
                break

##topMoviesActorMovie












##topMoviesCast    
    def topMoviesCastThree(self):
        moviesDB = IMDb()
        top = moviesDB.get_top250_movies()
        isFind = False
        movieNum = 0
        movie = top[0]
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
        
        self.answerOne = movie['cast'][index]['name']   

        
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
                        self.answerTwo = newMovie['cast'][c]['name']
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
                        self.answerThree = newMovie['cast'][c]['name']
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
                        self.answerFour = newMovie['cast'][c]['name']
                        flag = False
                        break
##topMoviesCast





    def get_question(self):
        return self.ques
    
    def get_answer_one(self):
        return self.answerOne
    
    def get_answer_two(self):
        return self.answerTwo
    
    def get_answer_three(self):
        return self.answerThree
    
    def get_answer_four(self):
        return self.answerFour