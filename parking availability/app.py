from flask import Flask, render_template, request, jsonify, session
import sqlite3
import secrets

connection = sqlite3.connect('user_data.db')
cursor = connection.cursor()

command = """CREATE TABLE IF NOT EXISTS user(name TEXT, password TEXT, mobile TEXT, email TEXT, address TEXT)"""
cursor.execute(command)


app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':

        connection = sqlite3.connect('user_data.db')
        cursor = connection.cursor()

        name = request.form['name']
        password = request.form['password']

        query = "SELECT * FROM user WHERE name = '"+name+"' AND password= '"+password+"'"
        cursor.execute(query)

        result = cursor.fetchone()

        if result:
            session['name'] = result[0]
            return render_template('home.html')
        else:
            return render_template('signin.html', msg='Sorry, Incorrect Credentials Provided,  Try Again')

    return render_template('signin.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':

        connection = sqlite3.connect('user_data.db')
        cursor = connection.cursor()

        name = request.form['name']
        password = request.form['password']
        mobile = request.form['phone']
        email = request.form['email']
        address = request.form['address']
        
        print(name, mobile, email, password)
        cursor.execute("INSERT INTO user VALUES ('"+name+"', '"+password+"', '"+mobile+"', '"+email+"', '"+address+"')")
        connection.commit()

        return render_template('signin.html', msg='Successfully Registered')
    
    return render_template('signup.html')

@app.route('/get_data')
def get_data():
   from serial_test import read_data
   Data1 = read_data()
   print("recieved data {}".format(Data1))
   return jsonify(Data1)

@app.route('/signout')
def signout():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
