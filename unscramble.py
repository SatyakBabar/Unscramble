#!/usr/bin/env python3


#Python GUI application/game to unscramble 10 TV shows and maximize the score
#Creator:Satyak Babar



#import the python framework tkinter for GUI
from tkinter import *
from tkinter import messagebox
import random


showlist = ( "Jessica Jones", "The Walking Dead", "Grey's Anatomy", "This Is Us","Arrow",
              "Game of Thrones ", "Homeland", "Sneaky Pete", "The Good Doctor",  "Lucifer",
              "Supernatural", "Shameless", "Black Mirror ", "Vikings","Love",
              "Altered Carbon", "Riverdale","The Blacklist","Gotham","The Flash ",
        "Criminal Minds","Stranger Things","Friends","Timeless","The Office", 
        "Money Heist","Modern Family","Westworld","The Big Bang Theory","Suits")


#Function to return the scrambled TV Show Name
def getScrambled():
    show = random.choice(showlist).upper()
    scrambled_list = list(show.replace(" ", ""))
    random.shuffle(scrambled_list)
    scrambled = ''.join(scrambled_list)
    return show, scrambled


class Application(Frame):
    """A GUI Application"""

    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=BOTH, expand=1, padx=10, pady=10) 

        self.columnconfigure(0, weight=1)
        for i in range(7):
            self.rowconfigure(i, weight=1)

        self.guess_ent = None
        self.scrambled_label = None
        self.tries = 1
        self.sum = 0

        self.displayComponents()
        self.new_game()



    def displayComponents(self):
        welcome = Label(self, text="Welcome!", font="bold")
        tryto = Label(self, text="Guess the TV show")
        scrambled = Label(self, font="sans-serif 12 bold", fg="red")
        yourguess = Label(self, text="What is your guess? ")
        guess_ent = Entry(self, font="sans-serif 12")
        submit = Button(self, text="Submit", command=self.guessing)

        welcome.grid(row=0, column=0, sticky=N+E+W+S)
        tryto.grid(row=1, column=0, sticky=N+E+W+S)
        scrambled.grid(row=2, column=0, sticky=N+E+W+S)
        yourguess.grid(row=4, column=0, sticky=W)
        guess_ent.grid(row=5, column=0, sticky=N+E+W+S)
        submit.grid(row=6, column=0, sticky=N+S, pady=5)

        self.guess_ent = guess_ent
        self.scrambled_label = scrambled
        root.bind("<Return>", self.guessing)


    def reset_input(self):
        self.guess_ent.delete(0, END)


    def guessing(self, event=None):
        guess = self.guess_ent.get().upper()
        show = self.the_show
        if not guess:
            return
        #loop to run the play 10 times    
        if self.tries<11:
            if guess != show:#if answer is incorrect just display the score
                title, message = "Wrong, Score=", self.sum
                messagebox.showwarning(title, message)
                self.new_game()
                return
            self.sum += 1#if answer is correct increase score by 1 and display
            title, message = "Correct, Score=", self.sum
            messagebox.showwarning(title, message)
            self.new_game()
            return
        else:#if game is played 10 times display the score and quit(root.destroy())
            title, message = "Game Over!! Your Score:", self.sum
            messagebox.showwarning(title, message)
            self.new_game()
            root.destroy()


    def new_game(self):#new play starts here
        self.the_show, self.scrambled = getScrambled()
        self.scrambled_label.configure(text=self.scrambled)
        self.reset_input()
        self.tries += 1#keeps count of the number of plays/chances played

     



if __name__ == "__main__":
    root = Tk()
    root.geometry("400x200")
    root.resizable(width=False, height=False)
    root.title("UnScramble")
    app = Application(root)
    root.mainloop()
