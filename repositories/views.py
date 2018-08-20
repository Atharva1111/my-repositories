from django.shortcuts import render
import requests
from .models import Repos

# Create your views here.
def Repo(request):
	r = requests.get("https://api.github.com/users/Atharva1111/repos")
#	names = []
	names_list = []
#	languages = []
	languages_list = []
	repos = []
	size=len(r.json())
	'''
	for i in range(size):
		names.append(r.json()[i]['name'])
		languages.append(r.json()[i]['language'])

	for name in names:
		print(name)

	for language in languages:
		print(langauage)
	'''
	for obj in Repos.objects.all():
		repos.append(str(obj))
		data=Repos.objects.get(name=obj)
		names_list.append(data.name)
		languages_list.append(data.language)
	
	for i in range(size):
		if(r.json()[i]['name'] not in repos):
			Repos.objects.create(name=r.json()[i]['name'], language=r.json()[i]['language'])

#	return render(request, 'templates.html', {'names' : names, 'languages' : languages})	
	return render(request, 'templates.html', {'names_list' : names_list, 'languages_list' : languages_list})