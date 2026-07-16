from quizz_data import question_data
from quizz_questions import Question
from quizz_brain import Quizz_brain

question_bank=[]
for questions in question_data:
    question_text=questions["text"]
    question_answer=questions["answer"]
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)


quiz=Quizz_brain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
    