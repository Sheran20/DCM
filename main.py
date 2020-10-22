import tkinter as tk

from user_control import User

HEIGHT = 700
WIDTH = 800

root = tk.Tk()
#global 
userObjects = []

# create_user
def create_user(username, password, label):
    if not username:                                    #Checks if password and username were entered
        label['text'] = "Please Enter a username"
        return
    if not password:
        label['text'] = "Please Enter a password"
        return

    if len(userObjects) == 10:                                #Checks if max users has been reached 
        label['text'] = "Max Users Stored"
        return
    
    for user in userObjects:
        if username == user.getName():
            label['text'] = "User already exists"
            return
    
    newUser = User(username,password)
    newUser.storeUser()
    userObjects.append(newUser)

    print("Current users are: ")
    for user in userObjects:
        print(user.getName())
    
    label['text'] = "User Has Been Created"
    
#pacing_modes_window
def pacing_modes_window():
    pacing_modes_window = tk.Toplevel(root, height = HEIGHT, width = WIDTH)
    pacing_modes_window.configure(background = '#551033')

    AOO_Button = tk.Button(pacing_modes_window, text = 'AOO', font = 96)
    AOO_Button.place(relx = 0.15, rely = 0.15, relwidth = 0.1, relheight = 0.1)

    VOO_Button = tk.Button(pacing_modes_window, text = 'VOO', font = 96)
    VOO_Button.place(relx = 0.15, rely = 0.80, relwidth = 0.1, relheight = 0.1)

    AAI_Button = tk.Button(pacing_modes_window, text = 'AAI', font = 96)
    AAI_Button.place(relx = 0.75, rely = 0.15, relwidth = 0.1, relheight = 0.1)

    VVI_Button = tk.Button(pacing_modes_window, text = 'VVI', font = 96)
    VVI_Button.place(relx = 0.75, rely = 0.80, relwidth = 0.1, relheight = 0.1)

    display_label = tk.Label(pacing_modes_window, bg = '#551033', text = "Please Select a Mode", font = 120)
    display_label.place(relx = 0.10, rely = 0.35, relwidth = 0.8, relheight = 0.30)

#homepage_window
def homepage_window():
    homepage_window = tk.Toplevel(root, height = HEIGHT, width = WIDTH)
    homepage_window.configure(background = '#551033')

    pace_now = tk.Button(homepage_window, text = "Pace Now", font = 96, command = lambda: pacing_modes_window())
    pace_now.place(relx = 0.5, rely = 0.9, relwidth = 0.30, relheight = 0.10, anchor = 'n')

# login function
def login(username, password, label):
    i = 0
    while(i < len(userObjects)):
        if userObjects[i].getName() == username and userObjects[i].getPassword() == password:
            label['text'] = 'Login Successful'
            homepage_window()
            return
        elif userObjects[i].getName() == username and userObjects[i].getPassword() != password:
            label['text'] = 'The Password You Entered Is Incorrect'
            return
        elif i == (len(userObjects) - 1):
            label['text'] = 'This User Does Not Exist'
            return
        else:
            i += 1

#register
def register_window():

    register_window = tk.Toplevel(root, height = HEIGHT, width = WIDTH)
    register_window.configure(background = '#551033')
    
    label_register = tk.Label(register_window, bg = '#551033', text = "Create New User", font = 96)
    label_register.place(relx = 0.5, rely = 0, relwidth = 0.75, relheight = 0.1, anchor = 'n')

    register_button = tk.Button(register_window, text = "Register", font = 12, command = lambda: create_user(create_username_entry.get(), create_password_entry.get(), label_response))
    register_button.place(relx = 0.5, rely = 0.75, relwidth = 0.5, relheight = 0.1, anchor = 'n')


    create_label_username = tk.Label(register_window, bg = '#551033', text = "Please Enter Desired Username", font = 24)
    create_label_username.place(relx = 0.5, rely = 0.15, relwidth = 0.5, relheight = 0.1, anchor = 'n')
    create_username_entry = tk.Entry(register_window, text = "Create User Name", font = 40)
    create_username_entry.place(relx = 0.5, rely = 0.25, relwidth = 0.5, relheight = 0.1, anchor = 'n')

    label__create_password = tk.Label(register_window, bg = '#551033', text = "Please Enter Desired Password", font = 24)
    label__create_password.place(relx = 0.5, rely = 0.40, relwidth = 0.5, relheight = 0.1, anchor = 'n')
    create_password_entry = tk.Entry(register_window, text = "Create Password", font = 40)
    create_password_entry.place(relx = 0.5, rely = 0.50, relwidth = 0.5, relheight = 0.1, anchor = 'n')

    label_response = tk.Label(register_window, font = 20)
    label_response.place(relx = 0.5, rely = 0.65, relwidth = 0.5, relheight = 0.05, anchor = 'n')


#Main Window
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

frame = tk.Frame(root, bg = '#551033', bd = 5)
frame.place(relx = 0, rely = 0, relwidth = 2, relheight = 1, anchor = 'n')


create_new_user_button = tk.Button(frame, text = "Create New User", font = 12, command = lambda: register_window())
create_new_user_button.place(relx = 0.75, rely = 0.9, relheight = 0.1, relwidth = 0.15, anchor = 'n')

title = tk.Label(root, bg = '#551033', text = "Welcome", font = 96)
title.place(relx = 0.5, rely = 0, relwidth = 0.5, relheight = 0.1, anchor = 'n')

label_username = tk.Label(root, bg = '#551033', text = "Enter Username", font = 24)
label_username.place(relx = 0.5, rely = 0.15, relwidth = 0.5, relheight = 0.1, anchor = 'n')
username_entry = tk.Entry(root, text = "User Name", font = 40)
username_entry.place(relx = 0.5, rely = 0.25, relwidth = 0.5, relheight = 0.1, anchor = 'n')

label_password = tk.Label(root, bg = '#551033', text = "Enter Password", font = 24)
label_password.place(relx = 0.5, rely = 0.40, relwidth = 0.5, relheight = 0.1, anchor = 'n')
password_entry = tk.Entry(root, text = "Password", font = 40, show = '*')
password_entry.place(relx = 0.5, rely = 0.50, relwidth = 0.5, relheight = 0.1, anchor = 'n')

login_button = tk.Button(root, text = "Login", font = 12, command = lambda: login(username_entry.get(), password_entry.get(), label_login_response))
login_button.place(relx = 0.5, rely = 0.7, relheight = .1, relwidth = 0.15, anchor = 'n')

label_login_response = tk.Label(root, bg = '#551033', font = 12)
label_login_response.place(relx = 0.5, rely = 0.65, relheight = 0.05, relwidth = 0.8, anchor = 'n')

root.mainloop()