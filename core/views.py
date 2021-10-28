from django.shortcuts import render

def index(request):
	return render(request, 'core/Home.html')

def about(request):
	return render(request, 'core/about.html')


def services(request):
	return render(request, 'core/service.html')

def contact(request):
	return render(request, 'core/contact.html')

