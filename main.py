from tkinter import *
from tkinter import ttk
import linecache

root = Tk()
root.title('GUI')
root.geometry('420x170')

def menu():
    for everything in root.winfo_children():
        everything.destroy()

    passwordDontMatch_label = Label(root, text = 'WELCOME')
    passwordDontMatch_label.place(x=185, y=15)

    logInButton = Button(root, text='log in', command= startLog, width=10)
    logInButton.place(x=270, y=60)

    SignUpButton = Button(root, text='sign up', command=startSign, width=10)
    SignUpButton.place(x=60, y=60)

def startLog():
    
    for everything in root.winfo_children():
        everything.destroy()

    #name 
    name_label = Label(root, text = 'Enter username:')
    name_label.place(x=40, y=40)

    name_entry = ttk.Entry()
    name_entry.place(x= 145, y = 40)


    #password
    password_label = Label(root, text = 'Enter password:')
    password_label.place(x=40, y=80)

    password_entry = ttk.Entry()
    password_entry.place(x= 145, y = 80)


    #logging system
    def log():                                  
        name = name_entry.get()
        password = password_entry.get()
        
        nameInDatabase = False
        lineIndex = -1

        f = open("database.txt", "r")
        #checking if possible for this name to be in the database according to its length
        if len(name) >= 5 :
            #if it is possible then checking for name
            for line in f:
                lineIndex+=1
                if name + '~' in line:    #at the end of every name in database
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
                        correctP_label = Label(root, text = f'{name} is logged in')
                        correctP_label.place(x=150, y=50)
                        confirmButton = Button(root, text='log out',command=menu, width=10)
                        confirmButton.place(x=300, y=100)

                    # if password is not in the database
                    else:
                        shortP_label = Label(root, text = 'Incorrect name or password   ')
                        shortP_label.place(x=20, y=110)
                
                #if password is too short
                else:
                    shortP_label = Label(root, text = 'Password is too short' + 10*'    ')
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

    backButton = Button(root, text='back', command= goBack, width=10)
    backButton.place(x=20, y=5)

def startSign():

    for everything in root.winfo_children():
        everything.destroy()

    #name 
    name_label = Label(root, text = 'Enter username:')
    name_label.place(x=40, y=30)

    name_entry = ttk.Entry()
    name_entry.place(x= 150, y = 30)


    #password
    password_label = Label(root, text = 'Enter password:')
    password_label.place(x=40, y=70)

    password_entry = ttk.Entry()
    password_entry.place(x= 150, y = 70)

    #confirm password
    password_label = Label(root, text = 'Confirm password:')
    password_label.place(x=40, y=105)

    confirmPassword_entry = ttk.Entry()
    confirmPassword_entry.place(x= 150, y = 105)


    #Signing system
    def sign():                                  
        name = name_entry.get()
        password = password_entry.get()
        confirmPassword = confirmPassword_entry.get()
        
        nameInDatabase = False
        nameLength = False
        lineIndex = -1

        f = open("database.txt", "r+")
        #checking if name is available
        if len(name) >= 5 :
            nameLength = True
            for line in f:
                lineIndex+=1
                if name + '~' in line:    #at the end of every name in database
                    nameInDatabase = True
                    break
        else:
            nameShort_label = Label(root, text = 'Name is too short' + 10*'     ')
            nameShort_label.place(x=280, y=30)

            blankIt_label = Label(root, text = 20 * '      ')
            blankIt_label.place(x=20, y=130)
        
        if nameInDatabase == True:
            nameUnavailable_label = Label(root, text = 'Name is already used')
            nameUnavailable_label.place(x=280, y=30)

            blankIt1_label = Label(root, text = 20 * '      ')
            blankIt1_label.place(x=20, y=130)

        elif nameInDatabase == False and nameLength == True:
            blank_label = Label(root, text = 20 * '      ')
            blank_label.place(x=260, y=30)
            if len(password) >= 8:
                if password == confirmPassword:
                    f.write(f'\n{name}~ {password}')
                    for everything in root.winfo_children():
                            everything.destroy()
                    correctP_label = Label(root, text = 'You are Signed in')
                    correctP_label.place(x=150, y=50)
                else:
                    passwordDontMatch_label = Label(root, text = 'Passwords does not match')
                    passwordDontMatch_label.place(x=20, y=130)
            else:
                    passwordDontMatch_label = Label(root, text = 'Password is too short     ')
                    passwordDontMatch_label.place(x=20, y=130)


        f.close()

    confirmButton = Button(root, text='Sign up', command= sign, width=10)
    confirmButton.place(x=300, y=100)

    backButton = Button(root, text='back', command= goBack, width=10)
    backButton.place(x=20, y=5)

def goBack():

    for everything in root.winfo_children():
        everything.destroy()

    logInButton = Button(root, text='log in', command= startLog, width=10)
    logInButton.place(x=260, y=60)

    SignUpButton = Button(root, text='sign up', command=startSign, width=10)
    SignUpButton.place(x=60, y=60)

menu()

root.mainloop()