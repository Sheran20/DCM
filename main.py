import tkinter as tk
import os
from user_control import User, getUserData, userObjects
from serial_control import set_data, serial_send, current_pacemakerID, DCM_status_val, serial_read_atr, serial_read_vent, serial_read_atr_vent

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
    dataMode = 0
    paceMode = 0
    if(int(lowerRate) < 30 or int(lowerRate) > 175 ):
        label['text'] = 'Please input a Lower Rate between 30ppm and 175ppm'
    elif(int(upperRate) < 50 or int(upperRate) > 175):
        label['text'] = 'Please input an Upper Rate between 50ppm and 175ppm'
    elif(float(atrialAmplitude) < 0.1 or float(atrialAmplitude) > 5.0):
        label['text'] = 'Please input a Atrial Amplitude between 0.1V and 5.0V'
    elif(float(atrialPulseWidth) < 1 or float(atrialPulseWidth) > 30):
        label['text'] = 'Please input an Atrial Pulse Width between 1ms and 30ms'
    else:
        print(lowerRate, upperRate, atrialPulseWidth, atrialAmplitude)
        label['text'] = 'Successfully sent parameters'
        # update user
        current_user.userUpdate(["lower_rate", "upper_rate", "atrial_amplitude", "atrial_pulse_width"], 
        [lowerRate, upperRate, atrialAmplitude, atrialPulseWidth])
        # send data to pacemaker
        serial_send(["data_mode", "pace_mode", "lower_rate", "atrial_amplitude", "atrial_pulse_width"],
        [dataMode, paceMode, lowerRate, atrialAmplitude, atrialPulseWidth])

# VOO_Pace Pacing Functionality
def VOO_Pace(lowerRate, upperRate, ventricularAmplitude, ventricularPulseWidth, label):
    dataMode = 0
    paceMode = 1
    if(int(lowerRate) < 30 or int(lowerRate) > 175 ):
        label['text'] = 'Please input a Lower Rate between 30ppm and 175ppm'
    elif(int(upperRate) < 50 or int(upperRate) > 175):
        label['text'] = 'Please input an Upper Rate between 50ppm and 175ppm'
    elif(float(ventricularAmplitude) < 0.1 or float(ventricularAmplitude) > 5.0):
        label['text'] = 'Please input a Ventricular Amplitude between 0.1V and 5.0V'
    elif(float(ventricularPulseWidth) < 1 or float(ventricularPulseWidth) > 30):
        label['text'] = 'Please input a Ventricular Pulse Width between 1ms and 30ms'
    else:
        print(lowerRate, upperRate, ventricularAmplitude, ventricularPulseWidth)
        label['text'] = 'Successfully sent parameters'
        # update user
        current_user.userUpdate(
            ["lower_rate", "upper_rate", "ventricular_amplitude", "ventricular_pulse_width"], 
            [lowerRate, upperRate, ventricularAmplitude, ventricularPulseWidth])
        # send data to pacemaker
        serial_send(
            ["data_mode", "pace_mode", "lower_rate", "ventricular_amplitude", "ventricular_pulse_width"],
            [dataMode, paceMode, lowerRate, ventricularAmplitude, ventricularPulseWidth])

# AAI Pacing Functionality
def AAI_Pace(lowerRate, upperRate, atrialPulseWidth, atrialAmplitude, ARP, label):
    dataMode = 0
    paceMode = 2
    if(int(lowerRate) < 30 or int(lowerRate) > 175 ):
        label['text'] = 'Please input a Lower Rate between 30ppm and 175ppm'
    elif(int(upperRate) < 50 or int(upperRate) > 175):
        label['text'] = 'Please input an Upper Rate between 50ppm and 175ppm'
    elif(float(atrialAmplitude) < 0.1 or float(atrialAmplitude) > 5.0):
        label['text'] = 'Please input a Atrial Amplitude between 0.1V and 5.0V'
    elif(float(atrialPulseWidth) < 1 or float(atrialPulseWidth) > 30):
        label['text'] = 'Please input an Atrial Pulse Width between 1ms and 30ms'
    elif(int(ARP) < 100 or int(ARP) > 500):
        label['text'] = 'Please input an ARP between 150ms and 500ms'
    else:
        print(lowerRate, upperRate, atrialPulseWidth, atrialAmplitude, ARP)
        label['text'] = 'Successfully sent parameters'
        # update user
        current_user.userUpdate(
            ["lower_rate", "upper_rate", "atrial_amplitude", "atrial_pulse_width", "ARP"], 
            [lowerRate, upperRate, atrialAmplitude, atrialPulseWidth, ARP])
        # send data to pacemaker
        serial_send(
            ["data_mode", "pace_mode", "lower_rate", "atrial_amplitude", "atrial_pulse_width", "ARP"],
            [dataMode, paceMode, lowerRate, atrialAmplitude, atrialPulseWidth, ARP])

# VVI Pacing Functionality
def VVI_Pace(lowerRate, upperRate, ventricularPulseWidth, ventricularAmplitude, VRP, label):
    dataMode = 0
    paceMode = 3
    if(int(lowerRate) < 30 or int(lowerRate) > 175 ):
        label['text'] = 'Please input a Lower Rate between 30ppm and 175ppm'
    elif(int(upperRate) < 50 or int(upperRate) > 175):
        label['text'] = 'Please input an Upper Rate between 50ppm and 175ppm'
    elif(float(ventricularAmplitude) < 0.1 or float(ventricularAmplitude) > 5.0):
        label['text'] = 'Please input a Ventricular Amplitude between 0.1V and 5.0V'
    elif(float(ventricularPulseWidth) < 1 or float(ventricularPulseWidth) > 30):
        label['text'] = 'Please input a Ventricular Pulse Width between 1ms and 30msms'
    elif(int(VRP) < 150 or int(VRP) > 500):
        label['text'] = 'Please input a VPR value between 150ms and 500ms'
    else:
        print(lowerRate, upperRate, ventricularAmplitude, ventricularPulseWidth, VRP)
        label['text'] = 'Successfully sent parameters'
        # update user
        current_user.userUpdate(
            ["lower_rate", "upper_rate", "ventricular_amplitude", "ventricular_pulse_width", "VRP"], 
            [lowerRate, upperRate, ventricularAmplitude, ventricularPulseWidth, VRP])
        # send data to pacemaker
        serial_send(
            ["data_mode", "pace_mode", "lower_rate", "ventricular_amplitude", "ventricular_pulse_width", "VRP"],
            [dataMode, paceMode, lowerRate, ventricularAmplitude, ventricularPulseWidth, VRP])

#DOO Pacing Functionality 
def DOO_Pace(lowerRate, upperRate, atrialAmplitude, ventricularAmplitude, atrialPulseWidth, ventricularPulseWidth, label):
    dataMode = 0
    paceMode = 4
    if(int(lowerRate) < 30 or int(lowerRate) > 175 ):
        label['text'] = 'Please input a Lower Rate between 30ppm and 175ppm'
    elif(int(upperRate) < 50 or int(upperRate) > 175):
        label['text'] = 'Please input an Upper Rate between 50ppm and 175ppm'
    elif(float(atrialAmplitude) < 0.1 or float(atrialAmplitude) > 5.0):
        label['text'] = 'Please input an Atrial Amplitude between 0.5V and'
    elif(float(atrialPulseWidth) < 1 or float(atrialPulseWidth) > 30):
        label['text'] = 'Please input an Atrial Pulse Width between 1ms and 30ms'
    elif(float(ventricularAmplitude) < 0.1 or float(ventricularAmplitude) > 5.0):
        label['text'] = 'Please input a Ventricular Amplitude between 0.1V and 5.0V'
    elif(float(ventricularPulseWidth) < 1 or float(ventricularPulseWidth) > 30):
        label['text'] = 'Please input a Ventricular Pulse Width between 1ms and 30msms'
    else:
        print(lowerRate, upperRate, atrialAmplitude, atrialPulseWidth, ventricularAmplitude, ventricularPulseWidth)
        label['text'] = 'Successfully sent parameters'
        # update user
        current_user.userUpdate(
            ["lower_rate", "upper_rate", "atrial_amplitude", "atrial_pulseWidth", "ventricular_amplitude", "ventricular_pulse_width"], 
            [lowerRate, upperRate, atrialAmplitude, atrialPulseWidth, ventricularAmplitude, ventricularPulseWidth])
        # send data to pacemaker
        serial_send(
            ["data_mode", "pace_mode", "lower_rate", "atrial_amplitude", "atrial_pulseWidth", "ventricular_amplitude", "ventricular_pulse_width"],
            [dataMode, paceMode, lowerRate, atrialAmplitude, atrialPulseWidth, ventricularAmplitude, ventricularPulseWidth])
        
#AOOR Pacing Functionality 
def AOOR_Pace(lowerRate, upperRate, maxSensorRate, atrialAmplitude, atrialPulseWidth, activityThreshold, reactionTime, responseFactor, recoveryTime, label):
    dataMode = 0
    paceMode = 10
    if(int(lowerRate) < 30 or int(lowerRate) > 175 ):
        label['text'] = 'Please input a Lower Rate between 30ppm and 175ppm'
    elif(int(upperRate) < 50 or int(upperRate) > 175):
        label['text'] = 'Please input an Upper Rate between 50ppm and 175ppm'
    elif(int(maxSensorRate) < 50 or int(maxSensorRate) > 175):
            label['text'] = 'Please input an Max Sensor Rate between 50ppm and 175ppm'
    elif(float(atrialAmplitude) < 0.1 or float(atrialAmplitude) > 5.0):
        label['text'] = 'Please input a Atrial Amplitude between 0.1V and 5.0V'
    elif(float(atrialPulseWidth) < 1 or float(atrialPulseWidth) > 30):
        label['text'] = 'Please input an Atrial Pulse Width between 1ms and 30ms'
    elif(int(activityThreshold) < 0 or int(activityThreshold) > 6):
        label['text'] = 'Please input one of the options: 0 = V-Low, 1 = Low, 2 = Med-Low, 3 = Med, 4 = Med-High, 5 = High, 6 = V-High'
    elif(int(reactionTime) < 10000 or int(reactionTime) > 50000):
        label['text'] = 'Please input a Reaction Time between the values of 10000ms and 50000ms'
    elif(int(responseFactor) < 1 or int(responseFactor) > 16):
        label['text'] = 'Please input a Resposne Factor value between 1 and 16'
    elif(int(recoveryTime) < 120000 or int(recoveryTime) > 960000):
        label['text'] = 'Please input a Recover Time value between 120000ms and 960000ms'
    else:
        print(lowerRate, upperRate, maxSensorRate, atrialAmplitude, atrialPulseWidth, activityThreshold, reactionTime, responseFactor, recoveryTime)
        label['text'] = 'Successfully sent parameters'
        # update user
        current_user.userUpdate(
            ["lower_rate", "upper_rate", "atrial_amplitude", "atrial_pulse_width", "activitiy_threshold", "activity_reaction_time", "activity_response_factor", "activity_recovery_time"], 
            [lowerRate, upperRate, maxSensorRate, atrialAmplitude, atrialPulseWidth, activityThreshold, reactionTime, responseFactor, recoveryTime])
        # send data to pacemaker 
        serial_send(["data_mode", "pace_mode", "lower_rate", "atrial_amplitude", "atrial_pulse_width", "activitiy_threshold", "activity_reaction_time", "activity_response_factor", "activity_recovery_time"],
        [dataMode, paceMode, lowerRate, atrialAmplitude, atrialPulseWidth, activityThreshold, reactionTime, responseFactor, recoveryTime])

#VOOR Pacing Functionality 
def VOOR_Pace(lowerRate, upperRate, maxSensorRate, ventricularAmplitude, ventricularPulseWidth, activityThreshold, reactionTime, responseFactor, recoveryTime, label):
    dataMode = 0
    paceMode = 11
    if(int(lowerRate) < 30 or int(lowerRate) > 175 ):
        label['text'] = 'Please input a Lower Rate between 30ppm and 175ppm'
    elif(int(upperRate) < 50 or int(upperRate) > 175):
        label['text'] = 'Please input an Upper Rate between 50ppm and 175ppm'
    elif(int(maxSensorRate) < 50 or int(maxSensorRate) > 175):
        label['text'] = 'Please input a Max Sensor Rate between 50ppm and 175ppm'
    elif(float(ventricularAmplitude) < 0.1 or float(ventricularAmplitude) > 5.0):
        label['text'] = 'Please input a Ventricular Amplitude between 0.1V and 5.0V'
    elif(float(ventricularPulseWidth) < 1 or float(ventricularPulseWidth) > 30):
        label['text'] = 'Please input a Ventricular Pulse Width between 1ms and 30msms'
    elif(int(activityThreshold) < 0 or int(activityThreshold) > 6):
        label['text'] = 'Input one of the options: 0 = V-Low, 1 = Low, 2 = Med-Low, 3 = Med, 4 = Med-High, 5 = High, 6 = V-High'
    elif(int(reactionTime) < 10000 or int(reactionTime) > 50000):
        label['text'] = 'Please input a Reaction Time between the values of 10000ms and 50000ms'
    elif(int(responseFactor) < 1 or int(responseFactor) > 16):
        label['text'] = 'Please input a Resposne Factor value between 1 and 16'
    elif(int(recoveryTime) < 120000 or int(recoveryTime) > 960000):
        label['text'] = 'Please input a Recover Time value between 120000ms and 960000ms'
    else:
        print(lowerRate, upperRate, maxSensorRate, ventricularAmplitude, ventricularPulseWidth, activityThreshold, reactionTime, responseFactor, recoveryTime)
        label['text'] = 'Successfully sent parameters'
        # update user
        current_user.userUpdate(
            ["lower_rate", "upper_rate", "ventricular_amplitude", "ventricular_pulse_width", "activitiy_threshold", "activity_reaction_time", "activity_response_factor", "activity_recovery_time"], 
            [lowerRate, upperRate, maxSensorRate, ventricularAmplitude, ventricularPulseWidth, activityThreshold, reactionTime, responseFactor, recoveryTime])
        # send data to pacemaker 
        serial_send(["data_mode", "pace_mode", "lower_rate", "atrial_amplitude", "atrial_pulse_width", "activitiy_threshold", "activity_reaction_time", "activity_response_factor", "activity_recovery_time"],
        [dataMode, paceMode, lowerRate, ventricularAmplitude, ventricularPulseWidth, activityThreshold, reactionTime, responseFactor, recoveryTime])

#AAIR Pacing Functionality 
def AAIR_Pace(lowerRate, upperRate, maxSensorRate, atrialAmplitude, atrialPulseWidth, atrialSensitivity, ARP, PVARP, hysteresis, rateSmoothing, activityThreshold, reactionTime, responseFactor, recoveryTime, label):
    dataMode = 0
    paceMode = 12
    if(int(lowerRate) < 30 or int(lowerRate) > 175 ):
        label['text'] = 'Please input a Lower Rate between 30ppm and 175ppm'
    elif(int(upperRate) < 50 or int(upperRate) > 175):
        label['text'] = 'Please input an Upper Rate between 50ppm and 175ppm'
    elif(int(maxSensorRate) < 50 or int(maxSensorRate) > 175):
        label['text'] = 'Please input an Max Sensor Rate between 50ppm and 175ppm'
    elif(float(atrialAmplitude) < 0.1 or float(atrialAmplitude) > 5.0):
        label['text'] = 'Please input a Atrial Amplitude between 0.1V and 5.0V'
    elif(float(atrialPulseWidth) < 1 or float(atrialPulseWidth) > 30):
        label['text'] = 'Please input an Atrial Pulse Width between 1ms and 30ms'
        return
    elif(int(ARP) < 100 or int(ARP) > 500):
        label['text'] = 'Please input an ARP between 150ms and 500ms'
        return
    elif(float(atrialSensitivity) not in [0.25, 0.50, 0.75] and (float(atrialSensitivity) < 1.0 or float(atrialSensitivity) > 10.0)):
        label['text'] = 'Please input a Ventricular Sensitivty of 0.25mV, 0.50mV, 0.75mV, or between the values of 1.0mV and 10.0mV'
    elif(float(int(rateSmoothing) > 21 or rateSmoothing) % 3 != 0):
        label['text'] = 'Please input a Rate Smoothing value of 0, 3, 6, 9, 12, 15, 18, or 21'
    elif(int(hysteresis) < 200 or int(hysteresis) > 500):
        label['text'] = 'Please input a Hysteresis value between 200ms and 500ms'
        return
    elif(activityThreshold < 0 or activityThreshold > 6):
        label['text'] = 'Please input an Activity Threshold Between 0 and 6'
    elif(int(reactionTime) < 10000 or int(reactionTime) > 50000):
        label['text'] = 'Please input a Reaction Time between the values of 10000ms and 50000ms'
    elif(int(responseFactor) < 1 or int(responseFactor) > 16):
        label['text'] = 'Please input a Resposne Factor value between 1 and 16'
    elif(int(recoveryTime) < 120000 or int(recoveryTime) > 960000):
        label['text'] = 'Please input a Recover Time value between 120000ms and 960000ms'
    else:
        print(lowerRate, upperRate, maxSensorRate, atrialAmplitude, atrialPulseWidth, ARP, atrialSensitivity, rateSmoothing, hysteresis, activityThreshold, reactionTime, responseFactor, recoveryTime)
        label['text'] = 'Successfully sent parameters'
        # update user
        current_user.userUpdate(
            ["lower_rate", "upper_rate", "atrial_amplitude", "atrial_pulse_width", "ARP", "atrial_sensitivity", "rate_smoothing", "activitiy_threshold", "activity_reaction_time", "activity_response_factor", "activity_recovery_time"], 
            [lowerRate, upperRate, maxSensorRate, atrialAmplitude, atrialPulseWidth, ARP, atrialSensitivity, rateSmoothing, activityThreshold, reactionTime, responseFactor, recoveryTime])
        # send data to pacemaker 
        serial_send(["data_mode", "pace_mode", "lower_rate", "atrial_amplitude", "atrial_pulse_width", "ARP", "atrial_sensitivity", "rate_smoothing", "activitiy_threshold", "activity_reaction_time", "activity_response_factor", "activity_recovery_time"],
        [dataMode, paceMode, lowerRate, atrialAmplitude, atrialPulseWidth, ARP, atrialSensitivity, rateSmoothing, activityThreshold, reactionTime, responseFactor, recoveryTime])

#VVIR Pacing Functionality 
def VVIR_Pace(lowerRate, upperRate, maxSensorRate, ventricularAmplitude, ventricularPulseWidth, ventricularSensitivity, VRP, RVVRP, hysteresis, rateSmoothing, activityThreshold, reactionTime, responseFactor, recoveryTime, label):
    dataMode = 0
    paceMode = 13
    if(int(lowerRate) < 30 or int(lowerRate) > 175 ):
        label['text'] = 'Please input a Lower Rate between 30ppm and 175ppm'
        return
    elif(int(upperRate) < 50 or int(upperRate) > 175):
        label['text'] = 'Please input an Upper Rate between 50ppm and 175ppm'
    elif(int(maxSensorRate) < 50 or int(maxSensorRate) > 175):
        label['text'] = 'Please input an Max Sensor Rate between 50ppm and 175ppm'
    elif(float(ventricularAmplitude) < 0.1 or float(ventricularAmplitude) > 5.0):
        label['text'] = 'Please input a Ventricular Amplitude between 0.1V and 5.0V'
    elif(float(ventricularPulseWidth) < 1 or float(ventricularPulseWidth) > 30):
        label['text'] = 'Please input a Ventricular Pulse Width between 1ms and 30msms'
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
    elif(activityThreshold < 0 or activityThreshold > 6):
        label['text'] = 'Please input an Activity Threshold Between 0 and 6'
    elif(int(reactionTime) < 10000 or int(reactionTime) > 50000):
        label['text'] = 'Please input a Reaction Time between the values of 10000ms and 50000ms'
    elif(int(responseFactor) < 1 or int(responseFactor) > 16):
        label['text'] = 'Please input a Resposne Factor value between 1 and 16'
    elif(int(recoveryTime) < 120000 or int(recoveryTime) > 960000):
        label['text'] = 'Please input a Recover Time value between 120000ms and 960000ms'
    else:
        print(lowerRate, upperRate, maxSensorRate, ventricularAmplitude, ventricularPulseWidth, VRP, ventricularSensitivity, rateSmoothing, hysteresis, activityThreshold, reactionTime, responseFactor, recoveryTime)
        label['text'] = 'Successfully sent parameters'
        # update user
        current_user.userUpdate(
            ["lower_rate", "upper_rate", "ventricular_amplitude", "ventricular_pulse_width", "VRP", "ventricular_sensitivity", "rate_smoothing", "activitiy_threshold", "activity_reaction_time", "activity_response_factor", "activity_recovery_time"], 
            [lowerRate, upperRate, maxSensorRate, ventricularAmplitude, ventricularPulseWidth, VRP, ventricularSensitivity, rateSmoothing, activityThreshold, reactionTime, responseFactor, recoveryTime])
        # send data to pacemaker 
        serial_send(["data_mode", "pace_mode", "lower_rate", "ventricular_amplitude", "ventricular_pulse_width", "VRP", "ventricular_sensitivity", "rate_smoothing", "activitiy_threshold", "activity_reaction_time", "activity_response_factor", "activity_recovery_time"],
        [dataMode, paceMode, lowerRate, ventricularAmplitude, ventricularPulseWidth, VRP, ventricularSensitivity, rateSmoothing, activityThreshold, reactionTime, responseFactor, recoveryTime])

#DOOR Pacing Functionality 
def DOOR_Pace(lowerRate, upperRate, maxSensorRate, fixedAVDelay, atrialAmplitude, ventricularAmplitude, atrialPulseWidth, ventricularPulseWidth, activityThreshold, reactionTime, responseFactor, recoveryTime, label):
    dataMode = 0
    paceMode = 14
    if(int(lowerRate) < 30 or int(lowerRate) > 175 ):
        label['text'] = 'Please input a Lower Rate between 30ppm and 175ppm'
    elif(int(upperRate) < 50 or int(upperRate) > 175):
        label['text'] = 'Please input an Upper Rate between 50ppm and 175ppm'
    elif(int(fixedAVDelay) < 70 or int(fixedAVDelay) > 300):
        label['text'] = 'Please input a Fixed AV Delay between 70ms and 300ms'
    elif(int(maxSensorRate) < 50 or int(maxSensorRate) > 175):
        label['text'] = 'Please input an Max Sensor Rate between 50ppm and 175ppm'
    elif(float(atrialAmplitude) < 0.1 or float(atrialAmplitude) > 5.0):
        label['text'] = 'Please input a Atrial Amplitude between 0.1V and 5.0V'
    elif(float(atrialPulseWidth) < 1 or float(atrialPulseWidth) > 30):
        label['text'] = 'Please input an Atrial Pulse Width between 1ms and 30ms'
    elif(float(ventricularAmplitude) < 0.1 or float(ventricularAmplitude) > 5.0):
        label['text'] = 'Please input a Ventricular Amplitude between 0.1V and 5.0V'
    elif(float(ventricularPulseWidth) < 1 or float(ventricularPulseWidth) > 30):
        label['text'] = 'Input a Ventricular Pulse Width between 1ms and 30ms'
    elif(int(activityThreshold) < 0 or int(activityThreshold) > 6):
        label['text'] = 'Input one of the options: 0 = V-Low, 1 = Low, 2 = Med-Low, 3 = Med, 4 = Med-High, 5 = High, 6 = V-High'
    elif(int(reactionTime) < 10000 or int(reactionTime) > 50000):
        label['text'] = 'Please input a Reaction Time between the values of 10000ms and 50000ms'
    elif(int(responseFactor) < 1 or int(responseFactor) > 16):
        label['text'] = 'Please input a Resposne Factor value between 1 and 16'
    elif(int(recoveryTime) < 120000 or int(recoveryTime) > 960000):
        label['text'] = 'Please input a Recover Time value between 120000ms and 960000ms'
    else:
        print(lowerRate, upperRate, maxSensorRate, fixedAVDelay, atrialAmplitude, atrialPulseWidth, ventricularAmplitude, ventricularPulseWidth, activityThreshold, reactionTime, responseFactor, recoveryTime)
        label['text'] = 'Successfully sent parameters'
        # update user
        current_user.userUpdate(
            ["lower_rate", "upper_rate", "max_sensor_rate", "av_delay", "atrial_amplitude", "atrial_pulse_width", "ventricular_amplitude", "ventricular_pulse_width", "activitiy_threshold", "activity_reaction_time", "activity_response_factor", "activity_recovery_time"], 
            [lowerRate, upperRate, maxSensorRate, fixedAVDelay, atrialAmplitude, atrialPulseWidth, ventricularAmplitude, ventricularPulseWidth, activityThreshold, reactionTime, responseFactor, recoveryTime])
        # send data to pacemaker 
        serial_send(["data_mode", "pace_mode", "lower_rate", "max_sensor_rate", "av_delay", "atrial_amplitude", "atrial_pulse_width", "ventricular_amplitude", "ventricular_pulse_width", "activitiy_threshold", "activity_reaction_time", "activity_response_factor", "activity_recovery_time"],
        [dataMode, paceMode, lowerRate, maxSensorRate, fixedAVDelay, atrialAmplitude, atrialPulseWidth, ventricularAmplitude, ventricularPulseWidth, activityThreshold, reactionTime, responseFactor, recoveryTime])

# def EGRAM_Plot(button):
#     if(button1):
#         serial_read_atr()
#     elif(button2):
#         serial_read_vent()
#     elif(button3):
#         serial_read_atr_vent()

########## Front End ##########

# AOO_window
def AOO_window():

    AOO_window = tk.Toplevel(root, height = HEIGHT, width = WIDTH)
    AOO_window.configure(background = '#bce6eb')

    lower_rate_limit = tk.Entry(AOO_window, text = "Lower Rate Limit ")
    lower_rate_limit.place(relx = 0.50, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    lower_rate_label = tk.Label(AOO_window, text = 'Lower Rate Limit (30ppm - 175ppm)', bg = '#bce6eb')
    lower_rate_label.place(relx = 0.50, rely = 0.09, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    upper_rate_limit = tk.Entry(AOO_window, text = "Upper Rate Limit")
    upper_rate_limit.place(relx = 0.50, rely = 0.20, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    upper_rate_label = tk.Label(AOO_window, text = 'Upper Rate Limit (50ppm - 175ppm)', bg = '#bce6eb')
    upper_rate_label.place(relx = 0.50, rely = 0.24, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    atrial_amplitude = tk.Entry(AOO_window, text = "Atrial Amplitude")
    atrial_amplitude.place(relx = 0.50, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    atrial_amplitude_label = tk.Label(AOO_window, text = 'Atrial Amplitude (500mV - 5000mV)', bg = '#bce6eb')
    atrial_amplitude_label.place(relx = 0.50, rely = 0.39, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    atrial_pulse_width = tk.Entry(AOO_window, text = "Atrial Pulse Width")
    atrial_pulse_width.place(relx = 0.50, rely = 0.50, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    atrial_pulse_label = tk.Label(AOO_window, text = 'Atrial Pulse Width (1ms - 30ms)', bg = '#bce6eb')
    atrial_pulse_label.place(relx = 0.50, rely = 0.54, relwidth = 0.30, relheight = 0.040, anchor = 'n')


    error_label = tk.Label(AOO_window, text = '', bg = '#bce6eb')
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
    VOO_window.configure(background = '#bce6eb')

    lower_rate_limit = tk.Entry(VOO_window)
    lower_rate_limit.place(relx = 0.50, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    lower_rate_label = tk.Label(VOO_window, text = 'Lower Rate Limit (30ppm - 175ppm)', bg = '#bce6eb')
    lower_rate_label.place(relx = 0.50, rely = 0.09, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    upper_rate_limit = tk.Entry(VOO_window)
    upper_rate_limit.place(relx = 0.50, rely = 0.20, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    upper_rate_label = tk.Label(VOO_window, text = 'Upper Rate Limit (50ppm - 175ppm)', bg = '#bce6eb')
    upper_rate_label.place(relx = 0.50, rely = 0.24, relwidth = 0.30, relheight = 0.040, anchor = 'n')
    
    ventricular_amplitude = tk.Entry(VOO_window)
    ventricular_amplitude.place(relx = 0.50, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    ventricular_amplitude_label = tk.Label(VOO_window, text = 'Ventricular Amplitude (500mv - 5000mv)', bg = '#bce6eb')
    ventricular_amplitude_label.place(relx = 0.50, rely = 0.39, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    ventricular_pulse_width = tk.Entry(VOO_window)
    ventricular_pulse_width.place(relx = 0.50, rely = 0.50, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    ventricular_pulse_width_label = tk.Label(VOO_window, text = 'Ventricular Pulse Width (1ms - 30ms)', bg = '#bce6eb')
    ventricular_pulse_width_label.place(relx = 0.50, rely = 0.54, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    error_label = tk.Label(VOO_window, text = '', bg = '#bce6eb')
    error_label.place(relx = 0.5, rely = 0.75, relwidth = 0.5, relheight = 0.05, anchor = 'n')

    if not lower_rate_limit.get() or not upper_rate_limit.get() or not ventricular_pulse_width.get() or not ventricular_amplitude.get():
        error_label['text'] = 'Please ensure every input is filled in' 

    send_parameters_button = tk.Button(
        VOO_window, 
        text = "Send Parameters", font = 96, 
        command = lambda: VOO_Pace(int(lower_rate_limit.get()), int(upper_rate_limit.get()), float(ventricular_amplitude.get()), float(ventricular_pulse_width.get()), error_label))
    send_parameters_button.place(relx = 0.5, rely = 0.80, relwidth = 0.40, relheight = 0.10, anchor = 'n')
    
# AAI_Window
def AAI_window():

    AAI_window = tk.Toplevel(root, height = HEIGHT, width = WIDTH)
    AAI_window.configure(background = '#bce6eb')

    lower_rate_limit = tk.Entry(AAI_window)
    lower_rate_limit.place(relx = 0.50, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    lower_rate_label = tk.Label(AAI_window, text = 'Lower Rate Limit (30ppm - 175ppm)', bg = '#bce6eb')
    lower_rate_label.place(relx = 0.50, rely = 0.09, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    upper_rate_limit = tk.Entry(AAI_window)
    upper_rate_limit.place(relx = 0.50, rely = 0.20, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    upper_rate_label = tk.Label(AAI_window, text = 'Upper Rate Limit (50ppm - 175ppm)', bg = '#bce6eb')
    upper_rate_label.place(relx = 0.50, rely = 0.24, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    atrial_amplitude = tk.Entry(AAI_window)
    atrial_amplitude.place(relx = 0.50, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    atrial_amplitude_label = tk.Label(AAI_window, text = 'Atrial Amplitude (500mV - 5000mV)', bg = '#bce6eb')
    atrial_amplitude_label.place(relx = 0.50, rely = 0.39, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    atrial_pulse_width = tk.Entry(AAI_window)
    atrial_pulse_width.place(relx = 0.50, rely = 0.50, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    atrial_pulse_width_label = tk.Label(AAI_window, text = 'Atrial Pulse Width (1ms - 30ms)', bg = '#bce6eb')
    atrial_pulse_width_label.place(relx = 0.50, rely = 0.54, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    ARP = tk.Entry(AAI_window, text = "ARP")
    ARP.place(relx = 0.50, rely = 0.65, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    ARP_label = tk.Label(AAI_window, text = 'ARP (150ms-500ms) (150ms - 500ms)', bg = '#bce6eb')
    ARP_label.place(relx = 0.50, rely = 0.69, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    error_label = tk.Label(AAI_window, text = '', bg = '#bce6eb')
    error_label.place(relx = 0.5, rely = 0.75, relwidth = 0.5, relheight = 0.05, anchor = 'n')

    if not lower_rate_limit.get() or upper_rate_limit.get() or not atrial_pulse_width.get() or not atrial_amplitude.get() or not ARP.get():
        error_label['text'] = 'Please ensure every input is filled in' 

    send_parameters_button = tk.Button(
        AAI_window, text = "Send Parameters", 
        font = 96, 
        command = lambda: AAI_Pace(int(lower_rate_limit.get()), int(upper_rate_limit.get()), float(atrial_pulse_width.get()), float(atrial_amplitude.get()), int(ARP.get()), error_label))
    send_parameters_button.place(relx = 0.5, rely = 0.80, relwidth = 0.40, relheight = 0.10, anchor = 'n')

#VVI_window
def VVI_window():

    VVI_window = tk.Toplevel(root, height = HEIGHT, width = WIDTH)
    VVI_window.configure(background = '#bce6eb')

    lower_rate_limit = tk.Entry(VVI_window)
    lower_rate_limit.place(relx = 0.50, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    lower_rate_label = tk.Label(VVI_window, text = 'Lower Rate Limit (30ppm - 175ppm)', bg = '#bce6eb')
    lower_rate_label.place(relx = 0.50, rely = 0.09, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    upper_rate_limit = tk.Entry(VVI_window)
    upper_rate_limit.place(relx = 0.50, rely = 0.20, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    upper_rate_label = tk.Label(VVI_window, text = 'Upper Rate Limit (50ppm - 175ppm)', bg = '#bce6eb')
    upper_rate_label.place(relx = 0.50, rely = 0.24, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    ventricular_amplitude = tk.Entry(VVI_window)
    ventricular_amplitude.place(relx = 0.50, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    ventricular_amplitude_label = tk.Label(VVI_window, text = 'Ventricular Amplitude (500mV - 5000mV)', bg = '#bce6eb')
    ventricular_amplitude_label.place(relx = 0.50, rely = 0.39, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    ventricular_pulse_width = tk.Entry(VVI_window)
    ventricular_pulse_width.place(relx = 0.50, rely = 0.50, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    ventricular_pulse_width_label = tk.Label(VVI_window, text = 'Ventricular Pulse Width (1ms - 30ms)', bg = '#bce6eb')
    ventricular_pulse_width_label.place(relx = 0.50, rely = 0.54, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    VRP = tk.Entry(VVI_window, text = "VRP")
    VRP.place(relx = 0.50, rely = 0.65, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    VRP_label = tk.Label(VVI_window, text = 'VRP (150ms - 500ms)', bg = '#bce6eb')
    VRP_label.place(relx = 0.50, rely = 0.69, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    error_label = tk.Label(VVI_window, text = '', bg = '#bce6eb')
    error_label.place(relx = 0.5, rely = 0.75, relwidth = 0.5, relheight = 0.05, anchor = 'n')

    if not lower_rate_limit.get() or not upper_rate_limit.get() or not ventricular_pulse_width.get() or not ventricular_amplitude.get() or not VRP.get():
        error_label['text'] = 'Please ensure every input is filled in' 

    send_parameters_button = tk.Button(
        VVI_window, text = "Send Parameters", 
        font = 96, 
        command = lambda: VVI_Pace(int(lower_rate_limit.get()), int(upper_rate_limit.get()), float(ventricular_pulse_width.get()), float(ventricular_amplitude.get()), int(VRP.get()), error_label))
    send_parameters_button.place(relx = 0.5, rely = 0.80, relwidth = 0.40, relheight = 0.10, anchor = 'n')

##DOO_window
def DOO_window():

    DOO_window = tk.Toplevel(root, height = HEIGHT, width = WIDTH)
    DOO_window.configure(background = '#bce6eb')

    lower_rate_limit = tk.Entry(DOO_window, text = "Lower Rate Limit")
    lower_rate_limit.place(relx = 0.50, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    lower_rate_label = tk.Label(DOO_window, text = 'Lower Rate Limit (30ppm - 175ppm)', bg = '#bce6eb')
    lower_rate_label.place(relx = 0.50, rely = 0.09, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    upper_rate_limit = tk.Entry(DOO_window, text = "Upper Rate Limit")
    upper_rate_limit.place(relx = 0.50, rely = 0.15, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    upper_rate_label = tk.Label(DOO_window, text = 'Upper Rate Limit (50ppm - 175ppm)', bg = '#bce6eb')
    upper_rate_label.place(relx = 0.50, rely = 0.19, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    atrial_pulse_width = tk.Entry(DOO_window, text = "Atrial Pulse Width")
    atrial_pulse_width.place(relx = 0.50, rely = 0.25, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    atrial_pulse_label = tk.Label(DOO_window, text = 'Atrial Pulse Width (1ms - 30ms)', bg = '#bce6eb')
    atrial_pulse_label.place(relx = 0.50, rely = 0.29, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    atrial_amplitude = tk.Entry(DOO_window, text = "Atrial Amplitude")
    atrial_amplitude.place(relx = 0.50, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    atrial_amplitude_label = tk.Label(DOO_window, text = 'Atrial Amplitude (0.1V - 5V)', bg = '#bce6eb')
    atrial_amplitude_label.place(relx = 0.50, rely = 0.39, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    ventricular_amplitude = tk.Entry(DOO_window)
    ventricular_amplitude.place(relx = 0.50, rely = 0.45, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    ventricular_amplitude_label = tk.Label(DOO_window, text = 'Ventricular Amplitude (0.1V - 5V)', bg = '#bce6eb')
    ventricular_amplitude_label.place(relx = 0.50, rely = 0.49, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    ventricular_pulse_width = tk.Entry(DOO_window)
    ventricular_pulse_width.place(relx = 0.50, rely = 0.55, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    ventricular_pulse_width_label = tk.Label(DOO_window, text = 'Ventricular Pulse Width (1ms - 30ms)', bg = '#bce6eb')
    ventricular_pulse_width_label.place(relx = 0.50, rely = 0.59, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    error_label = tk.Label(DOO_window, text = '', bg = '#bce6eb')
    error_label.place(relx = 0.5, rely = 0.75, relwidth = 0.5, relheight = 0.05, anchor = 'n')

    if not lower_rate_limit.get() or not upper_rate_limit.get() or not atrial_pulse_width.get() or not atrial_amplitude.get() or not ventricular_pulse_width.get() or not ventricular_amplitude.get():
        error_label['text'] = 'Please ensure every input is filled in' 

    pace_now_button = tk.Button(DOO_window, text = "Pace Now", font = 96, command = lambda: DOO_Pace(int(lower_rate_limit.get()), int(upper_rate_limit.get()), float(atrial_pulse_width.get()), float(ventricular_amplitude.get()), float(atrial_amplitude.get()), float(ventricular_pulse_width.get()), error_label))
    pace_now_button.place(relx = 0.5, rely = 0.80, relwidth = 0.40, relheight = 0.10, anchor = 'n')

#AOOR_window
def AOOR_window():
    AOOR_window = tk.Toplevel(root, height = HEIGHT, width = WIDTH)
    AOOR_window.configure(background = '#bce6eb')

    '''Left Side'''

    lower_rate_limit = tk.Entry(AOOR_window, text = "Lower Rate Limit ")
    lower_rate_limit.place(relx = 0.2, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    lower_rate_label = tk.Label(AOOR_window, text = 'Lower Rate Limit (30ppm - 175ppm)', bg = '#bce6eb')
    lower_rate_label.place(relx = 0.2, rely = 0.09, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    upper_rate_limit = tk.Entry(AOOR_window, text = "Upper Rate Limit")
    upper_rate_limit.place(relx = 0.2, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    upper_rate_label = tk.Label(AOOR_window, text = 'Upper Rate Limit (50ppm - 175ppm)', bg = '#bce6eb')
    upper_rate_label.place(relx = 0.2, rely = 0.39, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    atrial_pulse_width = tk.Entry(AOOR_window, text = "Atrial Pulse Width")
    atrial_pulse_width.place(relx = 0.20, rely = 0.65, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    atrial_pulse_width_label = tk.Label(AOOR_window, text = 'Atrial Pulse Width (1ms - 30ms)', bg = '#bce6eb')
    atrial_pulse_width_label.place(relx = 0.20, rely = 0.69, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    '''Middle'''

    atrial_amplitude = tk.Entry(AOOR_window)
    atrial_amplitude.place(relx = 0.50, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    atrial_amplitude_label = tk.Label(AOOR_window, text = 'Atrial Amplitude (0.1V - 5V)', bg = '#bce6eb')
    atrial_amplitude_label.place(relx = 0.50, rely = 0.09, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    activity_threshold = tk.Entry(AOOR_window)
    activity_threshold.place(relx = 0.5, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    activity_threshold_label = tk.Label(AOOR_window, text = 'Activity Threshold (1-6)', bg = '#bce6eb')
    activity_threshold_label.place(relx = 0.5, rely = 0.39, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    reaction_time = tk.Entry(AOOR_window)
    reaction_time.place(relx = 0.50, rely = 0.65, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    reaction_time_label = tk.Label(AOOR_window, text = 'Reaction Time (10000ms - 50000ms)', bg = '#bce6eb')
    reaction_time_label.place(relx = 0.50, rely = 0.69, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    '''Right Side'''

    response_factor = tk.Entry(AOOR_window)
    response_factor.place(relx = 0.80, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    response_factor_label = tk.Label(AOOR_window, text = 'Response Factor (1-16)', bg = '#bce6eb')
    response_factor_label.place(relx = 0.80, rely = 0.09, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    recovery_time = tk.Entry(AOOR_window)
    recovery_time.place(relx = 0.80, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    recovery_time_label = tk.Label(AOOR_window, text = 'Recovery Time (120000ms - 960000ms)', bg = '#bce6eb')
    recovery_time_label.place(relx = 0.80, rely = 0.39, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    maxSensorRate = tk.Entry(AOOR_window, text = "Max Sensor Rate")
    maxSensorRate.place(relx = 0.80, rely = 0.65, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    maxSensorRate_label = tk.Label(AOOR_window, text = 'Max Sensor Rate (50-175)', bg = '#bce6eb')
    maxSensorRate_label.place(relx = 0.80, rely = 0.69, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    error_label = tk.Label(AOOR_window, text = '', bg = '#bce6eb')
    error_label.place(relx = 0.5, rely = 0.85, relwidth = 0.5, relheight = 0.05, anchor = 'n')

    if not lower_rate_limit.get() or not upper_rate_limit.get() or not maxSensorRate.get() or not atrial_amplitude.get() or not atrial_pulse_width.get() or not activity_threshold.get() or not reaction_time.get() or not response_factor.get() or not recovery_time.get():
        error_label['text'] = 'Please ensure every input is filled in' 

    pace_now_button = tk.Button(
        AOOR_window, text = "Pace Now", 
        font = 96, 
        command = lambda: AOOR_Pace(int(lower_rate_limit.get()), int(upper_rate_limit.get()), int(maxSensorRate.get()), float(atrial_amplitude.get()), float(atrial_pulse_width.get()), int(activity_threshold.get()), int(reaction_time.get()), int(response_factor.get()), int(recovery_time.get()), error_label))
    pace_now_button.place(relx = 0.5, rely = 0.80, relwidth = 0.40, relheight = 0.10, anchor = 'n')

#VOOR_window
def VOOR_window():

    VOOR_window = tk.Toplevel(root, height = HEIGHT, width = WIDTH)
    VOOR_window.configure(background = '#bce6eb')

    '''Left Side'''

    lower_rate_limit = tk.Entry(VOOR_window, text = "Lower Rate Limit ")
    lower_rate_limit.place(relx = 0.2, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    lower_rate_label = tk.Label(VOOR_window, text = 'Lower Rate Limit (30ppm - 175ppm)', bg = '#bce6eb')
    lower_rate_label.place(relx = 0.2, rely = 0.09, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    upper_rate_limit = tk.Entry(VOOR_window, text = "Upper Rate Limit")
    upper_rate_limit.place(relx = 0.2, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    upper_rate_label = tk.Label(VOOR_window, text = 'Upper Rate Limit (50ppm - 175ppm)', bg = '#bce6eb')
    upper_rate_label.place(relx = 0.2, rely = 0.39, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    ventricular_pulse_width = tk.Entry(VOOR_window, text = "Ventricular Pulse Width")
    ventricular_pulse_width.place(relx = 0.20, rely = 0.65, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    ventricular_pulse_width_label = tk.Label(VOOR_window, text = 'Ventricular Pulse Width (1ms - 30ms)', bg = '#bce6eb')
    ventricular_pulse_width_label.place(relx = 0.20, rely = 0.69, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    '''Middle'''

    ventricular_amplitude = tk.Entry(VOOR_window)
    ventricular_amplitude.place(relx = 0.50, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    ventricular_amplitude_label = tk.Label(VOOR_window, text = 'Ventricular Amplitude (0.1V - 5V)', bg = '#bce6eb')
    ventricular_amplitude_label.place(relx = 0.50, rely = 0.09, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    activity_threshold = tk.Entry(VOOR_window)
    activity_threshold.place(relx = 0.5, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    activity_threshold_label = tk.Label(VOOR_window, text = 'Activity Threshold (1-6)', bg = '#bce6eb')
    activity_threshold_label.place(relx = 0.5, rely = 0.39, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    reaction_time = tk.Entry(VOOR_window)
    reaction_time.place(relx = 0.50, rely = 0.65, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    reaction_time_label = tk.Label(VOOR_window, text = 'Reaction Time (10000ms - 50000ms)', bg = '#bce6eb')
    reaction_time_label.place(relx = 0.50, rely = 0.69, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    '''Right Side'''

    response_factor = tk.Entry(VOOR_window)
    response_factor.place(relx = 0.80, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    response_factor_label = tk.Label(VOOR_window, text = 'Response Factor (1-16)', bg = '#bce6eb')
    response_factor_label.place(relx = 0.80, rely = 0.09, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    recovery_time = tk.Entry(VOOR_window)
    recovery_time.place(relx = 0.80, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    recovery_time_label = tk.Label(VOOR_window, text = 'Recovery Time (120000ms - 960000ms)', bg = '#bce6eb')
    recovery_time_label.place(relx = 0.80, rely = 0.39, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    maxSensorRate = tk.Entry(VOOR_window, text = "Max Sensor Rate")
    maxSensorRate.place(relx = 0.80, rely = 0.65, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    maxSensorRate_label = tk.Label(VOOR_window, text = 'Max Sensor Rate (50-175)', bg = '#bce6eb')
    maxSensorRate_label.place(relx = 0.80, rely = 0.69, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    error_label = tk.Label(VOOR_window, text = '', bg = '#bce6eb')
    error_label.place(relx = 0.5, rely = 0.85, relwidth = 0.5, relheight = 0.05, anchor = 'n')

    if not lower_rate_limit.get() or not upper_rate_limit.get() or not maxSensorRate.get() or not ventricular_amplitude.get() or not ventricular_pulse_width.get() or not activity_threshold.get() or not reaction_time.get() or not response_factor.get() or not recovery_time.get():
        error_label['text'] = 'Please ensure every input is filled in' 

    pace_now_button = tk.Button(VOOR_window, text = "Pace Now", font = 96, command = lambda: VOOR_Pace(int(lower_rate_limit.get()), int(upper_rate_limit.get()), int(maxSensorRate.get()), float(ventricular_amplitude.get()), float(ventricular_pulse_width.get()), int(activity_threshold.get()), int(reaction_time.get()), int(response_factor.get()), int(recovery_time.get()), error_label))
    pace_now_button.place(relx = 0.5, rely = 0.90, relwidth = 0.40, relheight = 0.10, anchor = 'n')

#AAIR_window
def AAIR_window():
    AAIR_window = tk.Toplevel(root, height = HEIGHT, width = WIDTH)
    AAIR_window.configure(background = '#bce6eb')

    '''LeftSide'''

    lower_rate_limit = tk.Entry(AAIR_window)
    lower_rate_limit.place(relx = 0.20, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    lower_rate_label = tk.Label(AAIR_window, text = 'Lower Rate Limit (30ppm-175ppm)', bg = '#bce6eb')
    lower_rate_label.place(relx = 0.20, rely = 0.09, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    upper_rate_limit = tk.Entry(AAIR_window)
    upper_rate_limit.place(relx = 0.20, rely = 0.20, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    upper_rate_label = tk.Label(AAIR_window, text = 'Upper Rate Limit (50ppm - 175ppm)', bg = '#bce6eb')
    upper_rate_label.place(relx = 0.20, rely = 0.24, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    maxSensorRate = tk.Entry(AAIR_window, text = "Max Sensor Rate")
    maxSensorRate.place(relx = 0.20, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    maxSensorRate_label = tk.Label(AAIR_window, text = 'Max Sensor Rate (50-175)', bg = '#bce6eb')
    maxSensorRate_label.place(relx = 0.20, rely = 0.39, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    atrial_amplitude = tk.Entry(AAIR_window)
    atrial_amplitude.place(relx = 0.20, rely = 0.50, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    atrial_amplitude_label = tk.Label(AAIR_window, text = 'Atrial Amplitude (0.1V - 5V)', bg = '#bce6eb')
    atrial_amplitude_label.place(relx = 0.20, rely = 0.54, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    '''MIDDLE'''

    atrial_sensitivity = tk.Entry(AAIR_window)
    atrial_sensitivity.place(relx = 0.50, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    atrial_sensitivity_label = tk.Label(AAIR_window, text = 'Atrial Sensitivity', bg = '#bce6eb')
    atrial_sensitivity_label.place(relx = 0.50, rely = 0.09, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    atrial_pulse_width = tk.Entry(AAIR_window)
    atrial_pulse_width.place(relx = 0.50, rely = 0.20, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    atrial_pulse_width_label = tk.Label(AAIR_window, text = 'Atrial Pulse Width (1ms - 30ms)', bg = '#bce6eb')
    atrial_pulse_width_label.place(relx = 0.50, rely = 0.24, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    ARP = tk.Entry(AAIR_window, text = "ARP")
    ARP.place(relx = 0.50, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    ARP_label = tk.Label(AAIR_window, text = 'ARP (150ms-500ms)', bg = '#bce6eb')
    ARP_label.place(relx = 0.50, rely = 0.39, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    PVARP = tk.Entry(AAIR_window, text = "PVARP")
    PVARP.place(relx = 0.50, rely = 0.50, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    PVARP_label = tk.Label(AAIR_window, text = 'PVARP (150ms-500ms)', bg = '#bce6eb')
    PVARP_label.place(relx = 0.50, rely = 0.54, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    '''Right'''

    hysteresis = tk.Entry(AAIR_window, text = "Hysteresis")
    hysteresis.place(relx = 0.80, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    hysteresis_label = tk.Label(AAIR_window, text = 'Hysteresis (200ms-500ms)', bg = '#bce6eb')
    hysteresis_label.place(relx = 0.80, rely = 0.09, relwidth = 0.30, relheight = 0.040, anchor = 'n')


    activity_threshold = tk.Entry(AAIR_window)
    activity_threshold.place(relx = 0.80, rely = 0.20, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    activity_threshold_label = tk.Label(AAIR_window, text = 'Activity Threshold (1-6)', bg = '#bce6eb')
    activity_threshold_label.place(relx = 0.80, rely = 0.24, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    reaction_time = tk.Entry(AAIR_window)
    reaction_time.place(relx = 0.80, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    reaction_time_label = tk.Label(AAIR_window, text = 'Reaction Time (10000ms - 50000ms)', bg = '#bce6eb')
    reaction_time_label.place(relx = 0.80, rely = 0.39, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    response_factor = tk.Entry(AAIR_window)
    response_factor.place(relx = 0.80, rely = 0.50, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    response_factor_label = tk.Label(AAIR_window, text = 'Response Factor (1-16)', bg = '#bce6eb')
    response_factor_label.place(relx = 0.80, rely = 0.54, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    '''Bottom'''

    recovery_time = tk.Entry(AAIR_window)
    recovery_time.place(relx = 0.65, rely = 0.65, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    recovery_time_label = tk.Label(AAIR_window, text = 'Recovery Time (120000ms - 960000ms)', bg = '#bce6eb')
    recovery_time_label.place(relx = 0.65, rely = 0.69, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    rate_smoothing = tk.Entry(AAIR_window)
    rate_smoothing.place(relx = 0.35, rely = 0.65, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    rate_smoothing_label = tk.Label(AAIR_window, text = 'Rate Smoothing (3,6,9,12,15,18,21)', bg = '#bce6eb')
    rate_smoothing_label.place(relx = 0.35, rely = 0.69, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    error_label = tk.Label(AAIR_window, text = '', bg = '#bce6eb')
    error_label.place(relx = 0.5, rely = 0.75, relwidth = 0.5, relheight = 0.05, anchor = 'n')

    if not lower_rate_limit.get() or not upper_rate_limit.get() or not maxSensorRate.get() or not atrial_amplitude.get() or not atrial_pulse_width.get() or not atrial_sensitivity.get() or not ARP.get() or not PVARP.get() or not hysteresis or not activity_threshold.get() or not reaction_time.get() or not response_factor.get() or not recovery_time.get() or not rate_smoothing.get():
        error_label['text'] = 'Please ensure every input is filled in' 

    pace_now_button = tk.Button(AAIR_window, text = "Pace Now", font = 96, command = lambda: AAIR_Pace(int(lower_rate_limit.get()), int(upper_rate_limit.get()), int(maxSensorRate.get()), float(atrial_amplitude.get()), float(atrial_pulse_width.get()), float(atrial_sensitivity.get()), int(ARP.get()), int(PVARP.get()), int(hysteresis.get()), float(rate_smoothing.get()), int(activity_threshold.get()), int(reaction_time.get()), int(response_factor.get()), int(recovery_time.get()), error_label))
    pace_now_button.place(relx = 0.5, rely = 0.80, relwidth = 0.40, relheight = 0.10, anchor = 'n')

#VVIR_window
def VVIR_window():
    VVIR_window = tk.Toplevel(root, height = HEIGHT, width = WIDTH)
    VVIR_window.configure(background = '#bce6eb')

    '''LeftSide'''

    lower_rate_limit = tk.Entry(VVIR_window)
    lower_rate_limit.place(relx = 0.20, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    lower_rate_label = tk.Label(VVIR_window, text = 'Lower Rate Limit (30ppm - 175ppm)', bg = '#bce6eb')
    lower_rate_label.place(relx = 0.20, rely = 0.09, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    upper_rate_limit = tk.Entry(VVIR_window)
    upper_rate_limit.place(relx = 0.20, rely = 0.15, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    upper_rate_label = tk.Label(VVIR_window, text = 'Upper Rate Limit (50ppm - 175ppm)', bg = '#bce6eb')
    upper_rate_label.place(relx = 0.20, rely = 0.19, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    maxSensorRate = tk.Entry(VVIR_window, text = "Max Sensor Rate")
    maxSensorRate.place(relx = 0.20, rely = 0.25, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    maxSensorRate_label = tk.Label(VVIR_window, text = 'Max Sensor Rate (50-175)', bg = '#bce6eb')
    maxSensorRate_label.place(relx = 0.20, rely = 0.29, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    ventricular_amplitude = tk.Entry(VVIR_window)
    ventricular_amplitude.place(relx = 0.20, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    ventricular_amplitude_label = tk.Label(VVIR_window, text = 'Ventricular Amplitude (0.1V - 5V)', bg = '#bce6eb')
    ventricular_amplitude_label.place(relx = 0.20, rely = 0.39, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    ventricular_sensitivity = tk.Entry(VVIR_window)
    ventricular_sensitivity.place(relx = 0.20, rely = 0.45, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    ventricular_sensitivity_label = tk.Label(VVIR_window, text = 'Ventricular Sensitivity', bg = '#bce6eb')
    ventricular_sensitivity_label.place(relx = 0.20, rely = 0.49, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    ventricular_pulse_width = tk.Entry(VVIR_window)
    ventricular_pulse_width.place(relx = 0.20, rely = 0.55, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    ventricular_pulse_width_label = tk.Label(VVIR_window, text = 'Ventricular Pulse Width (1ms - 30ms)', bg = '#bce6eb')
    ventricular_pulse_width_label.place(relx = 0.20, rely = 0.59, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    '''Right'''
    VRP = tk.Entry(VVIR_window, text = "VRP")
    VRP.place(relx = 0.80, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    VRP_label = tk.Label(VVIR_window, text = 'VRP (150ms-500ms)', bg = '#bce6eb')
    VRP_label.place(relx = 0.80, rely = 0.09, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    hysteresis = tk.Entry(VVIR_window, text = "Hysteresis")
    hysteresis.place(relx = 0.80, rely = 0.15, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    hysteresis_label = tk.Label(VVIR_window, text = 'Hysteresis (200ms-500ms)', bg = '#bce6eb')
    hysteresis_label.place(relx = 0.80, rely = 0.19, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    activity_threshold = tk.Entry(VVIR_window)
    activity_threshold.place(relx = 0.80, rely = 0.25, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    activity_threshold_label = tk.Label(VVIR_window, text = 'Activity Threshold (1-6)', bg = '#bce6eb')
    activity_threshold_label.place(relx = 0.80, rely = 0.29, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    reaction_time = tk.Entry(VVIR_window)
    reaction_time.place(relx = 0.80, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    reaction_time_label = tk.Label(VVIR_window, text = 'Reaction Time (10000ms - 50000ms)', bg = '#bce6eb')
    reaction_time_label.place(relx = 0.80, rely = 0.39, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    response_factor = tk.Entry(VVIR_window)
    response_factor.place(relx = 0.80, rely = 0.45, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    response_factor_label = tk.Label(VVIR_window, text = 'Response Factor (1-16)', bg = '#bce6eb')
    response_factor_label.place(relx = 0.80, rely = 0.49, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    recovery_time = tk.Entry(VVIR_window)
    recovery_time.place(relx = 0.80, rely = 0.55, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    recovery_time_label = tk.Label(VVIR_window, text = 'Recovery Time (120000ms - 960000ms)', bg = '#bce6eb')
    recovery_time_label.place(relx = 0.80, rely = 0.59, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    '''Bottom'''
    rate_smoothing = tk.Entry(VVIR_window)
    rate_smoothing.place(relx = 0.5, rely = 0.65, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    rate_smoothing_label = tk.Label(VVIR_window, text = 'Rate Smoothing (3,6,9,12,15,18,21)', bg = '#bce6eb')
    rate_smoothing_label.place(relx = 0.50, rely = 0.69, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    error_label = tk.Label(VVIR_window, text = '', bg = '#bce6eb')
    error_label.place(relx = 0.5, rely = 0.75, relwidth = 0.5, relheight = 0.05, anchor = 'n')

    if (not lower_rate_limit.get() or not upper_rate_limit.get() or not maxSensorRate.get() or not ventricular_amplitude.get() or not ventricular_pulse_width or not VRP.get() or not  hysteresis.get() or not rate_smoothing.get() or not activity_threshold.get() or not reaction_time.get() or not response_factor.get() or not recovery_time.get()):
        error_label['text'] = 'Please ensure every input is filled in' 

    pace_now_button = tk.Button(VVIR_window, text = "Pace Now", font = 96, command = lambda: VVIR_Pace(int(lower_rate_limit.get()), int(upper_rate_limit.get()), int(maxSensorRate.get()), float(ventricular_amplitude.get()), float(ventricular_pulse_width.get()), int(VRP.get()), int(hysteresis.get()), float(rate_smoothing.get()), int(activity_threshold.get()), int(reaction_time.get()), int(response_factor.get()), int(recovery_time.get()), error_label))
    pace_now_button.place(relx = 0.5, rely = 0.80, relwidth = 0.40, relheight = 0.10, anchor = 'n')

#DOOR_window
def DOOR_window():
    DOOR_window = tk.Toplevel(root, height = HEIGHT, width = WIDTH)
    DOOR_window.configure(background = '#bce6eb')

    lower_rate_limit = tk.Entry(DOOR_window, text = "Lower Rate Limit ")
    lower_rate_limit.place(relx = 0.2, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    lower_rate_label = tk.Label(DOOR_window, text = 'Lower Rate Limit (30ppm-175ppm)', bg = '#bce6eb')
    lower_rate_label.place(relx = 0.2, rely = 0.09, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    upper_rate_limit = tk.Entry(DOOR_window, text = "Upper Rate Limit")
    upper_rate_limit.place(relx = 0.2, rely = 0.20, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    upper_rate_label = tk.Label(DOOR_window, text = 'Upper Rate Limit (50ppm - 175ppm)', bg = '#bce6eb')
    upper_rate_label.place(relx = 0.2, rely = 0.24, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    atrial_pulse_width = tk.Entry(DOOR_window, text = "Atrial Pulse Width")
    atrial_pulse_width.place(relx = 0.2, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    atrial_pulse_label = tk.Label(DOOR_window, text = 'Atrial Pulse Width (1ms - 30ms)', bg = '#bce6eb')
    atrial_pulse_label.place(relx = 0.2, rely = 0.39, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    activity_threshold = tk.Entry(DOOR_window)
    activity_threshold.place(relx = 0.2, rely = 0.50, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    activity_threshold_label = tk.Label(DOOR_window, text = 'Activity Threshold (1-6)', bg = '#bce6eb')
    activity_threshold_label.place(relx = 0.2, rely = 0.54, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    reaction_time = tk.Entry(DOOR_window)
    reaction_time.place(relx = 0.50, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    reaction_time_label = tk.Label(DOOR_window, text = 'Reaction Time (10000ms - 50000ms)', bg = '#bce6eb')
    reaction_time_label.place(relx = 0.50, rely = 0.09, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    response_factor = tk.Entry(DOOR_window)
    response_factor.place(relx = 0.50, rely = 0.20, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    response_factor_label = tk.Label(DOOR_window, text = 'Response Factor (1-16)', bg = '#bce6eb')
    response_factor_label.place(relx = 0.50, rely = 0.24, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    recovery_time = tk.Entry(DOOR_window)
    recovery_time.place(relx = 0.50, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    recovery_time_label = tk.Label(DOOR_window, text = 'Recovery Time (120000ms - 960000ms)', bg = '#bce6eb')
    recovery_time_label.place(relx = 0.50, rely = 0.39, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    ventricular_pulse_width = tk.Entry(DOOR_window, text = "Ventricular Pulse Width")
    ventricular_pulse_width.place(relx = 0.50, rely = 0.50, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    ventricular_pulse_width_label = tk.Label(DOOR_window, text = 'Ventricular Pulse Width (1ms - 30ms)', bg = '#bce6eb')
    ventricular_pulse_width_label.place(relx = 0.50, rely = 0.54, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    atrial_amplitude = tk.Entry(DOOR_window, text = "Atrial Amplitude")
    atrial_amplitude.place(relx = 0.80, rely = 0.05, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    atrial_amplitude_label = tk.Label(DOOR_window, text = 'Atrial Amplitude (0.1V - 5V)', bg = '#bce6eb')
    atrial_amplitude_label.place(relx = 0.80, rely = 0.09, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    ventricular_amplitude = tk.Entry(DOOR_window)
    ventricular_amplitude.place(relx = 0.80, rely = 0.20, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    ventricular_amplitude_label = tk.Label(DOOR_window, text = 'Ventricular Amplitude (0.1V - 5V)', bg = '#bce6eb')
    ventricular_amplitude_label.place(relx = 0.80, rely = 0.24, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    maxSensorRate = tk.Entry(DOOR_window, text = "Max Sensor Rate")
    maxSensorRate.place(relx = 0.80, rely = 0.35, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    maxSensorRate_label = tk.Label(DOOR_window, text = 'Max Sensor Rate (50-175)', bg = '#bce6eb')
    maxSensorRate_label.place(relx = 0.80, rely = 0.39, relwidth = 0.30, relheight = 0.040, anchor = 'n')

    fixed_AV_delay = tk.Entry(DOOR_window, text = "Fixed AV Delay")
    fixed_AV_delay.place(relx = 0.80, rely = 0.50, relwidth = 0.20, relheight = 0.040, anchor = 'n')
    fixed_AV_delay_label = tk.Label(DOOR_window, text = 'Fixed AV Delay (70-300)', bg = '#bce6eb')
    fixed_AV_delay_label.place(relx = 0.80, rely = 0.54, relwidth = 0.30, relheight = 0.040, anchor = 'n')


    error_label = tk.Label(DOOR_window, text = '', bg = '#bce6eb')
    error_label.place(relx = 0.5, rely = 0.85, relwidth = 0.5, relheight = 0.05, anchor = 'n')

    if (not lower_rate_limit.get() or not upper_rate_limit.get() or not maxSensorRate.get() or not fixed_AV_delay.get() or not atrial_amplitude.get() or not ventricular_amplitude.get() or not atrial_amplitude.get() or not atrial_pulse_width.get() or not ventricular_pulse_width.get() or not activity_threshold.get() or not reaction_time.get() or not response_factor.get() or not recovery_time.get()):
        error_label['text'] = 'Please ensure every input is filled in' 

    pace_now_button = tk.Button(DOOR_window, text = "Pace Now", font = 96, command = lambda: DOOR_Pace(int(lower_rate_limit.get()), int(upper_rate_limit.get()), int(maxSensorRate.get()), int(fixed_AV_delay.get()), float(atrial_amplitude.get()), float(ventricular_amplitude.get()), float(atrial_pulse_width.get()), float(ventricular_pulse_width.get()), int(activity_threshold.get()), int(reaction_time.get()), int(response_factor.get()), int(recovery_time.get()), error_label))
    pace_now_button.place(relx = 0.5, rely = 0.90, relwidth = 0.40, relheight = 0.10, anchor = 'n')


# pacing_modes_window
def pacing_modes_window():
    pacing_modes_window = tk.Toplevel(root, height = HEIGHT, width = WIDTH)
    pacing_modes_window.configure(background = '#bce6eb')

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

    display_label = tk.Label(pacing_modes_window, bg = '#bce6eb', text = "Select Pacing Mode", font = 96)
    display_label.place(relx = 0.50, rely = 0.25, relwidth = 0.40, relheight = 0.10, anchor = 'n')

    pacemakerID = tk.Label(pacing_modes_window, text = 'Pacemaker Connected: ' + str(current_pacemakerID), bg = '#bce6eb')
    pacemakerID.place(relx = 0.10, rely = 0, relwidth = 0.30, relheight = 0.05, anchor = 'n')

    DCM_status = tk.Label(pacing_modes_window, font = 14)
    DCM_status.place(relx = 0.90, rely = 0, relwidth = 0.15, relheight = 0.05)

    DCM_status_label = tk.Label(pacing_modes_window, bg = '#bce6eb', text = "DCM Status")
    DCM_status_label.place(relx = 0.95, rely = 0.05, relwidth = 0.080, relheight = 0.040, anchor = 'n')

    #Selecting Egram data 

    data_option_label = tk.Label(pacing_modes_window, bg = '#bce6eb', text = 'Select Egram', font = 96)
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
    register_window.configure(background = '#bce6eb')
    
    label_register = tk.Label(register_window, bg = '#bce6eb', text = "Create New User", font = 96)
    label_register.place(relx = 0.5, rely = 0, relwidth = 0.75, relheight = 0.1, anchor = 'n')

    register_button = tk.Button(register_window, text = "Register", font = 12, command = lambda: create_user(create_username_entry.get(), create_password_entry.get(), label_response))
    register_button.place(relx = 0.5, rely = 0.75, relwidth = 0.5, relheight = 0.1, anchor = 'n')


    create_label_username = tk.Label(register_window, bg = '#bce6eb', text = "Please Enter Desired Username", font = 24)
    create_label_username.place(relx = 0.5, rely = 0.15, relwidth = 0.5, relheight = 0.1, anchor = 'n')
    create_username_entry = tk.Entry(register_window, text = "Create Username", font = 40)
    create_username_entry.place(relx = 0.5, rely = 0.25, relwidth = 0.5, relheight = 0.1, anchor = 'n')

    label__create_password = tk.Label(register_window, bg = '#bce6eb', text = "Please Enter Desired Password", font = 24)
    label__create_password.place(relx = 0.5, rely = 0.40, relwidth = 0.5, relheight = 0.1, anchor = 'n')
    create_password_entry = tk.Entry(register_window, text = "Create Password", font = 40)
    create_password_entry.place(relx = 0.5, rely = 0.50, relwidth = 0.5, relheight = 0.1, anchor = 'n')

    label_response = tk.Label(register_window, font = 20)
    label_response.place(relx = 0.5, rely = 0.65, relwidth = 0.5, relheight = 0.05, anchor = 'n')


########### Main/Root Window ##########
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

frame = tk.Frame(root, bg = '#bce6eb', bd = 5)
frame.place(relx = 0, rely = 0, relwidth = 2, relheight = 1, anchor = 'n')


create_new_user_button = tk.Button(frame, text = "Create New User", font = 12, command = lambda: register_window())
create_new_user_button.place(relx = 0.75, rely = 0.9, relheight = 0.1, relwidth = 0.15, anchor = 'n')

title = tk.Label(root, bg = '#bce6eb', text = "Welcome", font = 96)
title.place(relx = 0.5, rely = 0, relwidth = 0.5, relheight = 0.1, anchor = 'n')

label_username = tk.Label(root, bg = '#bce6eb', text = "Enter Username", font = 24)
label_username.place(relx = 0.5, rely = 0.15, relwidth = 0.5, relheight = 0.1, anchor = 'n')
username_entry = tk.Entry(root, text = "User Name", font = 40)
username_entry.place(relx = 0.5, rely = 0.25, relwidth = 0.5, relheight = 0.1, anchor = 'n')

label_password = tk.Label(root, bg = '#bce6eb', text = "Enter Password", font = 24)
label_password.place(relx = 0.5, rely = 0.40, relwidth = 0.5, relheight = 0.1, anchor = 'n')
password_entry = tk.Entry(root, text = "Password", font = 40, show = '*')
password_entry.place(relx = 0.5, rely = 0.50, relwidth = 0.5, relheight = 0.1, anchor = 'n')

login_button = tk.Button(root, text = "Login", font = 12, command = lambda: login(username_entry.get(), password_entry.get(), label_login_response))
login_button.place(relx = 0.5, rely = 0.7, relheight = .1, relwidth = 0.15, anchor = 'n')              

label_login_response = tk.Label(root, bg = '#bce6eb', font = 12)
label_login_response.place(relx = 0.5, rely = 0.65, relheight = 0.05, relwidth = 0.8, anchor = 'n')

root.mainloop()