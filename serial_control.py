import serial
import struct
from serial import tools

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

deviceName = 'COM4'
baudRate = 115200

def DCM_Status():
    ## check for Pacemaker connection - set status and id if connected
    try:
        with serial.Serial(port = deviceName, baudrate = baudRate) as device:
            if(device.name == deviceName):
                DCM_status_val = 1
                current_pacemakerID = device.name
                print(DCM_status_val, current_pacemakerID)
                return DCM_status_val, current_pacemakerID
    except:
        DCM_status_val = 0
        current_pacemakerID = "No Device Connected"
        return DCM_status_val, current_pacemakerID



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
    return data_array

def serial_recieve_av():
    with serial.Serial(port = deviceName, baudrate = baudRate) as device:
        packet = struct.pack("<BBhffddhhdhBBhhhhh",*[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        device.write(packet)

        y_range = [0,1]
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.set_ylim(y_range)
        xs = []
        ys = []
        ys2 = []

        i = 0
        def animate(i, xs, ys, ys2):
            received = device.readline()
            ventricular_signal = 0
            atrial_signal = 0
            if len(received) == 17:
                ventricular_signal = struct.unpack("d", received[0:8])[0]
                atrial_signal = struct.unpack("d", received[8:16])[0]
                print(ventricular_signal, atrial_signal)
                
            length = len(xs)
            if length > 100:
                xs.pop(0)
                ys.pop(0)
                ys2.pop(0)

            xs.append(i)
            ys.append(ventricular_signal)
            ys2.append(atrial_signal)
            
            ax.clear()
            i += 1
            ax.plot(xs, ys, label = 'Ventricular Signal')
            ax.plot(xs, ys2, label = 'Atrial Signal')

            plt.title('Ventricular & Atrial Egram over Time')
            plt.xlabel('Time (s)')
            plt.ylabel('Votlage (V)')
            plt.xticks(rotation=45, ha='right')
            plt.subplots_adjust(bottom=0.30)
            ax.set_ylim(y_range)

        ani = FuncAnimation(fig, animate, fargs=(xs, ys, ys2) , interval = 1)
        plt.show()

def serial_recieve_v():
    with serial.Serial(port = deviceName, baudrate = baudRate) as device:
        packet = struct.pack("<BBhffddhhdhBBhhhhh",*[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        device.write(packet)

        y_range = [0,1]
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.set_ylim(y_range)
        xs = []
        ys = []

        i = 0
        def animate(i, xs, ys):
            received = device.readline()
            ventricular_signal = 0
            if len(received) == 17:
                ventricular_signal = struct.unpack("d", received[0:8])[0]
                print(ventricular_signal)
                
            length = len(xs)
            if length > 100:
                xs.pop(0)
                ys.pop(0)

            xs.append(i)
            ys.append(ventricular_signal)
            
            ax.clear()
            i += 1
            ax.plot(xs, ys)

            plt.title('Ventricular Egram over Time')
            plt.xlabel('Time (s)')
            plt.ylabel('Votlage (V)')
            plt.xticks(rotation=45, ha='right')
            plt.subplots_adjust(bottom=0.30)
            ax.set_ylim(y_range)

        ani = FuncAnimation(fig, animate, fargs=(xs, ys) , interval = 1)
        plt.show()

def serial_recieve_a():
    with serial.Serial(port = deviceName, baudrate = baudRate) as device:
        packet = struct.pack("<BBhffddhhdhBBhhhhh",*[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        device.write(packet)

        y_range = [0,1]
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.set_ylim(y_range)
        xs = []
        ys = []

        i = 0
        def animate(i, xs, ys):
            received = device.readline()
            atrial_signal = 0
            if len(received) == 17:
                atrial_signal = struct.unpack("d", received[8:16])[0]
                print(atrial_signal)
                
            length = len(xs)
            if length > 100:
                xs.pop(0)
                ys.pop(0)

            xs.append(i/20)
            ys.append(atrial_signal)
            
            ax.clear()
            i += 1
            ax.plot(xs, ys)

            plt.title('Atrial Egram over Time')
            plt.xlabel('Time (s)')
            plt.ylabel('Votlage (V)')
            plt.xticks(rotation=45, ha='right')
            plt.subplots_adjust(bottom=0.30)
            ax.set_ylim(y_range)

        ani = FuncAnimation(fig, animate, fargs=(xs, ys) , interval = 1)
        plt.show()

def serial_send(parameters, values):
    data_array = set_data(parameters, values)
    print(data_array)
    with serial.Serial(port = deviceName, baudrate = baudRate) as device:
        packet = struct.pack("<BBhffddhhdhBBhhhhh",*data_array)
        device.write(packet)