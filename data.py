class Data:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.hearth = 3
        self.flag = True
        self.random = 0

    def reconstitute(self):
        self.score = 0
        self.level = 1
        self.hearth = 3

    def update_score(self):
        self.score = self.score + 10

    def update_level(self):
        self.level = self.level + 1
    
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