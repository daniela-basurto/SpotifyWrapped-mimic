import requests

url = 'https://jsonplaceholder.typicode.com/posts'

myobj = {'title': 'Special Agent',
          'body': 'Leroy Jethro Gibbs',
          'userId': '1'}

response = requests.post(url, data = myobj)

print(response.status_code)
print(response.json())