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

    # execute SQL commands
    record = util.run_and_fetch_sql(cursor, "SELECT FROM;")

    if record == -1:
        # you can replace this part with a 404 page
        print('Something is wrong with the SQL command')
    else:
        # this will return all column names of the select result table
        # ['customer_id','store_id','first_name','last_name','email','address_id','activebool','create_date','last_update','active']
        col_names = [desc[0] for desc in cursor.description]
        log = record

    # disconnect from database
    util.disconnect_from_db(connection,cursor)
    # using render_template function, Flask will search
    # the file named index.html under templates folder'''
    log = ''
    col_names =''
    return render_template('home.html', sql_table = log, table_title=col_names)

@app.route('/expenses')
def expenses():
    try:
        cursor, connection = util.connect_to_db(username,password,host,port,database)
        print("Connected to the database!")
    except:
        print("Couldn't connect to the database...")
    #cursor.execute("SELECT * FROM bills;")
    bills = util.run_and_fetch_sql(cursor, "SELECT * FROM bills;")
    print(bills)
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