import random
from tkinter import *
from tkinter import Tk

class Math():
    def __init__(self, parent):
        

        self.Welcome = Frame(parent)
        self.Welcome.grid(row=0, column=0)
        
    
        self.TitleLabel = Label(self.Welcome, text = "Welcome", 
                                bg = "black", fg = "white", width = 20, padx = 30, 
                                pady = 10, font = ("comic sans ms", "14", "bold italic"))
        self.TitleLabel.grid(row = 0, columnspan = 2)
        
        
        self.LabelName = Label(self.Welcome, text = "Enter Name: ", 
                               fg = "black", padx = 5, pady = 5, 
                               font = ("comic sans ms", "10", "bold italic"))
        self.LabelName.grid(row = 1, column = 0)
        
        self.EnterName = Entry(self.Welcome)
        self.EnterName.grid(row = 1, column = 1)
        
     
        self.LabelAge = Label(self.Welcome, text = "Enter Age: ", 
                               fg = "black", padx = 5, pady = 5,
                               font = ("comic sans ms", "10", "bold italic"))
        self.LabelAge.grid(row = 2, column = 0)
        
        self.EnterAge = Entry(self.Welcome)
        self.EnterAge.grid(row = 2, column = 1)

        self.WarningLabel = Label(self.Welcome, text = '', anchor = W, fg = "red", width= 20, padx = 30, pady = 10)
        self.WarningLabel.grid(row = 4, columnspan = 1)

        self.DifficultyLabel = Label(self.Welcome, text = 'Choose diffculity', anchor = W, fg = "black", width= 14, padx = 30, pady = 20, font = ("Time", "12", "bold italic"))
        self.DifficultyLabel.grid(row = 5, column = 0)
        
        self.difficulty = ["Easy", "Medium", "Hard"]
        self.diff_lvl = StringVar()
        self.diff_lvl.set(0)
        self.diff_btns = []

        for i in range(len(self.difficulty)):
            rb = Radiobutton(self.Welcome, variable = self.diff_lvl, value = i, text = self.difficulty[i], anchor = W, padx = 50, width = "5", height = "2")
            self.diff_btns.append(rb)
            rb.grid(row = i+6, column = 0, sticky = W)

        self.Return = Label(self.Welcome, fg = "red",
                            font = ("comic sans ms", "10", "italic"))
        self.Return.grid(row = 3, column = 1)
        self.Return.configure(text = "")

        self.Toquiz = Button(self.Welcome, text = "Next", 
                             activebackground = "gray",
                             command = lambda:[self.UserDetails()])
        self.Toquiz.grid(row = 4, column = 0)



    def UserDetails(self):

        if self.EnterName.get() == "":
            self.Return.configure(text = "Please enter your name!")
        
        else:
            try:
                if int(self.EnterAge.get()) <= 5:
                    self.Return.configure(text = "You're too young!")
                
                elif int(self.EnterAge.get()) >= 16:
                    self.Return.configure(text = "You're too old!")
                    
                else:
                    self.ShowQuiz()
            
            except ValueError:
                self.Return.configure(text = "Please enter your \nage in numbers")

if __name__ == "__main__":
    root = Tk()
    frames = Math(root)
    root.title("Math quiz")
    root.mainloop() 