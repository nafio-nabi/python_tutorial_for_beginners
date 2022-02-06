import requests

response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
my_projects = response.json()

for project in my_projects:
    print(f"Project Name: {project['name']}\nProject Url: {project['web_url']}\n")

# print(response)
# print(response.text)
# print(type(response.text))

# print(response.json())
# print(response.json()[0])
# print(response.json()[0]["id"])
# print(type(response.json()))