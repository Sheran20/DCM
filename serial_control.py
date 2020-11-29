import serial
import struct
from serial import tools

deviceName = 'COM4'
baudRate = 115200
DCM_status_val = None
current_pacemakerID = None

## check for Pacemaker connection - set status and id if connected
with serial.Serial(port = deviceName, baudrate = baudRate) as device:
    if(device.name == deviceName):
        DCM_status_val = 1
        current_pacemakerID = device.name
        print(DCM_status_val, current_pacemakerID)

data_dictionary = {
    "data_mode": 0,                     # B 
    "pace_mode": 0,                    # B  
    "lower_rate": 0,                   # h 
    "atrial_amplitude": 0,              # f 
    "ventricular_amplitude": 0,         # f 
    "atrial_pulse_width": 0,            # d 
    "ventricular_pulse_width": 0,       # d  
    "ARP": 0,                         # h 
    "VRP": 0,                         # h                  
    "rate_smooth": 0,                   # d 
    "av_delay": 0,                    # h   
    "atrial_sensitivity": 0,            # B  
    "ventricular_sensitivity": 0,       # B  
    "max_sensor_rate": 0,             # h  
    "activitiy_threshold": 0,           # h  
    "activity_reaction_time": 0,       # h  
    "activity_response_factor": 0,      # h  
    "activity_recovery_time": 0        # h  
}

def set_data(parameters, values):
    data_array = []
    i= 0
    for parameter in parameters:
        data_dictionary.update({parameter: values[i]}) 
        i += 1
    for key in data_dictionary:
        data_array.append(data_dictionary[key])         # appends every value for each key
    # print(data_array)
    # print(data_dictionary)
    return data_array

def serial_read_atr():
    with serial.Serial(port = deviceName, baudrate = baudRate) as device:
        packet = struct.pack("<BBhffddhhdhBBhhhhh",[1,data_dictionary["pace_mode"],0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        device.write(packet)
        received = device.read(16)
        data1 = struct.unpack("<dd", received)
        while(True):
            print(data1[0])

def serial_read_vent():
    with serial.Serial(port = deviceName, baudrate = baudRate) as device:
        with serial.Serial(port = deviceName, baudrate = baudRate) as device:
            packet = struct.pack("<BBhffddhhdhBBhhhhh",[1,data_dictionary["pace_mode"],0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            device.write(packet)
            received = device.read(16)
            data1 = struct.unpack("<dd", received)
            while(True):
                print(data1[1])

def serial_read_atr_vent():
    with serial.Serial(port = deviceName, baudrate = baudRate) as device:
        with serial.Serial(port = deviceName, baudrate = baudRate) as device:
            packet = struct.pack("<BBhffddhhdhBBhhhhh",[1,data_dictionary["pace_mode"],0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            device.write(packet)
            received = device.read(16)
            data1 = struct.unpack("<dd", received)
            while(True):
                print(data1[0], data1[1])



def serial_send(parameters, values):
    data_array = set_data(parameters, values)
    print(data_array)
    with serial.Serial(port = deviceName, baudrate = baudRate) as device:
        packet = struct.pack("<BBhffddhhdhBBhhhhh",*data_array)
        device.write(packet)



## for now leave the last five unchanged since the r modes are not complete
## the first byte is used to determine read write actions, 0 for model to receive, 1 for model to send 

## data = [
##     data_mode,
##     pacing_mode,
##     lower_rate,
##     atrial_amplitude,
##     ventricular_amplitude,
##     atrial_pulse_width,
##     ventricular_pulse_width, 
##     VRP, 
##     ARP, 
##     rate_smooth,
##     av_delay,
##     atrial_sensitivity,
##     ventricular_sensitivity,
##     max_sensor_rate,
##     activitiy_threshold,
##     activity_reaction_time,
##     activity_response_factor,
##     activity_recovery_time
## ]