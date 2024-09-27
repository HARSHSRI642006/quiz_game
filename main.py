from question_model import Question
from data import question_data
from quiz_brain import Quizbrain
question_bank = []

for char in question_data:
    char_question = char["question"]
    char_answer = char["correct_answer"]
    new_question = Question(char_question,char_answer)
    question_bank.append(new_question)
     
quiz = Quizbrain(question_bank)

while quiz.still_has_questions():
 quiz.next_question()
 