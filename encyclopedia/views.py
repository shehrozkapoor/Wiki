from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from markdown2 import Markdown
from . import util
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def clicked_entry(request, entry):
    markdowner = Markdown()
    get_entry = util.get_entry(entry)
    return render(request, 'encyclopedia/clicked_entry.html',{"list":markdowner.convert(get_entry),"title":entry})

def edit(request, t):
    if request.method == "POST":
        content = request.POST.get("content")
        util.save_entry(t, content)
        return HttpResponseRedirect(reverse('encyclopedia:index'))
    return render(request, "encyclopedia/edit.html",{"title":t,"content":util.get_entry(t)})
def search_entries(request):
    entry = request.GET.get("search_entries")
    entry = entry.lower()
    get_entry = util.list_entries()
    lower_entry = []
    for i in get_entry:
        lower_entry.append(i.lower())
    matching = [s for s in lower_entry if entry in s]
    matching_cap = []
    if len(matching)==0:
        return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),"message":"No Entry Found With That Name"})
    for i in matching:
        matching_cap.append(i.upper())
    return render(request , "encyclopedia/index.html",{"entries":matching})

def search(request, title):
    entry = util.get_entry(title)
    markdowner = Markdown()
    if entry is not None:
        return render(request, "encyclopedia/show_result.html", {"show_data":markdowner.convert(entry)})
    return render(request, "encyclopedia/show_result.html", {"show_data":"Sorry No Data is Found With That Title"})

def create_new(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        if util.get_entry(title) is None:
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse('encyclopedia:index'))
        return render(request, 'encyclopedia/create_new.html',{"message":"Entry Already Exist With That Title"})    
    return render(request, 'encyclopedia/create_new.html')

def random_func(request):
    list_entriess = util.list_entries()
    random_entry = random.choice(list_entriess)
    markdowner = Markdown()
    return render(request, "encyclopedia/random.html", {"list":markdowner.convert(util.get_entry(random_entry))})