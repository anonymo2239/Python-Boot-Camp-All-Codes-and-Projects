import requests
import json

# GET: veri alırken get kullanılır
userId = input("Enter a ID: ")
get_url = f"https://jsonplaceholder.typicode.com/todos/{userId}"

get_response = requests.get(get_url)
print(get_response.json())

# POST: veri yollarken post kullanılır (burada database'e ekliyormuş gibi yapıyor ama eklemiyor. Normalde ekliyor)
to_do_item = {"userId": 2, "title": "pick up home", "completed": True}  # bu bir dictionary
post_url = "https://jsonplaceholder.typicode.com/todos"
# optional header
headers = {"Content-Type": "application/json"}
post_response = requests.post(post_url, json=to_do_item, headers=headers)
print(post_response.json())
zort = json.dumps(to_do_item)  # dumps dict'i json a dönüştürmeye yarıyor. artık bu bir json
print(zort)
