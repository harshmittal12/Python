import socket 
import sys
from threading import Thread 
import time
import math

def main():
    #global Sf cansend = True Sn = 0
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) host = "127.0.0.1"
    port = 8999

    try:
        soc.connect((host, port))
    except:
        print("Connection error")
        sys.exit()

    data = str(input("Please provide the data:\t")) print("Frame size:\t4")
    if(len(data)%4!=0): print("Bitstuffing is required")

    data = '0'*(4-len(data)%4) + data print("New data:\t" + data )
    print("Value of m:\t" + '3') #Sw = pow(2,2)-1
    Sw = 3
    Sf = 0
    final_Sf = len(data)//4
    print("Number of frames to be send:\t" + str(final_Sf))

    Thread(target=sending, args=(soc,cansend,Sn,data,Sf,Sw,)).start() Thread(target=reading, args=(soc,data,)).start() Thread(target=timer, args=(soc,data,)).start()
    #if(Sf>final_Sf):
    #	print("Complete data send ....") #	quit()

def getMessage(Sn,data): message = str(int(Sn))
    message = message + data[(4*Sn):(4*(Sn+1))] print(data)
    print("Returning message:\t" + message) return message


def sending(soc,cansend_main,Sn_main,data,Sf_main,Sw_main): 
    global Sn
    global Sf 
    global Sw 
    global cansend 
    global timeout
    timeout = 0
    Sn = Sn_main Sw = Sw_main Sf = Sf_main
    cansend = cansend_main while True:
    if(Sf>=len(data)/4):
        print("Full data sent.......") # Sleep since full data sent #print("Waiting....")
    while(Sf>=len(data)/4): doNothing = True

    if(Sn-Sf>Sw):
        print("Sleeping......")	# Sleep till condition is not satisfied while(Sn-Sf>Sw):
        doNothing = True time.sleep(2) #sleep 10 seconds
    print("-----------SENDING DATA------------\n")
    message = getMessage(Sn,data) if(Sn>=len(data)/4):
    print("Waiting since full data sent .....") while(Sn>=len(data)/4):
    doNothing = True
    print("Sf:\t" + str(Sf) + "	Sn:\t" + str(Sn)) soc.sendall(message.encode("utf8"))
    print("Send data:\t" + message) if(timeout==0):
    timeout = time.time() + 30	# 20 seconds from now cansend = False
    Sn = Sn + 1
    print("------------------------------------\n")

def reading(soc,data): global Sn
    global Sf global Sw global cansend global timeout while True:
    server_input = soc.recv(5120)
    server_input = server_input.decode("utf8") print("-----PROCESSING RECEIVED DATA------\n")
    print("Received data:\t" + str(server_input)) server_input = int(server_input)
    if((server_input <= int(Sn))&(server_input > int(Sf))): print("SeqNo matched with AckNo") 
    while(int(Sf)<=server_input):
        Sf = Sf + 1
    timeout = 0 else:
    print("SeqNo not matched with AckNo !") if(Sf>=(len(data)/4)):
    message = '$'
    print("Sf:\t" + str(Sf) + "	Sn:\t" + str(Sn)) soc.sendall(message.encode("utf8"))
    print("Full data has been completely sent.") print("Exiting program")
    timeout = time.time() + 30000000 quit()
    print("------------------------------------\n")

def timer(soc,data): global Sn
    global Sf global Sw global cansend global timeout while(True):
    if((time.time() > timeout)&(timeout!=0)): timeout = time.time() + 30
    temp = Sf print("Timeout") while(temp < Sn):
    print("Sending data ... ") time.sleep(2) #sleep 10 seconds message = getMessage(Sf,data)
    print("Resending data:\t" + str(message)) print("Sf:\t" + str(Sf) + "	Sn:\t" + str(Sn)) soc.sendall(message.encode("utf8"))
    #Sf = Sf + 1
    temp += 1 if(Sf>=len(data)/4):
    break

if __name__ == "__main__": main()
