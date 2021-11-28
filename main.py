# My Vollyeyball project

from tkinter import *

# Creating Framework
window = Tk()
window.geometry('1000x1000')
window.title("Volleyball Statistics")
window.configure(background = "white")

# Creating a Logo 
logo = PhotoImage(file="Volleyball Stats.gif")
Label (window, image=logo, bg = "white").grid(row=0, column=0)

# CREATING A "CREATE TEAM" FUNCTION
def create_team():
 # formatting 
    new_team = Toplevel()
    new_team.geometry("500x500")
    new_team.title("Create a New Team")
 # Creating Header / Explanation
    new_team_lbl = Label(new_team, text = "Create a New Team!", font = "arial 12 bold", bg = "white" )
    new_team_lbl.grid(row = 1 , column = 0)
 # Creating Jersey and Player Number Fields
    jersey_lbl = Label(new_team, text = "Enter player's Jersey Number: ", font = "arial 9", bg = "white")
    player_lbl = Label(new_team, text = "Enter player's Name: ", font = "arial 9", bg = "white")
 # Packing Fields
    jersey_lbl.grid(row = 2 , column =0)
    player_lbl.grid(row = 2, column =1)
 # Creating Player Name and Jersey Entry Boxes
    player1 = Entry(new_team, width = 30, bg = "white")
    player2 = Entry(new_team, width = 30, bg = "white")
    player3 = Entry(new_team, width = 30, bg ="white")
    player4 = Entry(new_team, width = 30, bg = "white")
    player5 = Entry(new_team, width = 30, bg = "white")
    player6 = Entry(new_team, width = 30, bg = "white")
    player7 = Entry(new_team, width = 30, bg = "white")
    player8 = Entry(new_team, width = 30, bg = "white")
    player9 = Entry(new_team, width = 30, bg = "white")
    player10 = Entry(new_team, width = 30, bg = "white")
    player11 = Entry(new_team, width = 30, bg = "white")
    player12 = Entry(new_team, width = 30, bg = "white")
    player13 = Entry(new_team, width = 30, bg = "white")
    player14 = Entry(new_team, width = 30, bg = "white")
    player15 = Entry(new_team, width = 30, bg = "white")
    player16 = Entry(new_team, width = 30, bg = "white")
 #Jerseys Entry
    jersey1 = Entry(new_team, width = 10, bg = "white")
    jersey2 = Entry(new_team, width = 10, bg = "white")
    jersey3 = Entry(new_team, width = 10, bg = "white")
    jersey4 = Entry(new_team, width = 10, bg = "white")
    jersey5 = Entry(new_team, width = 10, bg = "white")
    jersey6 = Entry(new_team, width = 10, bg = "white")
    jersey7 = Entry(new_team, width = 10, bg = "white")
    jersey8 = Entry(new_team, width = 10, bg ="white")
    jersey9 = Entry(new_team, width = 10, bg = "white")
    jersey10 = Entry(new_team, width = 10, bg = "white")
    jersey11 = Entry(new_team, width = 10, bg = "white")
    jersey12 = Entry(new_team, width = 10, bg = "white")
    jersey13 = Entry(new_team, width = 10, bg = "white")
    jersey14 = Entry(new_team, width = 10, bg = "white")
    jersey15 = Entry(new_team, width = 10, bg = "white")
    jersey16 = Entry(new_team, width = 10, bg = "white")
 # Packing Jersey and Player Fields 
    player1.grid(row = 3, column = 1)
    player2.grid(row = 4, column = 1)
    player3.grid(row = 5, column = 1)
    player4.grid(row = 6, column = 1)
    player5.grid(row = 7, column = 1)
    player6.grid(row = 8, column = 1)
    player7.grid(row = 9, column = 1)
    player8.grid(row = 10, column = 1)
    player9.grid(row = 11, column = 1)
    player10.grid(row = 12, column = 1)
    player11.grid(row = 13, column = 1)
    player12.grid(row = 14, column = 1)
    player13.grid(row = 15, column = 1)
    player14.grid(row =16, column = 1)
    player15.grid(row = 17, column = 1)
    player16.grid(row = 18, column = 1)
 # Jersey Packing
    jersey1.grid(row = 3, column = 0)
    jersey2.grid(row = 4, column = 0)
    jersey3.grid(row = 5, column = 0)
    jersey4.grid(row = 6, column = 0)
    jersey5.grid(row = 7, column = 0)
    jersey6.grid(row =8, column = 0)
    jersey7.grid(row = 9, column = 0)
    jersey8.grid(row = 10, column = 0)
    jersey9.grid(row = 11, column = 0)
    jersey10.grid(row = 12, column = 0)
    jersey11.grid(row = 13, column = 0)
    jersey12.grid(row = 14, column = 0)
    jersey13.grid(row = 15, column = 0)
    jersey14.grid(row = 16, column = 0)
    jersey15.grid(row = 17, column = 0)
    jersey16.grid(row = 18, column = 0)
 # Submit & Cancel Button Functions
    def submit():
        name1 = player1.get()
        num1 = jersey1.get()
        print("Player One:" ,name1 ,"#", num1)
        name2 = player2.get()
        num2 = jersey2.get()
        print("Player Two:" ,name2 ,"#", num2)
        name3 = player3.get()
        num3 = jersey3.get()
        print("Player Three:" ,name3 ,"#", num3)
        name4 = player4.get()
        num4 = jersey4.get()
        print("Player Four:" ,name4 ,"#", num4)
        name5 = player1.get()
        num5 = jersey1.get()
        print("Player Five:" ,name5 ,"#", num5)
        name6 = player6.get()
        num6 = jersey6.get()
        print("Player Six:" ,name6 ,"#", num6)
        name7 = player7.get()
        num7 = jersey7.get()
        print("Player Seven:" ,name7 ,"#", num7)
        name8 = player8.get()
        num8 = jersey8.get()
        print("Player Eight:" ,name8 ,"#", num8)
        name9 = player9.get()
        num9 = jersey9.get()
        print("Player Nine:" ,name9 ,"#", num9)
        name10 = player10.get()
        num10 = jersey10.get()
        print("Player Ten:" ,name10 ,"#", num10)
        name11 = player11.get()
        num11 = jersey11.get()
        print("Player Eleven: " ,name11 ,"#", num11)
        name12 = player12.get()
        num12 = jersey12.get()
        print("Player Twelve" ,name12 ,"#", num12)
        name13 = player13.get()
        num13 = jersey13.get()
        print("Player Thirteen:" ,name13 ,"#", num13)
        name14 = player14.get()
        num14 = jersey14.get()
        print("Player Fourteen:" ,name14 ,"#", num14)
        name15 = player15.get()
        num15 = jersey15.get()
        print("Player Fifeteen:" ,name15 ,"#", num15)
        name16 = player16.get()
        num16 = jersey16.get()
        print("Player Sixteen:" ,name16 ,"#", num16)
    def cancel():
        print("Disapproved")
 # Creating Submit and Cancel Buttons
    submit_btn = Button(new_team, text = "Submit", command = submit)
    submit_btn.grid(row = 20 , column = 1)
    cancel_btn = Button(new_team, text = "Cancel", command = cancel)
    cancel_btn.grid(row = 20 , column = 0)


# Creating a "Create a Team" Button
newteam_label = Label(window, text = "Click below to create a new team!", bg = "white", font = "arial 15 bold").grid(row = 1, column = 0)
newteam_bttn = Button (window, text = "Create a New Team", width = 15 , command = create_team).grid(row = 2 , column = 0)


# CREATING "LOGIN" FUNCTION
def login():
 # formatting 
    log_in = Toplevel()
    log_in.geometry("500x500")
    log_in.title("Login Page")
 # Creating Labels
    email_phone = Label(log_in, text = "Enter your email or phone number: ")
    password = Label(log_in, text = "Enter your password: ")
 # Packing Labels
    email_phone.grid(row = 2, column = 0)
    password.grid(row = 3, column = 0)
 # Variable for storing data
    email_phonevalue = StringVar
    passwordvalue = StringVar
 # Creating Entry Fields
    email_phoneentry = Entry(log_in, textvariable = email_phonevalue)
    passwordentry = Entry(log_in, textvariable = passwordvalue)
 # Packing Entry Fields
    email_phoneentry.grid(row = 2, column = 1)
    passwordentry.grid(row = 3, column = 1)
    passwordentry.config(show = "*")
 # defining enter button
    def enter():
        username = email_phoneentry.get()
        password = passwordentry.get()
        print("Username," , username, "and Password, ", password, ", successful" )
 # Enter Button
    Button(log_in, text = "Enter", command = enter).grid(row = 4, column = 1)
 # CREATING A "CREATE A PROFILE" FUNCTION
    def create():
        create_profile = Toplevel()
        create_profile.geometry("500x500")
        create_profile.title("Create a Profile")

        name = Label(create_profile, text = "Enter your name: ")    
        email = Label(create_profile, text = "Enter your email: ")
        phone = Label(create_profile, text = "Enter your phone number: ")
        password = Label(create_profile, text = "Enter your password: ")
        confirm_password = Label(create_profile, text = "Confirm your password: ")
   # Packing Labels
        name.grid(row = 1, column = 0)
        email.grid(row = 2, column = 0)
        phone.grid(row = 3, column = 0)
        password.grid(row = 4, column = 0)
        confirm_password.grid(row = 5, column = 0)
   # Variable for storing data
        namevalue = StringVar
        emailvalue = StringVar
        phonevalue = StringVar
        passwordvalue = StringVar
        confirm_passwordvalue = StringVar
        checkvalue = IntVar
        checkvalue2 = IntVar
   # Creating Entry Fields
        nameentry = Entry(create_profile, textvariable = namevalue)
        emailentry = Entry(create_profile, textvariable = emailvalue)
        phoneentry = Entry(create_profile, textvariable = phonevalue)
        passwordentry = Entry(create_profile, textvariable = passwordvalue)
        confirm_passwordentry = Entry(create_profile, textvariable = confirm_passwordvalue)
   # Packing Entry Fields
        nameentry.grid(row = 1, column = 1)
        emailentry.grid(row = 2, column = 1)
        phoneentry.grid(row = 3, column = 1)
        passwordentry.grid(row = 4, column = 1)
        confirm_passwordentry.grid(row = 5, column = 1) 
   # Creating Checkbox
        checkbtn = Checkbutton(create_profile, text = "Coach", variable = checkvalue)
        checkbtn.grid(row=6, column = 0)

        checkbtn2 = Checkbutton(create_profile, text = "Player", variable = checkvalue2)
        checkbtn2.grid(row=6, column = 1)
   # defining submit button
        def profile():
            name = nameentry.get()
            email = emailentry.get()
            phone = phoneentry.get()
            password = passwordentry.get()
            confirm = confirm_passwordentry.get()

            print("Team creation successful. Information below:\n",name, email,phone,password,confirm)
   # Submit Button
        Button(create_profile, text = "Submit", command = profile).grid(row = 7, column = 1)
 # Creating a "Create a profile" button
    create_bttn = Button (log_in, text = "Create a New Profile", width = 15 , command = create)
    create_bttn.grid(row = 4 , column = 0)


# Creating a "Login" Button
login_bttn = Button (window, text = "Login", width = 5 , command = login).grid(row = 4 , column = 0)

# CREATING A "MY TEAMS" FUNCTION
def my_teams():
 # formatting 
    myteams = Toplevel()
    myteams.geometry("500x500")
    myteams.title("My Teams")
 # Creating Header / Explanation
    myteam_lbl = Label(myteams, text = "My Teams!", font = "arial 12 bold", bg = "white" )
    myteam_lbl.grid(row = 1 , column = 0)

# Creating a "My Teams" Button
myteams_bttn = Button (window, text = "My Teams", width = 15 , command = my_teams).grid(row = 2 , column = 1)




window.mainloop()


