from django.shortcuts import render
from django import forms


from . import util

class NewEntryForm (forms.Form):
    title = forms.CharField(label="Title")
    body = forms.CharField(label="Body")
    

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def new(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            form.cleaned_data[entry]
            entries.append(entry)
        else:
            return render(request, "encyclopedia/new.html", {
        "form": form
         })
            
    return render(request, "encyclopedia/new.html", {
        "form": NewEntryForm()
    })
        