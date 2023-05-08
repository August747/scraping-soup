from http.client import HTTPResponse

from django.shortcuts import render
from .models import TVShow


def top_tvshows(request):
    tvshows = TVShow.objects.all()

    context = {
        'tvshows': tvshows
    }

    return render(request, template_name='core/tvshows.html', context=context)


def scrape_tvshows(request):
    # add from index here
    return HTTPResponse(status='')
