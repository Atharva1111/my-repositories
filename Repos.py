import requests

#def repo():
print("Print")
r=requests.get("https://api.github.com/users/Atharva1111/repos")
size=len(r.json())
print(size)
#for i in range(size):
print(r.json()[0]['name'])
#print(repos)