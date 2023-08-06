# EzTDX
## What is this?
A Python wrapper for the [TeamDynamix Rest APIs](https://api.teamdynamix.com/TDWebApi/). Currently, the wrapper focuses on tickets, time entry, and people/users, but can be, and should be expanded to 
include Projects, Assets, etc.
## How do I use it in my project?
I'm glad you asked. It's meant to be as simple as possible to use and extend. If you follow the code patterns in the EzTDX.py 
file, you should be able to add new TDX API functionality with ease. To use the library in your project, you need to run ```pip install EzTDX```. Then import it in your application file.

[Searching Tickets](https://youtu.be/xPvckaN6WBA)

```
from EzTDX import EzTDX

BEID = <BEID>
WebServicesKey = <Web Services Key>

APP_ID = <Application ID>

if __name__ == '__main__':

    tdx = EzTDX(BEID, WebServicesKey, APP_ID)

    tickets = tdx.search_tickets('Directory Update Request', ['New', 'Open', 'Resolved'])

    for ticket in tickets:
        print(f"{ticket['ID']} - {ticket['Title']}")

    ticket = tdx.get_ticket_by_id('10821578')
    print(ticket)

    print(tdx.update_ticket(6564489,'testing 2', 'Resolved', False))
```

The BEID, Web Services Key, and Application ID should be stored in a secure manner if possible as they allow a lot of access into the TDX environment via the APIs. 

---
## Current Functionality
### **Initialization**
```EzTDX(BEID, WebServicesKey, APP_ID, Sandbox)```
- **BEID, WebServicesKey, and APP_ID**: If this is going to be used as part of a UC4 project, these should come from environment variables.
- **Sandbox**: Boolean value to point to either the test or production environment. *defaults to True so in order to use PROD, you must put False in it's place*

### **Get a single person**
```EzTDX.get_person(user_id)```
- **user_id**: The GUID of the user you would like information for.
> Returns a dictionary of a single person.

### **Get groups a person belongs to**
```EzTDX.get_people_groups(user_id)```
- **user_id**: The GUID of the user you would like information for.
> Returns a list of dictionary objects relating to the groups a person belongs to

### **Get a Single Ticket**
```EzTDX.get_ticket_by_id(ticket_id)```
- **ticket_id**: Ticket ID of the ticket you want to retrieve
> Returns a dictionary of a single ticket.

### **Get time types**
```EzTDX.get_time_types()```
> Returns a list of time types

### **Get single time type**
```EzTDX.get_time_type(time_type_id)```
- **time_type_id**: ID of the type of time you would like information for
> Returns dictionary with information on the type of time you requested.

### **Get Ticket Description**
```EzTDX.get_ticket_description(self, ticket_id: str)```
- **ticket_id**: ID of ticket to get the description of
> Returns the description field of the ticket.

### **Search People**
```EzTDX.search_people(search_by, max_results)```
- **search_by**: Searches last name, first name, user name, etc...
- **max_results**: Limit search to number of possible matches (default: 10)
> Returns a dictionary of person data

### **Search Tickets**
```EzTDX.search_tickets(search_str, ticket_status, max_results)```
- **search_str**: Search string * *required*
- **ticket_status**: List of ticket statuses you want to filter by (ex: ['New', 'Open', 'In Progress']) * *defaults to ['New']*
- **max_results**: How many tickets to be returned. *defaults to 5*
> Returns a list of tickets.

### **Search time entries**
```EzTDX.search_time_entries(entry_from_date, entry_to_date, person_ids, max_results)```
- **entry_from_date**: Start date in 2021-06-02T00:00:00Z format
- **entry_to_date**: End date in 2021-06-02T00:00:00Z format
- **person_ids**: List of GUIDS to search time entries for *defaults to empty list or everyone*
- **max_results**: How many entries to return *defaults to 1000*
> Returns a list of time entry dictionaries

### **Update a Ticket**
```EzTDX.update_ticket(ticket_id, comment, new_status, is_private)```
- **ticket_id**: ID of ticket to be updated * *required*
- **comment**: Comment to add to the feed * *required*
- **new_status**: Change the status of the ticket *defaults to None for no change*
- **is_private**: Mark the comment as private *defaults to False*
> Returns a success or failure message.