from django.http import HttpResponse
from django.shortcuts import render

from main.models import Artist, Song


# Create your views here.
def show(request):
    # print("Hello there")
    # artist = Artist.objects.order_by("?").first() # to get random value from the albums
    # print(artist)
    # albums = artist.album_set.all()
    # print(albums)
    # for alb in albums:
    #     print(alb.name, alb.release_year, "Album")
    #     songs = alb.songs.all()
    #     print(len(songs), "Songs")
    #     for s in songs:
    #         print("Songs - ", s.title, s.duration)

    song = Song.objects.order_by("?").first()
    print(song)
    album = song.album
    print(album)
    artists = album.artists.all().values("name")
    # for art in artists:
    print(artists)

    return HttpResponse("Check the results on the console")
