from flask import Flask, redirect, request, render_template, jsonify
from flask.helpers import url_for
from flask_cors import CORS
import mysql.connector

app = Flask(__name__, template_folder='templates')
CORS(app)    


# Configure your database connection
app.config['DB_HOST'] = "localhost"
app.config['DB_USER'] = "root"
app.config['DB_PASSWORD'] = "raas@2006"
app.config['DB_DATABASE'] = "blood_buddy"

def get_database_connection():
    return mysql.connector.connect(
        host=app.config['DB_HOST'],
        user=app.config['DB_USER'],
        password=app.config['DB_PASSWORD'],
        database=app.config['DB_DATABASE']
    )

@app.route('/api/schedule_appointment', methods=['POST'])
def schedule_appointment():
    # Handle the form data here
    data = request.form  # Access the form data
    # Perform your logic, check for success, etc.
    success = True  # Replace with your actual logic
    return jsonify({'success': success})

# Handle registration form submission
@app.route('/api/register', methods=['POST'])
def register_form():
    print('Reached register_form route')
    try:
        data = request.json
        print('Received data from client:', data) 
        connection = get_database_connection()
        cursor = connection.cursor()

        query = "INSERT INTO Registration (username, email, password, user_type) VALUES (%s, %s, %s, %s)"
        values = (data['username'], data['email'], data['password'], data['user_type'])
        cursor.execute(query, values)
        connection.commit()

        return jsonify({'message': 'Registration successful!', 'user_type': data['user_type']})

    except Exception as e:
        print('Error:', e)
        connection.rollback()
        return jsonify({'error': 'Database error'})
    finally:
        cursor.close()
        connection.close()

# Handle donor form submission
@app.route('/api/donate', methods=['POST'])
def donor_form():
    print('Reached donor_form route')
    try:
        data = request.json
        print('Received data from client:', data) 
        connection = get_database_connection()
        cursor = connection.cursor()

        query = "INSERT INTO donor (Name, Gender, Blood_Type, Contact_Number,Location) VALUES (%s, %s, %s,%s, %s)"
        values = (data['Name'], data['Gender'], data['Blood_Type'], str(data['Contact_Number']), data['Location'])

        cursor.execute(query, values)
        connection.commit()
        return jsonify({'message': 'Registration successful!'})

    except Exception as e:
        print('Error:', e)
        connection.rollback()
        return jsonify({'error': 'Database error'})
    finally:
        cursor.close()
        connection.close()

        # Handle seeker form submission
@app.route('/api/seeker', methods=['POST'])
def seeker_form():
    print('Reached seeker_form route')
    try:
        data = request.json
        print('Received data from client:', data) 
        connection = get_database_connection()
        cursor = connection.cursor()

        query = "INSERT INTO seeker (Name, Gender, Blood_Type, Contact_Number,Location) VALUES (%s, %s, %s,%s, %s)"
        values = (data['Name'], data['Gender'], data['Blood_Type'], str(data['Contact_Number']), data['Location'])

        cursor.execute(query, values)
        

        connection.commit()
        return jsonify({'message': 'Registration successful!'})

    except Exception as e:
        print('Error:', e)
        connection.rollback()
        return jsonify({'error': 'Database error'})
    finally:
        cursor.close()
        connection.close()

# Home pages based on user type

@app.route('/index1.html')
def index():
    return render_template(f'index1.html')

@app.route('/index1.html')
def index1():
    return render_template(f'index1.html')

@app.route('/index2.html')
def index2():
    return render_template(f'index2.html')




# Add this route to render the Register.html file
@app.route('/')
def register_html():
    return render_template('Register.html', html_safe=True)

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/helps')
def helps():
    return render_template('helps.html')



@app.route('/donate')
def donate():
    return render_template('donate.html')

@app.route('/seeker')
def seeker():
    return render_template('seeker.html', html_safe=True)

@app.route('/hospital')
def hospital():
     return render_template('hospital.html')





if __name__ == '__main__':
    app.run(debug=True, port=5500)
