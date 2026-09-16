from .models import Item
from django.shortcuts import render

# Create your views here.

def homepage(request):
    # items = Item.objects.all()
    return render(request, 'dclutterd/home.html')