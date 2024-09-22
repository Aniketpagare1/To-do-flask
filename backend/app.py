from flask import Flask, request, jsonify
from flask_graphql import GraphQLView
from keycloak import KeycloakOpenID
from payments import stripe_checkout_session
from auth import keycloak_middleware
from schema import schema
from models import db, ToDo
import os

app = Flask(__name__)

# Load configurations from environment variables
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///todos.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Middleware for Keycloak authentication
@app.before_request
def middleware():
    keycloak_middleware(request)

# GraphQL endpoint
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

# Stripe payment route (to purchase pro license)
@app.route('/create-checkout-session', methods=['POST'])
def create_checkout():
    session = stripe_checkout_session(request.json['email'])
    return jsonify(session)

# Initialize database and run app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
