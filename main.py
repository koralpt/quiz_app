from question_data import questions
from question_model import Question
from quiz_function import QuizFunction
from ui import QuizInterface

question_list = []
for question in questions:
    question_text = question['question']
    answer = question['correct_answer']
    new_question = Question(question_text, answer)
    question_list.append(new_question)

quiz = QuizFunction(question_list)
quiz_ui = QuizInterface(quiz)

