from django.shortcuts import render
from .models import Notes

def Show(request):
    return render(request,"index.html")

def create(request):
    return render(request,"Add.html")


def viewall(request):
    qs = Notes.objects.all()
    return render(request,"viewall.html",{"data":qs})

def saveNotes(request):
    id = request.POST.get("No")
    ti = request.POST.get("Title")
    des = request.POST.get("Desc")
    create = request.POST.get("create")
    update = request.POST.get("update")

    Notes(Description=des,No=id,Title=ti,Created_on=create,Updated_on=update).save()
    return render(request,"index.html",{"message":"Notes Created"})

def updateNotes(request):
    nid = request.GET.get("update_id")
    res = Notes.objects.get(No=nid)
    return render(request,"update.html",{"data":res})

def update_Notes(request):
    id = request.POST.get("n_id")
    na = request.POST.get("n_name")
    des = request.POST.get("n_desc")
    up = request.POST.get("n_up")
    Notes.objects.filter(No=id).update(Title=na,Description=des,Updated_on=up)
    return viewall(request)

def deleteNotes(request):
    did = request.POST.get("del_idno")
    Notes.objects.filter(No=did).delete()
    return viewall(request)