from app import create_app
import json
import atexit

# Load initial data from customers.json
with open('app/data/customers.json', 'r') as file:
    initial_customers_data = json.load(file)

# Function to reset customers.json with initial data
def reset_customers_file():
    with open('app/data/customers.json', 'w') as file:
        json.dump(initial_customers_data, file, indent=4)

# Register reset_customers_file to run on program exit
atexit.register(reset_customers_file)

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
