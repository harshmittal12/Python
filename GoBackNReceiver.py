import socket
import sys 
import time

def main():
    global Rn Rn = 0
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) host = "127.0.0.1"
    port = 8999 data = ''

    try:
        soc.connect((host, port))
    except:
        print("Connection error") sys.exit()

    while True:
        server_input = soc.recv(5120)
        server_input = server_input.decode("utf8") print("-----PROCESSING RECEIVED DATA------\n")
        print("Received data:\t" + str(server_input)) if(str(server_input[0])=='$'):
        print("Full data received. Quiting .....") quit()
        return
        matching_input = int(server_input[0]) 
        if(matching_input == int(Rn)):
            data += str(server_input[1:]) print("SeqNo matched with AckNo")
            print("Data accepted:\t" + server_input[1:len(server_input)])
            Rn = Rn + 1
            message = str(int(Rn)) time.sleep(1) soc.sendall(message.encode("utf8"))
            print("Sending Acknowledgement data:\t" + message	) print("Current received data:\t" + data)
        else:
            print("SeqNo not matched with AckNo !") print("Required AckNo :\t" + str(Rn)) print("Current received data:\t" + data)
        print("------------------------------------\n")


if __name__ == "__main__": main()
