from answer import Answer

class Quiz:
    def __init__(self):
        self.answers = {}
        self.question = ""
        self._last_answer_key = 0

    def add_answer(self, answer):
        self._last_answer_key += 1
        self.answers[self._last_answer_key] = answer
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