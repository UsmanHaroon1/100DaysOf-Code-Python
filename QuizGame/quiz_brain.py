class Quiz:
    def __init__(self,qlist):
        self.question_number=0
        self.score=0
        self.question_list=qlist

    def stillHasQuestions(self):
        return self.question_number<len(self.question_list)

    def nextQuestion(self):
        self.question_number+=1
        user_answer = input(f'Q{self.question_number}.{self.question_list[self.question_number-1].text}?(True/False)').title()
        self.checkAnswer(user_answer,self.question_list[self.question_number-1].answer)

    def checkAnswer(self,user_answer,correct_answer):
        if(user_answer == correct_answer):
            self.score+=1
            print("You got it Right")
            print(f"Correct answer is {correct_answer}")
            if self.question_number<len(self.question_list):
                print(f"Your current score is {self.score}/{self.question_number}")
            else:
                print(f"Your final score is {self.score}/{self.question_number}")
        else:
            print("You are wrong")
            if self.question_number <len(self.question_list):
                print(f"Your current score is {self.score}/{self.question_number}")
            else:
                print(f"Your final score is {self.score}/{self.question_number}")