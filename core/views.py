from django.shortcuts import render
# from services import ScrapeTVShowsService
from tvshows.models import TVShow


def index(request):
    # services = ScrapeTVShowsService()
    # top_tvshows = services.get_top_shows()

    top_tvshows = []
    for top_tvshow in top_tvshows:
        tvshow = (
            TVShow.objects
            .filter(
                title=top_tvshow.get('title'),
                year=top_tvshow.get('year'),
            )
            .first()
        )
        if tvshow:
            tvshow.poster_image = top_tvshow.get('poster_image')
            tvshow.rating = top_tvshow.get('rating')
            tvshow.save()
        else:
            tvshow = TVShow(
                poster_image=top_tvshow.get('poster_image'),
                title=top_tvshow.get('title'),
                year=top_tvshow.get('year'),
                rating=top_tvshow.get('rating'),
            )
            tvshow.save()

    return render(request, 'core/index.html')
