from django.shortcuts import render, get_object_or_404, redirect
from .models import Album
from .forms import AlbumForm

# Create your views here.


def album_list(request):
    albums = Album.objects.all()
    return render(request, 'index.html', {'albums': albums})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'details.html', {'album': album})


def new_album(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        return redirect(request, '')
    else:
        form = AlbumForm()
    return render(request, 'new_album.html', {'form': form})
