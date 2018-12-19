from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict={'insert_me':'Hello i am from veiws.py'}
    return render(request,'HelloWorldApp/index.html',context=my_dict)
def indexs(request):
    return HttpResponse("Hello World s")
