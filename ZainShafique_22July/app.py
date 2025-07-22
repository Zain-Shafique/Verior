from flask import Flask, jsonify

app = Flask(__name__)

# Helper function to structure responses
def make_response(status, message, data):
    return jsonify({
        "status": status,
        "message": message,
        "data": data
    }), status

# Dummy user data storage
users = {
    "1": {"id": "1", "name": "Ali", "email": "ali@example.com", "preferences": {"theme": "dark", "language": "en"}},
    "2": {"id": "2", "name": "Bob", "email": "bob@example.com", "preferences": {"theme": "light", "language": "fr"}}
}

# Basic test route
@app.route('/hello')
def hello():
    return make_response(200, "Success", {"greeting": "Hello World!"})

# Profile route with nested data
@app.route('/profile')
def profile():
    mock_profile = {
        "id": "123",
        "name": "Zain Shafique",
        "contact": {
            "email": "zain@example.com",
            "phone": "+1234567890"
        },
        "subscription": {"active": True, "plan": "premium"}
    }
    return make_response(200, "User profile retrieved", mock_profile)

# Dynamic user lookup route
@app.route('/user/<user_id>')
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return make_response(200, "User found", user)
    return make_response(404, "User not found", None)

if __name__ == '__main__':
    app.run(debug=True)