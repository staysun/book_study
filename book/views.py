from django.shortcuts import render,redirect,HttpResponse

from book.models import *
# Create your views here.


def base(req):
    return render(req, "base.html")


def index(req):
    return render(req, "index.html")



def addAuthor(req):
    try:
        name = req.GET.get("name")
        Author.objects.create(name=name)
    except:
        return render(req, "addAuthor.html")

    return render(req,"addAuthor.html")

def showAuthor(req):

    all_Author_list=Author.objects.filter()

    return render(req, "showAuthor.html", {"all_Author_list": all_Author_list})


def addPublisher(req):
    try:
        name = req.GET.get("name")
        address=req.GET.get("address")
        Publisher.objects.create(name=name,address=address)
    except:
        return render(req, "addPublisher.html")

    return render(req,"addPublisher.html")


def showPublisher(req):

    all_Publisher_list=Publisher.objects.filter()

    return render(req, "showPublisher.html", {"all_Publisher_list": all_Publisher_list})



def delPublisher(req):
    id = req.GET.get("id")
    Publisher.objects.filter(id=id).delete()
    return redirect("/showPublisher/")

def delAuthor(req):
    id = req.GET.get("id")
    Author.objects.filter(id=id).delete()
    return redirect("/showAuthor/")


def addbook(req):
    type=req.GET.get("type")
    if type=="1":
        all_Publisher_list = Publisher.objects.filter()
        all_Author_list = Author.objects.filter()
        return render(req, "addbook.html", locals())
    # return render(req, "addbook.html")
    elif type=="2":
        Publisher_id=req.GET.get("publisher")
        Author_id=req.GET.get("author")
        name=req.GET.get("name")
        time=req.GET.get("time")
        print(Publisher_id,Author_id,name,time)
        Book.objects.create(name=name,)
        return HttpResponse("注册成功")