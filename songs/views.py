from re import template
from django.shortcuts import render
from .models import Song
from django.views.generic import ListView
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request,'index.html')

def search(request):
      return render(request,'search.html')

class SearchResultsView(ListView):
    model = Song
    template_name = "search.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Song.objects.filter(
            Q(name__icontains=query) | Q(singer__icontains=query)
        )
        return object_list


# def search(ListView):
#   model = Song
#   template_name = 'search.html'
   
#    def get_queryset(self):  # new
#         query = self.request.GET.get("q")
#         object_list = City.objects.filter(
#             Q(name__icontains=query) | Q(state__icontains=query)
#         )
#         return object_list






