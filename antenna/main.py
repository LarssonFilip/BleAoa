from serial import Serial
import threading
import time
import sys
from antenna import Antenna
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

global antennas


measuredPower = -60
N = 2

antennas:Antenna = []
#antennas.append(Antenna(115200,"COM5",3,0)) 
#antennas.append(Antenna(115200,"COM5",1,1)) 
#antennas.append(Antenna(115200,"COM5",2,2)) 

# Test daat for plotting antenna calculations

def drawGraph():
    
    funcs = []
    xV = []
    yV = []
 
    # Creating vectors X and Y
    x = np.linspace(-100, 400, 1000)
    
    fig, ax = plt.subplots()
    square = patches.Rectangle((0, 0), 200, 300, edgecolor='orange', facecolor='none',)
    ax.add_patch(square)

    # Create the plot
    plt.xlim(-100, 300)
    plt.ylim(-100, 400)

    if(len(antennas) <= 1):
        
        plt.plot(antennas[0].x, antennas[0].y)
        distance = np.power(10, ((measuredPower-antennas[0].rssi)/(10*N)))
        print(distance)
        #draw a circle
        pos = antennas[0].pos
        if pos == 0:
            xOff = 0
            yOff = 300
        elif pos == 1:
            xOff = 100
            yOff = 300
        elif pos == 2:
            xOff = 200
            yOff = 300
        elif pos == 3:
            xOff = 0
            yOff = 150
        elif pos == 4:
            xOff = 200
            yOff = 150
        elif pos == 5:
            xOff = 0
            yOff = 0
        elif pos == 6:
            xOff = 100
            yOff = 0
        elif pos == 7:
            xOff = 200
            yOff = 0

        angles = np.linspace(0 * np.pi, 2 * np.pi, 100 )
        r = 100 * distance
        xs = r * np.cos(angles) + xOff
        ys = r * np.sin(angles) + yOff
        plt.plot(xs, ys, color = 'green')



    else:

        for antenna in antennas:
            y = antenna.y
            funcs.append(y)
            plt.plot(x,y)

            
        for i, func in enumerate(funcs):
            for j, fun in enumerate(funcs):
                if(i != len(funcs)-1):
                    if(j > i):
                        idx = np.argwhere(np.diff(np.sign(funcs[i] - funcs[j]))).flatten()
                        
                        plt.plot(x[idx], funcs[i][idx], 'ro')  
                        xV.append(x[idx])
                        yV.append(funcs[i][idx])
        
        
        xAverage = np.average(xV)
        print("y values")
        yAverage = np.average(yV)
        print(xAverage)
        print(yAverage)
        plt.plot(xAverage, yAverage, 'ro', color='b')

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