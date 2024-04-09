from serial import Serial
import threading
import time
import sys
from antenna import Antenna
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

antennas:Antenna = []

deg = 0


def getCommand():
    return input()

# Test daat for plotting antenna calculations

def drawGraph():
    
 
    # Creating vectors X and Y

    #xbox
    
    a0 = Antenna(115200,"COM3",0,0)
    a1 = Antenna(115200,"COM3",1,1)
    a2 = Antenna(115200,"COM3",2,2)
    a3 = Antenna(115200,"COM3",3,3)
    a4 = Antenna(115200,"COM3",4,4)
    a5 = Antenna(115200,"COM3",5,5)
    a6 = Antenna(115200,"COM3",6,6)
    a7 = Antenna(115200,"COM3",7,7)



    a0.deg = 55
    a1.deg = 80
    a2.deg = 105
    a3.deg = 25
    a4.deg = 120
    a5.deg = 90
    a6.deg = 135
    a7.deg = 120

    a0.switch(a0.pos)
    a1.switch(a1.pos)
    a2.switch(a2.pos)
    a3.switch(a3.pos)
    a4.switch(a4.pos)
    a5.switch(a5.pos)
    a6.switch(a6.pos)
    a7.switch(a7.pos)




    x1 = a0.x
    y1 = a0.y

    x2 = a1.x
    y2 = a1.y

    x3 = a2.x
    y3 = a2.y

    x4 = a3.x
    y4 = a3.y

    x5 = a4.x
    y5 = a4.y

    x6 = a5.x
    y6 = a5.y


    x7 = a6.x
    y7 = a6.y

    x8 = a7.x
    y8 = a7.y



    fig, ax = plt.subplots()
    square = patches.Rectangle((0, 0), 200, 300, edgecolor='orange', facecolor='none')
    ax.add_patch(square)
    
    
    # Create the plot
    plt.xlim(-100, 300)
    plt.ylim(-100, 400)     

    plt.plot(x1,y1)
    plt.plot(x2,y2)
    plt.plot(x3,y3)
    plt.plot(x4,y4)
    plt.plot(x5,y5)
    plt.plot(x6,y6)
    plt.plot(x7,y7)
    plt.plot(x8,y8)

    
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
        antenna = Antenna(parameters[0],parameters[1],parameters[2],id)
        antennas.append(antenna)
        


def switch(command):
    if command == "1":
        print("Add antenna:\n(baudrate)/(COM port)/(POS)")
        addAntenna(input())
    elif command == "2":
        run()
    elif command == "3":
        print(antennas[0].port)
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