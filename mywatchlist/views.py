from django.shortcuts import render
from mywatchlist.models import WishlistFilmKu

from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data_barang_mywatchlist = WishlistFilmKu.objects.all()
    sudahDitonton = 0
    belumDitonton = 0
    pesan = ""
    for i in data_barang_mywatchlist:
        if i.film_watched == True:
            sudahDitonton += 1
        else:
            belumDitonton += 1
    if sudahDitonton >= belumDitonton:
        pesan = "Selamat, kamu sudah banyak menonton!"
    else:
        pesan = "Wah, kamu masih sedikit menonton!"
    context ={
        'list_film': data_barang_mywatchlist,
        'nama': 'Afiq Ilyasa Akmal',
        'pesan': pesan
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = WishlistFilmKu.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WishlistFilmKu.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


