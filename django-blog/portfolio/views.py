from django.shortcuts import render


def portfolio_index(request):
    return render(request, "index.html")
