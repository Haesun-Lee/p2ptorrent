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

class p2pclient:
    def __init__(self, client_id, content, actions):
        
        ##############################################################################
        # TODO: Initialize the class variables with the arguments coming             #
        #       into the constructor                                                 #
        ##############################################################################

        self.client_id = client_id
        self.content = content
        self.actions = actions  # this list of actions that the client needs to execute

        self.content_originator_list = None  # None for now, it will be built eventually

        ##################################################################################
        # TODO:  You know that in a P2P architecture, each client acts as a client       #
        #        and the server. Now we need to setup the server socket of this client   #
        #        Initialize the the self.socket object on a random port, bind to the port#
        #        Refer to                                                                #
        #        https://docs.python.org/3/howto/sockets.html on how to do this.         #
        ##################################################################################
        
        self.socket = None

        ##############################################################################
        # TODO:  Register with the bootstrapper by calling the 'register' function   #
        #        Make sure you communicate to the B.S the serverport that this client#
        #        is running on to the bootstrapper.                                  #
        ##############################################################################

        
        ##############################################################################
        # TODO:  You can set status variable based on the status of the client:      #
        #        Registered: if registered to bootstrapper                           #
        #        Unregistered: unregistred from bootstrapper                         #
        #        Feel free to add more states if you need to                         #
        #        HINT: You may find enum datatype useful                             #
        ##############################################################################
        self.status = None

        # 'log' variable is used to record the series of events that happen on the client
        # Empty list for now, update as we take actions
        # See instructions above on how to append to log
        self.log = []

        # Timing variables:
        ###############################################################################################
        # TODO:  Ensure that you're doing actions according to time. B.S dictates time. Update this   #
        #        variable when BS sends a time increment signal                                       #
        ###############################################################################################
        self.time = 0


    def start_listening(self):
        ##############################################################################
        # TODO:  This function will make the client start listening on the randomly  #
        #        chosen server port. Refer to                                        #
        #        https://docs.python.org/3/howto/sockets.html on how to do this.     #
        #        You will need to link each connecting client to a new thread (using #
        #        client_thread function below) to handle the requested action.       #
        ##############################################################################
        pass

    def client_thread(self):
        ##############################################################################
        # TODO:  This function should handle the incoming connection requests from   #
        #        other clients.You are free to add more arguments to this function   #
        #        based your need                                                     #
        #        HINT: After reading the input from the buffer, you can decide what  #
        #        action needs to be done. For example, if the client is requesting   #
        #        list of known clients, you can return the output of self.return_list_of_known_clients #
        ##############################################################################
        pass

    def register(self, ip='127.0.0.1', port=8888):
        ##############################################################################
        # TODO:  Register with the bootstrapper. Make sure you communicate the server#
        #        port that this client is running on to the bootstrapper.            #
        #        Append an entry to self.log that registration is successful         #
        ##############################################################################
        pass

    def deregister(self, ip='127.0.0.1', port=8888):
        ##############################################################################
        # TODO:  Deregister/re-register with the bootstrapper                        #
        #        Append an entry to self.log that deregistration is successful       #
        ##############################################################################
        pass

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
        pass

    #TODO: clarify on logging
    def query_bootstrapper_all_clients(self):
        ##############################################################################
        # TODO:  Use the connection to ask the bootstrapper for the list of clients  #
        #        registered clients.                                                 #
        #        Append an entry to self.log                                         #
        ##############################################################################
        pass

    #TODO: clarify on logging
    def query_client_for_known_client(self, client_id):
        client_list = None
        ##############################################################################
        # TODO:  Connect to the client and get the list of clients it knows          #
        #        Append an entry to self.log                                         #
        ##############################################################################
        return client_list

    def return_list_of_known_clients(self):
        ##############################################################################
        # TODO:  Return the list of clients known to you                             #
        #        HINT: You can make a set of <client_id, IP, Port> from self.content_originator_list #
        #        and return it.                                                      #
        ##############################################################################
        pass

    def query_client_for_content_list(self, client_id):
        content_list = None
        ##############################################################################
        # TODO:  Connect to the client and get the list of content it has            #
        #        Append an entry to self.log                                         #
        ##############################################################################
        return content_list


    def return_content_list(self):
        ##############################################################################
        # TODO:  Return the content list that you have (self.content)                #
        ##############################################################################
        pass

    def request_content(self, content_id):
        #####################################################################################################
        # TODO:  Your task is to obtain the content and append it to the                                    #
        #        self.content list.  To do this:                                                            #
        #        Get the content as per the instructions in the pdf. You can use the above query_*          #
        #        methods to help you in fetching the content.                                               #
        #        Make sure that when you are querying different clients for the content you want, you record#
        #        their responses(hints, if present) appropriately in the self.content_originator_list       #
        #        Append an entry to self.log that content is obtained                                       #
        #####################################################################################################
        pass

    def purge_content(self, content_id):
        #####################################################################################################
        # TODO:  Delete the content from your content list                                                  #
        #        Append an entry to self.log that content is purged                                         #
        #####################################################################################################
        pass
