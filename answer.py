class Answer:
    def __init__(self,selection,is_true):
        self.selection = selection
        self.is_true = is_true
        
    def answerisTrue(self):
        if self.is_true==True:
            return True
        else:
            return False