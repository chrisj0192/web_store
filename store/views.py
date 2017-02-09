from django.shortcuts import render

# Create your views here.

def inicio(request):
	title_var = " D'Vouse"
	context = {
		'titulo': title_var
	}
	return render(request, "index.html", context)

def login(request):
	return render(request, "login.html", {})