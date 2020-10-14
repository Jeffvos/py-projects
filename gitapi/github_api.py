import requests
import json

with open('config.json') as file:
    CONFIG = json.load(file)


def get_git():
    r = requests.get(CONFIG['base-url']+CONFIG['repos'])
    git_response = r.json()
    git_response.sort(key=lambda items: items['created_at'], reverse=True)
    return r.json()


for item in get_git():
    print(item['name'])
    print(item['description'])
    print(item['html_url'])
    print('\n')

