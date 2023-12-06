from flask import Blueprint, jsonify, request, abort
from app.auth import authorize
from app.models.customer import Customer
import json
import uuid

customer_bp = Blueprint("customer", __name__)

@customer_bp.route("/customers", methods=["GET"])
def get_all_customers():
    authorize()  # Check authorization before processing
    with open('app/data/customers.json') as file:
        customers = json.load(file)
    return jsonify(customers), 200

@customer_bp.route("/customer/<int:customer_id>", methods=["GET"])
def get_customer(customer_id):
    authorize()  # Check authorization before processing
    with open('app/data/customers.json') as file:
        customers = json.load(file)
        for customer in customers:
            if customer.get("id") == customer_id:
                return jsonify(customer), 200
        return jsonify({"error": "Customer not found"}), 404

@customer_bp.route("/customer", methods=["POST"])
def create_customer():
    authorize()  # Check authorization before processing
    data = request.get_json()
    new_customer = {
        "id": uuid.uuid4().int,
        "email": data.get("email"),
        "firstname": data.get("firstname"),
        "lastname": data.get("lastname"),
        "sendOptInMail": data.get("sendOptInMail"),
        "billing": data.get("billing")
    }

    with open('app/data/customers.json', 'r+') as file:
        customers = json.load(file)
        customers.append(new_customer)
        file.seek(0)
        json.dump(customers, file, indent=4)
    
    return jsonify(new_customer), 201

@customer_bp.route("/customer/<int:customer_id>", methods=["PUT"])
def update_customer(customer_id):
    authorize()  # Check authorization before processing
    data = request.get_json()
    # Remove the 'id' field from the request data if present
    if 'id' in data:
        del data['id']
    with open('app/data/customers.json', 'r+') as file:
        customers = json.load(file)
        for customer in customers:
            if customer.get("id") == customer_id:
                customer.update(data)
                file.seek(0)
                json.dump(customers, file, indent=4)
                return jsonify(customer), 200
        return jsonify({"error": "Customer not found"}), 404

@customer_bp.route("/customer/<int:customer_id>", methods=["PATCH"])
def patch_customer(customer_id):
    authorize()  # Check authorization before processing
    data = request.get_json()
    # Remove the 'id' field from the request data if present
    if 'id' in data:
        del data['id']
    with open('app/data/customers.json', 'r+') as file:
        customers = json.load(file)
        for customer in customers:
            if customer.get("id") == customer_id:
                for key, value in data.items():
                    if key in customer:
                        customer[key] = value
                file.seek(0)
                json.dump(customers, file, indent=4)
                return jsonify(customer), 200
        return jsonify({"error": "Customer not found"}), 404

@customer_bp.route("/customer/<int:customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    authorize()  # Check authorization before processing
    with open('app/data/customers.json', 'r+') as file:
        customers = json.load(file)
        for idx, customer in enumerate(customers):
            if customer.get("id") == customer_id:
                del customers[idx]
                file.seek(0)
                json.dump(customers, file, indent=4)
                return jsonify({"message": "Customer deleted"}), 200
        return jsonify({"error": "Customer not found"}), 404
