from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request):
    # print(args,kwargs)
    return  render(request, 'welcome.html')


