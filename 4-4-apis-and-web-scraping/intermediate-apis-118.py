## 2. API Authentication ##

# Create a dictionary of headers containing our Authorization header.
headers = {"Authorization": "token 1f36137fbbe1602f779300dad26e4c1b7fbab631"}

# Make a GET request to the GitHub API with our headers.
# This API endpoint will give us details about Vik Paruchuri.
response = requests.get("https://api.github.com/users/VikParuchuri", headers=headers)

# Print the content of the response.  As you can see, this token corresponds to the account of Vik Paruchuri.
#print(response.json())

token_auth = {'Authorization': 'token 1f36137fbbe1602f779300dad26e4c1b7fbab631'}
response_orgs = requests.get('https://api.github.com/users/VikParuchuri/orgs', headers=token_auth)
orgs = (response_orgs.json())

## 3. Endpoints and Objects ##

# We've loaded headers in.
torvalds = (requests.get('https://api.github.com/users/torvalds', headers=headers)).json()

## 4. Other Objects ##

# Enter your answer here.

hello_world = (requests.get('https://api.github.com/repos/octocat/Hello-World', headers=headers)).json()

## 5. Pagination ##

params = {"per_page": 50, "page": 1}
response = requests.get("https://api.github.com/users/VikParuchuri/starred", headers=headers, params=params)
page1_repos = response.json()

params = {"per_page": 50, "page": 2}
response = requests.get("https://api.github.com/users/VikParuchuri/starred", headers=headers, params=params)
page2_repos = response.json()

## 6. User-Level Endpoints ##

# Enter your code here.

user = (requests.get('https://api.github.com/user', headers=headers)).json()

## 7. POST Requests ##

# Create the data we'll pass into the API endpoint.  While this endpoint only requires the "name" key, there are other optional keys.
payload = {"name": "test"}

# We need to pass in our authentication headers!
response = requests.post("https://api.github.com/user/repos", json=payload, headers=headers)
print(response.status_code)

payload2 = {'name': 'learning-about-apis'}
status = (requests.post('https://api.github.com/user/repos', json=payload2, headers=headers)).status_code
print(response2)

## 8. PUT/PATCH Requests ##

payload = {"description": "The best repository ever!", "name": "test"}
response = requests.patch("https://api.github.com/repos/VikParuchuri/test", json=payload, headers=headers)
print(response.status_code)


payload2 = {"description": "Learning about requests!", "name": "learning-about-apis"}
response2 = requests.patch("https://api.github.com/repos/VikParuchuri/learning-about-apis", json=payload2, headers=headers)
status = (response2.status_code)

## 9. DELETE Requests ##

response = requests.delete("https://api.github.com/repos/VikParuchuri/test", headers=headers)
print(response.status_code)

status = (requests.delete('https://api.github.com/repos/VikParuchuri/learning-about-apis', headers=headers)).status_code