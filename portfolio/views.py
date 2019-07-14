import requests
from django.shortcuts import render, redirect

# Create your views here.

def bio(request):
    print('rendering bio page')
    
    context = {
        'title': 'Bio' ,
        'bground': 'bg_bio',
    }
    return render(request, 'bio.html', context)
    
def ideas(request):
    print('rendering product ideas page')
    
    context = {
        'title': 'Ideas' ,
        'bground': 'bg_product_ideas',
    }
    return render(request, 'ideas.html', context)
    
def blog(request):
    print('rendering blog page')
    
    context = {
        'title': 'Blog' ,
        'bground': 'bg_blog',
    }
    return render(request, 'blog.html', context)
    
def send_email(request):
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    
    #send email using mailgun API
    requests.post(
        "https://api.mailgun.net/v3/sandboxb364b46bb57a4f7bb415814c33300234.mailgun.org/messages",
        auth=("api", "863844d01786527a48f7d716f56820d0"),
        data={"from": name + "<" + email + ">",
            "to": "Andrew Thornton <awjdthornton@gmail.com>",
            "subject": "Message from "+name,
            "text": message})
    
    return redirect ("/")

