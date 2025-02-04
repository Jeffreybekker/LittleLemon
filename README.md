# Little Lemon Capstone

<p>This is the last project of the Meta Backend Developer Professional certificate course.</p>
<p>In this project, you'll find the models used to create the database, which is stored in MySQL. Access to the database is granted based on authentication. The Djoser library is installed for user authentication, enabling user registration, login and logout, password reset and many more functionalities. To secure the APIs we make use of TokenAuthentication from the Django Rest Framework. The menu and table reservations are built using Django Rest Framework. For testing purposes, you can use Insomnia, and screenshots of Insomnia are shown below.</p>


## Table of Contents
* [Little Lemon Capstone](#little-lemon-capstone)
  * [Installation](#installation)
  * [Endpoints](#endpoints)
  	* [User Management Endpoints](#user-management-endpoints)
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

## Endpoints
### User Management Endpoints
#### Create user
```
http://127.0.0.1:8000/auth/users/
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
	<tbody>
		<tr>
			<td>POST</td>
			<td>Create new user</td>
			<td>No</td>
			<td>201 Created</td>
		</tr>
	</tbody>
</table>
<br>

![image](https://github.com/user-attachments/assets/cee12efb-6043-4f04-ab34-bce3e92e65e2)

#### Obtain user authentication token
```
http://127.0.0.1:8000/auth/token/login/
```
*Note: it takes username and password as content that you want to send in the body of the request.*

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
			<td>POST</td>
			<td>Obtain user auth token</td>
			<td>No</td>
			<td>200 OK</td>
		</tr>
	</tbody>
</table>
<br>

![image](https://github.com/user-attachments/assets/a18fd43d-3d0e-4e89-a332-6c004b965ac9)

#### Get current user
```
http://127.0.0.1:8000/auth/users/me/
```
*Note: first get your token (see previous point). Then add your Token in Auth. Make sure you select Bearer Token.*

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
			<td>Retrieve current user</td>
			<td>Yes</td>
			<td>200 OK</td>
		</tr>
	</tbody>
</table>
<br>

![image](https://github.com/user-attachments/assets/bea9f815-a2fd-4bab-ae6b-1282c298e489)

#### Get all users (admin)
```
http://127.0.0.1:8000/auth/users/
```
*Note: This is for Admin only. First get your Admin Token and then use it for authentication in Auth. Make sure you select Bearer Token.*

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
			<td>Retrieve all users</td>
			<td>Yes</td>
			<td>200 OK</td>
		</tr>
	</tbody>
</table>
<br>

![image](https://github.com/user-attachments/assets/dd97969b-3594-48c4-913b-b30f6aef15c1)

#### Logout current user
```
http://127.0.0.1:8000/auth/token/logout/
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
	<tbody>
		<tr>
			<td>POST</td>
			<td>Logout current user</td>
			<td>Yes</td>
			<td>204 No Content</td>
		</tr>
	</tbody>
</table>
<br>

![image](https://github.com/user-attachments/assets/ff2b2032-0f98-455b-9865-342affcf88a3)


### API Endpoints
<p>Below are the APIs endpoints explained with the URL, possible methods, actions, if a token is needed and the status codes:</p>

* Get all the menu items or add an item
```
http://127.0.0.1:8000/restaurant/menu/
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

*Here is an example how to send a POST request:*

![image](https://github.com/user-attachments/assets/472f5374-bb23-4331-81f9-70e506452215)

* Single view, update, partially update or delete item
```
http://127.0.0.1:8000/restaurant/menu/{id}
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
				<td>204 No Content</td>
		</tr>
	</tbody>
</table>


http://127.0.0.1:8000/restaurant/booking/tables/ (to get all reservations, use a BEARER TOKEN, use Insomnia) 
## Admin Panel
<p>Logging in on the admin panel: <br> 
Login: admin <br> 
Password: admin@123</p>

## Screenshots
![image](https://github.com/user-attachments/assets/62a6deaa-0af9-4a08-93b4-3154d8a30734)
![image](https://github.com/user-attachments/assets/cb8c4eb9-6e20-4c67-a932-855050e78a9f)

