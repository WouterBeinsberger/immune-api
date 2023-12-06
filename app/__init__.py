from flask import Flask
# from flask_cors import CORS

def create_app():
  app = Flask(__name__)
  # CORS(app)

  from app.controllers.token_controller import token_bp
  from app.controllers.customer_controller import customer_bp

  app.register_blueprint(token_bp)
  app.register_blueprint(customer_bp)

  return app
