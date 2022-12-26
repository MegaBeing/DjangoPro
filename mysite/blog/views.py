from django.shortcuts import render
from django.http import HttpResponse,Http404
# Create your views here.
post={
"1":"Welcome to first ever blog on my website",
"2":"Light tears darkness",
"3":"Bring Children to God"
}
def index(request):         #blog/posts
    return render(request,'blog/index.html',{
        "posts": post
    })

def posts(request,slug):        #blog/posts/<slug>
    try:
        ctext=post[slug]
        return render(request,"blog/posts.html",{
            "title": slug,
            "heading": ctext
        })
    except:
        return Http404()

def mainPage(request):          #blog/
    return HttpResponse("This is the main page of our blog")
