from django.shortcuts import get_object_or_404, render
from django.http.response import HttpResponse
from django.template.response import TemplateResponse
from django.shortcuts import redirect
from pprint import pprint
from django.contrib.auth.decorators import login_required

from organism.models import Organism

@login_required
def favorite_list(request):
    error = None
    return TemplateResponse(request,
                            'favorite/list.html',
                            {'favorite': request.favorite,
                             'varsFavorite': vars(request.favorite),
                             'error': error})

def favorite_delete(request, name_en):
    organism = get_object_or_404(Organism, name_en=name_en)
    request.favorite.delete_favorite(organism)
    return redirect('favorite:list')
