# myapp/views.py
from django.shortcuts import HttpResponse
from .models import DogecoinPrice
from CryptoMarket.Pobierz_Cene_DOGE import pobierz_dane_doge_binance
from django.shortcuts import render

def default_view(request):
    return render(request, 'default.html')  # Replace 'default.html' with your template

def get_doge_price(request):
    cena_dogecoin = pobierz_dane_doge_binance()

    if cena_dogecoin is not None:
        DogecoinPrice.objects.create(price=cena_dogecoin)
        return render(request, 'get_doge_price.html', {'cena_dogecoin': cena_dogecoin})
    else:
        return render(request, 'get_doge_price.html', {'error_message': 'Failed to fetch Dogecoin price.'})