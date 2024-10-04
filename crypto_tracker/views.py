import requests
from django.shortcuts import render

def home(request):
    crypto_data = {
        'bitcoin': {'usd': 40000},
        'ethereum': {'usd': 2500},
        'binancecoin': {'usd': 350},
        'cardano': {'usd': 1.20},
        'solana': {'usd': 35},}
    # Pass the data to the template
    context = {
        'crypto_data': crypto_data
    }

    return render(request, 'home.html', context)