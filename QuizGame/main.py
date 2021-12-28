
from question_model import Question
from data import question_data
from quiz_brain import Quiz
import random

question_list=[]
for q in question_data:
    QObj = Question(q["text"], q["answer"])
    question_list.append(QObj)

random.shuffle(question_list)
quiz = Quiz(question_list)

while quiz.stillHasQuestions():
    quiz.nextQuestion()
