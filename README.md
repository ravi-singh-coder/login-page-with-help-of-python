# Flask Login App

This is a simple Flask application that demonstrates user login and logout functionality. It uses hashed passwords for security and sessions to keep track of logged-in users.

## Features

- User login with username and password
- Secure password storage using hashing
- Session-based user authentication
- Simple, responsive HTML login form

## Requirements

- Python 3.7+
- Flask
- Werkzeug

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/flask-login-app.git
    cd flask-login-app
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install Flask Werkzeug
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000`.

3. Use the following credentials to log in:

    - Username: `ravi`
    - Password: `ravi123`

## Project Structure

```plaintext
flask-login-app/
├── static/
│   └── styles.css
├── templates/
│   └── index.html
├── app.py
└── README.md
