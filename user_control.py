import os

########## User Class Defenition #########
class User:
    
    # contructor
    def __init__(self, username, password):
        self.username = username
        self.password = password
        # user data
        self.lower_rate = 0
        self.upper_rate = 0
        self.atrial_amplitude = 0
        self.atrial_pulse_width = 0
        self.ventricular_amplitude = 0
        self.ventricular_pulse_width = 0
        self.VRP = 0
        self.ARP = 0
        self.file_directory = os.getcwd() + "\\users" +"\\" + username + ".txt"
        self.userData = ["username","password","lower_rate","upper_rate","atrial_amplitude","atrial_pulse_width","ventricular_amplitude","ventricular_pulse_width", "VRP", "ARP"]

    # getters
    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password   

    # setters and some getters removed - user can only set and get instance fields when authorized

    # methods
    def userStore(self):
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

    def userUpdate(self, fields, values):         #this method updates the text files, not the instance variables
        i = 0
        for field in fields:
            if field not in self.userData:                                  #check if the specified field exists
                print("Field does not exist")
                return
            else:
                j = self.userData.index(field)
                f = open(self.file_directory, "r")
                data = f.readlines()
                data[j] = field + ": " + str(values[i]) + "\n"              #change the line specified
                i += 1
                f = open(self.file_directory, "w")
                f.writelines(data)
                f.close



########## User Utility Functions ##########
userObjects = []                               # this array loads up all user data and is available only when application starts

def getUserData():                             # necessary function to authorize login
    
    directory = os.getcwd() + "\\users"
    for filename in os.listdir(directory):                        # loop through text files
        
        if filename.endswith(".txt"):
            file_directory = directory + "\\" + filename
            
            username = None                                       # set temporary user data
            password = None
            lower_rate = None
            upper_rate = None
            atrial_amplitude = None
            atrial_pulse_width = None
            ventricular_amplitude = None
            ventricular_pulse_width = None
            VRP = None
            ARP = None

            f = open(file_directory, "r")                        # read data from text files and store them
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
            
            oldUser = User(username, password)
            oldUser.userUpdate([
                "lower_rate", 
                "upper_rate", 
                "atrial_amplitude", 
                "atrial_pulse_width",
                "ventricular_amplitude", 
                "ventricular_pulse_width",
                "VRP",
                "ARP"
            ],
            [
                lower_rate,
                upper_rate,
                atrial_amplitude,
                atrial_pulse_width,
                ventricular_amplitude,
                ventricular_pulse_width,
                VRP,
                ARP
                ])
            userObjects.append(oldUser)

        else:
            print("No current users")







