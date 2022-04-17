"""
Follow the instructions in each method and complete the tasks. We have given most of the house-keeping variables
that you might require, feel free to add more if needed. Hints are provided in some places about what data types 
can be used, others are left to students' discretion, make sure that what you are returning from one method gets correctly
interpreted on the other end. Most functions ask you to create a log, this is important
as this is what the auto-grader will be looking for.
Follow the logging instructions carefully.
"""

"""
Appending to log: every time you have to add a log entry, create a new dictionary and append it to self.log. The dictionary formats for diff. cases are given below
Registraion: (R)
{
    "time": <time>,
    "text": "Client ID <client_id> registered"
}
Unregister: (U)
{
    "time": <time>,
    "text": "Unregistered"
}
Fetch content: (Q)
{
    "time": <time>,
    "text": "Obtained <content_id> from <IP>#<Port>
}
Purge: (P)
{
    "time": <time>,
    "text": "Removed <content_id>"
}
Obtain list of clients known to a client: (O)
{
    "time": <time>,
    "text": "Client <client_id>: <<client_id>, <IP>, <Port>>, <<client_id>, <IP>, <Port>>, ..., <<client_id>, <IP>, <Port>>"
}
Obtain list of content with a client: (M)
{
    "time": <time>,
    "text": "Client <client_id>: <content_id>, <content_id>, ..., <content_id>"
}
Obtain list of clients from Bootstrapper: (L)
{
    "time": <time>,
    "text": "Bootstrapper: <<client_id>, <IP>, <Port>>, <<client_id>, <IP>, <Port>>, ..., <<client_id>, <IP>, <Port>>"
}
"""
import socket
import time
import json
from enum import Enum
import random
import pickle
import threading
import struct 

PORTNUMBER = 8823

 #### Code added by HS ####
class Status(Enum):
            INITIAL = 0
            REGISTERED = 1
            UNREGISTERED = 2
 #### Code added by HS ####

class p2pclient:
    def __init__(self, client_id, content, actions, temp):
        
        ##############################################################################
        # TODO: Initialize the class variables with the arguments coming             #
        #       into the constructor                                                 #
        ##############################################################################

        '''
        original code
        self.client_id = None
        self.content = None
        self.actions = None  # this list of actions that the client needs to execute
        self.content_originator_list = None  # None for now, it will be built eventually
        '''
        
        #### Code added by HS ####
        self.client_id = temp
        self.content = content
        self.actions = actions  # this list of actions that the client needs to execute
        self.log = []
        self.content_originator_list = None  # This needs to be kept None here, it will be built eventually
        self.content_originator_list = {}

        #### Code added by HS ####
        
        ##################################################################################
        # TODO:  You know that in a P2P architecture, each client acts as a client       #
        #        and the server. Now we need to setup the server socket of this client   #
        #        Initialize the the self.socket object on a random port, bind to the port#
        #        Refer to                                                                #
        #        https://docs.python.org/3/howto/sockets.html on how to do this.         #
        ##################################################################################
        '''   
        original code
        self.socket = None
        '''
        #### Code added by HS ####
        time.sleep(0.5)
        print("starting p2p client initialization")
        self.p2pclientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        random.seed(int(temp))
        #random.seed(1)
        self.port = random.randint(9000, 9999)
        self.p2pclientsocket.bind(('127.0.0.1', self.port))
        print("client is connected to bs")
        #### Code added by HS ####
        
        
        ##############################################################################
        # TODO:  Register with the bootstrapper by calling the 'register' function   #
        #        Make sure you communicate to the B.S the serverport that this client#
        #        is running on to the bootstrapper.                                  #
        ##############################################################################

        #### Code added by HS ####
        self.status = Status.INITIAL
        self.register(0)
        self.status = Status.REGISTERED
        #### Code added by HS ####
        
        
        
        ##############################################################################
        # TODO:  You can set status variable based on the status of the client:      #
        #        Registered: if registered to bootstrapper                           #
        #        Unregistered: unregistred from bootstrapper                         #
        #        Feel free to add more states if you need to                         #
        #        HINT: You may find enum datatype useful                             #
        ##############################################################################
        
        '''
        original code
        self.status = None
        '''    
        # 'log' variable is used to record the series of events that happen on the client
        # Empty list for now, update as we take actions
        # See instructions above on how to append to log
        '''
        original code
        self.log = []
        '''
        #### Code added by HS ####
        #self.log = []
        #### Code added by HS ####
        
        # Timing variables:
        ###############################################################################################
        # TODO:  Ensure that you're doing actions according to time. B.S dictates time. Update this   #
        #        variable when BS sends a time increment signal                                       #
        ###############################################################################################
        '''
        original code
        self.time = 0
        '''

    def start_listening(self):
        ##############################################################################
        # TODO:  This function will make the client start listening on the randomly  #
        #        chosen server port. Refer to                                        #
        #        https://docs.python.org/3/howto/sockets.html on how to do this.     #
        #        You will need to link each connecting client to a new thread (using #
        #        client_thread function below) to handle the requested action.       #
        ##############################################################################
        
        #### Code added by HS ####
        self.p2pclientsocket.listen()
        while True:
            (clientsocket, (ip, port)) = self.p2pclientsocket.accept()  # accept connections from outside
            clientThread = threading.Thread(target = self.client_thread, args = (clientsocket, ip, port))
            clientThread.start()
        #### Code added by HS ####
        

    def client_thread(self, clientsocket, ip, port):
        ##############################################################################
        # TODO:  This function should handle the incoming connection requests from   #
        #        other clients.You are free to add more arguments to this function   #
        #        based your need                                                     #
        #        HINT: After reading the input from the buffer, you can decide what  #
        #        action needs to be done. For example, if the client is requesting   #
        #        list of known clients, you can return the output of self.return_list_of_known_clients #
        ##############################################################################
        print("******************** starting client_thread **********************")
        #### Code added by HS ####
        while True:
            data = clientsocket.recv(1024).decode()
            #print(data)
            data = data.replace('"', '')
            if data:
                print("p2pclient_thread data: " +data)
                data_arr = data.split(" ")
                data = data_arr[1]
                ip = data_arr[2]
                port = data_arr[3]
                
                if data == 'START':
                    self.start()
                
                if data == 'knownClientsQuery' :
                    client_list = self.return_list_of_known_clients() 
                    toSend = json.dumps(client_list)
                    clientsocket.send(toSend.encode())
                
                elif data == 'contentList' :
                    content_list = self.return_content_list()
                    toSend = json.dumps(content_list)
                    #print("content list : "+ str(self.client_id) +" " +toSend)
                    clientsocket.send(toSend.encode())
                    
        #### Code added by HS ####
        
    def register(self, curr_time, ip='127.0.0.1', port=PORTNUMBER):
        ##############################################################################
        # TODO:  Register with the bootstrapper. Make sure you communicate the server#
        #        port that this client is running on to the bootstrapper.            #
        #        Append an entry to self.log that registration is successful         #
        ##############################################################################
        print("register******************")
        #### Code added by HS ####
        bootstrapperSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        bootstrapperSocket.connect((ip, port))
        #print("what"+ip)
        
        toSend = str(str(self.client_id) + ' register '+ str(ip) +' '+str(self.port))
        print(toSend)
        bootstrapperSocket.send(toSend.encode())
        bootstrapperSocket.close()
        
        if curr_time == 0:
            register_dict = {}          # make register dictionary
            register_dict["time"] = curr_time
            register_dict["text"] = str("Client ID " +str(self.client_id)+" registered")
            self.log.append(register_dict)
            print(self.log)
        #### Code added by HS ####
        

    def deregister(self, curr_time, ip='127.0.0.1', port=PORTNUMBER):
        ##############################################################################
        # TODO:  Deregister/re-register with the bootstrapper                        #
        #        Append an entry to self.log that deregistration is successful       #
        ##############################################################################
        
        #### Code added by HS ####
        bootstrapperSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        bootstrapperSocket.connect((ip, port))
        toSend = str(str(self.client_id) + ' deregister '+ str(ip) +' '+str(self.port))
        bootstrapperSocket.send(toSend.encode())
        bootstrapperSocket.close()
        
        # should I also put if curr_time != 0 :
        deregister_dict = {}            # make deregister dictionary
        deregister_dict["time"] = curr_time
        deregister_dict["text"] = "Unregistered"
        self.log.append(deregister_dict)
        #### Code added by HS ####

    def start(self):
        ##############################################################################
        # TODO:  When the Bootstrapper sends a start signal, the client starts       #
        #        executing its actions. Once this is called, you have to             #
        #        start reading the items in self.actions and start performing them   #
        #        sequentially, at the time they have been scheduled for, and as timed#
        #        by B.S. Once you complete an action, let the B.S know and wait for  #
        #        B.S's signal before continuing to next action                       #
        ##############################################################################

        ##############################################################################
        # TODO:  ***IMPORTANT***                                                     #
        # At the end of your actions, “export” self.log to a file: client_x.json,    #
        # this is what the autograder is looking for. Python’s json package should   #
        # come handy.                                                                #
        ##############################################################################
        
        #### Code added by HS ####
        
        start = time.time()
        action_num = 0
        while action_num < len(self.actions):
            while_start = time.time()
            curr_time = self.actions[action_num]["time"]
            
            print("CLIENT "+ str(self.client_id)+" ACTION NUM: "+str(action_num) + " CODE: " + self.actions[action_num]["code"]+ " CURR TIME " + str(curr_time))
            
            code = self.actions[action_num]["code"]
            
            if code == "R":     # Register itself with the p2ptracker. send clientID.
                self.register(curr_time)
            
            elif code == "U":   # Unregister itself from the p2ptracker.
                self.deregister(curr_time)
            
            elif code == "L":   # Obtain a list of all clients from bootstrapper. Get clientID, IP, and Port
                self.query_bootstrapper_all_clients(curr_time)
            
            elif code == "Q":   # Request a data object.
                self.request_content(self.actions[action_num]["content_id"], curr_time)
            
            elif code == "P":   # Purge(remove) data object from bootstrapper(but retain it in the COL).
                self.purge_content(self.actions[action_num]["content_id"], curr_time)    
            
            elif code == "O":   # Obtain a list of all other clients known to a particular client(ClientID) .
                self.query_client_for_known_client(self.actions[action_num]["client_id"], curr_time)
            
            elif code == "M":   # obtain a list of all data object hashes from a particular client. 
                self.query_client_for_content_list(self.actions[action_num]["client_id"], curr_time)

            
            action_num += 1
            while_end = time.time()
            time.sleep(1.5 - (while_end-while_start))
                
        string = "client_" + str(self.client_id) + ".json"
        outfile = open(string, "w")
        json.dump(self.log, outfile)
        outfile.close()
        
        #### Code added by HS ####
        

    #TODO: clarify on logging
    def query_bootstrapper_all_clients(self,curr_time, log = True, ip='127.0.0.1', port=PORTNUMBER):
        ##############################################################################
        # TODO:  Use the connection to ask the bootstrapper for the list of clients  #
        #        registered clients.                                                 #
        #        Append an entry to self.log                                         #
        ##############################################################################
        
        #### Code added by HS ####
        
        while self.status == Status.INITIAL:
            pass
        
        bootstrapperSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        bootstrapperSocket.connect((ip, port))
        toSend = str(str(self.client_id) + ' sendList '+ '127.0.0.1' +' '+str(self.port))
        print("******************** bootstrapper query to send ***********************")
        print(toSend)
        bootstrapperSocket.send(toSend.encode())
        data = bootstrapperSocket.recv(1048).decode()
        bootstrapperSocket.close()
        
        clientDataToList = json.loads(data)
        newData = data.replace('[','<').replace(']','>').replace('\"','')
        newestData = newData[1:len(newData)-1]
        
        if log:
            q_dict = {}
            q_dict['time'] = curr_time
            q_dict['text'] = "Bootstrapper: "+newestData
            self.log.append(q_dict)
        return clientDataToList
        
        #### Code added by HS ####
        

    #TODO: clarify on logging
    def query_client_for_known_client(self, client_id, curr_time, log = True, ip='127.0.0.1', port=PORTNUMBER):
        '''
        original code
        client_list = None
        return client_list
        '''
        ##############################################################################
        # TODO:  Connect to the client and get the list of clients it knows          #
        #        Append an entry to self.log                                         #
        ##############################################################################
        
        #### Code added by HS ####
        
        correctClient = []
        bootstrapperClients = self.query_bootstrapper_all_clients(curr_time, log=False)
        count = 0
        for client in bootstrapperClients:
            if client[0] == client_id:
                correctClient = client
                break
            count += 1

        while self.status == Status.INITIAL:
            pass
        
        if len(correctClient) > 0:
            otherClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            otherClientSocket.connect((correctClient[1], int(correctClient[2])))
            toSend = str(str(self.client_id) + ' knownClientsQuery '+ '127.0.0.1' +' '+str(self.port))
            print("********************known client query to send ***********************")
            print(toSend)
            otherClientSocket.send(toSend.encode())
            data = otherClientSocket.recv(1048).decode()
            otherClientSocket.close()
            
            clientDataToList = json.loads(data)
            newData = data.replace('[','<').replace(']','>').replace('\"','')
            newestData = newData[1:len(newData)-1]
            
            if log:
                q_dict = {}
                q_dict['time'] = curr_time
                q_dict['text'] = "Client " + str(client_id) + ": " + newestData
                print("query_client_for_known_client log: "+ "time " + str(curr_time) + " Client " + str(client_id) + ": " + data)
                self.log.append(q_dict)
        
        return clientDataToList

        #### Code added by HS ####
    

    def return_list_of_known_clients(self):
        ##############################################################################
        # TODO:  Return the list of clients known to you                             #
        #        HINT: You can make a set of <client_id, IP, Port> from self.content_originator_list #
        #        and return it.                                                      #
        ##############################################################################
        
        #### Code added by HS ####
        returnClients = set()
        for content in self.content_originator_list:
            if self.client_id != int(self.content_originator_list[content][0]):
                returnClients.add((self.content_originator_list[content][0], self.content_originator_list[content][1], self.content_originator_list[content][2]))
        
        returnClients = [list(i) for i in returnClients]
        returnClients = sorted(returnClients, reverse=True)
        
        if self.client_id == 1:
            return [self.client_id, '127.0.0.1', self.port]
        
        return [list(i) for i in returnClients]
        
        #### Code added by HS ####

    def query_client_for_content_list(self, client_id, curr_time, log = True):
        '''
        original code
        content_list = None
        return content_list
        '''
        ##############################################################################
        # TODO:  Connect to the client and get the list of content it has            #
        #        Append an entry to self.log                                         #
        ##############################################################################
        
        #### Code added by HS ####
        
        correctClient = []
        if log:
            print("query_client_for_content_list called from client_thread")
        bootstrapperClients = self.query_bootstrapper_all_clients(curr_time, log=False)
        count = 0
        for client in bootstrapperClients:
            if client[0] == client_id:
                #print("client: "+str(self.client_id)+ " found correct client at: "+ str(count) + " " +str(client[0]) + " " + client[1] + " " + str(client[2]))
                correctClient = client
                break
            count += 1

        while self.status == Status.INITIAL:
            pass
        if len(correctClient) > 0:
            otherClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            otherClientSocket.connect((correctClient[1], int(correctClient[2])))
            toSend = str(str(self.client_id) + ' contentList '+ '127.0.0.1' +' '+str(self.port))
            print("******************** client for content list query to send ***********************")
            print(toSend)
            otherClientSocket.send(toSend.encode())
            data = otherClientSocket.recv(1048).decode()
            otherClientSocket.close()
            print("content list from client: "+str(client_id)+ " "+data)
            
            clientDataToList = json.loads(data)
            newData = data.replace('[','<').replace(']','>').replace('\"','')
            newestData = newData[1:len(newData)-1]
            
            if log:
                q_dict = {}
                q_dict['time'] = curr_time
                q_dict['text'] = "Client " + str(client_id) + ": " + newestData
                self.log.append(q_dict)
                print("end of logging")
            return clientDataToList
        
        #### Code added by HS ####


    def return_content_list(self):
        ##############################################################################
        # TODO:  Return the content list that you have (self.content)                #
        ##############################################################################
        
        #### Code added by HS ####
        return self.content.copy()
        #### Code added by HS ####

    def request_content(self, content_id, curr_time):
        #####################################################################################################
        # TODO:  Your task is to obtain the content and append it to the                                    #
        #        self.content list.  To do this:                                                            #
        #        Get the content as per the instructions in the pdf. You can use the above query_*          #
        #        methods to help you in fetching the content.                                               #
        #        Make sure that when you are querying different clients for the content you want, you record#
        #        their responses(hints, if present) appropriately in the self.content_originator_list       #
        #        Append an entry to self.log that content is obtained                                       #
        #####################################################################################################
        
        #### Code added by HS ####
        correctContentClient = ["1","IP","Port"]
        bootstrapperClients = self.query_bootstrapper_all_clients(curr_time, log=False)
        client_index = 0
        hint = 0
        found = False
        loop_count = 0   
        list_of_ids = [i[0] for i in bootstrapperClients]
        print("list of ids "+json.dumps(list_of_ids))
        while not found and client_index < len(bootstrapperClients) and loop_count < 10:
            print("Client index "+str(client_index) + " " + str(len(bootstrapperClients)))
            client = bootstrapperClients[client_index]
            print("Client: "+str(self.client_id)+" Looking at client: "+str(client[0]))
            
            if client[0] != self.client_id:
                contentList = self.query_client_for_content_list(client[0],curr_time, log=False)
                
                if not contentList:
                    print("content list is empty "+str(client[0]))
                    break
                
                in_content_list = False
                in_col = None
                
                for content in contentList:
                    print("##########################")
                    #print(client[0])
                    #print(client[1])
                    #print(client[2])
                    self.content_originator_list[content] = [client[0], client[1], client[2]]    
                    if content == content_id:
                        print("found content in "+str(client[0]))
                        correctContentClient = [client[0], client[1], client[2]]
                        found = True
                        in_content_list = True
                        break
                
                if not in_content_list:
                    if content_id in self.content_originator_list:
                        in_col = self.content_originator_list[content_id]
                        hint = in_col[0]
                        print("found hint at client_id "+str(hint))
                        client_index = list_of_ids.index(hint)
                    
                    else:
                        client_index += 1
            
            else:
                client_index += 1
            loop_count += 1


        content_copy = self.content.copy()
        content_copy.append(content_id)
        self.content = content_copy
        print("just added new content to client_id: "+str(self.client_id)+ " " + json.dumps(self.content))
        
        q_dict = {}
        q_dict["time"] = curr_time
        #q_dict["text"] = str("Obtained "+str(content_id)+" from " + correctContentClient[1] + "#" + correctContentClient[2])
        q_dict["text"] = str("Obtained "+str(content_id)+" from " + '127.0.0.1' + "#" + str(client[2]))
        
        self.log.append(q_dict)
       
        #### Code added by HS ####

    def purge_content(self, content_id, curr_time):
        #####################################################################################################
        # TODO:  Delete the content from your content list                                                  #
        #        Append an entry to self.log that content is purged                                         #
        #####################################################################################################
        
        #### Code added by HS ####
        
        self.content.remove(content_id)
        purge_dict = {}
        purge_dict["time"] = curr_time
        purge_dict["text"] = str("Removed "+str(content_id))
        self.log.append(purge_dict)
        
        #### Code added by HS ####
