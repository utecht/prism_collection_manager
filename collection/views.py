from django.shortcuts import render
from collection import models

# Create your views here.
def home(request):
    collections = models.Collection.objects.all()
    return render(request,
                  'collection/home.html',
                  {'collections': collections})

def collection(request, collection_short_name):
    collection = models.Collection.objects.get(short_name=collection_short_name)
    return render(request,
                  'collection/collection.html',
                  {'collection': collection})
