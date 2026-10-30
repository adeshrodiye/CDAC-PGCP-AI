from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.shortcuts import HttpResponse


books = [
    {
        'title':'Python for Beginners',
        'author':'abc',
        'price':800
    },
    {
        'title':'Python Data Science',
        'author':'xyz',
        'price':1000
    },
    {
        'title':'Java Cookbook',
        'author':'pqr',
        'price':1200
    }
]

def home(request):
    context = {'books':books}
    # return HttpResponse('<h3>Welcome to my Book Store</h3>')
    return render(request, 'book/index.html',context)
def about(request):
    return render(request, 'book/about.html',{'title':'About Us'})