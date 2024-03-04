from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import util

import random

class NewEntryForm (forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(label="Content")

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

## not working yet, still to define how the URL is served from the list of entries
# def random_page(request):
   # entries = util.list_entries()
    # selected_page = random.choice(entries)
    # return HttpResponseRedirect(reverse("wiki", args=[selected_page]))