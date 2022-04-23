from flask import Flask, render_template
import util

app = Flask(__name__)


# Evil global variables
# Should be placed in config
username='admin'
password='test'
host='127.0.0.1'
port='5432'
database='billboard'


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
    # the file named index.html under templates folder
    return render_template('index.html', sql_table = log, table_title=col_names)


if __name__ == '__main__':
	# set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)