from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from main.models import Artist, Song
from main.serializers import ArtistSerializer, ArtistAlbumSerializer


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


@api_view(["GET", "POST"])
def save_or_fetch_artists(request):
    if request.method == "GET":
        artists = Artist.objects.all()
        serializer = ArtistSerializer(instance=artists, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "Added artist", "data": serializer.data})
    return None


@api_view(["GET"])
def fetch_one_artist(request, id):
    try:
        artist = Artist.objects.get(pk=id)
        serializer = ArtistSerializer(instance=artist)
        return Response(serializer.data)
    except:
        return Response({"error": "Artist not found"}, status=404)


@api_view(["DELETE"])
def delete_artist(request):
    try:
        artist = Artist.objects.get(pk=id)
        artist.delete()
        return Response({"Message": "Successfully deleted artist"})
    except:
        return Response({"error": "Artist not found"}, status=404)


@api_view(["PUT", "PATCH"])
def update_artist(request, id):
    try:
        artist = Artist.objects.get(pk=id)
        serializer = ArtistSerializer(instance=artist, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
    except:
        return Response({"error": "Artist not found"}, status=404)


@api_view(["GET"])
def albums_for_artist(request, id):
    # try:
    artist = Artist.objects.get(pk=id)
    serializer = ArtistAlbumSerializer(instance=artist)
    return Response(serializer.data)
# except:
#     return Response({"error": "Invalid Data"}, status=404)
