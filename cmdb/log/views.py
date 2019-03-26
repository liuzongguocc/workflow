from django.shortcuts import render_to_response

# Create your views here.
from log.models import Employee
def  index(req):
    emp =Employee.objects.all()

    return render_to_response('index.html',{'emp':emp})
