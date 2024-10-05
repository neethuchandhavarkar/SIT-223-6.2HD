from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    """Return a JSON response with a greeting message."""
    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    """Run the application in debug mode."""
    app.run(debug=True)
