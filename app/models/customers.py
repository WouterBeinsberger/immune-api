from app.data.customers import CUSTOMERS

class Customers:
    def __init__(self):
        self.data = CUSTOMERS

    def all_customers(self):
        return self.data
    
    def get_customer_by_id(self, customer_id):
        for customer in self.data:
            if customer['id'] == customer_id:
                return customer
        return None
    
    def add_customer(self, new_customer_data):
        self.data.append(new_customer_data)

    def delete_customer_by_id(self, customer_id):
        for index, customer in enumerate(self.data):
            if customer['id'] == customer_id:
                del self.data[index]
                return True
        return False
    
    def update_customer_by_id(self, customer_id, new_data):
        for customer in self.data:
            if customer['id'] == customer_id:
                self._recursive_update(customer, new_data)
                return True
        return False
    
    def filter_customers(self, filter_criteria):
        filtered_customers = []
        for customer in self.data:
            # Convert all values to strings before checking against filter_criteria
            customer_str = {k: str(v) for k, v in customer.items()}
            if all(customer_str.get(key) == str(value) for key, value in filter_criteria.items()):
                filtered_customers.append(customer)
        return filtered_customers

    def _recursive_update(self, original, new_data):
        for key, value in new_data.items():
            if isinstance(value, dict) and key in original:
                self._recursive_update(original[key], value)
            elif key in original:
                original[key] = value