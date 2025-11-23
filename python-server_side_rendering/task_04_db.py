from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)


def get_products_from_json(product_id=None):
    products = []
    error = None
    file_path = os.path.join(os.path.dirname(__file__), "products.json")

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        for item in data:
            products.append({
                "id": int(item.get("id")),
                "name": item.get("name"),
                "category": item.get("category"),
                "price": float(item.get("price")),
            })

        if product_id is not None:
            products = [p for p in products if p["id"] == product_id]

    except (FileNotFoundError, json.JSONDecodeError):
        products = []
        error = "Error reading JSON file"

    return products, error


def get_products_from_csv(product_id=None):
    products = []
    error = None
    file_path = os.path.join(os.path.dirname(__file__), "products.csv")

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    "id": int(row.get("id")),
                    "name": row.get("name"),
                    "category": row.get("category"),
                    "price": float(row.get("price")),
                })

        if product_id is not None:
            products = [p for p in products if p["id"] == product_id]

    except FileNotFoundError:
        products = []
        error = "Error reading CSV file"

    return products, error


def get_products_from_sqlite(product_id=None):
    products = []
    error = None
    db_path = os.path.join(os.path.dirname(__file__), "products.db")

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        if product_id is not None:
            cursor.execute(
                "SELECT id, name, category, price FROM Products WHERE id = ?",
                (product_id,)
            )
        else:
            cursor.execute("SELECT id, name, category, price FROM Products")

        rows = cursor.fetchall()
        conn.close()

        for row in rows:
            prod_id, name, category, price = row
            products.append({
                "id": int(prod_id),
                "name": name,
                "category": category,
                "price": float(price),
            })

    except sqlite3.Error:
        products = []
        error = "Database error"

    return products, error


@app.route("/products")
def products():
    source = request.args.get("source")
    id_param = request.args.get("id")

    product_id = None
    if id_param is not None:
        try:
            product_id = int(id_param)
        except ValueError:
            return render_template(
                "product_display.html",
                products=[],
                error="Product not found"
            )

    products = []
    error = None

    if source == "json":
        products, error = get_products_from_json(product_id)
    elif source == "csv":
        products, error = get_products_from_csv(product_id)
    elif source == "sql":
        products, error = get_products_from_sqlite(product_id)
    else:
        error = "Wrong source"

    if error is None and product_id is not None and not products:
        error = "Product not found"

    return render_template("product_display.html", products=products, error=error)


if __name__ == "__main__":
    app.run(debug=True, port=5000)