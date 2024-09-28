from tkinter import *
from quiz_function import QuizFunction

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_func: QuizFunction):
        self.quiz = quiz_func
        self.window = Tk()
        self.window.title('Quiz App')
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_label = Label(text='Score: 0', fg="white",
                                 bg=THEME_COLOR, font=('Ariel', 12, 'bold'))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            text='Some Text',
            fill=THEME_COLOR,
            font=('Ariel', 18, 'italic')
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true)
        self.true_button.grid(row=2, column=1)
        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false)
        self.false_button.grid(row=2, column=0)
        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg='white')
        self.true_button.config(state='normal')
        self.false_button.config(state='normal')
        if self.quiz.has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f'You have reached the end of the quiz.'
                                                            f'Your final score was: {self.quiz.score}/{self.quiz.question_number}')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def true(self):
        self.feedback(self.quiz.check_answer('True'))

    def false(self):
        self.feedback(self.quiz.check_answer('False'))


    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
            self.score_label.config(text=f'Score: {self.quiz.score}')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
        else:
            self.canvas.config(bg='red')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
        self.window.after(1000, self.get_next_question)





