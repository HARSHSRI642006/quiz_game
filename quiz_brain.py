class Quizbrain():
    
    def __init__(self,qlist) :
       self.question_number = 0
       self.score= 0
       self.question_list = qlist
       
    def still_has_questions(self):
         if self.question_number == len(self.question_list):
             print("You have completed this quiz")
             print(f"Your final score was:{self.score}/{len(self.question_list)}")
         return self.question_number < len(self.question_list)
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number+=1
        x=input(f"Q.{self.question_number}:{current_question.text}(True/False):")
        self.check_answer(x,current_question.answer)
    def check_answer(self,x,correct_answer):
        if x == correct_answer:
            self.score += 1
            print("You got it correct!")
            
        else:
            print("You,got it wrong!")
        print(f"The correct answer is {correct_answer}")    
        print(f"Your current score is :{self.score}/{self.question_number}")
        print("\n")




        




        
    