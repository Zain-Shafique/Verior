from flask import Flask, request, jsonify
from pydantic import BaseModel, ValidationError, field_validator
from typing import Optional
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Add root endpoint
@app.route('/')
def home():
    return "Flask Validation API is running. Use POST /register to test."

# Pydantic Model for User Registration
class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    age: Optional[int] = None
    price: Optional[float] = None
    quantity: Optional[int] = None

    @field_validator('name', 'email', 'password')
    def check_non_empty(cls, v):
        if isinstance(v, str) and v.strip() == '':
            raise ValueError('must not be empty')
        return v

    @field_validator('age', 'price', 'quantity', mode='before')
    def check_numeric_type(cls, v):
        if v is None:
            return v
        if isinstance(v, str):
            raise ValueError('must be a valid number, not a string')
        return v

# Centralized Error Handlers
@app.errorhandler(ValidationError)
def handle_validation_error(e):
    errors = []
    for error in e.errors():
        field = ".".join(str(loc) for loc in error['loc'])
        msg = error['msg']
        errors.append(f"{field}: {msg}")
    return jsonify(error="Validation error", details=errors), 422

@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return jsonify(error="Bad Request", message=str(e.description)), 400

@app.errorhandler(500)
def handle_internal_server_error(e):
    return jsonify(error="Internal Server Error"), 500

# Registration Endpoint
@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    user_data = UserCreate(**data)
    # In a real app, you'd save to a database here
    return jsonify(message="User created successfully", user=user_data.model_dump()), 201

if __name__ == '__main__':
    app.run(debug=True)