from django.shortcuts import render

def search(request):
    return render(request, 'exercises/search.html')
# Create your views here.
