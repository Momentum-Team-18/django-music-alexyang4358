from django.shortcuts import render, get_object_or_404
from .models import Album

# Create your views here.


def album_list(request):
    albums = Album.objects.all()
    return render(request, 'index.html', {'albums': albums})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'details.html', {'album': album})
