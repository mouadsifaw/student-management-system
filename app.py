from flask import Flask, render_template, request, redirect, url_for, flash  # Add flash here
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'username',
    'password': 'password',
    'database': 'StudentDB'
}

# Function to connect to the database
def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/view')
def view_students():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM Students')
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('view_students.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        grade = request.form['grade']
        email = request.form['email']

        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                'INSERT INTO Students (Name, Age, Grade, Email) VALUES (%s, %s, %s, %s)',
                (name, age, grade, email)
            )
            conn.commit()
            flash('Student added successfully!', 'success')  # Flash message for success
        except mysql.connector.Error as err:
            flash(f'Error: {err}', 'error')  # Flash message for errors
        finally:
            cursor.close()
            conn.close()
        return redirect(url_for('view_students'))
    return render_template('add_student.html')

@app.route('/update/<int:student_id>', methods=['GET', 'POST'])
def update_student(student_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        grade = request.form['grade']
        email = request.form['email']

        try:
            cursor.execute(
                'UPDATE Students SET Name = %s, Age = %s, Grade = %s, Email = %s WHERE StudentID = %s',
                (name, age, grade, email, student_id)
            )
            conn.commit()
            flash('Student updated successfully!', 'success')  # Flash message for success
        except mysql.connector.Error as err:
            flash(f'Error: {err}', 'error')  # Flash message for errors
        finally:
            cursor.close()
            conn.close()
        return redirect(url_for('view_students'))

    cursor.execute('SELECT * FROM Students WHERE StudentID = %s', (student_id,))
    student = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('update_student.html', student=student)

@app.route('/delete/<int:student_id>')
def delete_student(student_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM Students WHERE StudentID = %s', (student_id,))
        conn.commit()
        flash('Student deleted successfully!', 'success')  # Flash message for success
    except mysql.connector.Error as err:
        flash(f'Error: {err}', 'error')  # Flash message for errors
    finally:
        cursor.close()
        conn.close()
    return redirect(url_for('view_students'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
