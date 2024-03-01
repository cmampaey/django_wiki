from django.shortcuts import render
from django import forms


from . import util

class NewEntryForm (forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(label="Content")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def new(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
        else:
            return render(request, "encyclopedia/new.html", {
        "form": form
         })
            
    return render(request, "encyclopedia/new.html", {
        "form": NewEntryForm()
    })
        