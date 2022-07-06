from .favorite import Favorite
from logging import getLogger
logger = getLogger(__name__)


def favorite_middleware(get_response):
    """ request に favorite を付与するミドルウェア
    """
    def middleware(request):
        favorites = request.session.get('favorite')
        if favorites:
            favorite = Favorite.from_json(favorites)

        else:
            favorite = Favorite()
        request.favorite = favorite
        response = get_response(request)
        if request.favorite.edited:
            request.session['favorite'] = request.favorite.as_json()

        return response
    return middleware
