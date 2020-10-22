import os

username = "bob"
password = "yeet"
lower_rate = 1
upper_rate= 2
atrial_amplitude = 3
atrial_pulse_width= 4
ventricular_amplitude = 5
ventricular_pulse_width = 6
VRP = 7 
ARP = 8

textFile = username + ".txt"
f = open(textFile, "x")
f.write(
    "username: %s\n"
    "password: %s\n"
    "lower_rate: %d\n" 
    "upper_rate: %d\n" 
    "atrial_amplitude: %d\n"
    "atrial_pulse_width: %d\n"
    "ventricular_amplitude: %d\n"
    "ventricular_pulse_width: %d\n"
    "VRP: %d\n"
    "ARP: %d\n"
     % (
        username,
        password,
        lower_rate, 
        upper_rate, 
        atrial_amplitude, 
        atrial_pulse_width, 
        ventricular_amplitude, 
        ventricular_pulse_width, 
        VRP, 
        ARP
        )
    )
f.close()

path = os.getcwd()
print(path)
os.rename(path + "/" + textFile, path + "/users" + "/" + textFile)
