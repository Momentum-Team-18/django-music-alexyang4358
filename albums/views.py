from django.shortcuts import render, get_object_or_404, redirect
from .models import Album, Artist
from .forms import AlbumForm


# Create your views here.


def album_list(request):
    albums = Album.objects.all()
    return render(request, 'extend/index.html', {'albums': albums})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'extend/details.html', {'album': album})


def artist_detail(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    return render(request, 'extend/artist_detail.html', {'artist': artist})


def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    album.delete()
    return redirect('home')


def new_album(request):
    if request.method == "GET":
        form = AlbumForm()
    else:
        form = AlbumForm(request.POST)
        album = form.save(commit=False)
        album.author = request.user
        album.save()
        return redirect('home')
    return render(request, 'extend/new_album.html', {'form': form})


def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            album = form.save(commit=False)
            album.author = request.user
            album.save()
            return redirect('album_detail', pk=pk)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'extend/edit_album.html', {'form': form})
