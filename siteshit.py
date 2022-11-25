import urllib.request
import requests
'''
#opener = urllib.request.build_opener()
#response = opener.open("https://httpbin.org/get")
#print(response.read())

response = requests.get("https://httpbin.org/get")
print(response.content)
print(f'Datatype - {type(response.content)}')
response = requests.get("https://httpbin.org/")
print(response.content)
print(f'Datatype - {type(response.content)}')

print(response.text)
print(f'Datatype - {type(response.content)}')
'''
response = requests.post('https://httpbin.org/post',
                         data={"Test data": "my_forms"},
                         headers={"h1": "Test title"})

print(response.text)
