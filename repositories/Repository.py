import requests

def repository()
	r = requests.get("https://api.github.com/users/mistryharsh28/repos")
	names = []
	languages = []
	repos = []
	size = len(r.json())
	for i in range(size):
		names.append(r.json()[i]['name'])
		languages.append(r.json()[i]['language'])
		if(languages[i]==None):
			languages[i]="None"
	return(names)