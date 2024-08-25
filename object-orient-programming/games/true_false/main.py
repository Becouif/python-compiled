from question_model import Question

from data import question_data
question_bank = []

# we loop through questions from data file

for question in question_data:
  # we tap into the data file keys 
  # and we assign them to variables
  question_text = question["text"]
  question_answer = question['answer']
  # here we create a new question object
  # and we append it to the question bank
  new_question = Question(question_text, question_answer)
  question_bank.append(new_question)



