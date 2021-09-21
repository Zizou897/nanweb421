from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html", locals())

def catagory(request):
    return render(request, "catagory.html", locals())

def about(request):
    return render(request, "about-us.html", locals())

def contact(request):
    return render(request, "contact.html", locals())

def detail(request):
    return render(request, "single-post.html", locals())