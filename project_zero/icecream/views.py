from django.shortcuts import render
from django.http import HttpResponse
from .models import icecream_db

def icecream_list(request):
    icecreamss = []
    for i in range(len(icecream_db)):
        icecreams = icecream_db[i]
        icecreams["index"]=i
        
        icecreamss.append(icecreams)
        #icecreams += f"<a href='{i}'>{icecream_db[i]['name']}</a><br>"
    context = {"icecreams": icecreamss}
    return render(request, "icecream/icecream-list.html", context)

def icecream_dtl(request,pk):
    name = icecream_db[pk]["name"]
    img = icecream_db[pk]['img']
    description = ""
    for i in icecream_db[pk]["description"]:
        description += f"{i} <br>"
    context = {
        "name":name,
        "description":description,
        "d":img
    }
    return render(request,"icecream/icecreams-details.html",context )