from serial import Serial
import threading
import time
import sys
from antenna import Antenna
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

global antennas

antennas:Antenna = []
#antennas.append(Antenna(115200,"COM5",0,0)) 


# Test daat for plotting antenna calculations

def drawGraph():
    
 
    # Creating vectors X and Y
    
    

    fig, ax = plt.subplots()
    square = patches.Rectangle((0, 0), 200, 300, edgecolor='orange', facecolor='none')
    ax.add_patch(square)
    
    
    # Create the plot
    plt.xlim(-100, 300)
    plt.ylim(-100, 400)   
    
    x1 = antennas[0].x
    y1 = antennas[0].y
    x2 = antennas[1].x
    y2 = antennas[1].y
    plt.plot(x1,y1)
    plt.plot(x2,y2)

    
    # function to show the plot
    plt.show()

    #End of test Data
    

def addAntenna(string):
    createAntenna = True
    parameters = string.split("/")
    id = len(antennas)
    for antenna in antennas:
        if antenna.pos == parameters[2]:
            print("ERROR Pos already in use!")
            createAntenna = False
            break  
    if createAntenna:
        print(parameters[0] + " " + parameters[1] + " " + parameters[2]+ " " + str(id))
        antennas.append(Antenna(parameters[0],parameters[1],int(parameters[2]),id))
        


def switch(command):
    if command == "1":
        print("Add antenna:\n(baudrate)/(COM port)/(POS)")
        addAntenna(input())
    elif command == "2":
        run()
    elif command == "3":
        print(antennas[0].port)
        print(antennas[0].deg)
    elif command == "4":
        writeCommand()
    elif command == "5":
        drawGraph()
    
def writeCommand():
    run = True

    
    print("Specify which antenna by its id:")
    for antenna in antennas:
        print(antenna.id)
    antenna = input()
    while run:
        print("write 'back' to exit")
        print(antennas[int(antenna)].port)
        print("Wite command:")
        command = input()
        if command == "back":
            run = False
        else:
            antennas[int(antenna)].write(command + "\r")
            time.sleep(0.2)
        



if __name__ == "__main__":

    run = True
    
    while run:
        print("Main Menu\n1:Add antenna\n2:Run\n3:List antenna\n4:Write Command\n5:Draw Graph")
        command = input()
        if command == "exit":
            run = False
        else:
            switch(command)
        



        

"""

Antenna angles 

0 = +45deg
1 = 0
2 = - 45deg
3 = + 90deg
4 = + 90deg
5 =  - 45deg
6 = 0
7 =  + 45deg


"""