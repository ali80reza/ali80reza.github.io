from django.shortcuts import redirect,render
from store.models import Product,Category

def frontpage (request):
    products = Product.objects.all()
    return render (request , 'core/frontpage.html' , {'products':products})


def about (request):
    return render (request , 'core/about.html')
def whatsapp (request):
    return render (request , 'core/whatsapp.html')
def instagram (request):
    return render (request , 'core/instagram.html')


def chat (request , query):
    query = request.GET.get ('query' , '')
    return render (request , 'core/main.html' , {'query' : query})
