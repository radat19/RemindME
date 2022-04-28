from flask import Flask, render_template, redirect, url_for, request
from datetime import datetime
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
    upcoming_bills = util.run_and_fetch_sql(cursor, "SELECT * FROM bills WHERE due_date >= '" + date + 
        "' AND active = True ORDER BY due_date;")

    # disconnect from database
    util.disconnect_from_db(connection,cursor)
    return render_template('home.html', bills_list = upcoming_bills)

@app.route('/update', methods=['GET', 'POST'])
def expenses():
    try:
        cursor, connection = util.connect_to_db(username,password,host,port,database)
        print("Connected to the database!")
    except:
        print("Couldn't connect to the database...")

    #cursor.execute("SELECT * FROM bills;")
    bills = util.run_and_fetch_sql(cursor, "SELECT * FROM bills ORDER BY due_date;")

    if request.method == 'POST':
        uid = request.form['user-id']
        bill_name = request.form['bill-name']
        bill_type = request.form['bill-type']
        total = request.form['total-amount']
        due = request.form['due-date']

        util.run_and_insert_sql(cursor, connection, "INSERT INTO bills (user_id, name, type, total_amt, remain_amt, due_date, active)" 
            " VALUES (" + uid + ",'" + bill_name + "','" + bill_type + "'," + total + "," + total + ",'" + due + "', True);")
        print(uid)
        return redirect(url_for('expenses'))

    # disconnect from databae
    util.disconnect_from_db(connection,cursor)
    return render_template('expenses.html', bills_list = bills)

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    try:
        cursor, connection = util.connect_to_db(username,password,host,port,database)
        print("Connected to the database!")
    except:
        print("Couldn't connect to the database...")

    if request.method == 'POST':
        bill_name = request.form['bill-name']
        bill_type = request.form['bill-type']
        total = request.form['total-amount']
        due = request.form['due-date']

        util.run_and_insert_sql(cursor, connection, "UPDATE bills SET name = '" + bill_name + 
            "', type = '" + bill_type + "', total_amt = " + total + ", remain_amt = " + total + 
            ", due_date = '" + due + "', active = True WHERE id = " + str(id) + ";")

    return redirect(url_for('expenses'))

@app.route('/update/<int:id>/del', methods=['POST'])
def delete_bill(id):
    try:
        cursor, connection = util.connect_to_db(username,password,host,port,database)
        print("Connected to the database!")
    except:
        print("Couldn't connect to the database...")

    if request.method == 'POST':
        util.run_and_insert_sql(cursor, connection, "DELETE FROM bills WHERE id = " + str(id) + ";")
        print(id)

    return redirect(url_for('expenses'))

@app.route('/statement')
def statement():
    try:
        cursor, connection = util.connect_to_db(username,password,host,port,database)
        print("Connected to the database!")
    except:
        print("Couldn't connect to the database...")

    chart_data = util.run_and_fetch_sql(cursor, "SELECT type, SUM(remain_amt)::numeric::float8 FROM bills GROUP BY type;")    

    #cursor.execute("SELECT * FROM bills;")
    bills = util.run_and_fetch_sql(cursor, "SELECT * FROM bills;")
    print(bills)
    util.disconnect_from_db(connection,cursor)
    return render_template('monthlybills.html', bills_list = bills, chart_data = chart_data)


@app.route('/pay/<int:id>', methods=['POST'])
def pay_bill(id):
    try:
        cursor, connection = util.connect_to_db(username,password,host,port,database)
        print("Connected to the database!")
    except:
        print("Couldn't connect to the database...")

    if request.method == 'POST':
        payment = int(request.form['pay-amt'])
        remaining = util.run_and_fetch_sql(cursor, "SELECT remain_amt::numeric::float8 FROM bills WHERE id = " + str(id) + ";")[0][0]
        new_remain = remaining - payment
        paid = "True"

        # Deactivates ability to make payments on this bill
        if new_remain <= 0:
            new_remain = 0
            paid = "False"
        
        util.run_and_insert_sql(cursor, connection, "UPDATE bills SET remain_amt = " + str(new_remain) +
           ", active = " + paid + " WHERE id = " + str(id) + ";")

    return redirect(url_for('home'))



if __name__ == '__main__':
	# set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)