from django.shortcuts import render

def home_view(request):
    user = request.user

    context = {'user':user,'hello':'hello world'}
    return render(request,'main/home.html',context)