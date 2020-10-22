import os

class User:
    
    # contructor
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # user data
    lower_rate = 0
    upper_rate = 0
    atrial_amplitude = 0
    atrial_pulse_width = 0
    ventricular_amplitude = 0
    ventricular_pulse_width = 0
    VRP = 0
    ARP = 0

    # getters
    def getName(self):
        return self.username

    def getPassword(self):
        return self.password   

    def getUpperRate(self):
        return self.upper_rate

    def getAtrialAmplitude(self):
        return self.atrial_amplitude

    def getAtrialPulseWidth(self):
        return self.atrial_pulse_width

    def getVentricularAmplitude(self):
        return self.ventricular_amplitude

    def getVentricularPulseWidth(self):
        return self.ventricular_pulse_width

    def getVRP(self):
        return self.VRP

    def getARP(self):
        return self.ARP
    
    #setters
    def setUpperRate(self, value):
        self.upper_rate = value

    def setAtrialAmplitude(self, value):
        self.atrial_amplitude = value

    def setAtrialPulseWidth(self, value):
        self.atrial_pulse_width = value

    def setVentricularAmplitude(self, value):
        self.ventricular_amplitude = value

    def setVentricularPulseWidth(self, value):
        self.ventricular_pulse_width = value

    def setVRP(self, value):
        self.VRP = value

    def setARP(self, value):
        self.ARP = value


    # methods
    def storeUser(self):
        textFile = self.username + ".txt"
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
                self.username,
                self.password,
                self.lower_rate, 
                self.upper_rate, 
                self.atrial_amplitude, 
                self.atrial_pulse_width, 
                self.ventricular_amplitude, 
                self.ventricular_pulse_width, 
                self.VRP, 
                self.ARP
            )
        )
        f.close()

        # moving user to users directory
        path = os.getcwd()
        print(path)
        os.rename(path + "\\" + textFile, path + "\\users" + "\\" + textFile)

    def deleteUser(self):
        textFile = self.username + ".txt"
        os.remove(textFile)

userObjects = []

def getUserData():
    
    directory = os.getcwd() + "\\users"
    for filename in os.listdir(directory):                        #loop through text files
        
        if filename.endswith(".txt"):
            file_directory = directory + "\\" + filename
            
            username = None                                       #set temporary user data
            password = None
            lower_rate = None
            upper_rate = None
            atrial_amplitude = None
            atrial_pulse_width = None
            ventricular_amplitude = None
            ventricular_pulse_width = None
            VRP = None
            ARP = None

            f = open(file_directory, "r")                        #read data from text files and store them
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

            oldUser = User(username, password)
            userObjects.append(oldUser)

        else:
            print("No current users")