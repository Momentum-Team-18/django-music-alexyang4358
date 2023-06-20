"""
URL configuration for django_music project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from albums import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.album_list, name='home'),
    path('album/new', views.new_album, name='new_album'),
    path('album/<int:pk>', views.album_detail, name='album_detail'),
    path('album/<int:pk>/delete', views.delete_album, name='delete_album'),
    path('album/<int:pk>/edit', views.edit_album, name='edit_album'),
    path('artist/<int:artist_pk>', views.albums_by_artist,
         name='albums_by_artist'),
]
