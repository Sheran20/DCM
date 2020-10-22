import os

# username = "Steve"
# password = "Rogers"
# lower_rate = 1
# upper_rate= 2
# atrial_amplitude = 3
# atrial_pulse_width= 4
# ventricular_amplitude = 5
# ventricular_pulse_width = 6
# VRP = 7 
# ARP = 8

# textFile = username + ".txt"
# f = open(textFile, "x")
# f.write(
#     "username: %s\n"
#     "password: %s\n"
#     "lower_rate: %d\n" 
#     "upper_rate: %d\n" 
#     "atrial_amplitude: %d\n"
#     "atrial_pulse_width: %d\n"
#     "ventricular_amplitude: %d\n"
#     "ventricular_pulse_width: %d\n"
#     "VRP: %d\n"
#     "ARP: %d\n"
#      % (
#         username,
#         password,
#         lower_rate, 
#         upper_rate, 
#         atrial_amplitude, 
#         atrial_pulse_width, 
#         ventricular_amplitude, 
#         ventricular_pulse_width, 
#         VRP, 
#         ARP
#         )
#     )
# f.close()

# path = os.getcwd()
# print(path)
# print(">>>>" + path + "\\users" + "\\" + textFile)
# os.rename(path + "\\" + textFile, path + "\\users" + "\\" + textFile)


directory = os.getcwd() + "\\users"
#print(directory)

for filename in os.listdir(directory):
    
    if filename.endswith(".txt"):
        file_directory = directory + "\\" + filename
        
        username = None
        password = None
        lower_rate = None
        upper_rate = None
        atrial_amplitude = None
        atrial_pulse_width = None
        ventricular_amplitude = None
        ventricular_pulse_width = None
        VRP = None
        ARP = None

        f = open(file_directory, "r")
        for line in f:
            if "username: " in line:
                username = line.split(":")[-1].strip()
            elif "password: " in line:
                password = line.split(":")[-1].strip()
            elif "lower_rate: " in line:
                lower_rate = line.split(":")[-1].strip()
            elif "upper_rate: " in line:
                upper_rate = line.split(":")[-1].strip()
            elif "atrial_amplitude: " in line:
                atrial_amplitude = line.split(":")[-1].strip()
            elif "atrial_pulse_width: " in line:
                atrial_pulse_width = line.split(":")[-1].strip()
            elif "ventricular_amplitude: " in line:
                ventricular_amplitude = line.split(":")[-1].strip()
            elif "ventricular_pulse_width: " in line:
                ventricular_pulse_width = line.split(":")[-1].strip()
            elif "VRP: " in line:
                VRP = line.split(":")[-1].strip()
            elif "ARP: " in line:
                ARP = line.split(":")[-1].strip()
        
        print(username)
        print(password)
        print(lower_rate)
        print(upper_rate)
        print(atrial_amplitude)
        print(atrial_pulse_width)
        print(ventricular_amplitude)
        print(ventricular_pulse_width)
        print(VRP)
        print(ARP)

    else:
        print("No current users")
