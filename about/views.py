from django.shortcuts import render
from django.views.generic import ListView
from .models import Team

# Create your views here.
# def about(request):
#     return render(request, "about/about.html")


def about(request):
    object_list = Team.objects.all()
    context = {'object_list':object_list}
    for team in object_list:
        print(team.name)
        print(team.role)
        print(team.email)
    return render(request, "about/about.html", context=context)

def index(request):
    return render(request, "home/index.html")