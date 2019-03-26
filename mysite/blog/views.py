from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def blog_title(request):
    # blogs = BlogArticles.objects.all()
    return render(request,"blog/titles.html",{"blogs":blogs})

def index(request):
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    return render(request, 'hello.html',{'TutorialList': TutorialList,'string':blogs})