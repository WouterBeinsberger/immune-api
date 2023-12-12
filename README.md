<a name="readme-top"></a>

## IMMUNE-API

An api created to learn all about api calls

## Requirements

1. [python 3](https://www.python.org/downloads/) installed

After installing python make sure to add python to your PATH variable.
- on [windows](https://datatofish.com/add-python-to-windows-path/)
- on [mac](https://opensource.com/article/19/5/python-3-default-mac)

<p align="right">[<a href="#readme-top">back to top</a>]</p>

## Getting started

### Installation

To install the python packages needed, navigate to the project root folder and use the following command:
```
pip install -r requirements.txt
```

Add a `.env` file to the project root folder and fill in the following:
```
TOKEN=
```
<p align="right">[<a href="#readme-top">back to top</a>]</p>

## Usage

To start the api use the following command:
```
python main.py
```

**IMPORTANT:** if at any point the api stops working then you can reset the api. The application has a build in reset. If you close the application by using `ctrl+c` in the terminal the data will reset.

<p align="right">[<a href="#readme-top">back to top</a>]</p>

## Token Generation Endpoint

### Generate Token
- **Description:** Generates a bearer token for authorization.
- **HTTP Method:** GET
- **Endpoint:** `/token`
- **Request:** No request parameters needed.
- **Response:** Returns a bearer token for authorization.

<p align="right">[<a href="#readme-top">back to top</a>]</p>

## Customer Endpoints

*Note: To access these endpoints, include the generated token in the header as follows: Authorization: <generated_token>*


### Get All Customers
- **Description:** Get all customers' information.
- **HTTP Method:** GET
- **Endpoint:** `/customers`
- **Request Headers:** 
```
Content-Type: application/json
Accept: application/json
Authorization: <generated_token>
```
- **Request:** No request parameters needed.
- **Response:** Returns a list of all customers' data.

### Get Customer by ID
- **Description:** Get a specific customer's information by ID.
- **HTTP Method:** GET
- **Endpoint:** `/customer/<customer_id>`
- **Request Headers:** 
```
Content-Type: application/json
Accept: application/json
Authorization: <generated_token>
```
- **Request:** `<customer_id>` is a numerical value representing the customer's ID.
- **Response:** Returns the customer's data corresponding to the provided ID.

### Create New Customer
- **Description:** Create a new customer.
- **HTTP Method:** POST
- **Endpoint:** `/customer`
- **Request Headers:** 
```
Content-Type: application/json
Accept: application/json
Authorization: <generated_token>
```
- **Request:** Send JSON payload containing customer details.
- **Request body:**
```
{
    "billing": {
        "city": "Anytown",
        "country": "USA",
        "email": "john@example.com",
        "firstname": "John",
        "lastname": "Doe",
        "street": "123 Main St",
        "zipcode": "12345"
    },
    "email": "john@example.com",
    "firstname": "wouter",
    "lastname": "beinsberger",
    "sendOptInMail": false
}
```
*Note: ID of the customer is automatically generated upon creation*
- **Response:** Returns a success message with the newly created customer's ID.

### Update Customer
- **Description:** Update customer information.
- **HTTP Method:** PUT
- **Endpoint:** `/customer/<customer_id>`
- **Request Headers:** 
```
Content-Type: application/json
Accept: application/json
Authorization: <generated_token>
```
- **Request:** `<customer_id>` is a numerical value representing the customer's ID. Send JSON payload containing updated customer details.
- **Request body:**
```
{
    "billing": {
        "city": "Anytown",
        "country": "USA",
        "email": "john@example.com",
        "firstname": "John",
        "lastname": "Doe",
        "street": "123 Main St",
        "zipcode": "12345"
    },
    "email": "john@example.com",
    "firstname": "wouter",
    "lastname": "beinsberger",
    "sendOptInMail": false
}
```
*Note: The 'id' field cannot be updated.*
- **Response:** Returns a success message upon updating the customer's information.

### Partially Update Customer
- **Description:** Partially update customer information.
- **HTTP Method:** PATCH
- **Endpoint:** `/customer/<customer_id>`
- **Request Headers:** 
```
Content-Type: application/json
Accept: application/json
Authorization: <generated_token>
```
- **Request:** `<customer_id>` is a numerical value representing the customer's ID. Send JSON payload containing the fields to be updated. The 'id' field cannot be updated.
- **Request body:**
```
{
    "sendOptInMail": true,
    "lastname": "Test"
}
```
*Note: The 'id' field cannot be updated.*
**DO NOT** *update billing, it will break the api.*
- **Response:** Returns a success message upon partially updating the customer's information.

### Delete Customer
- **Description:** Delete a specific customer by ID.
- **HTTP Method:** DELETE
- **Endpoint:** `/customer/<customer_id>`
- **Request Headers:** 
```
Content-Type: application/json
Accept: application/json
Authorization: <generated_token>
```
- **Request:** `<customer_id>` is a numerical value representing the customer's ID.
- **Response:** Returns a success message upon deleting the customer.

<p align="right">[<a href="#readme-top">back to top</a>]</p>
