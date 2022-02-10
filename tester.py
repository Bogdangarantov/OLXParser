import json
with open("users_info.json") as f :
    info = json.load(f)
print(info['users'][0]['id']==830944177)

