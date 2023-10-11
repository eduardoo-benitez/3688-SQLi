
used for presentation #1, Group Echo, for ITSC 3688, Fall 2023. requires python 3.10+.

1. run pipenv install in the previous directory.
3. set enviorment variable 'MY_SQL_PASSWORD' to the password of the relavent connection.
    - currently, the connection is set to happen on 127.0.0.1:3306 by default. db name is 'info', user is 'root' and host is 'local.'
    - these credentials can all be changed in the 'conn' object creation.
2. return back into this directory if needed.
4. use python -m flask run to lauch application.
5. go to localhost:5000 in a browser to access running app.

EXAMPLE INJECTION:

username: user
password: pass'; DROP TABLE users; #

This will drop the entire table 'users' within the current database.
