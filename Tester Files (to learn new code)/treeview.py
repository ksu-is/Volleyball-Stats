from tkinter import *
from tkinter import ttk


window = Tk()
window.geometry('1000x1000')
window.title("My Team Stats")
window.configure(background = "white")

volleyball = ttk.Treeview(window)

def view_table():
 # Define our Columns
    volleyball['columns'] = ("Name", "Serve", "Serve Receive", "Digs", "Assits", "Attacks", "Blocks", "%")

 # Formatting Columns
    volleyball.column("#0", width = 0, stretch= NO)
    volleyball.column("Name", anchor = CENTER, width = 120)
    volleyball.column("Serve", anchor = CENTER, width = 120)
    volleyball.column("Serve Receive", anchor = CENTER, width = 120)
    volleyball.column("Digs", anchor = CENTER, width = 120)
    volleyball.column("Assits", anchor = CENTER, width = 120)
    volleyball.column("Attacks", anchor = CENTER, width = 120)
    volleyball.column("Blocks", anchor = CENTER, width = 120)
    #volleyball.column("%", anchor = CENTER, width = 120)


 #Create Headings
    volleyball.heading("#0", text = "", anchor=CENTER)
    volleyball.heading("Name", text = "Name", anchor = CENTER)
    volleyball.heading("Serve", text = "Serve", anchor = CENTER)
    volleyball.heading("Serve Receive", text = "Serve Receive", anchor = CENTER)
    volleyball.heading("Digs", text = "Digs", anchor = CENTER)
    volleyball.heading("Assits", text = "Assits", anchor = CENTER)
    volleyball.heading("Attacks", text = "Attacks", anchor = CENTER)
    volleyball.heading("Blocks", text = "Blocks", anchor = CENTER)
    #volleyball.heading("%", text = "%", anchor = CENTER)

 # Add Data
    #Pulling from database
    data = [["Raven",3,2.5,2,2.7,1.35,3,2.21,3,3], ["Watts",3,2.5,2,2.7,1.35,3,2.21,3,3],["Volleyball",3,2.5,2,2.7,1.35,3,2.21,3,3],["Stats",3,2.5,2,2.7,1.35,3,2.21,3,3]]

    count = 0
    for record in data:
        volleyball.insert(parent = '', index = 'end', iid =count, text = "", values = (record[0], record[1],record[2], record[3],record[4], record[5],record[6], record[7])) 
        count += 1
    #volleyball.insert(parent = '', index = 'end', iid =0, text = "Parent", values = ("Raven",3,3,3,3,3,3,3,3,3,3))
    volleyball.pack()
view_table()


window.mainloop()
