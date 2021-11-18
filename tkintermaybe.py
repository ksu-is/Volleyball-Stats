# My Vollyeyball project

from tkinter import *
#Key down function
def click():
    entered_text = textentry.get()


# main:
window = Tk()
window.geometry('1000x1000')
window.title("Volleyball Statistics")
window.configure(background = "white")

# Logo
logo = PhotoImage(file="Volleyball Stats.gif")
Label (window, image=logo, bg = "white").grid(row=0, column=0)

# Player Name Input
Label(window, text = "Enter a player's name: ", bg = "white", font = "None 12 bold").grid(row=1, column=0,sticky = W)
textentry = Entry(window, width=20, bg="dark grey")
textentry.grid(row=2, column = 0, sticky = W)

Button (window, text = "ENTER", width = 5 , command = click).grid(row = 3 , column=0, sticky = W)


# Jersey Number Input
Label(window, text = "\nEnter a player's jersey number: ", bg = "white", font = "None 12 bold").grid(row=4, column=0,sticky = W)
textentry = Entry(window, width=20, bg="dark grey")
textentry.grid(row=5, column = 0, sticky = W)

Button (window, text = "ENTER", width = 5 , command = click).grid(row = 7 , column=0, sticky = W)


player_list = []

window.mainloop()


