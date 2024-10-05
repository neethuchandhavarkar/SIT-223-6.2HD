from flask import Flask, jsonify

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def hello_world():
    """
    Handles requests to the root endpoint and returns a greeting message.

    Returns:
        json: A JSON response containing a greeting message.
    """
    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    # Run the application in debug mode
    app.run(debug=True)
