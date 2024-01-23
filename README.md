# Product Management API Documentation

Welcome to the Product Management API documentation! This API allows you to perform various operations related to managing products, including adding new products, retrieving product details, updating product information, deleting products, and obtaining a list of top products based on retrieval counts.

## 1. Add a New Product

* **Endpoint:** `/add/`
* **Method:** `POST`

### Synopsis:
This endpoint enables you to add a new product to the system. Send a POST request with the necessary product details, including the title, description, and price.

### Example Usage:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"title": "New Product", "description": "A fantastic new product", "price": 29.99}' http://your-api-url/add/
# 2. Retrieve All Products

* **Endpoint:** `/detail/`
* **Method:** `GET`

### Synopsis:
Use this endpoint to retrieve details about all products currently available in the system.

### Example Usage:
```bash
curl http://your-api-url/detail/

### 3. Retrieve or Update a Specific Product

```markdown
# 3. Retrieve or Update a Specific Product

* **Endpoint:** `/detail/{product_id}/`
* **Methods:** `GET`, `PUT`, `DELETE`

### Synopsis:
This endpoint allows you to retrieve, update, or delete details for a specific product. Send a GET request to view details, a PUT request to update information, or a DELETE request to remove the product.

### Example Usage:

- **Retrieve Product Details:**
  ```bash
  curl http://your-api-url/detail/{product_id}/

### 4. Retrieve Top Products

```markdown
# 4. Retrieve Top Products

* **Endpoint:** `/summary/{period}/`
* **Method:** `GET`

### Synopsis:
Get a list of the top 5 products based on retrieval counts. You can specify the period as 'all', 'last_day', or 'last_week' to view top products for different time frames.

### Example Usage:
```bash
curl http://your-api-url/summary/{period}/
