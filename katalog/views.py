from django.shortcuts import render
from katalog.models import CatalogItem
# Create your views here.
def show_catalog(request):
    data_catalog = CatalogItem.objects.all()
    context = {
        'list_catalog': data_catalog,
        'name': 'Rafa Maritza',
        'studentid': '2106651944',
    }
    return render(request, "katalog.html", context)
