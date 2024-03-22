import random

class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

class FlashcardApp:
    def __init__(self):
        self.flashcards = []

    def add_flashcard(self, question, answer):
        flashcard = Flashcard(question, answer)
        self.flashcards.append(flashcard)
        print('Flashcard Added!')

    def review_flashcards(self):
        score = 0
        random.shuffle(self.flashcards)
        for flashcard in self.flashcards:
            print("Question: ", flashcard.question)
            input("Enter any key to reveal the answer")
            print("Answer: ", flashcard.answer)
            recalled_or_no = input("How well did you recalled the info? [Forgot], [Partially Recalled], [Recalled Easily]: ")
            if recalled_or_no.lower()  == 'forgot':
                print("No Worries, keep practicing!")

            elif recalled_or_no.lower() == 'partially recalled':
                print("Almost There! You're making progress :)")
                score += 0.5
            elif recalled_or_no.lower() == 'recalled easily':
                print("Correct, good job!")
                score += 1
        print(f"Your Score: {score}")
            
        input("Press Enter to continue: ")

    def run(self):
        while True:
            print("\nFlashcard App Menu:")
            print("1. Add Flashcard")
            print("2. Review Flashcards")
            print("3. Exit")
        
            selected_choice = input("Enter your choice\n")

            if selected_choice == '1':
                question = input("Enter your question: ")
                answer = input("Enter your answer: ")
                self.add_flashcard(question, answer)

            elif selected_choice == '2':
                if not self.flashcards:
                    print("You currently have no flashcards. Add them first.")
                else:
                    self.review_flashcards()
            
            elif selected_choice == '3':
                    while True:
                        exit_confirm = input("Are you sure you want to exit the Flashcard App? (y/n)")
                    
                        if exit_confirm == 'y':
                            return
                        elif exit_confirm == 'n':
                            break

if __name__ == "__main__":
    app = FlashcardApp()
    app.run()

                