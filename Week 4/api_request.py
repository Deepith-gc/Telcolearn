import requests
# GET METHOD
url = "https://jsonplaceholder.typicode.com/posts"
# response = requests.get(url)
# print(response.json())

#POST METHOD
data = {
    "userID":0,
    "id":1000,
    "title":"Telco",
    "body":"Devops and Cloud"
}
resp = requests.post(url,json=data)
print("Response:",resp.json())
print("Status:",resp.status_code)