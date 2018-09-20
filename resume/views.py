from django.shortcuts import render

def index(request):
	return render(request, 'resume/index.html', {})

def about(request):
	return render(request, 'resume/about.html', {})


