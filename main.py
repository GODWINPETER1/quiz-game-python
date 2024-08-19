from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [];


for questions in question_data:
    
    question_text = questions['text']
    question_ans = questions['answer']
    new_questions = Question(question_text , question_ans)
    new_q_list = question_bank.append(new_questions)

quiz = QuizBrain(question_bank)
print(quiz.next_question())