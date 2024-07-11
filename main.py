from bank_management_system import *
#or
#from bank_management_system import load_clients,save_client,add_client,update_client,delete_client,get_client,send_money
from stringcolor import cs
def main():
    while True:
        print("\n1. Add new client")
        print("2. Update existing client")
        print("3. Delete client")
        print("4. Display client")
        print("5. Display clients overview")
        print("6. Display total")
        print("t. Transfer Ca$h")
        print("d. Deposit")
        print("w Withdraw")
        print("q. Exit")

        option = input("\nSelect an option: ")
        clients = load_clients()
        if option == '1':
            name = input('Enter the new client name: ')
            dob = input('Enter the client dob (yyyy-mm-dd): ')
            balance = float(input('Enter client balance: '))
            add_client(clients,name,dob,balance)
        elif option == '2':
            client_id = int(input('Enter cliend ID: '))
            display_client(clients,client_id)
            name = input('Enter new client name (Leave empty to keep current)')
            dob = input('Enter new client dob (yyyy-mm-dd) (Leave empty to keep current)')
            balance = input('Enter new client balance (Leave empty to keep current)') 
            if balance != '':
                balance = float(balance)
            update_client(clients,client_id,name,dob,balance)
            print(cs(f'client {client_id} was updated succesfully'),'cyan')
        elif option == '3':
            client_id = int(input('Enter cliend ID: '))
            delete_client(clients,client_id)
            print(cs(f'Client was deleted succeasfully','red'))
        elif option == '4':
            client_id = int(input('Enter cliend ID: '))
            display_client(clients,client_id)
        elif option == '5':
            clients_overview(clients)
        elif option == '6':
            print(cs('Calculating...','green'))
            time.sleep(1)
            total = get_total_balance(clients)
            print("Total bank balance:", total)
        elif option == 't':
            client_send = int(input('Enter the sender ID: '))
            amount = float(input('Enter the amount: '))
            client_get = int(input('Enter the receiver ID: '))
            send_money(clients,client_send,client_get,amount)
        elif option == 'd':
            client_id = int(input('Enter cliend ID: '))
            amount = float(input('Enter the amount: '))
            client= get_client(clients,client_id)
            update_client(clients,client_id,client_balance=client['balance']+amount)
            print(f"The deposit to client {client_id} was successful the new balance is {client['balance']}")
        elif option == 'w':
            client_id = int(input('Enter cliend ID: '))
            amount = float(input('Enter the amount: '))
            client= get_client(clients,client_id)
            if client['balance'] > amount:
                update_client(clients,client_id,client_balance=client['balance']-amount)
                print(f"The withdraw from client {client_id} was successful the new balance is {client['balance']}")
            else:
                print('Not enough balance to perform this operation')
        elif option == 'q':
            break
        else:
            print("Invalid option. Please try again.")
main()