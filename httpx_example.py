import httpx

response = httpx.get("https://jsonplaceholder.typicode.com/posts")
print(response.status_code)
print(response.json())