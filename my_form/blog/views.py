from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http  import HttpResponse
from django import forms

# Create your views here.

class UserForm(forms.Form):
    name = forms.CharField()
    img =forms.FileField()
# class TestForm(forms.Form):
#     name = forms.CharField(label='单行输入',max_length=10)
#     mulirow = forms.CharField(label="多行输入",max_length=100,widget=forms.Textarea)
#     choice = forms.ChoiceField(label='选择框',choices=(
#         ("learn","学习"),
#         ("test","测试"),
#         ("django","python"),
#     ))
#     bool = forms.BooleanField(required=False)
#     urrf = forms.URLField(label="url格式")
#     data=forms.DateField(label="日期格式")
#     email = forms.EmailField(label="邮箱格式")
#     file = forms.FileField(label="文件格式")
#     imge = forms.ImageField(label="图片上传")

def register(req):
    print(req.method) 
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            print (form.cleaned_data)

    
            return HttpResponse('Ok')
    else :
        form = UserForm()
    return render_to_response('register.html',{'form':form})
    # form = TestForm()
    # return render(req,'test.html',{'form':form})
