import requests

host = "localhost:9696"

url = f'http://{host}/predict'

order= {"order_id" :  1478329,
            "customer_id"  : 116992,
            "restaurant_name" : "Tres Carnes",
            "cuisine_type" : "Mexican",
            "cost_of_the_order" : 33.32,
            "day_of_the_week" : "Weekday"}
try:
    response = requests.post(url, json=order, timeout=10)   # <-- use json=, not data=
    response.raise_for_status()                               # raises if 4xx/5xx
    # Optionally ensure the server claims JSON
    if "application/json" not in response.headers.get("Content-Type",""):
        print("Non-JSON response:\n", response.text)
    else:
        predictions = response.json()
        if "prediction" in predictions.keys():
            order_id = predictions["order_id"]
            customer_id = predictions["customer_id"]
            prediction = predictions["prediction"]
            print(f"order id {order_id}")
            print(f"customer id {customer_id}")
            print(f"predictions {prediction}")
        else:
            column = predictions["detail"][0]["loc"][1]
            msg = predictions["detail"][0]["msg"]
            input = predictions["detail"][0]["input"]
            print(f"wrong input for {column}, {msg}, got {input}")
except requests.HTTPError as e:
    print("HTTP error:", e, "Body:", response.text if 'r' in locals() else "")
except requests.exceptions.JSONDecodeError:
    print("Could not parse JSON. Raw body:\n", response.text)
except requests.RequestException as e:
    print("Request failed:", e)




# predictions = response.json()

# print(predictions)