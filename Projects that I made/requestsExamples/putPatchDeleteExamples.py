import requests

get_url = "https://jsonplaceholder.typicode.com/todos/15"

get_example = requests.get(get_url)
print(get_example.json())

# PUT: bir objedeki tüm parametreleri değiştirmeye yarar
to_do_item_15 = {"userId": 17, "title": "piss", "completed": False}
put_example = requests.put(url=get_url, json=to_do_item_15)
print(put_example.json())

# PATCH: bir objedeki sadece bir parametreyi değiştirmeye yarar. Genelde kullanılmaz.
to_do_item_15 = {"title": "come_on"}
patch_example = requests.patch(url=get_url, json=to_do_item_15)
print(patch_example.json())

#DELETE: silme
delete_response = requests.delete(get_url)
print(delete_response.json())
print(delete_response.status_code)

