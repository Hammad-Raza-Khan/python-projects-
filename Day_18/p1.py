from x import question_data

class Question:
    
    def __init__(self, text, answer):
        self.text = text
        self.answer= answer
    
question_bank = []
for x in question_data:
    question_text = x["text"]
    question_answer = x["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
     
class QuizBrain:
    def __init__(self, list ):
        self.question_number = 0 
        self.score =  0
        self.question_list = list
         
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)
        
        
        
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Right")
        else:
            print("Wrong")
        print(f"Correct Answer: {correct_answer}")
        print(f"Current Score: {self.score}/{self.question_number}")
        
    
abc = QuizBrain(question_bank)

while abc.still_has_questions():
    abc.next_question()