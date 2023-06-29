from django.shortcuts import render
from django.shortcuts import redirect

from .models import Artist, Song, Playlist
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView


#  class Home is child of TemplateView

class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["playlists"] = Playlist.objects.all()
        return context

class About(TemplateView):
    template_name = "about.html"

class ArtistList(TemplateView):
    template_name = "artist_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # self.request.GET === req.query in express

        print(self.request.GET)
        name = self.request.GET.get('name')
        if name != None:
            # regex matcher 
            context["artists"] = Artist.objects.filter(name__icontains = name)
        else:
            context["artists"] = Artist.objects.all()

        return context


class ArtistDetail(DetailView):
    model = Artist
    template_name = "artist_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["playlists"] = Playlist.objects.all()
        return context


class ArtistCreate(CreateView):
    template_name = "artist_create.html"
    model = Artist
    fields = ['name', 'img', 'bio', 'verified_artist']
    success_url = "/artists/"

class ArtistUpdate(UpdateView):
    model = Artist
    fields = ['name', 'img', 'bio', 'verified_artist']
    template_name = 'artist_update.html'
    success_url = '/artists/'

class ArtistDelete(DeleteView):
    model = Artist
    template_name = "artist_delete_confirmation.html"
    success_url = "/artists/"

# class Song:
#     def __init__(self, title, album):
#         self.title = title
#         self.album = album

# songs = [
#     Song("Lost", "stressed & depressed by The Circle Sessions"),
#     Song("Never Ending Song", "Never Ending Song")
# ]

class SongList(TemplateView):
    template_name = "song_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["songs"] = songs
        return context
        
class SongCreate(View):
    def post(self, request, pk):
        title = request.POST.get("title")
        length = request.POST.get("length")
        artist = Artist.objects.get(pk=pk)
        Song.objects.create(title=title, length=length, artist=artist)
        return redirect('artist_detail', pk=pk)

class PlaylistSongAssoc(View):

    def get(self, request, pk, song_pk):
        # get the query param from the url
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            # get the playlist by the id and
            # remove from the join table the given song_id
            Playlist.objects.get(pk=pk).songs.remove(song_pk)
        if assoc == "add":
            # get the playlist by the id and
            # add to the join table the given song_id
            Playlist.objects.get(pk=pk).songs.add(song_pk)
        return redirect('home')


# Create your views here.

