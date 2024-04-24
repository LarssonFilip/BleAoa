from serial import Serial
import threading
import time
import numpy as np


BUFFSIZE = 20


class Antenna:

    
   

    def __init__(self, baudrate, port, pos, id):

        self.buff = []
        self.buffix = 0
        self.pos = pos
        self.id = id
        self.baudrate = baudrate
        self.port = port
        self.y = 0
        self.x = np.linspace(-100, 400, 1000)
        self.deg = 0
        self.cDeg = 0
        self.rssi = -56
        self.parameters = []
        self.convAngle(self.deg)
        self.switch()
        


        #Remove to use antenna """
        

        self.serialPort = Serial(port=self.port, baudrate=self.baudrate)
        print(self.serialPort.name)
        self.threadRead = threading.Thread(target=self.read)
        self.threadRead.start()


    


    def read(self):
        while True:
            string = self.serialPort.readline().decode("ASCII")
            if string != "" or string != "\n":
                if "UUDF" in string:
                    self.parameters = string.split(",")
                    self.convAngle(self.parameters[2])
                    self.rssi = self.parameters[1]
                    self.switch()
                else: 
                    print(string.strip())

    def write(self, input):
        self.serialPort.write(input.encode())
        #"""
        #Remove to use antenna

    def convAngle(self,angle):
        if self.buffix != BUFFSIZE:
            self.buff[self.buffix] = int(angle)
            self.buffix + 1
        else:
            self.buffix = 0
            self.buff[self.buffix] = int(angle)
        average = np.average(self.buff)
        print(average)
        self.deg = 90 - average


        
    def switch(self):
        if self.pos == 0:
            self.cDeg = self.deg + 45
            self.y = ((np.sin(np.deg2rad(self.cDeg))/np.cos(np.deg2rad(self.cDeg))) * self.x) + 300
        elif self.pos == 1:
            self.cDeg = self.deg
            self.y = ((np.sin(np.deg2rad(self.cDeg))/np.cos(np.deg2rad(self.cDeg))) * self.x) + ((300/np.tan(np.deg2rad(self.cDeg)))-100)*(np.sin(np.deg2rad(self.cDeg))/np.cos(np.deg2rad(self.cDeg)))
        elif self.pos == 2:
            self.cDeg = self.deg - 45
            self.y = ((np.sin(np.deg2rad(self.cDeg))/np.cos(np.deg2rad(self.cDeg))) * self.x) - (200*np.tan(np.deg2rad(self.cDeg))-300)
        elif self.pos == 3:
            self.cDeg = self.deg + 90
            self.y = ((np.sin(np.deg2rad(self.cDeg))/np.cos(np.deg2rad(self.cDeg))) * self.x) + 150
        elif self.pos == 4:
            self.cDeg = self.deg + 90
            self.y = ((np.sin(np.deg2rad(self.cDeg))/np.cos(np.deg2rad(self.cDeg))) * self.x) - (200*np.tan(np.deg2rad(self.cDeg))-150)
        elif self.pos == 5:
            self.cDeg = self.deg - 45
            self.y = ((np.sin(np.deg2rad(self.cDeg))/np.cos(np.deg2rad(self.cDeg))) * self.x) 
        elif self.pos == 6:
            self.cDeg = self.deg 
            self.y = ((np.sin(np.deg2rad(self.cDeg))/np.cos(np.deg2rad(self.cDeg))) * self.x) - (100*(np.sin(np.deg2rad(self.cDeg))/np.cos(np.deg2rad(self.cDeg))))
        elif self.pos == 7:
            self.cDeg = self.deg + 45    
            self.y = ((np.sin(np.deg2rad(self.cDeg))/np.cos(np.deg2rad(self.cDeg))) * self.x) - (200*(np.sin(np.deg2rad(self.cDeg))/np.cos(np.deg2rad(self.cDeg))))
  
        
        

