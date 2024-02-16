from flask import Blueprint, jsonify, request
from app.auth import authorize
from app.models.customers import Customers
import json
import uuid

customer_bp = Blueprint("customer", __name__)
customers = Customers()

@customer_bp.route("/customers", methods=["GET"])
def get_all_customers():
    return customers.all_customers(), 200

@customer_bp.route("/customer/<int:customer_id>", methods=["GET"])
def get_customer(customer_id):
    customer = customers.get_customer_by_id(customer_id)
    if customer:
        return customer, 200
    else:
        return jsonify({"error": f"Customer with ID {customer_id} not found"}), 404


@customer_bp.route("/customer", methods=["POST"])
def create_customer():
    authorize()  # Check authorization before processing
    data = request.get_json()
    new_customer = {
        "id": int(str(uuid.uuid4().int)[0:6]),
        "email": data.get("email"),
        "firstname": data.get("firstname"),
        "lastname": data.get("lastname"),
        "sendOptInMail": data.get("sendOptInMail"),
        "billing": data.get("billing")
    }

    customers.add_customer(new_customer)
    return jsonify({"success": f"Customer {new_customer['id']} added"}), 201


@customer_bp.route("/customer/<int:customer_id>", methods=["PUT"])
def update_customer(customer_id):
    authorize()  # Check authorization before processing
    data = request.get_json()
    # Remove the 'id' field from the request data if present
    if 'id' in data:
        del data['id']
    if customers.get_customer_by_id(customer_id):
        customers.update_customer_by_id(customer_id, data)
        return customers.get_customer_by_id(customer_id), 200
    else:
        return jsonify({"error": f"Customer with ID {customer_id} not found"}), 404
        
    

@customer_bp.route("/customer/<int:customer_id>", methods=["PATCH"])
def patch_customer(customer_id):
    authorize()  # Check authorization before processing
    data = request.get_json()
    # Remove the 'id' field from the request data if present
    if 'id' in data:
        del data['id']
    if customers.get_customer_by_id(customer_id):
        customers.update_customer_by_id(customer_id, data)
        return customers.get_customer_by_id(customer_id), 200
    else:
        return jsonify({"error": f"Customer with ID {customer_id} not found"}), 404

@customer_bp.route("/customer/<int:customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    authorize()  # Check authorization before processing
    customer = customers.get_customer_by_id(customer_id)
    if customer:
        customers.delete_customer_by_id(customer_id)
        return jsonify({"message": f"Customer with ID {customer_id} deleted"}), 200
    else:
        return jsonify({"error": f"Customer with ID {customer_id} not found"}), 404
