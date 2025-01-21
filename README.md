# Little Lemon Capstone

<p>This is the last project of the Meta Backend Developer Professional certificate.</p>
<p>In this project it is possible to:</p>

* Get all menu items
* Create items to the menu
* Get, update and delete a single menu item
* Get all bookings and create bookings
* Get, update and delete a single booking

## Table of Contents
* [Little Lemon Capstone](#little-lemon-capstone)
  * [Installation](#installation)
  * [API Endpoints](#api-endpoints)
  * [Admin Panel](#admin-panel)
  * [Screenshots](#screenshots)

## Installation
1. Clone the Repository:
```
git clone https://github.com/Jeffreybekker/LittleLemon.git
```
2. Create a virtual environment:
```
python -m venv env
```
3. Start the virtual environment, depending on your system. You can get more information about this <a href="https://docs.python.org/3/tutorial/venv.html">here</a>.

## API Endpoints
<p>Logging in on the admin panel: <br> 
Login: admin <br> 
Password: admin@123</p>

<p>Below are the APIs endpoints explained with the URL, possible methods, actions, if a token is needed and the status codes:</p>

```
http://127.0.0.1:8000/restaturant/menu/items
```
<table>
	<thead>
		<tr>
			<th>HTTP Method</th>
			<th>Action</th>
			<th>Auth token</th>
			<th>Status code</th>
		</tr>
	</thead>
</table>

http://127.0.0.1:8000/restaurant/menu/     (to get all menu items, use GET)
http://127.0.0.1:8000/restaurant/menu/1    (to get a specific menu item, you can use GET, PUT and DELETE)
http://127.0.0.1:8000/restaurant/booking/tables/ (to get all reservations, use a BEARER TOKEN, use Insomnia)

User registration you can do on the admin panel or use this link http://127.0.0.1:8000/auth/users/
Example adding new user in Insomnia (use POST request):
{
	"username": "Jan",
	"password": "jan@1234",
	"email": "jan@gmail.com"
	}
## Admin Panel

## Screenshots
