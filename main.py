import tkinter as tk
import os
from user_control import User, getUserData, userObjects

######### Environment Variables ##########
HEIGHT = 700
WIDTH = 800
root = tk.Tk()


########## Functionality ##########

getUserData()                        #get users data from database on application boot

current_user = None                  #set an empty class instance for the current user of application

# create_user
def create_user(username, password, label):
    if not username:                                         #Checks if password and username were entered
        label['text'] = "Please Enter a username"
        return
    if not password:
        label['text'] = "Please Enter a password"
        return

    if len(userObjects) == 10:                                #Checks if max users has been reached 
        label['text'] = "Max Users Stored"
        return
    
    for user in userObjects:
        if username == user.getUsername():
            label['text'] = "User already exists"
            return
    
    newUser = User(username, password)
    newUser.userStore()
    userObjects.append(newUser)

    print("Current users are: ")
    for user in userObjects:
        print(user.getUsername())
    
    label['text'] = "User Has Been Created"

# login function
def login(username, password, label):
    i = 0

    if(len(userObjects) == 0):                               #determines if users even exist           
        label['text'] = 'This User Does Not Exist'
        return

    while(i < len(userObjects)):
        if userObjects[i].getUsername() == username and userObjects[i].getPassword() == password:
            label['text'] = 'Login Successful'               
            global current_user                    #set the current user
            current_user = userObjects[i]
            pacing_modes_window()
            return 
        elif userObjects[i].getUsername() == username and userObjects[i].getPassword() != password:
            label['text'] = 'The Password You Entered Is Incorrect'
            return
        elif i == (len(userObjects) - 1):
            label['text'] = 'This User Does Not Exist'
            return
        else:
            i += 1

# AOO Pacing Functionality
def AOO_Pace(lowerRate, upperRate, atrialPulseWidth, atrialAmplitude):
    print(lowerRate, upperRate, atrialPulseWidth, atrialAmplitude)
    current_user.userUpdate(["lower_rate", "upper_rate", "atrial_pulse_width", "atrial_amplitude"], [lowerRate, upperRate, atrialPulseWidth, atrialAmplitude])

# VOO_Pace Pacing Functionality
def VOO_Pace(lowerRate, upperRate, ventricularAmplitude, ventricularPulseWidth):
    print(lowerRate, upperRate, ventricularAmplitude, ventricularPulseWidth)
    current_user.userUpdate(["lower_rate", "upper_rate", "ventricular_amplitude", "ventricular_pulse_width"], [lowerRate, upperRate, ventricularAmplitude, ventricularPulseWidth])

# AAI Pacing Functionality
def AAI_Pace(lowerRate, upperRate, atrialPulseWidth, atrialAmplitude, ARP):
    print(lowerRate, upperRate, atrialPulseWidth, atrialAmplitude, ARP)
    current_user.userUpdate(["lower_rate", "upper_rate", "atrial_pulse_width", "atrial_amplitude", "ARP"], [lowerRate, upperRate, atrialPulseWidth, atrialAmplitude, ARP])


# VVI Pacing Functionality
def VVI_Pace(lowerRate, upperRate, ventricularPulseWidth, ventricualrAmplitude, VRP):
    print(lowerRate, upperRate, ventricularPulseWidth, ventricualrAmplitude, VRP)
    current_user.userUpdate(["lower_rate", "upper_rate", "ventricular_pulse_width", "ventricular_amplitude", "VRP"], [lowerRate, upperRate, ventricularPulseWidth, ventricualrAmplitude, VRP])

########## Front End ##########

# AOO_window
def AOO_window():

    AOO_window = tk.Toplevel(root, height = HEIGHT, width = WIDTH)
    AOO_window.configure(background = '#551033')

    lower_rate_limit = tk.Entry(AOO_window, text = "Lower Rate Limit ")
    lower_rate_limit.place(relx = 0.50, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    lower_rate_label = tk.Label(AOO_window, text = 'Lower Rate Limit', bg = '#551033')
    lower_rate_label.place(relx = 0.50, rely = 0.09, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    upper_rate_limit = tk.Entry(AOO_window, text = "Upper Rate Limit")
    upper_rate_limit.place(relx = 0.50, rely = 0.20, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    upper_rate_label = tk.Label(AOO_window, text = 'Upper Rate Limit', bg = '#551033')
    upper_rate_label.place(relx = 0.50, rely = 0.24, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    atrial_pulse_width = tk.Entry(AOO_window, text = "Atrial Pules Width")
    atrial_pulse_width.place(relx = 0.50, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    atrial_pulse_label = tk.Label(AOO_window, text = 'Atrial Pules', bg = '#551033')
    atrial_pulse_label.place(relx = 0.50, rely = 0.39, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    atrial_amplitude = tk.Entry(AOO_window, text = "Atrial Amplitude")
    atrial_amplitude.place(relx = 0.50, rely = 0.50, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    atrial_amplitude_label = tk.Label(AOO_window, text = 'Atrial Amplitude', bg = '#551033')
    atrial_amplitude_label.place(relx = 0.50, rely = 0.54, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    pace_now_button = tk.Button(AOO_window, text = "Pace Now", font = 96, command = lambda: AOO_Pace(lower_rate_limit.get(), upper_rate_limit.get(), atrial_pulse_width.get(), atrial_amplitude.get()))
    pace_now_button.place(relx = 0.5, rely = 0.80, relwidth = 0.40, relheight = 0.10, anchor = 'n')
    # pace_now_label = tk.Label(AOO_window, font = 40, bg = '#551033')
    # pace_now_label.place(relx = 0.5, rely = 0.70, relwidth = 0.40, relheight = 0.10, anchor = 'n')

# VOO_window
def VOO_window():

    VOO_window = tk.Toplevel(root, height = HEIGHT, width = WIDTH)
    VOO_window.configure(background = '#551033')

    lower_rate_limit = tk.Entry(VOO_window)
    lower_rate_limit.place(relx = 0.50, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    lower_rate_label = tk.Label(VOO_window, text = 'Lower Rate Limit', bg = '#551033')
    lower_rate_label.place(relx = 0.50, rely = 0.09, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    upper_rate_limit = tk.Entry(VOO_window)
    upper_rate_limit.place(relx = 0.50, rely = 0.20, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    upper_rate_label = tk.Label(VOO_window, text = 'Upper Rate Limit', bg = '#551033')
    upper_rate_label.place(relx = 0.50, rely = 0.24, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    ventricular_amplitude = tk.Entry(VOO_window)
    ventricular_amplitude.place(relx = 0.50, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    ventricular_amplitude_label = tk.Label(VOO_window, text = 'Ventricular Amplitude', bg = '#551033')
    ventricular_amplitude_label.place(relx = 0.50, rely = 0.39, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    ventricular_pulse_width = tk.Entry(VOO_window)
    ventricular_pulse_width.place(relx = 0.50, rely = 0.50, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    ventricular_pulse_width_label = tk.Label(VOO_window, text = 'Ventricular Pulse Width', bg = '#551033')
    ventricular_pulse_width_label.place(relx = 0.50, rely = 0.54, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    pace_now_button = tk.Button(VOO_window, text = "Pace Now", font = 96, command = lambda: VOO_Pace(lower_rate_limit.get(), upper_rate_limit.get(), ventricular_amplitude.get(), ventricular_pulse_width.get()))
    pace_now_button.place(relx = 0.5, rely = 0.80, relwidth = 0.40, relheight = 0.10, anchor = 'n')
    
# AAI_Window
def AAI_window():

    AAI_window = tk.Toplevel(root, height = HEIGHT, width = WIDTH)
    AAI_window.configure(background = '#551033')

    lower_rate_limit = tk.Entry(AAI_window)
    lower_rate_limit.place(relx = 0.50, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    lower_rate_label = tk.Label(AAI_window, text = 'Lower Rate Limit', bg = '#551033')
    lower_rate_label.place(relx = 0.50, rely = 0.09, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    upper_rate_limit = tk.Entry(AAI_window)
    upper_rate_limit.place(relx = 0.50, rely = 0.20, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    upper_rate_label = tk.Label(AAI_window, text = 'Upper Rate Limit', bg = '#551033')
    upper_rate_label.place(relx = 0.50, rely = 0.24, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    atrial_amplitude = tk.Entry(AAI_window)
    atrial_amplitude.place(relx = 0.50, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    atrial_amplitude_label = tk.Label(AAI_window, text = 'Atrial Ampltiude', bg = '#551033')
    atrial_amplitude_label.place(relx = 0.50, rely = 0.39, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    atrial_pulse_width = tk.Entry(AAI_window)
    atrial_pulse_width.place(relx = 0.50, rely = 0.50, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    atrial_pulse_width_label = tk.Label(AAI_window, text = 'Atrial Pulse Width', bg = '#551033')
    atrial_pulse_width_label.place(relx = 0.50, rely = 0.54, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    ARP = tk.Entry(AAI_window, text = "ARP")
    ARP.place(relx = 0.50, rely = 0.65, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    ARP_label = tk.Label(AAI_window, text = 'ARP', bg = '#551033')
    ARP_label.place(relx = 0.50, rely = 0.69, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    pace_now_button = tk.Button(AAI_window, text = "Pace Now", font = 96, command = lambda: AAI_Pace(lower_rate_limit.get(), upper_rate_limit.get(), atrial_amplitude.get(), atrial_pulse_width.get(), ARP.get()))
    pace_now_button.place(relx = 0.5, rely = 0.80, relwidth = 0.40, relheight = 0.10, anchor = 'n')

#VVI_window
def VVI_window():

    VVI_window = tk.Toplevel(root, height = HEIGHT, width = WIDTH)
    VVI_window.configure(background = '#551033')

    lower_rate_limit = tk.Entry(VVI_window)
    lower_rate_limit.place(relx = 0.50, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    lower_rate_label = tk.Label(VVI_window, text = 'Lower Rate Limit', bg = '#551033')
    lower_rate_label.place(relx = 0.50, rely = 0.09, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    upper_rate_limit = tk.Entry(VVI_window)
    upper_rate_limit.place(relx = 0.50, rely = 0.20, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    upper_rate_label = tk.Label(VVI_window, text = 'Upper Rate Limit', bg = '#551033')
    upper_rate_label.place(relx = 0.50, rely = 0.24, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    ventricular_amplitude = tk.Entry(VVI_window)
    ventricular_amplitude.place(relx = 0.50, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    ventricular_amplitude_label = tk.Label(VVI_window, text = 'Ventricular Ampltiude', bg = '#551033')
    ventricular_amplitude_label.place(relx = 0.50, rely = 0.39, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    ventricular_pulse_width = tk.Entry(VVI_window)
    ventricular_pulse_width.place(relx = 0.50, rely = 0.50, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    ventricular_pulse_width_label = tk.Label(VVI_window, text = 'Atrial Pulse Width', bg = '#551033')
    ventricular_pulse_width_label.place(relx = 0.50, rely = 0.54, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    VRP = tk.Entry(VVI_window, text = "VRP")
    VRP.place(relx = 0.50, rely = 0.65, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    VRP_label = tk.Label(VVI_window, text = 'VRP', bg = '#551033')
    VRP_label.place(relx = 0.50, rely = 0.69, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    pace_now_button = tk.Button(VVI_window, text = "Pace Now", font = 96, command = lambda: VVI_Pace(lower_rate_limit.get(), upper_rate_limit.get(), ventricular_amplitude.get(), ventricular_pulse_width.get(), VRP.get()))
    pace_now_button.place(relx = 0.5, rely = 0.80, relwidth = 0.40, relheight = 0.10, anchor = 'n')

# pacing_modes_window
def pacing_modes_window():
    pacing_modes_window = tk.Toplevel(root, height = HEIGHT, width = WIDTH)
    pacing_modes_window.configure(background = '#551033')

    AOO_Button = tk.Button(pacing_modes_window, text = 'AOO', font = 96, command = lambda: AOO_window())
    AOO_Button.place(relx = 0.15, rely = 0.15, relwidth = 0.1, relheight = 0.1)

    VOO_Button = tk.Button(pacing_modes_window, text = 'VOO', font = 96, command = lambda: VOO_window())
    VOO_Button.place(relx = 0.15, rely = 0.80, relwidth = 0.1, relheight = 0.1)

    AAI_Button = tk.Button(pacing_modes_window, text = 'AAI', font = 96, command = lambda: AAI_window())
    AAI_Button.place(relx = 0.75, rely = 0.15, relwidth = 0.1, relheight = 0.1)

    VVI_Button = tk.Button(pacing_modes_window, text = 'VVI', font = 96, command = lambda: VVI_window())
    VVI_Button.place(relx = 0.75, rely = 0.80, relwidth = 0.1, relheight = 0.1)

    display_label = tk.Label(pacing_modes_window, bg = '#551033', text = "Please Select a Mode")
    display_label.place(relx = 0.10, rely = 0.35, relwidth = 0.8, relheight = 0.30)

    pacemakerID = tk.Label(pacing_modes_window, text = 'Pacemaker Connected: 4125', bg = '#551033')
    pacemakerID.place(relx = 0, rely = 0, relwidth = 0.20, relheight = 0.05)

    DCM_status = tk.Label(pacing_modes_window, font = 14)
    DCM_status.place(relx = 0.90, rely = 0, relwidth = 0.15, relheight = 0.05)

    DCM_status_label = tk.Label(pacing_modes_window, bg = '#551033', text = "DCM Status")
    DCM_status_label.place(relx = 0.95, rely = 0.05, relwidth = 0.080, relheight = 0.040, anchor = 'n')
    
    val = 1

    if(val == 1):
        DCM_status['bg'] = '#7BFF33'
    else:
        DCM_status['bg'] = '#EF2B0B'

# homepage_window
def homepage_window():
    print(current_user.getUsername())
    current_user.userUpdate("upper_rate", 123)
    homepage_window = tk.Toplevel(root, height = HEIGHT, width = WIDTH)
    homepage_window.configure(background = '#551033')
    pace_now = tk.Button(homepage_window, text = "Pace Now", font = 96, command = lambda: pacing_modes_window())
    pace_now.place(relx = 0.5, rely = 0.9, relwidth = 0.30, relheight = 0.10, anchor = 'n')
    
    DCM_status = tk.Label(homepage_window, font = 14)
    DCM_status.place(relx = 0.90, rely = 0, relwidth = 0.15, relheight = 0.05)

    DCM_status_label = tk.Label(homepage_window, bg = '#551033', text = "DCM Status")
    DCM_status_label.place(relx = 0.95, rely = 0.05, relwidth = 0.080, relheight = 0.040, anchor = 'n')
    
    val = 1

    if(val == 1):
        DCM_status['bg'] = '#7BFF33'
    else:
        DCM_status['bg'] = '#EF2B0B'

# register
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


########### Main/Root Window ##########
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