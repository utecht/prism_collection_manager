from django.shortcuts import render
from collection import models
from django.contrib.auth.decorators import login_required
from django import forms
from trix.widgets import TrixEditor
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def home(request):
    collections = models.Collection.objects.all()
    return render(request,
                  'collection/home.html',
                  {'collections': collections})

class EditorForm(forms.Form):
    content = forms.CharField(widget=TrixEditor)

@login_required()
def editor(request, collection_short_name):
    collection = models.Collection.objects.get(short_name=collection_short_name)
    if request.method == 'POST':
        form = EditorForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            collection.content = form.cleaned_data['content']
            collection.save()
            return HttpResponseRedirect(reverse('collection', args=(collection.short_name,)))
    form = EditorForm({'content': collection.content})
    return render(request,
                  'collection/editor.html',
                  {'collection': collection,
                   'form': form})

def collection(request, collection_short_name):
    collection = models.Collection.objects.get(short_name=collection_short_name)
    return render(request,
                  'collection/collection.html',
                  {'collection': collection})
