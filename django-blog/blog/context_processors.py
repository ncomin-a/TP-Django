from django.conf import settings


def portfolio(request):
    return {"PORTFOLIO_URL": settings.PORTFOLIO_URL}
