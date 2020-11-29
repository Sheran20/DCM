import tkinter as tk
import os
from user_control import User, getUserData, userObjects
from serial_control import set_data, serial_send

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
        label['text'] = "Please Enter a Username"
        return
    if not password:
        label['text'] = "Please Enter a Password"
        return

    if len(userObjects) == 10:                                #Checks if max users has been reached 
        label['text'] = "Max Users Stored"
        return
    
    for user in userObjects:
        if username == user.getUsername():
            label['text'] = "Registration Failed, Please Enter a Different Username"
            return
    
    newUser = User(username, password)
    newUser.userStore()
    userObjects.append(newUser)

    # print("Current users are: ")
    # for user in userObjects:
    #     print(user.getUsername())
    
    label['text'] = "User Has Been Created"

# login function
def login(username, password, label):

    i = 0

    if(len(userObjects) == 0):                               #determines if users even exist           
        label['text'] = 'The username or password you entered did not match our records'
        return

    while(i < len(userObjects)):
        if userObjects[i].getUsername() == username and userObjects[i].getPassword() == password:
            label['text'] = 'Login Successful'               
            global current_user                    #set the current user
            current_user = userObjects[i]
            pacing_modes_window()
            return 
        else:
            i += 1

    label['text'] = 'The username or password you entered did not match our records'
    return

# AOO Pacing Functionality
def AOO_Pace(lowerRate, upperRate, atrialPulseWidth, atrialAmplitude, label):
    data_mode = 1
    pace_mode = 0
    if(int(lowerRate) < 30 or int(lowerRate) > 120):
        label['text'] = 'Please input a Lower Rate between 343ms and 2000ms'
    elif(float(atrialAmplitude) < 0.5 or float(atrialAmplitude) > 5):
        label['text'] = 'Please input an Atrial Amplitude between 500mV and 5000mV'
    elif(float(atrialPulseWidth) < 0.1 or float(atrialPulseWidth) > 1.9):
        label['text'] = 'Please input an Atrial Pulse Width between 1ms and 30ms'
    else:
        print(lowerRate, upperRate, atrialPulseWidth, atrialAmplitude)
        label['text'] = 'Successfully sent parameters'
        current_user.userUpdate(["lower_rate", "upper_rate", "atrial_pulse_width", "atrial_amplitude"], [lowerRate, upperRate, atrialPulseWidth, atrialAmplitude])
        set_data(["data_mode", "pace_mode", "lower_rate", "atrial_pulse_width", "atrial_amplitude"],[data_mode, pace_mode, lowerRate, atrialPulseWidth, atrialAmplitude])
        serial_send()

# VOO_Pace Pacing Functionality
def VOO_Pace(lowerRate, upperRate, ventricularAmplitude, ventricularPulseWidth, label):
    data_mode = 0
    pace_mode = 1
    if(int(lowerRate) < 343 or int(lowerRate) > 2000 ):
        label['text'] = 'Please input a Lower Rate between 343ms and 2000ms'
    elif(int(ventricularAmplitude) < 500 or int(ventricularAmplitude) > 5000):
        label['text'] = 'Please input a Ventricular Amplitude between 500mv and 5000mv'
    elif(int(ventricularPulseWidth) < 1 or int(ventricularPulseWidth) > 30):
        label['text'] = 'Please input a Ventricular Pulse Width between 1ms and 30'
    else:
        print(lowerRate, upperRate, ventricularAmplitude, ventricularPulseWidth)
        label['text'] = 'Successfully sent parameters'
        current_user.userUpdate(["lower_rate", "upper_rate", "ventricular_amplitude", "ventricular_pulse_width"], [lowerRate, upperRate, ventricularAmplitude, ventricularPulseWidth])
        set_data(["data_mode", "pace_mode", "lower_rate", "ventricular_amplitude", "ventricular_pulse_width"],[data_mode, pace_mode, lowerRate, ventricularAmplitude, ventricularPulseWidth])
        serial_send()

# AAI Pacing Functionality
def AAI_Pace(lowerRate, upperRate, atrialPulseWidth, atrialAmplitude, ARP, label):
    data_mode = 0
    pace_mode = 2
    if(int(lowerRate) < 343 or int(lowerRate) > 2000 ):
        label['text'] = 'Please input a Lower Rate between 343ms and 2000ms'
    elif(int(atrialAmplitude) < 500 or int(atrialAmplitude) > 5000):
        label['text'] = 'Please input an Atrial Amplitude between 500mV and 5000mV'
    elif(int(atrialPulseWidth) < 1 or int(atrialPulseWidth) > 30):
        label['text'] = 'Please input an Atrial Pulse Width between 1ms and 30ms'
    elif(int(ARP) < 150 or int(ARP) > 500):
        label['text'] = 'Please input an ARP between 150ms and 500ms'
    else:
        print(lowerRate, upperRate, atrialPulseWidth, atrialAmplitude, ARP)
        label['text'] = 'Successfully sent parameters'
        current_user.userUpdate(["lower_rate", "upper_rate", "atrial_pulse_width", "atrial_amplitude", "ARP"], [lowerRate, upperRate, atrialPulseWidth, atrialAmplitude, ARP])
        set_data(["data_mode", "pace_mode", "lower_rate", "atrial_pulse_width", "atrial_amplitude", "ARP"],[data_mode, pace_mode, lowerRate, atrialPulseWidth, atrialAmplitude, ARP])
        serial_send()

# VVI Pacing Functionality
def VVI_Pace(lowerRate, upperRate, ventricularPulseWidth, ventricularAmplitude, VRP, label):
    data_mode = 0
    pace_mode = 3
    if(int(lowerRate) < 343 or int(lowerRate) > 2000 ):
        label['text'] = 'Please input a Lower Rate between 343ms and 2000ms'
    elif(int(ventricularAmplitude) < 500 or int(ventricularAmplitude) > 5000):
        label['text'] = 'Please input a Ventricular Amplitude between 500mV and 5000mV'
    elif(int(ventricularPulseWidth) < 1 or int(ventricularPulseWidth) > 30):
        label['text'] = 'Please input a Ventricular Pulse Width between 1ms and 30ms'
    elif(int(VRP) < 150 or int(VRP) > 500):
        label['text'] = 'Please input a VPR value between 150ms and 500ms'
    else:
        print(lowerRate, upperRate, ventricularPulseWidth, ventricularAmplitude, VRP)
        label['text'] = 'Successfully sent parameters'
        current_user.userUpdate(["lower_rate", "upper_rate", "ventricular_pulse_width", "ventricular_amplitude", "VRP"], [lowerRate, upperRate, ventricularPulseWidth, ventricularAmplitude, VRP])
        set_data(["data_mode", "pace_mode", "lower_rate", "ventricular_pulse_width", "ventricular_amplitude", "VRP"],[data_mode, pace_mode, lowerRate, ventricularPulseWidth, ventricularAmplitude, VRP])
        serial_send()

#DOO Pacing Functionality 
def DOO_Pace(lowerRate, upperRate, atrialAmplitude, ventricularAmplitude, atrialPulseWidth, ventricularPulseWidth, label):
    if(int(lowerRate) < 30 or int(lowerRate) > 175 ):
        label['text'] = 'Please input a Lower Rate between 30ms and 175ms'
    elif(int(upperRate) < 50 or int(upperRate) > 175):
        label['text'] = 'Please input an Upper Rate between 50ppm and 175ppm'
    elif(float(atrialAmplitude) != 0 or float(atrialAmplitude) != 1.25 or float(atrialAmplitude) != 2.5 or float(atrialAmplitude) != 3.75 or float(atrialAmplitude) != 5.0):
        label['text'] = 'Please input an Atrial Amplitude of 0, 1.25V, 2.5V, 3.75V, or 5.0V'
    elif(float(atrialPulseWidth) < 0.1 or float(atrialPulseWidth) > 1.9):
        label['text'] = 'Please input an Atrial Pulse Width between 0.1ms and 1.9ms'
    elif(float(ventricularAmplitude) not in [0, 1.25, 2.50, 3.75, 5.0]):
        label['text'] = 'Please input a Ventricular Amplitude of 0, 1.25V, 2.5V, 3.75V, or 5.0V'
    elif(float(ventricularPulseWidth) < 0.1 or float(ventricularPulseWidth) > 1.9):
        label['text'] = 'Please input a Ventricular Pulse Width between 1ms and 30ms'
        return

#AOOR Pacing Functionality 
def AOOR_Pace(lowerRate, upperRate, maxSensorRate, atrialAmplitude, atrialPulseWidth, label):
    if(int(lowerRate) < 30 or int(lowerRate) > 175 ):
        label['text'] = 'Please input a Lower Rate between 30ms and 175ms'
    elif(int(upperRate) < 50 or int(upperRate) > 175):
        label['text'] = 'Please input an Upper Rate between 50ppm and 175ppm'
    elif(int(maxSensorRate) < 50 or int(maxSensorRate) > 175):
        label['text'] = 'Please input an Max Sensor Rate between 50ppm and 175ppm'
    elif(float(atrialAmplitude) not in [0, 1.25, 2.50, 3.75, 5.0]):
        label['text'] = 'Please input a Atrial Amplitude of 0, 1.25V, 2.5V, 3.75V, or 5.0V'
    elif(float(atrialPulseWidth) < 0.1 or float(atrialPulseWidth) > 1.9):
        label['text'] = 'Please input an Atrial Pulse Width between 0.1ms and 1.9ms'

#VOOR Pacing Functionality 
def VOOR_Pace(lowerRate, upperRate, maxSensorRate, ventricularAmplitude, ventricularPulseWidth, activityThreshold, reactionTime, responseFactor, recoveryTime, label):
    print(float(ventricularAmplitude) == 1.25)
    if(int(lowerRate) < 30 or int(lowerRate) > 175 ):
        label['text'] = 'Please input a Lower Rate between 30ms and 175ms'
    elif(int(upperRate) < 50 or int(upperRate) > 175):
        label['text'] = 'Please input an Upper Rate between 50ppm and 175ppm'
    elif(int(maxSensorRate) < 50 or int(maxSensorRate) > 175):
        label['text'] = 'Please input an Max Sensor Rate between 50ppm and 175ppm'
    elif(float(ventricularAmplitude) not in [0, 1.25, 2.50, 3.75, 5.0]):
        label['text'] = 'Please input a Ventricular Amplitude of 0, 1.25V, 2.5V, 3.75V, or 5.0V'
    elif(float(ventricularPulseWidth) < 0.1 or float(ventricularPulseWidth) > 1.9):
        label['text'] = 'Please input a Ventricular Pulse Width between 1ms and 30ms'
    elif(activityThreshold not in ['V-Low', 'Low', 'Med-Low', 'Med', 'Med-High', 'High', 'V-High']):
        label['text'] = 'Input one of the options: V-Low, Low, Med-Low, Med, Med-High, High, V-High'
    elif(int(reactionTime) < 10 or int(reactionTime) > 50):
        label['text'] = 'Please input a Reaction Time between the values of 10s and 50s'
    elif(int(responseFactor) < 1 or int(responseFactor) > 16):
        label['text'] = 'Please input a Resposne Factor value between 1 and 16'
    elif(int(recoveryTime) < 2 or int(recoveryTime) > 16):
        label['text'] = 'Please input a Recover Time value between 2 and 16'

#AAIR Pacing Functionality 
def AAIR_Pace(lowerRate, upperRate, maxSensorRate, atrialAmplitude, atrialPulseWidth, atrialSensitivity, ARP, RVARP, hysteresis, rateSmoothing, activityThreshold, reactionTime, responseFactor, recoveryTime, label):
    if(int(lowerRate) < 30 or int(lowerRate) > 175 ):
        label['text'] = 'Please input a Lower Rate between 30ms and 175ms'
    elif(int(upperRate) < 50 or int(upperRate) > 175):
        label['text'] = 'Please input an Upper Rate between 50ppm and 175ppm'
    elif(int(maxSensorRate) < 50 or int(maxSensorRate) > 175):
        label['text'] = 'Please input an Max Sensor Rate between 50ppm and 175ppm'
    elif(float(atrialAmplitude) not in [0, 1.25, 2.50, 3.75, 5.0]):
        label['text'] = 'Please input a Atrial Amplitude of 0, 1.25V, 2.5V, 3.75V, or 5.0V'
    elif(float(atrialPulseWidth) < 0.1 or float(atrialPulseWidth) > 1.9):
        label['text'] = 'Please input an Atrial Pulse Width between 0.1ms and 1.9ms'
        return
    elif(int(ARP) < 150 or int(ARP) > 500):
        label['text'] = 'Please input an ARP between 150ms and 500ms'
        return
    elif(float(atrialSensitivity) not in [0.25, 0.50, 0.75] and (float(atrialSensitivity) < 1.0 or float(atrialSensitivity) > 10.0)):
        label['text'] = 'Please input a Ventricular Sensitivty of 0.25mV, 0.50mV, 0.75mV, or between the values of 1.0mV and 10.0mV'
    elif(float(int(rateSmoothing) > 21 or rateSmoothing) % 3 != 0):
        label['text'] = 'Please input a Rate Smoothing value of 0, 3, 6, 9, 12, 15, 18, or 21'
    elif(int(hysteresis) < 200 or int(hysteresis) > 500):
        label['text'] = 'Please input a Hysteresis value between 200ms and 500ms'
        return
    # elif(activityThreshold not in ['V-Low', 'Low', 'Med-Low', 'Med', 'Med-High', 'High', 'V-High']):
    #     label['text'] = 'Please input one of the options: V-Low, Low, Med-Low, Med, Med-High, High, V-High'
    elif(int(reactionTime) < 10 or int(reactionTime) > 50):
        label['text'] = 'Please input a Reaction Time between the values of 10s and 50s'
    elif(int(responseFactor) < 1 or int(responseFactor) > 16):
        label['text'] = 'Please input a Resposne Factor value between 1 and 16'
    elif(int(recoveryTime) < 2 or int(recoveryTime) > 16):
        label['text'] = 'Please input a Recover Time value between 2 and 16'

#VVIR Pacing Functionality 
def VVIR_Pace(lowerRate, upperRate, maxSensorRate, ventricularAmplitude, ventricularPulseWidth, ventricularSensitivity, VRP, RVVRP, hysteresis, rateSmoothing, activityThreshold, reactionTime, responseFactor, recoveryTime, label):
    if(int(lowerRate) < 30 or int(lowerRate) > 175 ):
        label['text'] = 'Please input a Lower Rate between 30ms and 175ms'
        return
    elif(int(upperRate) < 50 or int(upperRate) > 175):
        label['text'] = 'Please input an Upper Rate between 50ppm and 175ppm'
    elif(int(maxSensorRate) < 50 or int(maxSensorRate) > 175):
        label['text'] = 'Please input an Max Sensor Rate between 50ppm and 175ppm'
    elif(float(ventricularAmplitude) not in [0, 1.25, 2.50, 3.75, 5.0]):
        label['text'] = 'Please input a Ventricular Amplitude of 0, 1.25V, 2.5V, 3.75V, or 5.0V'
    elif(float(ventricularPulseWidth) < 0.1 or float(ventricularPulseWidth) > 1.9):
        label['text'] = 'Please input a Ventricular Pulse Width between 1ms and 30ms'
        return
    elif(int(VRP) < 150 or int(VRP) > 500):
        label['text'] = 'Please input a VPR value between 150ms and 500ms'
        return
    elif(float(ventricularSensitivity) not in [0.25, 0.50, 0.75] and float(ventricularSensitivity) < 1.0 or float(ventricularSensitivity) > 10.0):
        label['text'] = 'Please input a Ventricular Sensitivty of 0.25mV, 0.50mV, 0.75mV, or between the values of 1.0mV and 10.0mV'
    elif(float(int(rateSmoothing) > 21 or rateSmoothing) % 3 != 0):
        label['text'] = 'Please input a Rate Smoothing value of 0, 3, 6, 9, 12, 15, 18, or 21'
    elif(int(hysteresis) < 200 or int(hysteresis) > 500):
        label['text'] = 'Please input a Hysteresis value between 200ms and 500ms'
        return
    # elif(activityThreshold not in ['V-Low', 'Low', 'Med-Low', 'Med', 'Med-High', 'High', 'V-High']):
    #     label['text'] = 'Please input one of the options: V-Low, Low, Med-Low, Med, Med-High, High, V-High'
    elif(int(reactionTime) < 10 or int(reactionTime) > 50):
        label['text'] = 'Please input a Reaction Time between the values of 10s and 50s'
    elif(int(responseFactor) < 1 or int(responseFactor) > 16):
        label['text'] = 'Please input a Resposne Factor value between 1 and 16'
    elif(int(recoveryTime) < 2 or int(recoveryTime) > 16):
        label['text'] = 'Please input a Recover Time value between 2 and 16'

#DOOR Pacing Functionality 
def DOOR_Pace(lowerRate, upperRate, maxSensorRate, fixedAVDelay, atrialAmplitude, ventricularAmplitude, atrialPulseWidth, ventricularPulseWidth, activityThreshold, reactionTime, responseFactor, recoveryTime, label):
    if(int(lowerRate) < 30 or int(lowerRate) > 175 ):
        label['text'] = 'Please input a Lower Rate between 30ppm and 175ppm'
    elif(int(upperRate) < 50 or int(upperRate) > 175):
        label['text'] = 'Please input an Upper Rate between 50ppm and 175ppm'
    elif(int(fixedAVDelay) < 70 or int(fixedAVDelay) > 300):
        label['text'] = 'Please input a Fixed AV Delay between 70ms and 300ms'
    elif(int(maxSensorRate) < 50 or int(maxSensorRate) > 175):
        label['text'] = 'Please input an Max Sensor Rate between 50ppm and 175ppm'
    elif(float(atrialAmplitude) not in [0, 1.25, 2.50, 3.75, 5.0]):
        label['text'] = 'Please input a Atrial Amplitude of 0, 1.25V, 2.5V, 3.75V, or 5.0V'
    elif(float(atrialPulseWidth) < 0.1 or float(atrialPulseWidth) > 1.9):
        label['text'] = 'Please input an Atrial Pulse Width between 0.1ms and 1.9ms'
    elif(float(ventricularAmplitude) not in [0, 1.25, 2.50, 3.75, 5.0]):
        label['text'] = 'Please input a Ventricular Amplitude of 0, 1.25V, 2.5V, 3.75V, or 5.0V'
        return
    elif(float(ventricularPulseWidth) < 0.1 or float(ventricularPulseWidth) > 1.9):
        label['text'] = 'Input a Ventricular Pulse Width between 0.1ms and 1.9ms'
        return
    # elif(activityThreshold not in ['V-Low', 'Low', 'Med-Low', 'Med', 'Med-High', 'High', 'V-High']):
    #     label['text'] = 'Please input one of the options: V-Low, Low, Med-Low, Med, Med-High, High, V-High'
    elif(int(reactionTime) < 10 or int(reactionTime) > 50):
        label['text'] = 'Please input a Reaction Time between the values of 10s and 50s'
    elif(int(responseFactor) < 1 or int(responseFactor) > 16):
        label['text'] = 'Please input a Resposne Factor value between 1 and 16'
    elif(int(recoveryTime) < 2 or int(recoveryTime) > 16):
        label['text'] = 'Please input a Recover Time value between 2 and 16'

# Receiving Pacemaker ID and connection status
current_pacemakerID = 4125
DCM_status_val = 1                 # 1 = connected, 0 = no connection


########## Front End ##########

# AOO_window
def AOO_window():

    AOO_window = tk.Toplevel(root, height = HEIGHT, width = WIDTH)
    AOO_window.configure(background = '#551033')

    lower_rate_limit = tk.Entry(AOO_window, text = "Lower Rate Limit ")
    lower_rate_limit.place(relx = 0.50, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    lower_rate_label = tk.Label(AOO_window, text = 'Lower Rate Limit (343ms - 2000ms)', bg = '#551033')
    lower_rate_label.place(relx = 0.50, rely = 0.09, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    upper_rate_limit = tk.Entry(AOO_window, text = "Upper Rate Limit")
    upper_rate_limit.place(relx = 0.50, rely = 0.20, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    upper_rate_label = tk.Label(AOO_window, text = 'Upper Rate Limit', bg = '#551033')
    upper_rate_label.place(relx = 0.50, rely = 0.24, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    atrial_amplitude = tk.Entry(AOO_window, text = "Atrial Amplitude")
    atrial_amplitude.place(relx = 0.50, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    atrial_amplitude_label = tk.Label(AOO_window, text = 'Atrial Amplitude (500mV - 5000mV)', bg = '#551033')
    atrial_amplitude_label.place(relx = 0.50, rely = 0.39, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    atrial_pulse_width = tk.Entry(AOO_window, text = "Atrial Pulse Width")
    atrial_pulse_width.place(relx = 0.50, rely = 0.50, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    atrial_pulse_label = tk.Label(AOO_window, text = 'Atrial Pulse Width (1ms - 30ms)', bg = '#551033')
    atrial_pulse_label.place(relx = 0.50, rely = 0.54, relwidth = 0.30, relheight = 0.040, anchor = 'n')


    error_label = tk.Label(AOO_window, text = '', bg = '#551033')
    error_label.place(relx = 0.5, rely = 0.75, relwidth = 0.5, relheight = 0.05, anchor = 'n')

    if not lower_rate_limit.get() or upper_rate_limit.get() or not atrial_pulse_width.get() or not atrial_amplitude.get():
        error_label['text'] = 'Please ensure every input is filled in' 

    send_parameters_button = tk.Button(
        AOO_window, 
        text = "Send Parameters", 
        font = 96, 
        command = lambda: AOO_Pace(int(lower_rate_limit.get()), int(upper_rate_limit.get()), float(atrial_pulse_width.get()), float(atrial_amplitude.get()), error_label))

    send_parameters_button.place(relx = 0.5, rely = 0.80, relwidth = 0.40, relheight = 0.10, anchor = 'n')

# VOO_window
def VOO_window():

    VOO_window = tk.Toplevel(root, height = HEIGHT, width = WIDTH)
    VOO_window.configure(background = '#551033')

    lower_rate_limit = tk.Entry(VOO_window)
    lower_rate_limit.place(relx = 0.50, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    lower_rate_label = tk.Label(VOO_window, text = 'Lower Rate Limit (343ms - 2000ms)', bg = '#551033')
    lower_rate_label.place(relx = 0.50, rely = 0.09, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    upper_rate_limit = tk.Entry(VOO_window)
    upper_rate_limit.place(relx = 0.50, rely = 0.20, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    upper_rate_label = tk.Label(VOO_window, text = 'Upper Rate Limit', bg = '#551033')
    upper_rate_label.place(relx = 0.50, rely = 0.24, relwidth = 0.30, relheight = 0.040, anchor = 'n')
    
    ventricular_amplitude = tk.Entry(VOO_window)
    ventricular_amplitude.place(relx = 0.50, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    ventricular_amplitude_label = tk.Label(VOO_window, text = 'Ventricular Amplitude (500mv - 5000mv)', bg = '#551033')
    ventricular_amplitude_label.place(relx = 0.50, rely = 0.39, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    ventricular_pulse_width = tk.Entry(VOO_window)
    ventricular_pulse_width.place(relx = 0.50, rely = 0.50, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    ventricular_pulse_width_label = tk.Label(VOO_window, text = 'Ventricular Pulse Width (1ms - 30ms)', bg = '#551033')
    ventricular_pulse_width_label.place(relx = 0.50, rely = 0.54, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    error_label = tk.Label(VOO_window, text = '', bg = '#551033')
    error_label.place(relx = 0.5, rely = 0.75, relwidth = 0.5, relheight = 0.05, anchor = 'n')

    send_parameters_button = tk.Button(
        VOO_window, 
        text = "Send Parameters", 
        font = 96, command = lambda: VOO_Pace(lower_rate_limit.get(), upper_rate_limit.get(), ventricular_amplitude.get(), ventricular_pulse_width.get(), error_label))

    send_parameters_button.place(relx = 0.5, rely = 0.80, relwidth = 0.40, relheight = 0.10, anchor = 'n')
    
# AAI_Window
def AAI_window():

    AAI_window = tk.Toplevel(root, height = HEIGHT, width = WIDTH)
    AAI_window.configure(background = '#551033')

    lower_rate_limit = tk.Entry(AAI_window)
    lower_rate_limit.place(relx = 0.50, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    lower_rate_label = tk.Label(AAI_window, text = 'Lower Rate Limit (343ms - 2000ms)', bg = '#551033')
    lower_rate_label.place(relx = 0.50, rely = 0.09, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    upper_rate_limit = tk.Entry(AAI_window)
    upper_rate_limit.place(relx = 0.50, rely = 0.20, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    upper_rate_label = tk.Label(AAI_window, text = 'Upper Rate Limit', bg = '#551033')
    upper_rate_label.place(relx = 0.50, rely = 0.24, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    atrial_amplitude = tk.Entry(AAI_window)
    atrial_amplitude.place(relx = 0.50, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    atrial_amplitude_label = tk.Label(AAI_window, text = 'Atrial Ampltiude (500mV - 5000mV)', bg = '#551033')
    atrial_amplitude_label.place(relx = 0.50, rely = 0.39, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    atrial_pulse_width = tk.Entry(AAI_window)
    atrial_pulse_width.place(relx = 0.50, rely = 0.50, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    atrial_pulse_width_label = tk.Label(AAI_window, text = 'Atrial Pulse Width (1ms - 30ms)', bg = '#551033')
    atrial_pulse_width_label.place(relx = 0.50, rely = 0.54, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    ARP = tk.Entry(AAI_window, text = "ARP")
    ARP.place(relx = 0.50, rely = 0.65, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    ARP_label = tk.Label(AAI_window, text = 'ARP (150ms - 500ms)', bg = '#551033')
    ARP_label.place(relx = 0.50, rely = 0.69, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    error_label = tk.Label(AAI_window, text = '', bg = '#551033')
    error_label.place(relx = 0.5, rely = 0.75, relwidth = 0.5, relheight = 0.05, anchor = 'n')

    send_parameters_button = tk.Button(AAI_window, text = "Send Parameters", font = 96, command = lambda: AAI_Pace(lower_rate_limit.get(), upper_rate_limit.get(), atrial_pulse_width.get(), atrial_amplitude.get(), ARP.get(), error_label))
    send_parameters_button.place(relx = 0.5, rely = 0.80, relwidth = 0.40, relheight = 0.10, anchor = 'n')

#VVI_window
def VVI_window():

    VVI_window = tk.Toplevel(root, height = HEIGHT, width = WIDTH)
    VVI_window.configure(background = '#551033')

    lower_rate_limit = tk.Entry(VVI_window)
    lower_rate_limit.place(relx = 0.50, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    lower_rate_label = tk.Label(VVI_window, text = 'Lower Rate Limit (343ms - 2000ms)', bg = '#551033')
    lower_rate_label.place(relx = 0.50, rely = 0.09, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    upper_rate_limit = tk.Entry(VVI_window)
    upper_rate_limit.place(relx = 0.50, rely = 0.20, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    upper_rate_label = tk.Label(VVI_window, text = 'Upper Rate Limit', bg = '#551033')
    upper_rate_label.place(relx = 0.50, rely = 0.24, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    ventricular_amplitude = tk.Entry(VVI_window)
    ventricular_amplitude.place(relx = 0.50, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    ventricular_amplitude_label = tk.Label(VVI_window, text = 'Ventricular Ampltiude (500mV - 5000mV)', bg = '#551033')
    ventricular_amplitude_label.place(relx = 0.50, rely = 0.39, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    ventricular_pulse_width = tk.Entry(VVI_window)
    ventricular_pulse_width.place(relx = 0.50, rely = 0.50, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    ventricular_pulse_width_label = tk.Label(VVI_window, text = 'Ventricular Pulse Width (1ms - 30ms)', bg = '#551033')
    ventricular_pulse_width_label.place(relx = 0.50, rely = 0.54, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    VRP = tk.Entry(VVI_window, text = "VRP")
    VRP.place(relx = 0.50, rely = 0.65, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    VRP_label = tk.Label(VVI_window, text = 'VRP (150ms - 500ms)', bg = '#551033')
    VRP_label.place(relx = 0.50, rely = 0.69, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    error_label = tk.Label(VVI_window, text = '', bg = '#551033')
    error_label.place(relx = 0.5, rely = 0.75, relwidth = 0.5, relheight = 0.05, anchor = 'n')

    send_parameters_button = tk.Button(VVI_window, text = "Send Parameters", font = 96, command = lambda: VVI_Pace(lower_rate_limit.get(), upper_rate_limit.get(), ventricular_pulse_width.get(), ventricular_amplitude.get(), VRP.get(), error_label))
    send_parameters_button.place(relx = 0.5, rely = 0.80, relwidth = 0.40, relheight = 0.10, anchor = 'n')

##DOO_window
def DOO_window():

    DOO_window = tk.Toplevel(root, height = HEIGHT, width = WIDTH)
    DOO_window.configure(background = '#551033')

    lower_rate_limit = tk.Entry(DOO_window, text = "Lower Rate Limit ")
    lower_rate_limit.place(relx = 0.50, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    lower_rate_label = tk.Label(DOO_window, text = 'Lower Rate Limit', bg = '#551033')
    lower_rate_label.place(relx = 0.50, rely = 0.09, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    upper_rate_limit = tk.Entry(DOO_window, text = "Upper Rate Limit")
    upper_rate_limit.place(relx = 0.50, rely = 0.15, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    upper_rate_label = tk.Label(DOO_window, text = 'Upper Rate Limit', bg = '#551033')
    upper_rate_label.place(relx = 0.50, rely = 0.19, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    atrial_pules_width = tk.Entry(DOO_window, text = "Atrial Pules Width")
    atrial_pules_width.place(relx = 0.50, rely = 0.25, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    atrial_pules_label = tk.Label(DOO_window, text = 'Atrial Pules', bg = '#551033')
    atrial_pules_label.place(relx = 0.50, rely = 0.29, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    atrial_amplitude = tk.Entry(DOO_window, text = "Atrial Amplitude")
    atrial_amplitude.place(relx = 0.50, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    atrial_amplitude_label = tk.Label(DOO_window, text = 'Atrial Amplitude', bg = '#551033')
    atrial_amplitude_label.place(relx = 0.50, rely = 0.39, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    ventricular_amplitude = tk.Entry(DOO_window)
    ventricular_amplitude.place(relx = 0.50, rely = 0.45, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    ventricular_amplitude_label = tk.Label(DOO_window, text = 'Ventricular Amplitude', bg = '#551033')
    ventricular_amplitude_label.place(relx = 0.50, rely = 0.49, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    ventricular_pulse_width = tk.Entry(DOO_window)
    ventricular_pulse_width.place(relx = 0.50, rely = 0.55, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    ventricular_pulse_width_label = tk.Label(DOO_window, text = 'Ventricular Pulse Width', bg = '#551033')
    ventricular_pulse_width_label.place(relx = 0.50, rely = 0.59, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    error_label = tk.Label(DOO_window, text = '', bg = '#551033')
    error_label.place(relx = 0.5, rely = 0.75, relwidth = 0.5, relheight = 0.05, anchor = 'n')

    if not lower_rate_limit.get() or not upper_rate_limit.get() or not atrial_pules_width.get() or not atrial_amplitude.get() or not ventricular_pulse_width.get() or not ventricular_amplitude.get():
        error_label['text'] = 'Please ensure every input is filled in' 

    pace_now_button = tk.Button(DOO_window, text = "Pace Now", font = 96, command = lambda: DOO_Pace(int(lower_rate_limit.get()), int(upper_rate_limit.get()), float(atrial_pules_width.get()), float(ventricular_amplitude.get()), float(atrial_amplitude.get()), float(ventricular_pulse_width.get()), error_label))
    pace_now_button.place(relx = 0.5, rely = 0.80, relwidth = 0.40, relheight = 0.10, anchor = 'n')

#AOOR_window
def AOOR_window():
    AOOR_window = tk.Toplevel(root, height = HEIGHT, width = WIDTH)
    AOOR_window.configure(background = '#551033')

    lower_rate_limit = tk.Entry(AOOR_window, text = "Lower Rate Limit ")
    lower_rate_limit.place(relx = 0.50, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    lower_rate_label = tk.Label(AOOR_window, text = 'Lower Rate Limit', bg = '#551033')
    lower_rate_label.place(relx = 0.50, rely = 0.09, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    upper_rate_limit = tk.Entry(AOOR_window, text = "Upper Rate Limit")
    upper_rate_limit.place(relx = 0.50, rely = 0.20, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    upper_rate_label = tk.Label(AOOR_window, text = 'Upper Rate Limit', bg = '#551033')
    upper_rate_label.place(relx = 0.50, rely = 0.24, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    atrial_pules_width = tk.Entry(AOOR_window, text = "Atrial Pules Width")
    atrial_pules_width.place(relx = 0.50, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    atrial_pules_label = tk.Label(AOOR_window, text = 'Atrial Pules', bg = '#551033')
    atrial_pules_label.place(relx = 0.50, rely = 0.39, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    atrial_amplitude = tk.Entry(AOOR_window, text = "Atrial Amplitude")
    atrial_amplitude.place(relx = 0.50, rely = 0.50, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    atrial_amplitude_label = tk.Label(AOOR_window, text = 'Atrial Amplitude', bg = '#551033')
    atrial_amplitude_label.place(relx = 0.50, rely = 0.54, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    maxSensorRate = tk.Entry(AOOR_window, text = "Max Sensor Rate")
    maxSensorRate.place(relx = 0.50, rely = 0.65, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    maxSensorRate_label = tk.Label(AOOR_window, text = 'Max Sensor Rate', bg = '#551033')
    maxSensorRate_label.place(relx = 0.50, rely = 0.69, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    error_label = tk.Label(AOOR_window, text = '', bg = '#551033')
    error_label.place(relx = 0.5, rely = 0.75, relwidth = 0.5, relheight = 0.05, anchor = 'n')

    if not lower_rate_limit.get() or not upper_rate_limit.get() or not maxSensorRate.get() or not atrial_amplitude.get() or not atrial_pules_width.get():
        error_label['text'] = 'Please ensure every input is filled in' 

    pace_now_button = tk.Button(AOOR_window, text = "Pace Now", font = 96, command = lambda: AOOR_Pace(int(lower_rate_limit.get()), int(upper_rate_limit.get()), int(maxSensorRate.get()), float(atrial_amplitude.get()), float(atrial_pules_width.get()), error_label))
    pace_now_button.place(relx = 0.5, rely = 0.80, relwidth = 0.40, relheight = 0.10, anchor = 'n')

#VOOR_window
def VOOR_window():

    VOOR_window = tk.Toplevel(root, height = HEIGHT, width = WIDTH)
    VOOR_window.configure(background = '#551033')

    '''Left Side'''

    lower_rate_limit = tk.Entry(VOOR_window, text = "Lower Rate Limit ")
    lower_rate_limit.place(relx = 0.2, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    lower_rate_label = tk.Label(VOOR_window, text = 'Lower Rate Limit', bg = '#551033')
    lower_rate_label.place(relx = 0.2, rely = 0.09, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    upper_rate_limit = tk.Entry(VOOR_window, text = "Upper Rate Limit")
    upper_rate_limit.place(relx = 0.2, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    upper_rate_label = tk.Label(VOOR_window, text = 'Upper Rate Limit', bg = '#551033')
    upper_rate_label.place(relx = 0.2, rely = 0.39, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    ventricular_pulse_width = tk.Entry(VOOR_window, text = "Ventricular Pulse Width")
    ventricular_pulse_width.place(relx = 0.20, rely = 0.65, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    ventricular_pulse_width_label = tk.Label(VOOR_window, text = 'Ventricular Pulse Width', bg = '#551033')
    ventricular_pulse_width_label.place(relx = 0.20, rely = 0.69, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    '''Middle'''

    ventricular_amplitude = tk.Entry(VOOR_window)
    ventricular_amplitude.place(relx = 0.50, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    ventricular_amplitude_label = tk.Label(VOOR_window, text = 'Ventricular Ampltiude', bg = '#551033')
    ventricular_amplitude_label.place(relx = 0.50, rely = 0.09, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    activity_threshold = tk.Entry(VOOR_window)
    activity_threshold.place(relx = 0.5, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    activity_threshold_label = tk.Label(VOOR_window, text = 'Activity Threshold', bg = '#551033')
    activity_threshold_label.place(relx = 0.5, rely = 0.39, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    recation_time = tk.Entry(VOOR_window)
    recation_time.place(relx = 0.50, rely = 0.65, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    recation_time_label = tk.Label(VOOR_window, text = 'Reaction Time', bg = '#551033')
    recation_time_label.place(relx = 0.50, rely = 0.69, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    '''Right Side'''

    response_factor = tk.Entry(VOOR_window)
    response_factor.place(relx = 0.80, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    response_factor_label = tk.Label(VOOR_window, text = 'Response Factor', bg = '#551033')
    response_factor_label.place(relx = 0.80, rely = 0.09, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    recovery_time = tk.Entry(VOOR_window)
    recovery_time.place(relx = 0.80, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    recovery_time_label = tk.Label(VOOR_window, text = 'Recovery Time', bg = '#551033')
    recovery_time_label.place(relx = 0.80, rely = 0.39, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    maxSensorRate = tk.Entry(VOOR_window, text = "Max Sensor Rate")
    maxSensorRate.place(relx = 0.80, rely = 0.65, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    maxSensorRate_label = tk.Label(VOOR_window, text = 'Max Sensor Rate', bg = '#551033')
    maxSensorRate_label.place(relx = 0.80, rely = 0.69, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    error_label = tk.Label(VOOR_window, text = '', bg = '#551033')
    error_label.place(relx = 0.5, rely = 0.85, relwidth = 0.5, relheight = 0.05, anchor = 'n')

    if not lower_rate_limit.get() or not upper_rate_limit.get() or not maxSensorRate.get() or not ventricular_amplitude.get() or not ventricular_pulse_width.get() or not activity_threshold.get() or not recation_time.get() or not response_factor.get() or not recovery_time.get():
        error_label['text'] = 'Please ensure every input is filled in' 

    pace_now_button = tk.Button(VOOR_window, text = "Pace Now", font = 96, command = lambda: VOOR_Pace(int(lower_rate_limit.get()), int(upper_rate_limit.get()), int(maxSensorRate.get()), float(ventricular_amplitude.get()), float(ventricular_pulse_width.get()), int(activity_threshold.get()), int(recation_time.get()), int(response_factor.get()), int(recovery_time.get()), error_label))
    pace_now_button.place(relx = 0.5, rely = 0.90, relwidth = 0.40, relheight = 0.10, anchor = 'n')

#AAIR_window
def AAIR_window():
    AAIR_window = tk.Toplevel(root, height = HEIGHT, width = WIDTH)
    AAIR_window.configure(background = '#551033')

    '''LeftSide'''

    lower_rate_limit = tk.Entry(AAIR_window)
    lower_rate_limit.place(relx = 0.20, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    lower_rate_label = tk.Label(AAIR_window, text = 'Lower Rate Limit', bg = '#551033')
    lower_rate_label.place(relx = 0.20, rely = 0.09, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    upper_rate_limit = tk.Entry(AAIR_window)
    upper_rate_limit.place(relx = 0.20, rely = 0.20, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    upper_rate_label = tk.Label(AAIR_window, text = 'Upper Rate Limit', bg = '#551033')
    upper_rate_label.place(relx = 0.20, rely = 0.24, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    maxSensorRate = tk.Entry(AAIR_window, text = "Max Sensor Rate")
    maxSensorRate.place(relx = 0.20, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    maxSensorRate_label = tk.Label(AAIR_window, text = 'Max Sensor Rate', bg = '#551033')
    maxSensorRate_label.place(relx = 0.20, rely = 0.39, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    atrial_amplitude = tk.Entry(AAIR_window)
    atrial_amplitude.place(relx = 0.20, rely = 0.50, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    atrial_amplitude_label = tk.Label(AAIR_window, text = 'Atrial Ampltiude', bg = '#551033')
    atrial_amplitude_label.place(relx = 0.20, rely = 0.54, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    '''MIDDLE'''

    atrial_sensitivity = tk.Entry(AAIR_window)
    atrial_sensitivity.place(relx = 0.50, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    atrial_sensitivity_label = tk.Label(AAIR_window, text = 'Atrial Sensitivity', bg = '#551033')
    atrial_sensitivity_label.place(relx = 0.50, rely = 0.09, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    atrial_pulse_width = tk.Entry(AAIR_window)
    atrial_pulse_width.place(relx = 0.50, rely = 0.20, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    atrial_pulse_width_label = tk.Label(AAIR_window, text = 'Atrial Pulse Width', bg = '#551033')
    atrial_pulse_width_label.place(relx = 0.50, rely = 0.24, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    ARP = tk.Entry(AAIR_window, text = "ARP")
    ARP.place(relx = 0.50, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    ARP_label = tk.Label(AAIR_window, text = 'ARP', bg = '#551033')
    ARP_label.place(relx = 0.50, rely = 0.39, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    RVARP = tk.Entry(AAIR_window, text = "RVARP")
    RVARP.place(relx = 0.50, rely = 0.50, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    RVARP_label = tk.Label(AAIR_window, text = 'RVARP', bg = '#551033')
    RVARP_label.place(relx = 0.50, rely = 0.54, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    '''Right'''

    hysteresis = tk.Entry(AAIR_window, text = "Hysteresis")
    hysteresis.place(relx = 0.80, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    hysteresis_label = tk.Label(AAIR_window, text = 'Hysteresis', bg = '#551033')
    hysteresis_label.place(relx = 0.80, rely = 0.09, relwidth = 0.20, relheight = 0.040, anchor = 'n')


    activity_threshold = tk.Entry(AAIR_window)
    activity_threshold.place(relx = 0.80, rely = 0.20, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    activity_threshold_label = tk.Label(AAIR_window, text = 'Activity Threshold', bg = '#551033')
    activity_threshold_label.place(relx = 0.80, rely = 0.24, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    recation_time = tk.Entry(AAIR_window)
    recation_time.place(relx = 0.80, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    recation_time_label = tk.Label(AAIR_window, text = 'Reaction Time', bg = '#551033')
    recation_time_label.place(relx = 0.80, rely = 0.39, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    response_factor = tk.Entry(AAIR_window)
    response_factor.place(relx = 0.80, rely = 0.50, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    response_factor_label = tk.Label(AAIR_window, text = 'Response Factor', bg = '#551033')
    response_factor_label.place(relx = 0.80, rely = 0.54, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    '''Bottom'''

    recovery_time = tk.Entry(AAIR_window)
    recovery_time.place(relx = 0.65, rely = 0.65, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    recovery_time_label = tk.Label(AAIR_window, text = 'Recovery Time', bg = '#551033')
    recovery_time_label.place(relx = 0.65, rely = 0.69, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    rate_smoothing = tk.Entry(AAIR_window)
    rate_smoothing.place(relx = 0.35, rely = 0.65, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    rate_smoothing_label = tk.Label(AAIR_window, text = 'Rate Smoothing', bg = '#551033')
    rate_smoothing_label.place(relx = 0.35, rely = 0.69, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    error_label = tk.Label(AAIR_window, text = '', bg = '#551033')
    error_label.place(relx = 0.5, rely = 0.75, relwidth = 0.5, relheight = 0.05, anchor = 'n')

    if not lower_rate_limit.get() or not upper_rate_limit.get() or not maxSensorRate.get() or not atrial_amplitude.get() or not atrial_pulse_width.get() or not atrial_sensitivity.get() or not ARP.get() or not RVARP.get() or not hysteresis or not activity_threshold.get() or not recation_time.get() or not response_factor.get() or not recovery_time.get() or not rate_smoothing.get():
        error_label['text'] = 'Please ensure every input is filled in' 

    pace_now_button = tk.Button(AAIR_window, text = "Pace Now", font = 96, command = lambda: AAIR_Pace(int(lower_rate_limit.get()), int(upper_rate_limit.get()), int(maxSensorRate.get()), float(atrial_amplitude.get()), float(atrial_pulse_width.get()), float(atrial_sensitivity.get()), int(ARP.get()), int(RVARP.get()), int(hysteresis.get()), float(rate_smoothing.get()), int(activity_threshold.get()), int(recation_time.get()), int(response_factor.get()), int(recovery_time.get()), error_label))
    pace_now_button.place(relx = 0.5, rely = 0.80, relwidth = 0.40, relheight = 0.10, anchor = 'n')

#VVIR_window
def VVIR_window():
    VVIR_window = tk.Toplevel(root, height = HEIGHT, width = WIDTH)
    VVIR_window.configure(background = '#551033')

    '''LeftSide'''

    lower_rate_limit = tk.Entry(VVIR_window)
    lower_rate_limit.place(relx = 0.20, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    lower_rate_label = tk.Label(VVIR_window, text = 'Lower Rate Limit', bg = '#551033')
    lower_rate_label.place(relx = 0.20, rely = 0.09, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    upper_rate_limit = tk.Entry(VVIR_window)
    upper_rate_limit.place(relx = 0.20, rely = 0.15, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    upper_rate_label = tk.Label(VVIR_window, text = 'Upper Rate Limit', bg = '#551033')
    upper_rate_label.place(relx = 0.20, rely = 0.19, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    maxSensorRate = tk.Entry(VVIR_window, text = "Max Sensor Rate")
    maxSensorRate.place(relx = 0.20, rely = 0.25, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    maxSensorRate_label = tk.Label(VVIR_window, text = 'Max Sensor Rate', bg = '#551033')
    maxSensorRate_label.place(relx = 0.20, rely = 0.39, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    ventricular_amplitude = tk.Entry(VVIR_window)
    ventricular_amplitude.place(relx = 0.20, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    ventricular_amplitude_label = tk.Label(VVIR_window, text = 'Ventricular Ampltiude', bg = '#551033')
    ventricular_amplitude_label.place(relx = 0.20, rely = 0.39, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    ventricular_sensitivity = tk.Entry(VVIR_window)
    ventricular_sensitivity.place(relx = 0.20, rely = 0.45, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    ventricular_sensitivity_label = tk.Label(VVIR_window, text = 'Ventricular Sensitivity', bg = '#551033')
    ventricular_sensitivity_label.place(relx = 0.20, rely = 0.49, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    ventricular_pulse_width = tk.Entry(VVIR_window)
    ventricular_pulse_width.place(relx = 0.20, rely = 0.55, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    ventricular_pulse_width_label = tk.Label(VVIR_window, text = 'Ventricular Pulse Width', bg = '#551033')
    ventricular_pulse_width_label.place(relx = 0.20, rely = 0.59, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    '''Right'''
    VRP = tk.Entry(VVIR_window, text = "VRP")
    VRP.place(relx = 0.80, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    VRP_label = tk.Label(VVIR_window, text = 'VRP', bg = '#551033')
    VRP_label.place(relx = 0.80, rely = 0.09, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    hysteresis = tk.Entry(VVIR_window, text = "Hysteresis")
    hysteresis.place(relx = 0.80, rely = 0.15, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    hysteresis_label = tk.Label(VVIR_window, text = 'Hysteresis', bg = '#551033')
    hysteresis_label.place(relx = 0.80, rely = 0.19, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    activity_threshold = tk.Entry(VVIR_window)
    activity_threshold.place(relx = 0.80, rely = 0.25, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    activity_threshold_label = tk.Label(VVIR_window, text = 'Activity Threshold', bg = '#551033')
    activity_threshold_label.place(relx = 0.80, rely = 0.29, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    recation_time = tk.Entry(VVIR_window)
    recation_time.place(relx = 0.80, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    recation_time_label = tk.Label(VVIR_window, text = 'Reaction Time', bg = '#551033')
    recation_time_label.place(relx = 0.80, rely = 0.39, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    response_factor = tk.Entry(VVIR_window)
    response_factor.place(relx = 0.80, rely = 0.45, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    response_factor_label = tk.Label(VVIR_window, text = 'Response Factor', bg = '#551033')
    response_factor_label.place(relx = 0.80, rely = 0.49, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    recovery_time = tk.Entry(VVIR_window)
    recovery_time.place(relx = 0.80, rely = 0.55, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    recovery_time_label = tk.Label(VVIR_window, text = 'Recovery Time', bg = '#551033')
    recovery_time_label.place(relx = 0.80, rely = 0.59, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    '''Bottom'''
    rate_smoothing = tk.Entry(VVIR_window)
    rate_smoothing.place(relx = 0.5, rely = 0.65, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    rate_smoothing_label = tk.Label(VVIR_window, text = 'Rate Smoothing', bg = '#551033')
    rate_smoothing_label.place(relx = 0.50, rely = 0.69, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    error_label = tk.Label(VVIR_window, text = '', bg = '#551033')
    error_label.place(relx = 0.5, rely = 0.75, relwidth = 0.5, relheight = 0.05, anchor = 'n')

    if (not lower_rate_limit.get() or not upper_rate_limit.get() or not maxSensorRate.get() or not ventricular_amplitude.get() or not ventricular_pulse_width or not VRP.get() or not  hysteresis.get() or not rate_smoothing.get() or not activity_threshold.get() or not recation_time.get() or not response_factor.get() or not recovery_time.get()):
        error_label['text'] = 'Please ensure every input is filled in' 

    pace_now_button = tk.Button(VVIR_window, text = "Pace Now", font = 96, command = lambda: VVIR_Pace(int(lower_rate_limit.get()), int(upper_rate_limit.get()), int(maxSensorRate.get()), float(ventricular_amplitude.get()), float(ventricular_pulse_width.get()), int(VRP.get()), int(hysteresis.get()), float(rate_smoothing.get()), int(activity_threshold.get()), int(recation_time.get()), int(response_factor.get()), int(recovery_time.get()), error_label))
    pace_now_button.place(relx = 0.5, rely = 0.80, relwidth = 0.40, relheight = 0.10, anchor = 'n')

#DOOR_window
def DOOR_window():
    DOOR_window = tk.Toplevel(root, height = HEIGHT, width = WIDTH)
    DOOR_window.configure(background = '#551033')

    lower_rate_limit = tk.Entry(DOOR_window, text = "Lower Rate Limit ")
    lower_rate_limit.place(relx = 0.2, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    lower_rate_label = tk.Label(DOOR_window, text = 'Lower Rate Limit', bg = '#551033')
    lower_rate_label.place(relx = 0.2, rely = 0.09, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    upper_rate_limit = tk.Entry(DOOR_window, text = "Upper Rate Limit")
    upper_rate_limit.place(relx = 0.2, rely = 0.20, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    upper_rate_label = tk.Label(DOOR_window, text = 'Upper Rate Limit', bg = '#551033')
    upper_rate_label.place(relx = 0.2, rely = 0.24, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    atrial_pules_width = tk.Entry(DOOR_window, text = "Atrial Pules Width")
    atrial_pules_width.place(relx = 0.2, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    atrial_pules_label = tk.Label(DOOR_window, text = 'Atrial Pulse Width', bg = '#551033')
    atrial_pules_label.place(relx = 0.2, rely = 0.39, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    activity_threshold = tk.Entry(DOOR_window)
    activity_threshold.place(relx = 0.2, rely = 0.50, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    activity_threshold_label = tk.Label(DOOR_window, text = 'Activity Threshold', bg = '#551033')
    activity_threshold_label.place(relx = 0.2, rely = 0.54, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    recation_time = tk.Entry(DOOR_window)
    recation_time.place(relx = 0.50, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    recation_time_label = tk.Label(DOOR_window, text = 'Reaction Time', bg = '#551033')
    recation_time_label.place(relx = 0.50, rely = 0.09, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    response_factor = tk.Entry(DOOR_window)
    response_factor.place(relx = 0.50, rely = 0.20, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    response_factor_label = tk.Label(DOOR_window, text = 'Response Factor', bg = '#551033')
    response_factor_label.place(relx = 0.50, rely = 0.24, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    recovery_time = tk.Entry(DOOR_window)
    recovery_time.place(relx = 0.50, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    recovery_time_label = tk.Label(DOOR_window, text = 'Recovery Time', bg = '#551033')
    recovery_time_label.place(relx = 0.50, rely = 0.39, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    ventricular_pulse_width = tk.Entry(DOOR_window, text = "Ventricular Pulse Width")
    ventricular_pulse_width.place(relx = 0.50, rely = 0.50, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    ventricular_pulse_width_label = tk.Label(DOOR_window, text = 'Ventricular Pulse Width', bg = '#551033')
    ventricular_pulse_width_label.place(relx = 0.50, rely = 0.54, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    atrial_amplitude = tk.Entry(DOOR_window, text = "Atrial Amplitude")
    atrial_amplitude.place(relx = 0.80, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    atrial_amplitude_label = tk.Label(DOOR_window, text = 'Atrial Amplitude', bg = '#551033')
    atrial_amplitude_label.place(relx = 0.80, rely = 0.09, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    ventricular_amplitude = tk.Entry(DOOR_window)
    ventricular_amplitude.place(relx = 0.80, rely = 0.20, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    ventricular_amplitude_label = tk.Label(DOOR_window, text = 'Ventricular Ampltiude', bg = '#551033')
    ventricular_amplitude_label.place(relx = 0.80, rely = 0.24, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    maxSensorRate = tk.Entry(DOOR_window, text = "Max Sensor Rate")
    maxSensorRate.place(relx = 0.80, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    maxSensorRate_label = tk.Label(DOOR_window, text = 'Max Sensor Rate', bg = '#551033')
    maxSensorRate_label.place(relx = 0.80, rely = 0.39, relwidth = 0.20, relheight = 0.040, anchor = 'n')

    fixed_AV_delay = tk.Entry(DOOR_window, text = "Fixed AV Delay")
    fixed_AV_delay.place(relx = 0.80, rely = 0.50, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    fixed_AV_delay_label = tk.Label(DOOR_window, text = 'Fixed AV Delay', bg = '#551033')
    fixed_AV_delay_label.place(relx = 0.80, rely = 0.54, relwidth = 0.20, relheight = 0.040, anchor = 'n')


    error_label = tk.Label(DOOR_window, text = '', bg = '#551033')
    error_label.place(relx = 0.5, rely = 0.85, relwidth = 0.5, relheight = 0.05, anchor = 'n')

    if (not lower_rate_limit.get() or not upper_rate_limit.get() or not maxSensorRate.get() or not fixed_AV_delay.get() or not atrial_amplitude.get() or not ventricular_amplitude.get() or not atrial_amplitude.get() or not atrial_pules_width.get() or not ventricular_pulse_width.get() or not activity_threshold.get() or not recation_time.get() or not response_factor.get() or not recovery_time.get()):
        error_label['text'] = 'Please ensure every input is filled in' 

    pace_now_button = tk.Button(DOOR_window, text = "Pace Now", font = 96, command = lambda: DOOR_Pace(int(lower_rate_limit.get()), int(upper_rate_limit.get()), int(maxSensorRate.get()), int(fixed_AV_delay.get()), float(atrial_amplitude.get()), float(ventricular_amplitude.get()), float(atrial_pules_width.get()), float(ventricular_pulse_width.get()), int(activity_threshold.get()), int(recation_time.get()), int(response_factor.get()), int(recovery_time.get()), error_label))
    pace_now_button.place(relx = 0.5, rely = 0.90, relwidth = 0.40, relheight = 0.10, anchor = 'n')

# pacing_modes_window
# pacing_modes_window
def pacing_modes_window():
    pacing_modes_window = tk.Toplevel(root, height = HEIGHT, width = WIDTH)
    pacing_modes_window.configure(background = '#551033')

    AOO_Button = tk.Button(pacing_modes_window, text = 'AOO', font = 96, command = lambda: AOO_window())
    AOO_Button.place(relx = 0.15, rely = 0.05, relwidth = 0.1, relheight = 0.1)

    VOO_Button = tk.Button(pacing_modes_window, text = 'VOO', font = 96, command = lambda: VOO_window())
    VOO_Button.place(relx = 0.35, rely = 0.45, relwidth = 0.1, relheight = 0.1)

    AAI_Button = tk.Button(pacing_modes_window, text = 'AAI', font = 96, command = lambda: AAI_window())
    AAI_Button.place(relx = 0.75, rely = 0.05, relwidth = 0.1, relheight = 0.1)

    VVI_Button = tk.Button(pacing_modes_window, text = 'VVI', font = 96, command = lambda: VVI_window())
    VVI_Button.place(relx = 0.55, rely = 0.45, relwidth = 0.1, relheight = 0.1)

    DOO_Button = tk.Button(pacing_modes_window, text = 'DOO', font = 96, command = lambda: DOO_window())
    DOO_Button.place(relx = 0.15, rely = 0.25, relwidth = 0.1, relheight = 0.1)

    AOOR_Button = tk.Button(pacing_modes_window, text = 'AOOR', font = 96, command = lambda: AOOR_window())
    AOOR_Button.place(relx = 0.15, rely = 0.45, relwidth = 0.1, relheight = 0.1)

    VOOR_Button = tk.Button(pacing_modes_window, text = 'VOOR', font = 96, command = lambda: VOOR_window())
    VOOR_Button.place(relx = 0.75, rely = 0.45, relwidth = 0.1, relheight = 0.1)

    AAIR_Button = tk.Button(pacing_modes_window, text = 'AAIR', font = 96, command = lambda: AAIR_window())
    AAIR_Button.place(relx = 0.35, rely = 0.05, relwidth = 0.1, relheight = 0.1)

    VVIR_Button = tk.Button(pacing_modes_window, text = 'VVIR', font = 96, command = lambda: VVIR_window())
    VVIR_Button.place(relx = 0.55, rely = 0.05, relwidth = 0.1, relheight = 0.1)

    DOOR_Button = tk.Button(pacing_modes_window, text = 'DOOR', font = 96, command = lambda: DOOR_window())
    DOOR_Button.place(relx = 0.75, rely = 0.25, relwidth = 0.1, relheight = 0.1)

    display_label = tk.Label(pacing_modes_window, bg = '#551033', text = "Select Pacing Mode", font = 96)
    display_label.place(relx = 0.50, rely = 0.25, relwidth = 0.40, relheight = 0.10, anchor = 'n')

    pacemakerID = tk.Label(pacing_modes_window, text = 'Pacemaker Connected: ' + str(current_pacemakerID), bg = '#551033')
    pacemakerID.place(relx = 0.10, rely = 0, relwidth = 0.30, relheight = 0.05, anchor = 'n')

    DCM_status = tk.Label(pacing_modes_window, font = 14)
    DCM_status.place(relx = 0.90, rely = 0, relwidth = 0.15, relheight = 0.05)

    DCM_status_label = tk.Label(pacing_modes_window, bg = '#551033', text = "DCM Status")
    DCM_status_label.place(relx = 0.95, rely = 0.05, relwidth = 0.080, relheight = 0.040, anchor = 'n')

    #Selecting Egram data 

    data_option_label = tk.Label(pacing_modes_window, bg = '#551033', text = 'Select Egram', font = 96)
    data_option_label.place(relx = 0.50, rely = 0.65, relwidth = 0.40, relheight = 0.05, anchor = 'n')

    ventricular_option = tk.Button(pacing_modes_window, text = 'Ventricular Egram', font = 24)
    ventricular_option.place(relx = 0.50, rely = 0.725, relwidth = 0.30, relheight = 0.05, anchor = 'n')

    atrial_option = tk.Button(pacing_modes_window, text = 'Atrial Egram', font = 24)
    atrial_option.place(relx = 0.50, rely = 0.825, relwidth = 0.30, relheight = 0.05, anchor = 'n')

    both_option = tk.Button(pacing_modes_window, text = 'Atrial & Ventricular Egram', font = 24)
    both_option.place(relx = 0.50, rely = 0.925, relwidth = 0.30, relheight = 0.05, anchor = 'n')
    
    global DCM_status_val

    if(DCM_status_val == 1):
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
    create_username_entry = tk.Entry(register_window, text = "Create Username", font = 40)
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