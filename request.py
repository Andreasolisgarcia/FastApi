import requests

# creating a GET request
r = requests.get('https://jsonplaceholder.typicode.com/posts/1')


# getting the response elements
response_dict = r.json
response_header = r.headers
status_code = r.status_code

print(response_dict)