<!DOCTYPE html>
<html>

<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 40px;
        }

        h1, h2, h3, h4, h5, h6 {
            color: #333;
        }

        h1 {
            border-bottom: 2px solid #333;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }

        h2 {
            margin-top: 40px;
            margin-bottom: 20px;
        }

        h3 {
            margin-top: 30px;
            margin-bottom: 15px;
        }

        p {
            margin-bottom: 20px;
        }

        code {
            background-color: #f4f4f4;
            border: 1px solid #ddd;
            padding: 5px;
            font-family: "Courier New", Courier, monospace;
        }

        pre {
            background-color: #f4f4f4;
            border: 1px solid #ddd;
            padding: 10px;
            overflow: auto;
            font-family: "Courier New", Courier, monospace;
        }
    </style>
</head>

<body>

    <h1>Product Management API Documentation</h1>

    <p>Welcome to the Product Management API documentation! This API allows you to perform various operations related to managing products, including adding new products, retrieving product details, updating product information, deleting products, and obtaining a list of top products based on retrieval counts.</p>

    <h2>1. Add a New Product</h2>

    <strong>Endpoint:</strong> <code>/add_product/</code><br>
    <strong>Method:</strong> <code>POST</code>

    <h3>Synopsis:</h3>
    <p>This endpoint enables you to add a new product to the system. Send a POST request with the necessary product details, including the title, description, and price.</p>

    <h3>Example Usage:</h3>
    <pre>
curl -X POST -H "Content-Type: application/json" -d '{"title": "New Product", "description": "A fantastic new product", "price": 29.99}' http://your-api-url/add_product/
    </pre>

    <h2>2. Retrieve All Products</h2>

    <strong>Endpoint:</strong> <code>/all_product/</code><br>
    <strong>Method:</strong> <code>GET</code>

    <h3>Synopsis:</h3>
    <p>Use this endpoint to retrieve details about all products currently available in the system.</p>

    <h3>Example Usage:</h3>
    <pre>
curl http://your-api-url/all_product/
    </pre>

    <h2>3. Retrieve or Update a Specific Product</h2>

    <strong>Endpoint:</strong> <code>/product_detail/{product_id}/</code><br>
    <strong>Methods:</strong> <code>GET</code>, <code>PUT</code>, <code>DELETE</code>

    <h3>Synopsis:</h3>
    <p>This endpoint allows you to retrieve, update, or delete details for a specific product. Send a GET request to view details, a PUT request to update information, or a DELETE request to remove the product.</p>

    <h3>Example Usage:</h3>
    <ul>
        <li>Retrieve Product Details:
            <pre>
curl http://your-api-url/product_detail/1/
            </pre>
        </li>
        <li>Update Product Information:
            <pre>
curl -X PUT -H "Content-Type: application/json" -d '{"title": "Updated Product", "description": "An improved version", "price": 39.99}' http://your-api-url/product_detail/1/
            </pre>
        </li>
        <li>Delete a Product:
            <pre>
curl -X DELETE http://your-api-url/product_detail/1/
            </pre>
        </li>
    </ul>

    <h2>4. Retrieve Top Products</h2>

    <strong>Endpoint:</strong> <code>/top_products/{period}/</code><br>
    <strong>Method:</strong> <code>GET</code>

    <h3>Synopsis:</h3>
    <p>Get a list of the top 5 products based on retrieval counts. You can specify the period as 'all', 'last_day', or 'last_week' to view top products for different time frames.</p>

    <h3>Example Usage:</h3>
    <pre>
curl http://your-api-url/top_products/last_week/
    </pre>

    <p>That's it! Feel free to explore and interact with the API using the provided endpoints. If you have any questions or issues, please refer to the API documentation or contact our support team. Happy managing your products!</p>

</body>

</html>
