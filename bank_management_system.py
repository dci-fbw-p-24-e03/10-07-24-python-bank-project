import json 
from stringcolor import cs
import time
def load_clients():
    with open('clients.json') as f:
        data = json.load(f)#we are converting the data from json => dict
    return data['clients']

def save_client(clients):
    with open('clients.json','w') as file:#w is write mode
        json.dump({"clients":clients},file,indent=4)
        
        
def add_client(clients,client_name,client_dob,client_balance):
    if clients == []:
        client_id = 1
    else :
        client_id = clients[-1]['client id']+1
    clients.append({"client id":client_id,"client name":client_name,"client dob":client_dob,'balance':client_balance})
    save_client(clients)
def get_client(clients,client_id):
    for client in clients:
        if client['client id'] == client_id:
            return client
        
def update_client(clients,client_id,client_name=None,client_dob=None,client_balance=None):
    client = get_client(clients,client_id)
    if client_name:
        client['client name'] = client_name
    if client_dob :
        client['client dob'] =client_dob
    if client_balance:
        client['balance'] = client_balance               
    save_client(clients)
    
def delete_client(clients,client_id):
    client = get_client(clients,client_id)
    clients.remove(client)
    
    save_client(clients)
    
def display_client(clients,client_id):
    client = get_client(clients,client_id)
    print(cs(f"Client name {client['client name']}",'blue'))
    print(cs(f"Client dob {client['client dob']}",'green'))
    print(cs(f"Client balance {client['balance']}",'orchid'))
            

def clients_overview(clients):
    for client in clients:
        print(cs(f"Client id {client['client id']}",'red'))
        print(cs(f"Client name {client['client name']}",'blue'))
        print(cs(f"Client dob {client['client dob']}",'green'))
        print(cs(f"Client balance {client['balance']}",'orchid'))
        print(cs('-'*50,'yellow'))
        time.sleep(1.5)
        
def get_total_balance(clients):

    total = sum([client['balance'] for client in clients])
    return total

def send_money(clients,from_id,to_id,amount):
    client_send = get_client(clients,from_id)
    if amount < client_send['balance']:
        client_send['balance'] -= amount
        
        client_receive = get_client(clients,to_id)
        client_receive['balance'] += amount
        print(f'The amount of {amount} will be deducted from Client {from_id}\nThe new balance is {client_send["balance"]}')
        print(f"The amount of {amount} was added to Client {client_receive['client id']} account\nThe new balance is {client_receive['balance']}")
    else:
        print("Not enough money in account!")  
             
   
            
    save_client(clients)

send_money(load_clients(),4,3,60000)



