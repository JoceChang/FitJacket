from django.shortcuts import render

def user(request):
    return render(request, 'accounts/user.html')
# Create your views here.
