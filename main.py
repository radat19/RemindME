from datetime import datetime
from flask import Flask, render_template
import util

app = Flask(__name__)


# Evil global variables
# Should be placed in config
username='admin'
password='test'
host='127.0.0.1'
port='5432'
database='remindme'


@app.route('/')
def home():
	# connect to DB
    cursor, connection = util.connect_to_db(username,password,host,port,database)

    # Get today's date
    date = datetime.now().strftime('%Y-%m-%d')

    # execute SQL commands
    upcoming_bills = util.run_and_fetch_sql(cursor, "SELECT * FROM bills WHERE due_date >= '" + date + "';")

    # disconnect from database
    util.disconnect_from_db(connection,cursor)
    return render_template('home.html', bills_list = upcoming_bills)

@app.route('/expenses', methods=['GET', 'POST'])
def expenses():
    try:
        cursor, connection = util.connect_to_db(username,password,host,port,database)
        print("Connected to the database!")
    except:
        print("Couldn't connect to the database...")

    #cursor.execute("SELECT * FROM bills;")
    bills = util.run_and_fetch_sql(cursor, "SELECT * FROM bills;")

    ''''if request.method == 'POST':
        util.run_and_insert(cursor, 'INSERT INTO bills')'''

    # disconnect from databae
    util.disconnect_from_db(connection,cursor)
    return render_template('expenses.html', bills_list = bills)

@app.route('/monthlybills')
def monthlybills():
    return render_template('monthlybills.html')


if __name__ == '__main__':
	# set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)