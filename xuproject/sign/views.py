from django.shortcuts import render

# Create your views here.

# from django.http import HttpResponse
#
# #create your views here.
#
# def index(request):
#     return HttpResponse('Hello django')

from django.shortcuts import render

#create you views here.

#登录页面

def index(request):
    return render(request,'index.html')