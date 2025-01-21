# Little Lemon Capstone

<p>This is the last project of the Meta Backend Developer Professional certificate.</p>

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
<p>Below are the APIs endpoints explained with the URL, possible methods, actions, if a token is needed and the status codes:</p>

```
http://127.0.0.1:8000/restaurant/menu/
```
* Check out all the menu items or add an item
<table>
	<thead>
		<tr>
			<th>HTTP Method</th>
			<th>Action</th>
			<th>Auth token</th>
			<th>Status code</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>GET</td>
			<td>Retrieve all menu items</td>
			<td>No</td>
			<td>200 OK</td>
		</tr>
		<tr>
			<td>POST</td>
			<td>Add a new menu item</td>
			<td>No</td>
			<td>201 Created</td>
		</tr>
	</tbody>
</table>
<br>

```
http://127.0.0.1:8000/restaurant/menu/{id}
```
* Single view, update, partially update or delete item
<table>
	<thead>
		<tr>
			<th>HTTP Method</th>
			<th>Action</th>
			<th>Auth token</th>
			<th>Status code</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>GET</td>
			<td>Retrieve single menu item</td>
			<td>No</td>
			<td>200 OK</td>
		</tr>
		<tr>
			<td>PUT</td>
			<td>Update menu item</td>
			<td>No</td>
			<td>200 OK</td>
		</tr>
			<tr>
				<td>PATCH</td>
				<td>Partially update menu item</td>
				<td>No</td>
				<td>200 OK</td>
		</tr>
			<tr>
				<td>DELETE</td>
				<td>Delete menu item</td>
				<td>No</td>
				<td>200 OK</td>
		</tr>
	</tbody>
</table>

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
<p>Logging in on the admin panel: <br> 
Login: admin <br> 
Password: admin@123</p>

## Screenshots
![image](https://github.com/user-attachments/assets/62a6deaa-0af9-4a08-93b4-3154d8a30734)
![image](https://github.com/user-attachments/assets/cb8c4eb9-6e20-4c67-a932-855050e78a9f)

