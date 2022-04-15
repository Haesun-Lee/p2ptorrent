import imp
from p2pclient import p2pclient
import json
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='p2p bit torrent') 
    parser.add_argument('--file')
    args = parser.parse_args()
    #print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    #print(args.file)
    temp = args.file.split(".")
    client_id = temp[0]
    #print(client_id)
    content = None
    actions = None

    ##############################################################################
    # You need to perform the following tasks:                                   #  
    # 1) Instantiate the client                                                  #
    # 2) Client needs to pick its serveport,bind to it                           #
    # 3) Register with bootstrapper                                              #
    # 4) STart listening on the port picked in step 2                            #
    # 5) Start executing its actions                                             #
    ##############################################################################

    #########################################################################################
    # TODO:  Read the client_id, content and actions from <file>.json, which you can obtain #
    #        from command line arguments. and feed it into the constructor of               #
    #        the p2pclient below                                                            #
    #########################################################################################

    '''
    Original code
    client = p2pclient(client_id=client_id, content=content, actions=actions)
    '''
    temp_client_id = client_id
    #### Code added by HS ####
    Filename = str(client_id)
    Format = '.json'
    Filename = Filename + Format
    print("File name : " + Filename)
    with open(Filename) as f:
        client_id = json.load(f)

    content = client_id['content']
    actions = client_id['actions']
    client = p2pclient(client_id=client_id, content=content, actions=actions, temp = temp_client_id)
    #### Code added by HS ####
    
    ##############################################################################
    # Now provided you have completed the steps in the p2pclient constructor     #
    # properly, steps                                                            #                  
    # 1, 2 and 3 are completed when you instantiate the client object            #  
    # We are left with steps 4 and 5                                             #
    ##############################################################################

    ##############################################################################
    # TODO: For step 4: call clients.start_listening()                           #
    ##############################################################################

    ##############################################################################
    # For step 5: the bootstrapper will call the start() on this client, which  #
    # will make this client start taking its actions.                            #
    ##############################################################################