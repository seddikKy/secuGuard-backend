import requests
from getpass import getpass
endpoint = "http://192.168.0.11:8000/api-token-auth/" 
username ="seddik" #input("entrer votre nom d'utilisateur : \n")
password = 1 #getpass("Entrer votre password :  \n")
auth_response = requests.post(endpoint, json={'username':username,'password':password})

print(auth_response.json())

# endpoint = "http://192.168.0.11:8000/core/api/zones/"
# header = {
#         'Authorization' : 'Token 480e1f0dedfc650ecd228a5a8291a18e0f5f850f'
#     }

# response = requests.get(endpoint,headers=header)
# print(response.json())
# print(response.status_code)