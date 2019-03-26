from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import loader,Context
# Create your views here.
class Person(object):
    def __init__(self,name,age):    
        self.name =name
        self.age =age
    def hello(self):
        return "hello world"
        

def index(req,id):
    # per =Person("liuming",12)
    # list =[1,2,3,13]
    # return render_to_response('index.html',{'title':"123",'user':per,'list':list,'id':id})
    t = loader.get_template('index2.html')
    c = Context({'uname':'alen'})
    return HttpResponse(t.render(c))