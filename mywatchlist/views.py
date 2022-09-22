from django.shortcuts import render
from mywatchlist.models import MywatchlistItem
from django.http import HttpResponse
from django.core import serializers
# Create your views here.

def show_mywatchlist(request):
    tontonan = ""
    mywatchlist_watched = MywatchlistItem.objects.filter(watched="Yes").count()>= MywatchlistItem.objects.filter(watched="No").count()
    if mywatchlist_watched == True:
        tontonan = "Selamat, kamu sudah banyak menonton!"
    else:
        tontonan = "Wah, kamu masih sedikit menonton!"
    data_mywatchlist = MywatchlistItem.objects.all()
    context = {
        'tontonan': tontonan,
        'list_mywatchlist': data_mywatchlist,
        'name': 'Rafa Maritza',
        'studentid': '2106651944',
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MywatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MywatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_html(request):
    data = MywatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("html", data), content_type="application/html")

def show_xml_by_id(request,id):
    data = MywatchlistItem.objects.all().filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request,id):
    data = MywatchlistItem.objects.all().filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")