from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
import markdown

from . import util

import random

class NewEntryForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(label="Content", widget=forms.Textarea)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def new_page(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "encyclopedia/new.html", {
        "form": form
         })
            
    return render(request, "encyclopedia/new.html", {
        "form": NewEntryForm()
    })

def md_html(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)
    
def entry(request, title):
    html_content = md_html(title)
    if html_content == None:
        return render(request, "encyclopedia/404.html",  {
            "message": "The entry you are looking for does not exist, consider creating this page"
            })
    else: 
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content
        } )

# def random_page(request):
   # entries = util.list_entries()
    # selected_page = random.choice(entries)
    # return HttpResponseRedirect(reverse("wiki", args=[selected_page]))
## not working yet, still to define how the URL is served from the list of entries
