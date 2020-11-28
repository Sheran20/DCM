import serial
import struct
from serial import tools

deviceName = 'COM4'
baudRate = 115200
data = [1,1,60,5,3.5,0.05,1,250,320,1,150,3,3,120,2,30,10,300]

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
##     activity_response_time
## ]

# for item in serial.tools.list_ports.comports():
#   print(item)

with serial.Serial(port = deviceName, baudrate = baudRate) as device:
    packet = struct.pack("<BBhffddhhdhBBhhhhh",*data)
    device.write(packet)
    if (data[0]):
        received = device.read(16)
        data1 = struct.unpack("<dd", received)
        print(device.name)
        print(data1[0]) ## Atrial egram signal
        print(data1[1]) ## ventricle egram signal