import json
import datetime

#Function to load clients from the json file
def load_clients():
    #open file in read mode, by default its in read mode.
    with open("clients.json") as file:  # with open then we do not need to close it , otherwise if we use open then we need to close it.
        #load JSON data from the file into this data variable
        data = json.load(file)
    return data["clients"]    

# function save clients to the json file
def save_clients(clients):
    # open the file in write mode
    with open("clients.json","w") as file:
        # dump (write) the clients to the json file
        json.dump({"clients": clients},file, indent=4) #  if you want to format your json file to be displayed in nice way you can add indent=4 in the json.dump so it won't be single line 

def get_age(dob):
    #convert the dob from string to datetime object
    date_of_birth = datetime.datetime.strptime(dob,"%Y-%m-%d")
    #get current date
    today = datetime.datetime.today()
    #calculation
    age = today.year - date_of_birth.year
    return age

def add_client(clients,name,dob,balance):
    # determing id of the last client
    client_id = clients[-1]["client_id"] + 1
    # adding new client
    clients.append({
        "client_id":client_id,
        "name":name,
        "dob":dob,
        "balance":balance
        
    })
    #saving updated clients list to JSON file
    save_clients(clients)

def update_client(clients, client_id, name=None, dob=None, balance=None):
    if not check_user(clients, client_id):
        print("Customer does not exist. ")
    # loop though the client list
    else:
        # loop through client list
        for client in clients:
            #select client by id
            if client["client_id"] == client_id:
                # if name is provided, update clients name
                if name:
                    client["name"] == name
                # if dob is provided, update clients dob    
                if dob:
                    client["dob"] == dob
                # if balance is provided, update clients balance
                if balance:
                    client["balance"] == balance 
                break

    # save updated clients list to JSON file
    save_clients(clients)               
    
def delete_client(clients, client_id):
    if not check_user(clients, client_id):
        print("Customer does not exist. ")
    # loop though the client list
    else:
        # loop through client list
        for client in clients:
            #select client by id
            if client["client_id"] == client_id:
                # delete client
                clients.remove(client)
                # end loop to avoid ugnnecessary loopin
                break
       
    # save updated client list to JSON    
    save_clients(clients)

def display_client(clients, client_id):
    if not check_user(clients, client_id):
        print("Customer does not exist. ")
    # loop though the client list
    else:
        for client in clients:
            #if client["client_id"] != client_id or client["client_id"] is None:
            
            #select client by client_id
            if client["client_id"] == client_id:
            # print the client information
                print(f"\nClient Id {client['client_id']}")
                print(f"Client Name {client['name']}")
                print(f"Client DOB {client['dob']}")
                print(f"Client Age {get_age(client['dob'])}")
                print(f"Client Balance {client['balance']}")
    
def display_total(clients):
    #calculate the total balance by adding up the balance of each client
    total = sum(client["balance"] for client in clients)
    # print the total balance
    print("Total bank balance :", total)

def make_trasfer(clients, client_id1, client_id2, amount):
    # created client1 and client2 dictionary and set set the default value as None.
    client1 = None
    client2 = None
    # loop through client list
    for client in clients:
        # select client by client_id
        if client["client_id"] == client_id1:
            # if valid client id then store the client dictionay data in client1
            client1 = client
            # select client by another client_id
        elif client["client_id"] == client_id2:
            # if valid client id then store the client dictionay data in client2
            client2 = client

    # if client dictionary are empty then it's invalid customer
    if client1 is None or client2 is None:
        print("Invalid Customer. ")
        #if amount is more than the balance of the transferee, then it's a insufficient funds
    elif client1["balance"] < amount:
        print("Insufficient Funds to transfer")
        # if valid clients and balance is also sufficient then amount is deducted from one client and added to another client
    else:
        client1["balance"] -= amount
        client2["balance"] += amount
        print(f"Transfer {amount}€ amount successfully. ")

    #saving the client information
    save_clients(clients)    

def make_vip(clients):
    # loop through the client list
    for client in clients:
        if float(client["balance"]) > 10000.0:
            client["vip"] = True
 
        else:
            client["vip"] = False    

    #saving the client information
    save_clients(clients) 

def check_user(clients, client_id):
    test_value = False
    for client in clients:
        if client["client_id"] == client_id:
            test_value = True
            break            
    return test_value        






#print(get_age("1996-03-25"))

#clients = load_clients()
#add_client(clients,"Igor","1980-04-01",14)