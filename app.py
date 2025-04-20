import os
import numpy as np
from flask import Flask, request, render_template
import contextlib
import joblib
import re
import sqlite3
import pandas as pd
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from create_database import setup_database
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.applications.vgg16 import preprocess_input
from utils import login_required, set_session
from flask import (
    Flask, render_template, 
    request, session, redirect
)

# Initialize Flask app
app = Flask(__name__)

# Load pre-trained model (adjust the path if necessary)
model = load_model('model/model.h5')

database = "users.db"
setup_database(name=database)

app.secret_key = 'xpSm7p5bgJY8rNoBjGWiz5yjxM-NEBlW6SIBI62OkLc='

# Define the class names (replace with your actual class names)
class_names = ['Basal Cell Carcinoma', 'Melanoma', 'Squamous Cell Carcinoma']

# Confidence threshold for "Non-Cancerous" detection
CONFIDENCE_THRESHOLD = 0.6  # Adjust based on your experiments

# Create an uploads folder if it doesn't exist
UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Homepage route
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    # Set data to variables
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Attempt to query associated user data
    query = 'select username, password, email from users where username = :username'

    with contextlib.closing(sqlite3.connect(database)) as conn:
        with conn:
            account = conn.execute(query, {'username': username}).fetchone()

    if not account: 
        return render_template('login.html', error='Username does not exist')

    # Verify password
    try:
        ph = PasswordHasher()
        ph.verify(account[1], password)
    except VerifyMismatchError:
        return render_template('login.html', error='Incorrect password')

    # Check if password hash needs to be updated
    if ph.check_needs_rehash(account[1]):
        query = 'update set password = :password where username = :username'
        params = {'password': ph.hash(password), 'username': account[0]}

        with contextlib.closing(sqlite3.connect(database)) as conn:
            with conn:
                conn.execute(query, params)

    # Set cookie for user session
    set_session(
        username=account[0], 
        email=account[2], 
        remember_me='remember-me' in request.form
    )
    
    return redirect('/predict_page')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    
    # Store data to variables 
    password = request.form.get('password')
    confirm_password = request.form.get('confirm-password')
    username = request.form.get('username')
    email = request.form.get('email')

    # Verify data
    if len(password) < 8:
        return render_template('register.html', error='Your password must be 8 or more characters')
    if password != confirm_password:
        return render_template('register.html', error='Passwords do not match')
    if not re.match(r'^[a-zA-Z0-9]+$', username):
        return render_template('register.html', error='Username must only be letters and numbers')
    if not 3 < len(username) < 26:
        return render_template('register.html', error='Username must be between 4 and 25 characters')

    query = 'select username from users where username = :username;'
    with contextlib.closing(sqlite3.connect(database)) as conn:
        with conn:
            result = conn.execute(query, {'username': username}).fetchone()
    if result:
        return render_template('register.html', error='Username already exists')

    # Create password hash
    pw = PasswordHasher()
    hashed_password = pw.hash(password)

    query = 'insert into users(username, password, email) values (:username, :password, :email);'
    params = {
        'username': username,
        'password': hashed_password,
        'email': email
    }

    with contextlib.closing(sqlite3.connect(database)) as conn:
        with conn:
            result = conn.execute(query, params)

    # We can log the user in right away since no email verification
    set_session( username=username, email=email)
    return redirect('/')

@app.route('/predict_page')
def predict_page():
    return render_template('predict.html')

# Route for handling image upload and prediction
@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return render_template('predict.html', error="No image uploaded")

    file = request.files['image']
    
    # Ensure a valid file is uploaded
    if file.filename == '':
        return render_template('predict.html', error="No selected file")

    # Save the uploaded file
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    
    try:
        # Preprocess the image for prediction
        img = load_img(file_path, target_size=(224, 224))  # Resize to model input size
        img_array = img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
        img_array = preprocess_input(img_array)  # Normalize using preprocess_input
        
        # Predict the class
        predictions = model.predict(img_array)
        confidence_scores = predictions[0]
        
        # Determine the result based on confidence
        if max(confidence_scores) < CONFIDENCE_THRESHOLD:
            predicted_class = "Non-Cancerous"
        else:
            predicted_class = class_names[np.argmax(confidence_scores)]
        
        confidence = max(confidence_scores) * 96
        
        return render_template('result.html', 
                               image=file.filename, 
                               predicted_class=predicted_class, 
                               confidence=f"{confidence:.2f}%")
    except Exception as e:
        # Handle any errors during prediction
        return render_template('predict.html', error=f"An error occurred: {str(e)}")

# Main execution
if __name__ == "__main__":
    app.run(debug=True)
