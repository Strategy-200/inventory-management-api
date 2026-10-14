# Inventory Management API

A RESTful API built using Python and FastAPI to manage products and inventory.

## Features

- Create a new product
- Retrieve all products
- Retrieve a product by ID
- Update product details
- Delete a product
- Filter products by category
- Filter products by price range
- Retrieve low-stock products
- Calculate total inventory value
- Validate product data using Pydantic
- Handle errors using HTTP exceptions

## Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn
- Git and GitHub

## Project Structure

```text
inventory-management-api/
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd inventory-management-api
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your repository URL.

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment on Windows

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Start the application

```bash
uvicorn main:app --reload
```

### 6. Open the API documentation

Visit:

http://127.0.0.1:8000/docs

Use the Swagger UI interface to test the API endpoints.

## Available Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/products` | Create a product |
| GET | `/products` | Retrieve all products |
| GET | `/products/{product_id}` | Retrieve a product by ID |
| PUT | `/products/{product_id}` | Update a product |
| DELETE | `/products/{product_id}` | Delete a product |
| GET | `/products/filter/category` | Filter by category |
| GET | `/products/filter/price` | Filter by price range |
| GET | `/inventory/low-stock` | Find low-stock products |
| GET | `/inventory/value` | Calculate inventory value |

## Note

This project currently stores products in an in-memory Python dictionary. Product data is lost when the application restarts. Database persistence can be added in a future version.

## Future Improvements

- PostgreSQL database integration
- Automated API tests using pytest
- Pagination and sorting
- Authentication and authorization
- Docker support