from tkinter import*
from tkinter import ttk 

class maths:
    def __innit__(self,parent):

        self.Welcome = Frame(parent)
        self.Welcome.grid(row=0,column=1)

        self.TitleLabel = Label(self.Welcome, text = "Welcome to the Maths Quiz", bg = "black", fg = "white", width = 20, padx = 30, pady = 10)
        self.TitleLabel.grid(columnspan=2)

        self.NextButton = ttk.Button(self.Welcome, text = "next", command = Show_Questions)
        self.NextButton.grid(row=8, column=1)

        self.Questions = Frame(parent)
        self.Questions.grid(row=0, column = 1)

        self.QuestionsLabel= Label(self.Questions, text = "quiz questions", bg = "black", fg = "white", width = 20, padx = 30, pady = 10)
        self.QuestionsLabel.grid(columnspan=2)

        self.HomeButton = ttk.Button(self.Questions, text = "home", command = Show_Welcome)
        self.HomeButton.grid(row=8, column=1)

def Show_Welcome(self):
    self.Questions.grid_remove()
    self.Welcome.grid()

def Show_Questions(self):
    self.Welcome.grid_remove()
    self.Questions.grid()

if __name__ == "__main__":
    root= Tk()
    frames = maths()
    root.title("Quiz")
    root.mainloop()