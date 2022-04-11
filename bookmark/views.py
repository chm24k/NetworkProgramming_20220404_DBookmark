from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from bookmark.models import Bookmark


class BookmarkListView(ListView):
    model = Bookmark
    #bookmark_list.html, {'bookmark_list': Bookmark.objects.all()}
    # render(request, 'bookmark/bookmark_list.html', {'bookmark_list': Bookmark.objects.all()})
