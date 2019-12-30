# Movies API
_______________________

# Instalation
To run locally, do the usual:<br>
1. Create a Python virtualenv<br>
    `pip install virtualenv`<br>
    `virtualenv ENV`<br>
    
2. Activate your ENV:<br>
    `ENV\Scripts\activate`<br>
    
3. Install dependencies:<br>
    `pip install -r requirements.txt`<br>
    
4. Run Django server:<br>
    `python manage.py runserver`<br>
    
Migrate and create super user. <br>
Admin page - http://localhost:8000/admin<br>

# Instruction
<b>Create new user</b><br>
Go to http://localhost:8000/api/users/ and POST username and password:
<img src="screens/new-user.png"/>

<b>Get auth token</b><br>
Go to http://localhost:8000/auth/, POST username and password and copy your token:
<img src="screens/get-tokenpng.png"/>

<b>Add new movie</b><br>
Go to http://localhost:8000/api/movies/, POST movie title in BODY and token in HEADERS:
<img src="screens/new-movie-auth.png"/>
<img src="screens/new-movie.png"/>

<b>See also</b><br>
Reviews - http://localhost:8000/api/reviews/<BR>
Favorites - http://localhost:8000/api/favorite/<BR>
