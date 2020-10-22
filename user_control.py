import os

class User:
    
    # contructor
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # user data
    lower_rate = 1
    upper_rate = 2
    atrial_amplitude = 3
    atrial_pulse_width = 4
    ventricular_amplitude = 5
    ventricular_pulse_width = 6
    VRP = 7
    ARP = 8

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
        os.rename(path + "/" + textFile, path + "/users" + "/" + textFile)

    def deleteUser(self):
        textFile = self.username + ".txt"
        os.remove(textFile)


