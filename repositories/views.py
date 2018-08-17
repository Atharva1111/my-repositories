from django.shortcuts import render
import requests
from .models import Repos

# Create your views here.
def Repo(request):
	r = requests.get("https://api.github.com/users/Atharva1111/repos")
	names = []
	languages = []
	repos = []
	size = len(r.json())
	for i in range(size):
		names.append(r.json()[i]['name'])
		languages.append(r.json()[i]['language'])
		if(languages[i]==None):
			languages[i]="None"
	return render(request, 'templates.html', {'names' : names, 'languages' : languages})