from sre_constants import SUCCESS
from click import pass_context
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Organism
from pprint import pprint
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from . import forms
# def LoginView(request):
#     return HttpResponseRedirect('social:begin')

# def login(request):
#     return render(request, 'organism/login.html')

SUCCESS = 'SUCCESS'
FAIL = 'FAIL'


def organism_list(request):
    pprint((request.user._wrapped))
    organisms = Organism.objects.all().order_by('-id')
    paginator = Paginator(organisms, 4)
    page = request.GET.get('page')
    try:
        organisms = paginator.page(page)
    except (EmptyPage, PageNotAnInteger):
        organisms = paginator.page(1)
    return TemplateResponse(request, 'organism/list.html',
                            {'organisms': organisms})


def organism_detail(request, organism_name_en):
    organism = Organism.objects.filter(name_en=organism_name_en).first()
    if request.method == 'POST':
        request.favorite.add_favorite(organism)
        return redirect(request.path)
    else:
        pass
    return TemplateResponse(request, 'organism/detail.html', {'organism': organism})


def organism_edit(request, organism_name_en):
    """ 生物情報編集
    """
    organism = Organism.objects.filter(name_en=organism_name_en).first()
    if request.method == 'POST':
        form = forms.OrganismEditForm(
            request.POST, request.FILES, instance=organism)
        if form.is_valid():
            form.save()
            messages.success(request, SUCCESS)
            return redirect('organism:list')
        messages.error(request, FAIL)
    else:
        form = forms.OrganismEditForm(instance=organism)
    return TemplateResponse(request, 'organism/edit.html', {'organism': organism, 'form': form})


def organism_register(request):
    """ 生物情報登録
    """

    if request.method == 'POST':
        form = forms.OrganismEditForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            # messages.add_message(request, messages.SUCCESS, "SUCCESS")
            messages.success(request, SUCCESS)
            return redirect('organism:register')
        messages.error(request, FAIL)
    else:
        form = forms.OrganismEditForm()

    return TemplateResponse(request, 'organism/register.html', {'form': form})


def organism_delete(request, organism_name_en):
    """ 生物情報削除
    """

    if request.method == 'POST':
        Organism.objects.filter(name_en=organism_name_en).delete()
        messages.success(request, SUCCESS)
        return redirect('organism:list')
    else:
        return redirect('organism:list')
