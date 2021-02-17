from tkinter import*
from tkinter import ttk 
from random import*



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

        self.Problems = Label(self.Questions, text = "")
        self.Problems.grid(row=w, column = 0)

        self.next_button = ttk.Button9self.Questions, text = "Next Question", commant = self.next_question)
        self.next_button.grid(row=8, column=1)

        self.NameLabel = Label(self.Welcome, text = "name", anchor = W, fg = "black", width = 10, padx= 30, pady = 10)
        self.NameLabel.grid(row=2, column=0)

        self.AgeLabel = Label(self.Welcome, text = "age", anchor=W, fg = "black", width = 10, padx= 30, pady = 10)
        self.AgeLebel.grid(row=3, column=0)

        self.NameEntry=ttk.Entry(self.Welcome, width = 20)
        self.NameEntry.grid(row=3, column = 1, columnspan =2)

        self.AgeEntry=ttk.Entry(self.Welcome, width = 20)
        self.AgeEntry.grid(row=3, column = 1)

        self.WarningLabel= Label(self.Welcome, text = "", anchor  = W, fg = "red", width = 20, padx = 30, pady = 10)
        self.WarningLabel.grid(row=4, columnspan=2)


        self.DifficultyLabel = Label(self.Welcome, text = "Choose difficulity level", anchor = W, fg = "black", width = 10, padx = 30, pady = 10)
        self.DifficultyLabel.grid(row=4, column=0)

        self.difficulty = ["Easy", "Medium", "Hard", "Super Hard"]
        self.diff_lvl = StringVar()
        self.diff_level.set(0)
        self.diff_btns = []

        for i in range(len(self.difficulty)):
            rb = Radiobutton(self.Welcome, variable = self.diff_lvl, value = 1, text = self.difficulty[i], anchor = W, padx = 50, width = "5", height = "2")
            self.diff_btns.append(rb)
            rb.grid(row= i+5, column = 0, sticky = W)
        
        
        

def next_question(self):
    x = randrange(10)
    y = randrange(10)
    self.answer = x + y

    question_text = str(x) + " + " + str(y) + " = "
    self.Problems.configure(text = question_text)

def Show_Welcome(self):
    self.Questions.grid_remove()
    self.Welcome.grid()

    try:
        if self.NameEntry.get() == " ":
            self.WarningLabel.congifure(text="Please Enter a Name")
            self.NameEntry.focus()

        elif self.NameEntry.get.isalpha() == False:
            self.WarningLabel.configure(text ="Please enter text")
            self.NameEntry.delete(0, END)
            self.NameEntry.focus()

        elif self.AgeEntry.get() == " ":
            self.WarningLabel.congifure(text="Please Enter an Age")
            self.AgeEntry.focus()   

        elif int(self.AgeEntry.get()) > 12:
            self.WarningLabel.configure(text ="You are too old!")
            self.AgeEntry.delete(0, END)
            self.AgeEntry.focus()

        elif int(self.AgeEntry.get()) < 0:
            self.WarningLabel.configure(text ="Enter a valid age")
            self.AgeEntry.delete(0, END)
            self.AgeEntry.focus()

        elif int(self.AgeEntry.get()) < 7:
            self.WarningLabel.configure(text ="You are too young")
            self.AgeEntry.delete(0, END)
            self.AgeEntry.focus()
        
        else:
            self.Welcome.grid_remove()
            self.Questions.grid()
    
    except ValueError:
        self.WarningLabel.configure(text = "Please enter a number")
        self.AgeEntry.delete(0,END)
        self.AgeEntry.focus()





def Show_Questions(self):
    self.Welcome.grid_remove()
    self.Questions.grid()

if __name__ == "__main__":
    root= Tk()
    frames = maths()
    
    root.title("Quiz")
    root.mainloop()