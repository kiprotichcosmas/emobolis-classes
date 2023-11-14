from django.shortcuts import render

from main_app.users import people


# Create your views here.

def home_page(request):
    name = "Cosmas Kiprotich"
    age = 18
    users = people
    data = {
        "name": name,
        "age": age,
        "users": people,
    }
    return render(request, "index.html", context=data)
