
from flask import Flask, request
import json
from http import HTTPStatus


app = Flask("_name_")

@app.get("/")
def home():
    return "Hello from flask"

# @app.post("/")
# @app.put("/")
# @app.patch("/")
# @app.delete("/")



@app.get("/test")
def test():
    return "this is another endpoint"


# This is a JSON implementation
@app.get("/api/about")
def about():
    name={"name":"Vonda"}
    return json.dumps(name)


products = []


@app.get("/api/products")
def get_products():
    return json.dumps(products), HTTPStatus.OK

@app.post("/api/products")
def save_product():
    product = request.get_json()
    print(f"product {product}")
    products.append(product)
    return "Product saved", 201

# Put a product
@app.put("/api/products/<int:index>")
def update_product(index):
    update_product = request.get_json()
    print(f"update the product with index {index}")

    
    if 0 <= index < len(products):
        products[index] = updated_product
        return json.dumps(updated_product)
    else:
        return "That index does not exist", 404
    

# DELETE a product
@app.delete("/api/products/<int:index")
def delete_product(index):
    print(f"delete the product with index {index}")

    if index >= 0 and index <len(products):
        deleted_product = products.pop(index)
        return json.dumps(delete_product)
    else:
        return "That index does not exist"



    return "Product deleted"



app.run(debug=True)
