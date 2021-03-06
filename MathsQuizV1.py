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


if __name__ == "__main__":
    root = Tk()
    frames = Math(root)
    root.title("Math quiz")
    root.mainloop() 