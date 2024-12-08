from question_model import Question
from data import question_data,question_API
from quiz_brain import QuizBrain

question_bank = [] 
for question in question_data:
  question_text = question["text"]
  question_answer = question["answer"]
  new_question = Question(text=question_text,answer=question_answer)
  question_bank.append(new_question)
  


question_bankAPI = []
for question  in question_API:
  question_text = question["question"]
  question_answer = question["correct_answer"]
  new_question = Question(text=question_text,answer=question_answer)
  question_bankAPI.append(new_question)


# quiz = QuizBrain(question_list=question_bankAPI)
# while quiz.still_has_question():
#   quiz.next_question()
# quiz.finish()
quiz = QuizBrain(question_list=question_bank)
while quiz.still_has_question():
  quiz.next_question()
quiz.finish()