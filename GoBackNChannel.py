import socket 
import sys
import traceback
from threading import Thread

def main():
    start_server()


def start_server(): 
    host = "127.0.0.1"
    port = 8888	# arbitrary non-privileged port

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)	# SO_REUSEADDR flag tells
    the kernel to reuse a local socket in TIME_WAIT state, without waiting for its natural timeout to expire
    print("Socket created")

    try:
        soc.bind((host, port))
    except:
        print("Bind failed. Error : " + str(sys.exc_info())) sys.exit()

    soc.listen(6)	# queue up to 6 requests

    print("Socket now listening")

    # infinite loop- do not reset for every requests while True:
    connection1, address1 = soc.accept()
    ip1, port1 = str(address1[0]), str(address1[1]) print("Sender is now connected with " + ip1 + ":" + port1)

    connection2, address2 = soc.accept()
    ip2, port2 = str(address2[0]), str(address2[1]) print("Receiver is now connected with " + ip2 + ":" + port2)

    print("Sender and Receiver now connected, can start transmission.")

    try:
        Thread(target=common_thread, args=(connection1, ip1, port1, connection2, ip2,
        port2)).start()
    except:
        print("Thread did not start.") traceback.print_exc()

    soc.close()

def common_thread(connection1, ip1, port1, connection2, ip2, port2, max_buffer_size = 5120):
    Thread(target=sender_send_thread, args=(connection1, ip1, port1, connection2, ip2, port2)).start()
    Thread(target=receiver_send_thread, args=(connection1, ip1, port1, connection2, ip2, port2)).start()


def sender_send_thread(connection1, ip1, port1, connection2, ip2, port2, max_buffer_size = 5120):
    while True:
        server_input = receive_input(connection1, max_buffer_size) server_input = server_input.decode("utf8")
        print("--------SENDER TO RECEIVER DATA TRANSFER--------\n")
        print("Received data from Sender(" + ip1 + ":" + port1 + ")") print("Data :\t" + str(server_input))
        random_error = int(input()) if(random_error==0):
        continue connection2.sendall(server_input.encode("utf8")) print("Send data to Receiver(" + ip2 + ":" + port2 + ")")
        print("------------------------------------------------\n\n")


def receiver_send_thread(connection1, ip1, port1, connection2, ip2, port2, max_buffer_size= 5120):
    while True:
        server_input = receive_input(connection2, max_buffer_size) server_input = server_input.decode("utf8")
        print("--------RECEIVER TO SENDER DATA TRANSFER--------\n")
        print("Received data from Receiver(" + ip2 + ":" + port2 + ")") print("Data :\t" + str(server_input))
        random_error = int(input()) if(random_error==0):
        continue connection1.sendall(server_input.encode("utf8")) print("Send data to Sender(" + ip1 + ":" + port1 + ")")
        print("------------------------------------------------\n\n")

def receive_input(connection, max_buffer_size): 
    client_input = connection.recv(max_buffer_size) client_input_size = sys.getsizeof(client_input)

    if client_input_size > max_buffer_size:
        print("The input size is greater than expected {}".format(client_input_size))

    decoded_input = client_input.decode("utf8").rstrip()	# decode and strip end of line result = process_input(decoded_input)

    return result

def process_input(input_str): return str(input_str).upper()

if __name__ == "__main__": main()
