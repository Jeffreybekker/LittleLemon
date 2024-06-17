Logging in on the admin panel:
Login: admin
Password: admin@123

Use the following links to test the APIs with Insomnia:
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

 
