from flask import *
import datetime
import psycopg2


def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="phonedb",
        user="postgres",
        password="xxxxxx")
    return conn

def read_phonelist():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonelist;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def delete_contact(name):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(f"DELETE FROM phonelist WHERE name = '{name}';")
    cur.execute("COMMIT")
    cur.close()
    conn.close()
    return name

dum = [
  ['arne', '013-131313'], ['berith','01234'], ['caesar','077-1212321']
]

app = Flask(__name__)

@app.route("/")
def start():
    now = datetime.datetime.now()
    D = [str(now.year%100), str(now.month), str(now.day)]
    if len(D[1])<2:
        D[1] = '0'+D[1]
    if len(D[2])<2:
        D[2] = '0'+D[2]
    return render_template('list.html', list=read_phonelist(), date=D)   # list = dum från början

@app.route("/delete", methods = ['POST', 'GET'])
def delete():
    if request.method == 'POST':
        name = request.form('name')
        return render_template('delete.html', req=delete_contact(name))

    else:   # GET method
        return render_template('list.html', list = read_phonelist())


@app.route("/insert")
def insert():
    return render_template('insert.html')



if __name__ == '__main__':
    app.run(debug = True)