from django.shortcuts import render
from .models import Tasks

# Create your views here.
def index(request):
    return render(request, 'main/index.html')