import requests

url = "http://127.0.0.1:5000/predict"

customer_data = {
    "total_sales": 5000,
    "total_profit": 800,
    "total_quantity": 20,
    "number_of_orders": 5,
    "average_discount": 0.10,
    "average_shipping_days": 4
}

response = requests.post(
    url,
    json=customer_data
)

print("API Response:")
print(response.json())