Ticketing System
A ticketing system that supports buying multiple ticket types where each ticket type has their own constraints of buying. Assume there is only one event that tickets are bought for. 
An event can have multiple tickets associated with it and each of those tickets can be one of the following types:
Open ticket
Seated Ticket
Eg.: Let’s take the example of a concert, the concert can have the following tickets associated with it:
Food - 1: Open ticket - $10
Food - 2: Open ticket - $50
T-Shirt: Open ticket - $30
<ticket_name>: Seated ticket - $50 - {A10-A50}
Concert seat - Gold: Seated ticket - $250 - {A1-A10}
We need to support the following functionality
Ability to buy tickets for a user 
Ability to get available tickets given an event.
Ability for the admin team to get the following reports
Total amount received for an event.
Top 10 highly sold tickets.
Show the users in decreasing order of their total purchased amount and have a way to search users based on name and filter by their age.
Age wise distribution of total ticket amount.


What’s expected:
Database Schema
Logic for above functionality
Handle concurrent cases

—--------------------------------------------------------------------

Database schema 

Tables name
Events 
	Event_id (PK)
	Event_name 
	Event_date 

TicketTypes
	Ticket_type_id (PK)
	Event_id (FK)
	Type_name 
	Ticket_catgory (open / seated) 
	Price 
		Seating_details 
	
Users 
	User_id (PK)
	Username
	Age
	Total_purchased_tickets 

Tickets 
	Ticket_id (PK)
	Event_id (FK)
	Ticket_type_id (FK)
	User_id (FK)
	Purchase_date 
	Status (purchased, reserved)
	seat_number

—-----------------------------------------------------------
Logic 
Ability to buy tickets for a user 
Ability to get available tickets given an event.
Ability for the admin team to get the following reports
Total amount received for an event.




Show the users in decreasing order of their total purchased amount and have a way to search users based on name and filter by their age.
Age wise distribution of total ticket amount.

Ability to buy tickets for a user 
Validate4 input data (user, event, ticketType)
Check ticket availability based on the constraints
Process payment 
Update tickets, users, events tables 

Ability to get available tickets given an event.
Query tickets table based on the event_id and status 
Filter tickets based on constraints if necesoory 
Ability for the admin team to get the following reports
Total amount received for an event.
Query TicketTypes table based on the event_id and calculate total amount received 
SQL 
	Select event_id, sum(price) as total_amount_price 
	From tickets 
Join ticketstype on tickets.ticket_type_id = tickettypes.ticket_type_id
Where ticket.event_id = “event_id”
And tickets.staus = “purchased”
Top 10 highly sold tickets.
Query tickets table , aggregate ticket sales and sort by sales count 
	Select ticket_type_id, count(*) as sales_count
	From tickets 
	Where status = “purchased”
	Group by ticket_type_id 
	Order by sales_count desc limit 10;
Show the users in decreasing order of their total purchased amount and have a way to search users based on name and filter by their age.
Query users table sort by total_purchase_amount
			Select users.user_id, users,username, users.age, sum (Tickets.total_purchased_Amount)
			From users 
			Join tickets on users.user_id = tickets.used_id
			Where ( :name is Null or users.username like ‘%’ || :name || ‘%’)
			And ( :min_age is Null or users.age >= :min_Age)
			And ( :max_age is Null or users.age <= :max_Age)
			Group by users.user_id, users.username, users.age
			Order by total_purchase_Amount desc;



Age wise distribution of total ticket amount.
Query users_table, aggregate total_purchased_amount based on the age
Select case 
when age between 0 and 18 then ‘0-18’
when age between 19 and 30 then ‘19-30’
when age between 31 and 50 then ‘31-50’
ELSE ‘51+’
			END AS AGE_GROUP
			SUM(TOTal_purchased_Amount) as total_Amount
			From users 
			Group by age_group 
			Order by age_group;









