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

        self.NameLabel = Label(self.Welcome, text = "name", anchor = W, fg = "black", width = 10, padx= 30, pady = 10)
        self.NameLabel.grid(row=2, column=0)

        self.AgeLabel = Label(self.Welcome, text = "age", anchor=W, fg = "black", width = 10, padx= 30, pady = 10)
        self.AgeLebel.grid(row=3, column=0)

        self.NameEntry=ttk.Entry(self.Welcome, width = 20)
        self.NameEntry.grid(row=3, column = 1, columnspan =2)

        self.AgeEntry=ttk.Entry(self.Welcome, width = 20)
        self.AgeEntry.grid(row=3, column = 1)

        self.DifficultyLabel = Label(self.Welcome, text = "Choose difficulity level", anchor = W, fg = "black", width = 10, padx = 30, pady = 10)
        self.DifficultyLabel.grid(row=4, column=0)

        self.difficulty = ["Easy", "Medium", "Hard", "Super Hard"]
        self.diff_lvl = StringVar()
        self.diff_level.set(0)
        self.diff_btns = []

        for i in range(len(self.difficulty)):
            rb = Radiobutton(self.Welcome, variable = self.diff_lvl, value = 1, text = selff.difficulty[i], anchor = W, padx = 50, width = "5", height = "2")
            self.diff_btns.append(rb)
            rb.grid(row= i+5, column = 0, sticky = W)

def Show_Welcome(self):
    self.Questions.grid_remove()
    self.Welcome.grid()

def Show_Questions(self):
    self.Welcome.grid_remove()
    self.Questions.grid()


if __name__ == "__main__":
    root= Tk()
    frames = maths(root)
    
    root.title("Quiz")
    root.mainloop()