Django superuser: This will be your superuser as the one I created has been
registered in my MySql database. You can create your own superuser by running the following command in the terminal:
python3 manage.py createsuperuser


Restaurant home: http://127.0.0.1:8000/restaurant/

Please check the model schema to understand what fields are needed. Hopefully you are
using the same field names in the MySql tables that you have created.


# You can test the following API routes either in the browser or through 
# Insomnia/Postman
** Please do not forget to append backslash '/' at the end of the url **
# You need to be logged in as a user to access these routes

restaurant/menu_api/                 
restaurant/menu_api/<int:pk>/   
restaurant/booking_api/tables/


For user registration
/auth/token/login/     # To create the token. You need to be logged in as superuser to access this route
/auth/users/           # To register a new user. You need to be logged in as superuser to access this route
/api-token-auth/       # Make a post call to this route with username and password to get the token

For running the tests
Pagination has been commented in the settings files to enable to run the tests. 
Please uncomment it after running the unit tests if you want to test pagination.