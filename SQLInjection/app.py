from flask import Flask, redirect, render_template, request

import pymysql
from pymysql.constants.CLIENT import MULTI_STATEMENTS as MS

import os

app = Flask(__name__)

conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = os.environ.get('MY_SQL_PASSWORD'),
    db = 'info',
    client_flag=MS #allows for multiple queries per execute.
)

#helper function that attempts a query. an instance of an error sends
#a user back to the login page.
def tryExec(query):
    try: 
        cursor.execute(query)
        conn.commit()
    except Exception as e:
        print(e)
        return False
    else:
        return True

cursor = conn.cursor()

@app.get('/')
def login_form():
    return render_template('login.html')

@app.post('/')
def login():
    username = request.form.get('usern')
    password = request.form.get('passw')

    select = f"SELECT * FROM users WHERE usern = '{username}' AND passw = '{password}'"
    if (tryExec(select)):
        data = cursor.fetchone()
        print(data)
        
        if data:
            print('Logging in as existing user...')
            return redirect(f'/user/{username}')
        else:
            insert = f"INSERT INTO users (usern, passw) VALUES ('{username}', '{password}')"

            if (tryExec(insert)):
                print('Registering as new user...')
                return redirect(f'/user/{username}')
            else:
                return redirect('/')
    else:
        return redirect('/')

@app.get('/user/<string:username>')
def profile_form(username):
    query = f"SELECT usern, passw FROM users WHERE usern='{username}'"
    
    cursor.execute(query)
    conn.commit()
    data = cursor.fetchone()
    print(data)

    return render_template('user.html', data=data)

