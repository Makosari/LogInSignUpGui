from tkinter import *
from tkinter import ttk
import linecache


root = Tk()
root.title('LogIn')
root.geometry('400x150')


def startLog():
    
    for everything in root.winfo_children():
        everything.destroy()

    #name 
    name_label = Label(root, text = 'Enter username:')
    name_label.place(x=20, y=30)

    name_entry = ttk.Entry()
    name_entry.place(x= 125, y = 30)


    #password
    password_label = Label(root, text = 'Enter password:')
    password_label.place(x=20, y=80)

    password_entry = ttk.Entry()
    password_entry.place(x= 125, y = 80)


    #logging system
    def log():                                  
        name = name_entry.get()
        password = password_entry.get()
        
        nameInDatabase = False
        lineIndex = -1

        f = open("database.txt", "r")

        #checking if if possible for this name to be in the database according to its length
        if len(name) >= 5 and name[-1] == '~':
            #if it is possible then checking for name
            for line in f:
                lineIndex+=1
                if name in line:
                    nameInDatabase = True
                    break
            
            #if name is in the database
            if nameInDatabase == True:

                #checking if password is at least 8 characters long
                if len(password) >= 8:

                    #checking if password is in the database
                    passCheck = linecache.getline('database.txt', lineIndex + 1)
                    if password in passCheck:
                        for everything in root.winfo_children():
                            everything.destroy()
                        correctP_label = Label(root, text = 'You are logged in')
                        correctP_label.place(x=150, y=50)

                    # if password is not in the database
                    else:
                        shortP_label = Label(root, text = 'Incorrect password   ')
                        shortP_label.place(x=20, y=110)
                
                #if password is too short
                else:
                    shortP_label = Label(root, text = 'Password is too short')
                    shortP_label.place(x=20, y=110)

            #if name is not in the database
            else:
                noName_label = Label(root, text = 'Invladin name' + 10*'    ')
                noName_label.place(x=20, y=110) 
        #if name is too short there is no point to check if it is in the database
        else:
            noName_label = Label(root, text = 'Invladin name' + 10*'    ')
            noName_label.place(x=20, y=110) 

        f.close()
        

    #button for log in
    confirmButton = Button(root, text='log in', command= log, width=10)
    confirmButton.place(x=300, y=100)

logInButton = Button(root, text='log in', command= startLog, width=10)
logInButton.place(x=260, y=50)

SignUpButton = Button(root, text='sign up', width=10)
SignUpButton.place(x=60, y=50)

root.mainloop()