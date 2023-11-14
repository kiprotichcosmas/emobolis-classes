from django.shortcuts import render


# Create your views here.
def home(request):
    # return None
    return render(request, 'index.html')


def shop(request):
    # return None
    return render(request, 'shop.html')


def about(request):
    # return None
    return render(request, 'about.html')


def contact(request):
    # return None
    return render(request, 'contact.html')


def faq(request):
    # return None
    return render(request, 'faq.html')