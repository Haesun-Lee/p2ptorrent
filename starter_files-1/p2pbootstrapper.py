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
import time

class p2pbootstrapper:
    def __init__(self, ip='127.0.0.1', port=8888):
        ##############################################################################
        # TODO:  Initialize the socket object and bind it to the IP and port, refer  #
        #        https://docs.python.org/3/howto/sockets.html on how to do this.     #
        ##############################################################################
        self.boots_socket = None
        self.clients = None  # None for now, will get updates as clients register
        
        self.sock.connect((ip, port)) # bind to the IP and port
        
        # Append the log to this variable.
        self.log = []

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
        pass

    def client_thread(self):
        ##############################################################################
        # TODO:  This function should handle the incoming connection requests from   #
        #        clients. You are free to add more arguments to this function based  #
        #        on your need                                                        #
        #        HINT: After reading the input from the buffer, you can decide what  #
        #        action needs to be done. For example, if the client wants to        #
        #        deregister, call self.deregister_client                             #
        ##############################################################################
        pass

    def register_client(self, client_id, ip, port):  
        ########################################################################################
        # TODO:  Add client to self.clients, if already present, update status to 'registered  #
        ########################################################################################
        pass

    def deregister_client(self, client_id):
        ##############################################################################
        # TODO:  Update status of client to 'deregisterd'                            #
        ##############################################################################
        pass

    def return_clients(self):
        ##############################################################################
        # TODO:  Return self.clients                                                 #
        ##############################################################################
        
        return self.clients             ###### revised by hs
        pass

    def start(self):
        ##############################################################################
        # TODO:  Start timer for all clients so clients can start performing their   #
        #        actions                                                             #
        ##############################################################################
        pass

    def process_action_complete(self, msg):
        ##############################################################################
        # TODO:  Process the 'action complete' message from a client,update time if  #
        #        all clients are done, inform all clients about time increment       #
        ##############################################################################
        pass