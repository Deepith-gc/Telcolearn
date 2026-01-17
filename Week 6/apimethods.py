import requests


headers = {
    "Authorization": "Bearer token123",
    "Content-Type": "application/json"
}

base_url = "https://reqres.in/api/users"

get_response = requests.get(base_url, headers=headers)
print("GET Status:", get_response.status_code)
print("GET Response:", get_response.json()["data"][0])


post_data = {
    "name": "Ram",
    "job": "Student"
}

post_response = requests.post(base_url, headers=headers, json=post_data)
post_result = post_response.json()

print("\nPOST Status:", post_response.status_code)
print("POST Response:", post_result)


id = post_result["id"]
print("Extracted ID:", id)



put_data = {
    "name": "Ram",
    "job": "Developer"
}

put_response = requests.put(base_url + "/" + str(id), headers=headers, json=put_data)
print("\nPUT Status:", put_response.status_code)
print("PUT Response:", put_response.json())


patch_data = {
    "job": "Tester"
}

patch_response = requests.patch(base_url + "/" + str(id), headers=headers, json=patch_data)
print("\nPATCH Status:", patch_response.status_code)
print("PATCH Response:", patch_response.json())


delete_response = requests.delete(base_url + "/" + str(id), headers=headers)
print("\nDELETE Status:", delete_response.status_code)
print("Deleted ID:", id)