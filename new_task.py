import requests

# GET Method
api_url = "https://jsonplaceholder.typicode.com/users/1"
response = requests.get(api_url)
json_response = response.json()
print(json_response)

# POST Method
api_url = "https://jsonplaceholder.typicode.com/posts"
new_post = {
    "userId": 10,
    "id": 10,
    "title": "Python practice",
    "body": "Hello, I am Maryam. Nice to meet you!"
}
json_response = requests.post(api_url, json=new_post)
print(json_response)

# PUT Method
api_url = "https://jsonplaceholder.typicode.com/users/1"
update_post = {
    "userId": 1,
    "id": 1,
    "title": "The Art of War",
    "body": "The Art of War is an ancient Chinese military text written by Sun Tzu around the 5th century BC."}
response = requests.get(api_url)
json_response = response.json()
print(json_response)
