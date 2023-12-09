import random, sys
class Quiz:
    def __init__(self):
        pass
    
    question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can kill a small dog.", "answer": "True"}
]   
    question_number = 1
    question_index = 0
    score = 0

    def get_question(self):
        if self.question_number == 1:
            self.question_index = self.question_data.index(self.question_data[random.randint(0, len(self.question_data) - 1)])
            self.question_number += 1
            return self.question_data[self.question_index]["text"]
        else:
            self.question_index =  self.question_data.index(self.question_data[random.randint(0, len(self.question_data) - 1)])
            print(self.question_index)
            self.question_number += 1
            return self.question_data[self.question_index]['text']


    def check_question(self, user_answer):
        if self.question_data[self.question_index]["answer"] == user_answer:
            return True
        else:
            return False



    


user = Quiz()

quit = False
while quit != True:
    if user.check_question(input(f'{user.get_question()} True or False: ')) == True:
        user.score += 1
        print(f'Your score is {user.score}')
        if input('Type \'y\' to continue or \'n\' to quit: ').lower() == 'n':
            sys.exit('You quit the game.')
    else:
        print(f'Incorrect! Your score is {user.score}')
        sys.exit()