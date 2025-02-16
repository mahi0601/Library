import requests

BASE_URL = "http://127.0.0.1:8000"

response = requests.get(f"{BASE_URL}/")
print(response.json())
# Test Get All Books
response = requests.get(f"{BASE_URL}/books/books", params={"page": 1, "page_size": 1})
print(response.json())

# Test Search by Title
response = requests.get(f"{BASE_URL}/books/books", params={"title": "The Adventures of Sherlock Holmes"})
print(response.json())

# Test Get Book by ID
response = requests.get(f"{BASE_URL}/books/books/12345")
print(response.json())
