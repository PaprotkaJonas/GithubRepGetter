import requests
import json

#########################
# Replace with your GitHub username
username = "KingfernJohn"
#########################

response = requests.get(f"https://api.github.com/users/{username}/repos")
data = json.loads(response.text)
formatted_data = {"username": username, "repositories": []}

for repo in data:
    repository = {
        "name": repo["name"],
        "stars": repo["stargazers_count"],
        "license": repo["license"]["name"] if repo["license"] else None,
        "language": repo["language"]
    }
    formatted_data["repositories"].append(repository)

json_data = json.dumps(formatted_data, indent=4)

with open(f"{username}-gitdata.json", "w") as f:
    f.write(json_data)

print(json_data)
