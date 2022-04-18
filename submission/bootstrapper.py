from p2pbootstrapper import p2pbootstrapper
import time
import threading
import argparse

if __name__ == "__main__":
    ##############################################################################
    # You need to perform the following tasks:                                   #  
    # 1) Instantiate the bootstrapper                                            #
    # 2) STart listening on the well-known port                                  #
    # 3) Wait for 10 sec so that all clients come up and register                #
    # 4) Call bootst.start() which inturn calls the start of all clients         #
    ##############################################################################
    
    '''
    Original code
    bootst = p2pbootstrapper()
    '''
    
    #### Code added by HS ####
    print("starting bootstrapper")
    bootst = p2pbootstrapper()
    listenThread = threading.Thread(target = bootst.start_listening, args = ())
    listenThread.start()
    time.sleep(10)
    bootst.start()
    #### Code added by HS ####
    
    ##############################################################################
    #  We know that listenign on a port is a blocking action, and the B.S        #
    #  cannot call start() once it starts listening. Threads to the rescue!     #
    #                                                                            #
    #  For step 2) create a thread to handle bootst.start_listening() method     #
    #  Now execute steps 3 and 4.                                                #
    ##############################################################################    
