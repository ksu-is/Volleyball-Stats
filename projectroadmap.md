# Project Map 
# Step 1
- [x] Pick a topic
- [x] View code repositorys that is similar to my topic
- [x] Pick repository or create a new on
- [x] Enter the topic on teams spreadsheet 
- [x] Join KSU-is team on Github
- [x] Fork repository to IS team on Github
- [x] Create a ReadMe.md file
- [x] Make changes and / or add comments to code

 # Step 2
- [x] Edit code
    - created a log in page
    - created a 'create team' page
    - created a 'create profile page'
- [x] Update changes to main browser every other day
- [x] Complete at least 6 code changes every 3 days
    - note exactly every three days but have made major progress
        - [] Need to create a my team page 
        - [] Need to create a stats page (where stats will be taken during matches)
        - [] create a place where the stats are being generated and kept for review 
    - Week of 11/15
    - [x] attempting to find an application that allows me to build an app or website. Was looking into Kivy, Website using flask, or Tkinter (Gui)
        - I didn't like website because I wanted something that I could potentially turn into an app that I can download onto my Ipad in the future.
        - I wasn't able to download Kivy due to some technical issues so I opted to use Tkinter to prepare an app
        - I am able to get the application running and have a logo set up
        - currently testing different ideas to see which one will work best with the ideas I have for my project 
            - offically going with tkinter
 # Step 3 
- [x] Create Powerpoint Slide 
- [x] Finish editing code and making minor tweaks
    - Satisfied for project
- [x] Update my projectroadmap to show progress by dates along with the steps / process



# Daily Processes 
# November 10th, 2021
- Created inital commit 
- Created and update README file
- Created Projectroadmap file
- Created Playerstats.py
    - Created a simple class code 
- Research
    - looking for similar codes
    - running similar codes to see what type of application I should use to develop my app
    - watched lots of videos on different ways to keep stats through python 

# November 18th, 2021
- Testing different applications like Kivy and Tkinter
- More research
- Created some files and made minor code changes

# November 25th, 2021
- Found an application that would work well for me and what I wanted to accomplish
    - I chose to use Tkinter
    - I got rid of the previous class functions that I created
    - Went through a lot of tester trials to find code that worked for what I needed
- Main window format
- Created a Log in Button
    - Enter in username and password
    - Created an Enter button
        - Had no working function
- Created a Create New Profile Button
    - Enter Name, Phone #, Email, Password, Password confirmation, & check box for coach or player
    - Created a submit button
        - Had no working function
- Created a Create New Team Button
    - Allows you to enter player's names and jersey numbers
    - Created a submit button
        - Had no working function

# November 28th, 2021
- Created Stats.py 
    - tester page to find a system that could keep stats efficently
    - created buttons to align with the data I would want to track
- Updated Main.py 
    - made comments to help seperate and organize my different areas of code
    - played with some formatting
    - adding functions to the submit button for create_team(), create_profile()
        - attempted to find a way to retrieve data from entry boxes and print them using .get()
- Created a window where we will eventually be able to see all of the new teams we create
    - button in the main window
- Downloaded openpyxl 
    - wanting to incorporate retriving and inputing data into an excel sheet

# November 30th, 2021
- Created a few files used to test and practice some code before adding it the main.py
- Began testing ways to incorporate a table
    - ultimately opted out until further notice
- Lots of clean up
    - Incorperated clearing data automatically after using submit or enter buttons
         - Messages that pop up after submission
    - Moved create_team button into myteams window
- Got rid of files I was not using or that were used for trial and tutorial walkthroughs codes
    - not vital to the running of the app
- Submit button for create new team:
    - retrieves player entry input
    - Add player names and numbers to a list
        - for future use using excel 
    - Creates a new window specifically for that team
    - Creates a new sheet in the excel file that we are using
    - Clears previous entries




