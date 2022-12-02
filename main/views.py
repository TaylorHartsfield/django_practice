from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.


def index(reponse, id):
    try:
        ls = ToDoList.objects.get(id=id)
        Item = ls.item_set.all()
    except:
        return render(response, "main/base.html", {})

    return render(response, "main/base.html", {"list_name": ls})


def home(response):
    return render(response, "main/home.html", {})


def lists(response):
    all_lists = ToDoList.objects.all()
    print(all_lists)
    
    return render(response, "main/list.html", {"todolists":all_lists})