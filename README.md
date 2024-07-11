# Client Management System

## Overview
This is a Python-based client management system that uses JSON for data storage and the `stringcolor` library for colorful console outputs. The system allows you to perform various operations such as adding, updating, deleting clients, displaying client details, and transferring money between clients.

## Features
- **Load Clients**: Load client data from a JSON file.
- **Save Client**: Save client data to a JSON file.
- **Add Client**: Add a new client to the system.
- **Get Client**: Retrieve a client's information by their ID.
- **Update Client**: Update a client's details.
- **Delete Client**: Delete a client from the system.
- **Display Client**: Display a client's details in the console.
- **Clients Overview**: Display an overview of all clients.
- **Get Total Balance**: Calculate the total balance of all clients.
- **Send Money**: Transfer money between clients.

## Files
- `clients.json`: The JSON file that stores client data.

## Functions

### `load_clients()`
Loads client data from the `clients.json` file and returns it as a dictionary.

### `save_client(clients)`
Saves the client data to the `clients.json` file.
- `clients`: A list of client dictionaries to save.

### `add_client(clients, client_name, client_dob, client_balance)`
Adds a new client to the list.
- `clients`: The current list of clients.
- `client_name`: The name of the new client.
- `client_dob`: The date of birth of the new client.
- `client_balance`: The initial balance of the new client.

### `get_client(clients, client_id)`
Retrieves a client by their ID.
- `clients`: The current list of clients.
- `client_id`: The ID of the client to retrieve.

### `update_client(clients, client_id, client_name=None, client_dob=None, client_balance=None)`
Updates a client's details.
- `clients`: The current list of clients.
- `client_id`: The ID of the client to update.
- `client_name`: The new name of the client (optional).
- `client_dob`: The new date of birth of the client (optional).
- `client_balance`: The new balance of the client (optional).

### `delete_client(clients, client_id)`
Deletes a client from the list.
- `clients`: The current list of clients.
- `client_id`: The ID of the client to delete.

### `display_client(clients, client_id)`
Displays a client's details in the console.
- `clients`: The current list of clients.
- `client_id`: The ID of the client to display.

### `clients_overview(clients)`
Displays an overview of all clients in the console.
- `clients`: The current list of clients.

### `get_total_balance(clients)`
Calculates and returns the total balance of all clients.
- `clients`: The current list of clients.

### `send_money(clients, from_id, to_id, amount)`
Transfers money from one client to another.
- `clients`: The current list of clients.
- `from_id`: The ID of the client sending money.
- `to_id`: The ID of the client receiving money.
- `amount`: The amount of money to transfer.

## Usage
To use this client management system, ensure you have a `clients.json` file in the same directory. The file should be structured as follows:
```json
{
    "clients": []
}
```
Here is an example of a typical workflow:
```python
clients = load_clients()
add_client(clients, "John Doe", "1990-01-01", 1000)
add_client(clients, "Jane Smith", "1985-05-15", 1500)
clients_overview(clients)
update_client(clients, 1, client_balance=1200)
delete_client(clients, 2)
display_client(clients, 1)
total_balance = get_total_balance(clients)
send_money(clients, 1, 2, 200)
```

Ensure you have the required `stringcolor` library installed:
```bash
pip install stringcolor
```

## Notes
- The `clients.json` file must be present in the same directory as the script.
- Client IDs are auto-incremented based on the last client's ID in the list.
- The system uses colorful console outputs to enhance readability.

## License
This project is licensed under the MIT License.