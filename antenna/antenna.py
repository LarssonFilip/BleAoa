from serial import Serial
import threading
import time
import numpy as np





class Antenna:

   

    def __init__(self, baudrate, port, pos, id):

        self.pos = pos
        self.id = id
        self.baudrate = baudrate
        self.port = port
        self.x = np.linspace(-100, 400, 100)
        self.y = 0
        self.deg = 45
        self.cDeg = 0
        #Remove to use antenna
        """

        self.serialPort = Serial(port=self.port, baudrate=self.baudrate)
        print(self.serialPort.name)
        self.threadRead = threading.Thread(target=self.read)
        self.threadRead.start()



    def read(self):
        while True:
            string = self.serialPort.readline().decode("ASCII")
            if string != "" or string != "\n":
                print(string.strip())

    def write(self, input):
        self.serialPort.write(input.encode())
        """
        #Remove to use antenna
    
    def switch(self,pos):
        if pos == 0:
            self.cDeg = self.deg + 45
            self.y = ((np.sin(np.deg2rad(self.cDeg))/np.cos(np.deg2rad(self.cDeg))) * self.x) + 300
        elif pos == 1:
            self.cDeg = self.deg
            self.y = ((np.sin(np.deg2rad(self.cDeg))/np.cos(np.deg2rad(self.cDeg))) * self.x) + ((300/np.tan(np.deg2rad(self.cDeg)))-100)*(np.sin(np.deg2rad(self.cDeg))/np.cos(np.deg2rad(self.cDeg)))
        elif pos == 2:
            self.cDeg = self.deg - 45
            self.y = ((np.sin(np.deg2rad(self.cDeg))/np.cos(np.deg2rad(self.cDeg))) * self.x) - (200*np.tan(np.deg2rad(self.cDeg))-300)
        elif pos == 3:
            self.cDeg = self.deg + 90
            self.y = ((np.sin(np.deg2rad(self.cDeg))/np.cos(np.deg2rad(self.cDeg))) * self.x) + 150
        elif pos == 4:
            self.cDeg = self.deg + 90
            self.y = ((np.sin(np.deg2rad(self.cDeg))/np.cos(np.deg2rad(self.cDeg))) * self.x) - (200*np.tan(np.deg2rad(self.cDeg))-150)
        elif pos == 5:
            self.cDeg = self.deg - 45
            self.y = ((np.sin(np.deg2rad(self.cDeg))/np.cos(np.deg2rad(self.cDeg))) * self.x) 
        elif pos == 6:
            self.cDeg = self.deg 
            self.y = ((np.sin(np.deg2rad(self.cDeg))/np.cos(np.deg2rad(self.cDeg))) * self.x) - (100*(np.sin(np.deg2rad(self.cDeg))/np.cos(np.deg2rad(self.cDeg))))
        elif pos == 7:
            self.cDeg = self.deg + 45    
            self.y = ((np.sin(np.deg2rad(self.cDeg))/np.cos(np.deg2rad(self.cDeg))) * self.x) - (200*(np.sin(np.deg2rad(self.cDeg))/np.cos(np.deg2rad(self.cDeg))))
  
        
        

