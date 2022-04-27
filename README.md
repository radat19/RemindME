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

install pip
install flask
install requirements.txt

set main.py as app.py
export FLASK_APP=main.py

set environment to developer
export FLASK_ENV=development


flask run
