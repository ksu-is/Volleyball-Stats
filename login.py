from tkinter import * 

root = Tk()
root.geometry("1000x1000")

def getvals():
    print("Accepted")

#Title 
Label(root, text = "Create a Team", font= "arial 15 bold").grid(row = 0 , column = 3)

# Textbox Label
name = Label(root, text = "Name")
phone = Label(root, text = "Phone")
email = Label(root, text = "Email:")


# Packing Labels
name.grid(row = 1, column = 0)
phone.grid(row = 2, column = 0)
email.grid(row = 3, column = 0)

#Variable for storing data
namevalue = StringVar
phonevalue = StringVar
emailvalue = StringVar
checkvalue = IntVar
checkvalue2 = IntVar

# Creating Entry Fields
nameentry = Entry(root, textvariable = namevalue)
phoneentry = Entry(root, textvariable = phonevalue)
emailentry = Entry(root, textvariable = emailvalue)

# Packing Entry Fields
nameentry.grid(row = 1, column = 1)
phoneentry.grid(row = 2, column = 1)
emailentry.grid(row = 3, column = 1)


# Creating Checkbox
checkbtn = Checkbutton(text = "Coach", variable = checkvalue)
checkbtn.grid(row=6, column = 1)

checkbtn2 = Checkbutton(text = "Player", variable = checkvalue2)
checkbtn2.grid(row=6, column = 2)

# Submit Button
Button(text = "Submit", command = getvals).grid(row = 7, column = 1)


root.mainloop()