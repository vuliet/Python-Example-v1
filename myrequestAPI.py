import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.json())  # In dữ liệu JSON
