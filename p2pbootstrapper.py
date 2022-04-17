"""
Follow the instructions in each method and complete the tasks. We have given most of the house-keeping variables
that you might require, feel free to add more if needed. Hints are provided in some places about what data types 
can be used, others are left to user discretion, make sure that what you are returning from one method gets correctly
interpreted on the other end. 
At end of each timestep, after all clients have completed their actions, log the registered clients in the format below
{
    "time": <time>,
    "text": "Clients registered: <<client_id>, <IP>, <Port>>, <<client_id>, <IP>, <Port>>, ..., <<client_id>, <IP>, <Port>>"
}
"""
import socket
import threading
import sys
import pickle
import json
import random

PORTNUMBER = 8823

class p2pbootstrapper:
    def __init__(self, ip='127.0.0.1', port=PORTNUMBER):
        ##############################################################################
        # TODO:  Initialize the socket object and bind it to the IP and port, refer  #
        #        https://docs.python.org/3/howto/sockets.html on how to do this.     #
        ##############################################################################
        '''
        self.boots_socket = None
        self.clients = None  # None for now, will get updates as clients register
        self.log = []       # Append the log to this variable.
        '''
        
        #### Code added by HS ####
        self.boots_socket = None
        self.clients = []  # None for now, will get updates as clients register
        self.mutex = threading.Lock()        
        self.boots_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.boots_socket.bind((ip, port))
        #### Code added by HS ####

        # Timing variables:
        ###############################################################################################
        # TODO:  To track the time for all clients, self.time starts at 0, when all clients register  #
        #        self.MAX_CLIENTS is the number of clients we will be spinnign up. You can use this   #
        #        to keep track of how many 'complete' messages to get before incrementing time.       #
        #        CHange this when testing locally                                                     #
        ###############################################################################################
        self.time = 0
        self.MAX_CLIENTS = 20

    def start_listening(self):
        ##############################################################################
        # TODO:  This function will make the BS start listening on the port 8888     #
        #        Refer to                                                            #
        #        https://docs.python.org/3/howto/sockets.html on how to do this.     #
        #        You will need to link each connecting client to a new thread (using #
        #        client_thread function below) to handle the requested action.       #
        ##############################################################################
        
        #### Code added by HS ####
        print("******************* p2pbootstrapper start_listening ********************")
        self.boots_socket.listen(20)     # how many client should I be listening?
        while True:
            (clientsocket, (ip, port)) = self.boots_socket.accept()
            clientThread = threading.Thread(target = self.client_thread, args = (clientsocket, ip, port))
            clientThread.start()
        
        #### Code added by HS ####
        

    def client_thread(self, clientsocket, ip, port):
        ##############################################################################
        # TODO:  This function should handle the incoming connection requests from   #
        #        clients. You are free to add more arguments to this function based  #
        #        on your need                                                        #
        #        HINT: After reading the input from the buffer, you can decide what  #
        #        action needs to be done. For example, if the client wants to        #
        #        deregister, call self.deregister_client                             #
        ##############################################################################
        
        #### Code added by HS ####
        while True :
            #print("#################################")
            data = clientsocket.recv(1024).decode()
            print(data)
            #print("################################# data : " +data)
            data = data.replace('"', '')
            #print("################################# after data : " +data)
            if data:
                data_arr = data.split(" ")
                client_id = data_arr[0]
                data = data_arr[1]
                ip = data_arr[2]
                port = data_arr[3]
                
                if data == 'deregister' :
                    self.deregister_client(client_id)
                
                elif data == 'register' :
                    self.register_client(client_id, ip, port, clientsocket)
                
                elif data == 'sendList':
                    client_list = self.return_clients()
                    sorted_list = sorted(client_list, key=lambda x: x[0]) 
                    toSend = json.dumps(sorted_list)
                    clientsocket.send(toSend.encode())
        #### Code added by HS ####

        

    def register_client(self, client_id, ip, port, clientsocket):  
        ########################################################################################
        # TODO:  Add client to self.clients, if already present, update status to 'registered  #
        ########################################################################################
        
        #### Code added by HS ####
        self.mutex.acquire()
        self.clients.append((client_id, ip, port))
        self.mutex.release()
        
        print("boostrapper clients register "+client_id)
        print("     "+json.dumps(self.clients))
        #### Code added by HS ####
        
    def deregister_client(self, client_id):
        ##############################################################################
        # TODO:  Update status of client to 'deregisterd'                            #
        ##############################################################################
        pass

    def return_clients(self):
        ##############################################################################
        # TODO:  Return self.clients                                                 #
        ##############################################################################
        
        #### Code added by HS ####
        clients_copy = self.clients.copy()
        return clients_copy
        #### Code added by HS ####

    def start(self):
        ##############################################################################
        # TODO:  Start timer for all clients so clients can start performing their   #
        #        actions                                                             #
        ##############################################################################
        
        #### Code added by HS ####
        for client in self.clients:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((client[1], int(client[2])))

            toSend = str(str(0) + ' START '+ '127.0.0.1' +' '+str(PORTNUMBER))
            client_socket.send(toSend.encode())
            client_socket.close()
        #### Code added by HS ####

    def process_action_complete(self, msg):
        ##############################################################################
        # TODO:  Process the 'action complete' message from a client,update time if  #
        #        all clients are done, inform all clients about time increment       #
        ##############################################################################
        pass
