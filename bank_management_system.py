import json 
from stringcolor import cs
import time

#function to load the clients from the json file
def load_clients():
    with open('clients.json') as f:
        data = json.load(f)#we are converting the data from json => dict
    return data['clients']

#function to save the clients to the json file
def save_client(clients):
    with open('clients.json','w') as file:#w is write mode
        json.dump({"clients":clients},file,indent=4)

#function to add a new client
def add_client(clients,client_name,client_dob,client_balance):
    if clients == []:
        client_id = 1
    else :
        client_id = clients[-1]['client id']+1
    clients.append({
        "client id":client_id,
        "client name":client_name,
        "client dob":client_dob,
        "balance":client_balance})
    save_client(clients)

#function to get a specific client
def get_client(clients,client_id):
    for client in clients:
        if client['client id'] == client_id:
            return client

#function to update the client details
def update_client(clients,client_id,client_name=None,client_dob=None,client_balance=None):
    client = get_client(clients,client_id)
    if client_name:
        client['client name'] = client_name
    if client_dob :
        client['client dob'] =client_dob
    if client_balance:
        client['balance'] = client_balance               
    save_client(clients)

#function to delete a client
def delete_client(clients,client_id):
    client = get_client(clients,client_id)
    clients.remove(client)
    save_client(clients)

#function to display a client
def display_client(clients,client_id):
    client = get_client(clients,client_id)
    print(cs(f"Client name {client['client name']}",'blue'))
    print(cs(f"Client dob {client['client dob']}",'green'))
    print(cs(f"Client balance {client['balance']}",'orchid'))

#function to display all clients
def clients_overview(clients):
    for client in clients:
        print(cs(f"Client id {client['client id']}",'red'))
        print(cs(f"Client name {client['client name']}",'blue'))
        print(cs(f"Client dob {client['client dob']}",'green'))
        print(cs(f"Client balance {client['balance']}",'orchid'))
        print(cs('-'*50,'yellow'))
        time.sleep(1.5)

#function to get the total balance
def get_total_balance(clients):
    total = sum([client['balance'] for client in clients])
    return total

#function to get the balance of a specific client
def get_balance(clients, id):
    client = get_client(clients, id)
    print("The current balance of the client {} is €:{}".format(client['client name'], client['balance']))
    return client['balance']

#function to deposit money to a specific client
def deposit_money(Clients, id, amount):
    balance = get_balance(Clients, id)
    new_balance = balance + amount # add the amount to the balance
    update_client(Clients, id, client_balance=new_balance) # update the client balance
    print(f"€{amount} has been deposited to the account of client {id}\nThe new balance is €{new_balance}")
    return new_balance

#function to withdraw money from a specific client
def withdraw_money(Clients, id: int, amount: float): # id is the client id, amount is the amount to withdraw could be float
    balance = get_balance(Clients, id)
    if balance >= amount: # check if the balance is enough to withdraw the amount
        new_balance = balance - amount # subtract the amount from the balance
        update_client(Clients, client_id=id, client_balance=new_balance) # update the client balance
        print(f"€{amount} has been withdrawn from the account of client {id}\nThe new balance is €{new_balance}")
        return new_balance 
    else:
        print(f"Sorry, The €{amount} cannot be withdrawn, that exceeds you balance of €{balance}")
        return None

#function to send money
def send_money(clients, from_id, to_id, amount):
    sender = get_client(clients, from_id)
    receptor = get_client(clients, to_id)
    if amount < sender["balance"]:
        sender["balance"] -= amount
        receptor["balance"] += amount
        print("-"*80)
        print(f"Sending €{amount} from Client {from_id} to Client {to_id}")
        print("Please wait....")
        time.sleep(1)
        print(f'The amount of {amount} will be deducted from Client {from_id} Account\nThe new balance is {sender["balance"]}')
        time.sleep(1.5)
        print("-"*80)
        print("sending money....")
        time.sleep(1)
        print(f"The amount of {amount} was added to Client {receptor['client id']} Account\nThe new balance is {receptor['balance']}")
        print("The transaction was successful, thank you for using our services")
        print("-"*80)
    else:
        print("-"*80)
        print("Transaction failed....")
        print(f"Sorry, The amount of €{amount} cannot be sent,\namount exceeds you current balance of €{sender['balance']}")
        print('-'*80)
        print("Please deposit more money to your account or try sending a smaller amount\nIf you have any questions, please contact our customer service 24/7:\nCall free: 0-800-123-456")
        print("-"*80)
    
    save_client(clients)
