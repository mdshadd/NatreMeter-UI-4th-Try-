from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import permission_required

# Create your views here.

def home(request):
    return render(request, 'account/prof.html')
