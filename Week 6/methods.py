# import requests
# headers = {
#     "Authorization": "Bearer token123",
#     "Content-Type": "application/json"
# }

# base_url = "https://jsonplaceholder.typicode.com/posts"

# get_response = requests.get(base_url, headers=headers)
# print("GET Status:", get_response.status_code)
# print("GET Response (first item):", get_response.json()[0])


# post_data = {
#     "title": "Sample Title",
#     "body": "Sample Body",
#     "userId": 1
# }

# post_response = requests.post(base_url, headers=headers, json=post_data)
# post_result = post_response.json()

# print("\nPOST Status:", post_response.status_code)
# print("POST Response:", post_result)

# # Extract numeric field
# id = post_result["id"]
# print("Extracted ID:", id)



# put_data = {
#     "id": id,
#     "title": "Updated Title",
#     "body": "Updated Body",
#     "userId": 1
# }

# put_response = requests.put(base_url + "/" + str(id), headers=headers, json=put_data)
# print("\nPUT Status:", put_response.status_code)
# print("PUT Response:", put_response.json())



# patch_data = {
#     "title": "Patched Title"
# }

# patch_response = requests.patch(base_url + "/" + str(id), headers=headers, json=patch_data)
# print("\nPATCH Status:", patch_response.status_code)
# print("PATCH Response:", patch_response.json())


# delete_response = requests.delete(base_url + "/" + str(id), headers=headers)
# print("\nDELETE Status:", delete_response.status_code)
# print("Deleted ID:", id)

