from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from django.utils import timezone
from datetime import date

# from .models import ToDo

# Create your views here.
def index(req):
	return render(req, "add/add.html")

def todos(request, id):
	# list_todo = get_list_or_404(ToDo, pk=id)
	list_todo = {
		"todo_text": "testing to do 1",
		"due_date": date
	}

	print(list_todo["due_date"])
	return render(request, "add/index.html", {"todo_list":list_todo})
