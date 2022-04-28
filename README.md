# RemindME
Web App Final Project

To create server: <br>
<br>
sudo su - postgres <br>
psql <br>
CREATE USER admin WITH PASSWORD'test'; <br>
CREATE DATABASE remindme; <br>
GRANT ALL PRIVILEGES ON DATABASE remindme to admin; <br>
\q <br>
exit <br>
<br>
<br>


create tables for application
create table users (
    id SERIAL PRIMARY KEY,
    first_name varchar(50),
    last_name varchar(50),
    email varchar(50),
    password varchar(256)
);
create table bills (
    id SERIAL PRIMARY KEY,
    user_id SERIAL,
    name varchar(25),
    type varchar(15),
    total_amt MONEY,
    remain_amt MONEY,
    due_date DATE,
    active BOOL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);



import included csv's to respective tables.



install pip
  sudo apt install pip
  
install flask
  pip install flask
  
install requirements.txt
  pip install -r requirements.txt

set main.py as app.py
  export FLASK_APP=main.py

set environment to developer
  export FLASK_ENV=development


flask run
