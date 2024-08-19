class QuizBrain:
    
    def __init__(self , q_list ):
        self.text_number = 0
        self.question_list = q_list
    
    # Method for the next question
    
    def next_question(self):
        score = 0
        while True:
            
            current_question = self.question_list[self.text_number]
            self.text_number += 1
            q_ans = input(f"Q{self.text_number}: {current_question.text}(True/False): ")
            
            if q_ans == current_question.answer:
                score += 1
                print("Your right!")
                print(f"Your final answer is : {current_question.answer}")
                print(f"Your score is: {score}")
            
            else:
                print("Your wrong!")
                print(f"Your final answer is : {current_question.answer}")
                print(f"Your score is: {score}")
                break