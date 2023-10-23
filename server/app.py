from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restx import Api, Resource, fields
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, create_refresh_token, get_jwt_identity
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = 'some_random_secret_key'
app.config['JWT_SECRET_KEY'] = '4KlDjfoaawgoCZtRxKmijn73a4Uiq30g-yzZLKgi_iY='
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

api = Api(app, version='1.0', title='My API', description='A simple demo API')
jwt = JWTManager(app)

login_model = api.model('Login', {
    'email': fields.String(required=True, description='Email'),
    'password': fields.String(required=True, description='User password')
})

register_model = api.model('Register', {
    'email': fields.String(required=True, description='Email'),
    'password': fields.String(required=True, description='User password'),
    'firstName': fields.String(required=True, description='First name'),
    'lastName': fields.String(required=True, description='Last name'),
    'role': fields.String(required=True, description='User role (e.g., specialist or parent)')
})

users = {}

@api.route('/register')
class RegisterResource(Resource):
    @api.expect(register_model, validate=True)
    def post(self):
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        firstName = data.get('firstName')
        lastName = data.get('lastName')
        role = data.get('role')

        if email in users:
            return {"message": "email already exists"}, 400

        hashed_password = generate_password_hash(password, method='sha256')
        print(role)
        users[email] = {
            'password': hashed_password,
            'firstName': firstName,
            'lastName': lastName,
            'role': role
        }

        access_token = create_access_token(identity=email)
        refresh_token = create_refresh_token(identity=email)
        return {
            "accessToken": access_token,
            "refreshToken": refresh_token,
            "message": "User registered successfully"
        }, 201

@api.route('/login')
class LoginResource(Resource):
    @api.expect(login_model, validate=True)
    def post(self):
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        user_data = users.get(email, {})
        if user_data and check_password_hash(user_data.get('password', ''), password):
            access_token = create_access_token(identity=email)
            refresh_token = create_refresh_token(identity=email)
            return {
                "accessToken": access_token,
                "refreshToken": refresh_token,
                "message": "Logged in successfully"
            }

        return {"message": "Invalid credentials"}, 401

@api.route('/refresh')
class RefreshResource(Resource):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return {"access_token": access_token}

@app.route('/profile')
@jwt_required()
def get():
    current_user = get_jwt_identity()
    user_data = users.get(current_user)
    if user_data:
        user_data.pop('jwt_required', None)
        return jsonify(user_data)
    return {"message": "User not found"}, 404


if __name__ == '__main__':
    app.run(debug=True)
