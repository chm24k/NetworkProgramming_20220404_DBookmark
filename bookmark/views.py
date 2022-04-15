from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from bookmark.models import Bookmark


class BookmarkListView(ListView):
    model = Bookmark
    #bookmark_list.html, {'bookmark_list': Bookmark.objects.all()}
    # render(request, 'bookmark/bookmark_list.html', {'bookmark_list': Bookmark.objects.all()})

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['name', 'url']    #'__all__'도 가능
    template_name_suffix = '_create'  #bookmark_form.html --> bookmark_create.html
    success_url = reverse_lazy('bookmark:list')