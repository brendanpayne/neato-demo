print("Launching Neato Robot Controller")
import serial
import time

usb = '/dev/ttyACM0'			#User specified port (ACM0)
print("Using Serial Port: " + usb)	#Print to user which port is being used	
robot = serial.Serial(usb)		#Establishes connection via serial port
print("Serial Connection Established")	#Print to user confirmation of connection

def docommand(port, command):		#Sends encoded command to bot 		
    port.write((command + '\n').encode()) 

docommand(robot, 'testmode on')		#Turns on testmode (required to send commands)
print('TestMode Enabled')		#Prints to user confirmation

docommand(robot, 'playsound soundid 1')	#Plays sound for my enjoyment
time.sleep(0.5)				#0.5 second delay to not overload serial port

def print_menu():			#Prints menu to terminal
    print (30 * "-" , "MENU" , 30 * "-")
    print ("1. User Input Straight")
    print ("2. Right Box")
    print ("3. Left Box")
    print ("4. Right turn")
    print ("5. Left turn")
    print ("6. Build your own program")
    print ("7. Exit")
    print (67 * "-")
def print_menu_2():
    print (30 * "-" , "MENU" , 30 * "-")
    print ("1. Straight")
    print ("2. Reverse")
    print ("3. Right Turn")
    print ("4. Left Turn")
    print ("5. Right wheel only")
    print ("6. Left wheel only")
    print ("7. Exit")
    print (67 * "-")

def Straight(Dist,speed):		#Forward Function
    docommand(robot, "setmotor lwheeldist " + Dist + " rwheeldist " + Dist + " speed " + str(speed))

def Reverse(Dist,speed):		#Forward Function
    docommand(robot, "setmotor lwheeldist " + -Dist + " rwheeldist " + -Dist + " speed " + speed)
   
def Right_Turn():			#Right Turn Function
    docommand(robot, "setmotor lwheeldist 191 rwheeldist -191 speed 150")

def Left_Turn():			#Left Turn Function
    docommand(robot, "setmotor lwheeldist -191 rwheeldist 191 speed 150")

def Big_Right_Turn():			#Big Right Turn Function
    docommand(robot, "setmotor lwheeldist -500 rwheeldist 0 speed 200")

def Big_Left_Turn():			#Big Left Turn Function
    docommand(robot, "setmotor lwheeldist 0 rwheeldist -500 speed 200")
    
def Left_Wheel_Only(Dist):			#Left Wheel Only Function
    docommand(robot, "setmotor lwheeldist " + str(Dist) + " rwheeldist 0 speed 200")
    
def Right_Wheel_Only(Dist):			#Right Wheel Only Function
    docommand(robot, "setmotor lwheeldist 0 rwheeldist " + str(Dist) + " speed 200")

def Time_Delay(dist, speed):   #Predefined time constant
    if speed == 100:
        Delay = (dist / 91.65) + 0.4
        print(Delay)
        return Delay
    if speed == 150:
        Delay = (dist / 139.14) + 0.4
        print(Delay)
        return Delay
    if speed == 200:
        Delay = (dist / 176.70) + 0.4
        print(Delay)
        return Delay

def Speed_Check():
    switch = True
    while (switch == True):
        switch = False
        speed= input("Enter Speed: Slow (100), Medium (150), Fast(200)\n")       
        
        if speed == 'Slow' or speed == 'slow' or speed == '100':
        
            return 100
            
        elif speed == 'Medium' or speed == 'medium' or speed == '150':
        
            return 150
        
        elif speed == 'Fast' or speed == 'fast' or speed == '200':
        
            return 200
        else:
            print ("Enter Valid Selection.\n")
            switch = True
            
def QueueFunction():
    functionQ={
        'time':False,
        'distance':False,
        'speed':False,
        'function':""
    }
    switch=True
    while switch:
        switch=False
        print_menu_2()
        choice = input("Enter your choice [1-7]: ")
        if choice=='1':     		
            print("Straight has been selected")
            Dist= input("Enter your Distance for forward (mm): ")
            dist=int(Dist)#convert to int
            speed=Speed_Check()
            timeT=Time_Delay(dist,speed)
            #speed= input("Enter your Speed (1-250): ")
            #Straight(Dist,speed)
            switch=False
            functionQ['function']=Straight#stores beginning of function without function call
            functionQ['speed']=speed#stores the speed for use when calling function later
            functionQ['distance']=Dist#stores distance for calling function later
            functionQ['time']=timeT
            return(functionQ)
        elif choice=='2':
            print("Reverse has been selected")
            Dist= input("Enter your Distance for reverse (mm): ")
            dist=int(Dist)#convert to int
            #Dist=str(-dist)
            speed=Speed_Check()
            timeT=Time_Delay(dist,speed)
            #speed= input("Enter your Speed (1-250): ")
            #Straight(Dist,speed)
            switch=False
            functionQ['function']=Reverse#stores beginning of function without function call
            functionQ['speed']=speed#stores the speed for use when calling function later
            functionQ['distance']=Dist#stores distance for calling function later
            functionQ['time']=timeT
            return(functionQ)
        elif choice=='3':
            print ("Right turn has been selected")
            time.sleep(0.5)
            #Right_Turn()
            switch=False
            functionQ['function']=Right_Turn#stores beginning of function without function call
            functionQ['time']=3
            return(functionQ)
        elif choice=='4':
            print ("Left turn has been selected")
            time.sleep(0.5)
            #Left_Turn()
            switch=False
            functionQ['function']=Left_Turn#stores beginning of function without function call
            functionQ['time']=3
            return(functionQ)
        elif choice=='5':
            print ("Right wheel only has been selected")
            Dist= input("Enter your Distance for right wheel only (mm): ")
            dist=int(Dist)
            #Right_Wheel_Only(Dist)
            switch=False
            functionQ['function']=Right_Wheel_Only#stores beginning of function without function call
            functionQ['distance']=dist #stores the distance for use when calling the function
            functionQ['time']=3
            return(functionQ)

        elif choice=='6':
            print ("Menu 4 has been selected")
            Dist= input("Enter your Distance for left wheel only (mm): ")
            dist=int(Dist)
            #Left_Wheel_Only(Dist)
            switch=False
            functionQ['function']=Left_Wheel_Only#stores beginning of function without function call
            functionQ['distance']=dist#stores the distance for use when calling the function
            functionQ['time']=3
            return(functionQ)

        elif choice=='7':
            print ("List Compiled")
            return(False)
        else:
            input("Invalid input. Press enter to try again...")
            switch=True
 
def Main():
    pass
loop=True			     
while loop:				#Loop for user's input         
    print_menu()    
    choice = input("Enter your choice [1-7]: ")
    
    if choice=='1':     		
        print ("User Input Straight")
        Dist= input("Enter your Distance for straights (mm): ") 
        speed = Speed_Check()
        print(speed)
        dist = int(Dist)
        print(dist)
        Straight(Dist,speed)
        time.sleep(Time_Delay(dist, speed))
        
    elif choice=='2':
        print ("Right Box Selected")
        Dist= input("Enter your Distance for straights (mm): ") 
        speed = Speed_Check()
        Straight(Dist,speed)
        dist = int(Dist)
        time.sleep(Time_Delay(dist, speed))
        Right_Turn()
        time.sleep(3)
        Straight(Dist,speed)
        time.sleep(Time_Delay(dist, speed))
        Right_Turn
        time.sleep(3)
        Straight(Dist,speed)
        time.sleep(Time_Delay(dist, speed))
        Right_Turn
        time.sleep(3)
        Straight(Dist,speed)
        time.sleep(Time_Delay(dist, speed))
        Right_Turn

    elif choice=='3':
        print ("Left Box Selected")
        Dist= input("Enter your Distance for straights (mm): ") 
        speed = Speed_Check()
        Straight(Dist,speed)
        dist = int(Dist)
        time.sleep(Time_Delay(dist, speed))
        Left_Turn()
        time.sleep(3)
        Straight(Dist,speed)
        time.sleep(Time_Delay(dist, speed))
        Left_Turn
        time.sleep(3)
        Straight(Dist,speed)
        time.sleep(Time_Delay(dist, speed))
        Left_Turn
        time.sleep(3)
        Straight(Dist,speed)
        time.sleep(Time_Delay(dist, speed))
        Left_Turn
        
    elif choice=='4':
        print ("Right turn selected")
        time.sleep(0.5)
        Right_Turn()

    elif choice=='5':
        print ("Left turn selected")
        time.sleep(0.5)
        Left_Turn()
        
    elif choice=='6':
        off=False
        functionList=[]
        print("Build your own selected")
        while off==False:
            values=QueueFunction()
            print(values)
            if(values==False):
                off=True
            else:
                functionList.append(values)
        for i in range(len(functionList)):
            if(functionList[i]['speed']!=False and functionList[i]['distance']!=False):
                functionList[i]['function'](functionList[i]['distance'],functionList[i]['speed'])
            elif(functionList[i]['distance']!=False):
                functionList[i]['function'](functionList[i]['distance'])
            else:
                functionList[i]['function']()
            time.sleep(functionList[i]['time'])
            print("Went through once")

    elif choice=='6':
        print ("Program Terminated")
        loop=False
        
    else:
        input("Invalid input. Press enter to try again...")
        Main()

exit()

